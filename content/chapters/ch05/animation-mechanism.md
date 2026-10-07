---
title: Animation 机制
---

# Animation 机制

前面所有的 `FadeIn`、`Transform` 都是 `Animation` 的子孙类。本节拆开 `Animation` 本身：它有哪些可调的要素、生命周期怎么走、`play()` 在背后做了什么，以及两个进阶机制——`prepare_animation` 与 `override_animation`。掌握这些，你才能在组合动画与自定义动画时不踩坑。

## Animation

`Animation(mobject, ...)` 是一切动画的基类。它把"一段时间内的状态变化"抽象成统一接口：渲染器每帧调用 `interpolate(alpha)`，由子类决定如何把进度 `alpha`（0 到 1）翻译成物体的状态。

:::inheritance
Animation → object
:::

### 构造参数（五要素全展开）

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `mobject` | Mobject \| None | — | 被动画驱动的物体；`Add`/`Wait` 等不驱动具体物体的动画可传 None |
| `run_time` | float | 1.0 | 动画时长（秒） |
| `rate_func` | Callable | `smooth` | 速率函数，把线性时间映射为动画进度，见 Rate Functions 一节 |
| `lag_ratio` | float | 0.0 | 子对象错峰比例：第 n 个子对象比前一个晚 `lag_ratio × run_time` 开始，只影响多点/子对象动画的内部节奏，不改变总时长 |
| `remover` | bool | False | True 时动画结束后把物体从场景移除（`FadeOut` 即如此） |
| `reverse_rate_function` | bool | False | 反转速率函数；不影响 `remover`/`introducer`，需成对显式设置 |
| `name` | str \| None | None | 渲染日志中显示的动画名，默认 `<类名>(<物体名>)` |
| `suspend_mobject_updating` | bool | True | 播放期间是否挂起物体自身的 updater |
| `introducer` | bool | False | True 时动画开始时把物体加入场景（`FadeIn`/`Create` 即如此） |
:::

常被称作"五要素"的是前五个：`mobject`、`run_time`、`rate_func`、`lag_ratio`、`remover`。`introducer` 与 `remover` 是一对镜像开关，分别管"开头进场"和"结尾离场"。

### 生命周期

每个动画在播放时依次经历：

1. `begin()` —— 记录起始状态（多数动画会先把物体拷贝一份作为"起点"）
2. 逐帧 `update_mobjects(dt)` + `interpolate(alpha)`
3. `finish()` —— 确保落在终点状态
4. `clean_up_from_scene(scene)` —— 处理 `remover`（离场）或把目标物留在场景中

### .animate 构造器

`m.animate` 不是动画，而是一个**动画构造器**（`_AnimationBuilder`）：访问 `m.animate` 时它立即对 `m` 调用 `generate_target()`，之后的每个方法调用都作用在**目标副本**上，最后由 `play()` 内部的 `prepare_animation` 调 `build()` 生成真正的 `_MethodAnimation`。

```python
square.animate.shift(LEFT).scale(2)      # 返回构造器，链式记录方法
self.play(square.animate(run_time=2, rate_func=linear).shift(LEFT))  # 动画参数要放在方法之前，且只能传一次
```

:::notice warning
常见错误
- `m.animate.shift(LEFT)` 的返回值是构造器而**不是** `m`，不能继续当物体用（例如 `.next_to(...)` 会构造出错误的动画）。
- 动画参数（`run_time`、`rate_func` 等）必须通过 `m.animate(...)` 在**访问任何方法之前**传入，且只能传一次；之后再传会抛 `ValueError`。
:::

:::demo examples/ch05/anim_mechanism.py AnimMechanism
`run_time`/`rate_func` 控制单个动画，`lag_ratio` 让多个动画错峰；`Add` 与 `Wait` 也是 `Animation` 家族成员。
:::

## Add

`Add(*mobjects, run_time=0.0)` 把物体**瞬间**放进场景——相当于 `Scene.add()` 的动画版，好处是可以塞进 `AnimationGroup`/`Succession` 里与其他动画编排。默认 `run_time=0` 意味着"加入后不再额外停留"。

:::notice warning
常见错误
单独播放 `Add` 会抛 `ValueError: ... has a total run_time of 0 <= 0 seconds which Manim cannot render`（本机 v0.21.0 实测）。因为整个 `play()` 的总时长为 0。修法：显式给一个正的 `run_time`（语义是"出现后静止这么久"），或把它和别的动画放进同一个 `play()`/`Succession`。
:::

## Wait

`Wait` 是"空操作"动画：不改变任何物体，只消耗时间，常用来穿插停顿。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `run_time` | float | 1 | 静止时长（秒） |
| `stop_condition` | Callable \| None | None | 每帧求值，返回真值即提前结束；不能与 `frozen_frame` 同时使用 |
| `frozen_frame` | bool \| None | None | 是否按静止帧处理；None 时由 `Scene.should_mobjects_update` 自动判断 |
| `rate_func` | Callable | `linear` | 速率函数（通常无需改动） |
:::

`Scene.wait(...)` 本质就是 `self.play(Wait(...))`。有 updater 时 `Wait` 默认逐帧推进 updater；若确定画面静止，传 `frozen_frame=True` 可按单帧延展、加快渲染。

## prepare_animation

`prepare_animation(anim)` 是 `play()` 的入口转换器（`manim.animation.animation` 模块）：

- 传入 `_AnimationBuilder` → 调 `build()` 生成 `_MethodAnimation`
- 传入 `Animation` → 原样返回
- 其他任何东西 → 抛 `TypeError: Object ... cannot be converted to an animation`

```python
prepare_animation(FadeIn(square))                    # FadeIn(Square)
prepare_animation(square.animate.shift(LEFT))        # _MethodAnimation(Square)
prepare_animation(42)                                # TypeError
```

`Scene.play` 内部对每个参数都调用它，因此裸 `Mobject` 会在这一步被拒绝：

:::notice warning
常见错误
`self.play(Square())` 会抛 `TypeError: Unexpected argument Square passed to Scene.play().`（本机 v0.21.0 实测，源自内部的 `prepare_animation`）。正确写法是 `self.play(FadeIn(Square()))` 或 `self.play(Square().animate.shift(LEFT))`——`play` 只认动画和 `.animate` 构造器。
:::

## override_animation

`override_animation(animation_class)` 是装饰器：为某个 `Mobject` 子类指定"当播放某类动画时，实际改播什么"。被标记的方法会在 `m.animate` 构造器的 `build()` 阶段被调用，返回替代动画。

```python
class MySquare(Square):
    @override_animation(FadeIn)
    def _fade_in_override(self, **kwargs):
        return Create(self, **kwargs)

class Demo(Scene):
    def construct(self):
        self.play(FadeIn(MySquare()))  # 实际播放 Create(MySquare())
```

要点：

- 只修饰 `Mobject` 子类的方法；**覆写会被该物体的子类继承**，但不会覆写动画类的子类（例如覆写 `FadeIn` 不影响 `FadeInFrom` 之类）。
- 覆写后的动画**不支持方法链式**：`m.animate.shift(...).scale(...)` 中若命中覆写方法，构造器会抛 `NotImplementedError`。
- 传入的 `anim_args`（即 `m.animate(...)` 的参数）会以关键字形式交给覆写方法。

## 自测

:::exercise
`self.play(Add(m))` 报错 `total run_time of 0 <= 0 seconds`，为什么？怎么改？
:::answer
`Add` 默认 `run_time=0`，单独一个零时长动画让整个 `play()` 总时长为 0，渲染器拒绝渲染。改法：给它显式正的时长（`self.play(Add(m), run_time=0.5)`，含义是出现后再静止 0.5 秒），或与其他动画同播 / 放进 `Succession`。
:::
:::

:::exercise
`text.animate.set_color(RED).scale(2)` 与 `text.animate(run_time=2).set_color(RED).scale(2)` 有什么区别？第二行的 `run_time` 写到最后会怎样？
:::answer
前者用默认 `run_time=1.0`、`rate_func=smooth`；后者把 `run_time=2` 交给构造器，`build()` 时写进生成的动画。若把 `run_time` 写在方法之后（如 `text.animate.set_color(RED)(run_time=2)`），构造器已锁定参数，会抛 `ValueError: Animation arguments must be passed before accessing methods and can only be passed once`。
:::
:::

## 下一步

机制清楚了，接下来按家族认识具体的进场动画：先讲"画出来"的创建家族——`Create`、`Write`、打字机与逐字出场。
