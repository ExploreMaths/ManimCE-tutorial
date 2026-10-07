---
title: Updater 系统
---

# Updater 系统

前面的动画都是"播放时改变、播完就停"。Updater（更新器）则相反：它是挂在 `Mobject` 上的一个函数，**只要画面在推进（`play` 或 `wait` 的每一帧），渲染器就会反复调用它**，让物体持续跟随某个状态。做"图形跟着数值走""轨迹拖尾""持续旋转"这类效果离不开它。

工作原理一句话：每渲染一帧，场景对所有 mobject 调用 `mob.update(dt)`，`dt` 是距上一帧的秒数；每个 updater 按它声明的形参个数被调用——`f(mob)` 或 `f(mob, dt)`。

## ValueTracker

`ValueTracker` 是一个**不可见的数值容器**：本身不渲染任何图形，但可以被 `animate` 驱动、被 updater 读取，是"数值 → 图形"联动的事实标准枢纽。

:::inheritance
ValueTracker → Mobject → object
:::

```python
ValueTracker(value: float = 0, **kwargs)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `value` | float | 0 | 初始数值 |
:::

常用成员：

:::compare
| 成员 | 说明 |
| ---- | ---- |
| `get_value()` | 读取当前数值 |
| `set_value(value)` | 直接设置数值（无动画） |
| `increment_value(d_value)` | 累加一个增量 |
| `tracker.animate.set_value(v)` | 以动画方式把数值过渡到 v，常用 |
:::

:::notice tip
提示
`ValueTracker` 是 `Mobject` 子类，所以 `self.play(tracker.animate.set_value(3))` 完全合法——播放的是 tracker 的"方法动画"。真正可见的物体通过 updater 读它，就实现了数值驱动动画。
:::

## add_updater

`Mobject.add_updater()` 给物体挂一个更新函数。签名为 `add_updater(update_function, index=None, call_updater=False)`：

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `update_function` | callable | — | 更新函数，`f(mob)` 或 `f(mob, dt)` 两种形态 |
| `index` | int \| None | None | 插入到 updater 列表的位置；None 追加到末尾 |
| `call_updater` | bool | False | 为 True 时挂上立即先调用一次（用于把物体摆到初始正确位置） |
:::

配套管理方法：

:::compare
| 方法 | 说明 |
| ---- | ---- |
| `get_updaters()` | 返回 updater 列表；判断是否"有 updater"就用它的真值 |
| `suspend_updating(recursive=True)` | 暂停执行 updater（保留列表） |
| `resume_updating(recursive=True)` | 恢复执行 |
:::

## remove_updater

`remove_updater(update_function)` 按**函数对象 identity** 移除指定 updater——这要求你拿到当初 `add_updater` 时传入的同一个引用，匿名 lambda 请事先保存：

```python
follow = lambda d: d.move_to(target.get_center())
dot.add_updater(follow)
# ...之后
dot.remove_updater(follow)
```

## clear_updaters

`clear_updaters(recursive=True)` 一次清空全部 updater；`recursive=True` 时子物体的 updater 一并清除。`remove_updater` 移除不存在的函数不会报错，`clear_updaters` 对空列表同样安全。

:::notice version
版本说明
v0.21.0 **没有** `has_updater()` 方法（旧教程里的写法已不存在），判断是否有 updater 请用 `if mob.get_updaters():`。
:::

典型模式：tracker 驱动多个物体。

:::demo examples/ch05/updater_value_tracker.py UpdaterValueTracker
`DecimalNumber` 和 `Dot` 各自挂 updater 读同一个 `ValueTracker`；中段 `suspend_updating()` 让圆点暂停跟随而数字照常更新，二者对比清晰可见。
:::

## always_redraw

`always_redraw(func)` 每帧执行 `func()`（无参函数，返回一个新 mobject）并让物体 `become` 结果，等于"持续重绘"：

```python
always_redraw(func: Callable[[], Mobject]) -> Mobject
```

## always_shift

`always_shift(mobject, direction=RIGHT, rate=0.1)` 给物体挂一个漂移 updater，每帧平移 `direction * rate * dt`。

## always_rotate

`always_rotate(mobject, rate=0.349..., **kwargs)` 给物体挂一个旋转 updater，每帧旋转 `rate * dt` 弧度（默认值约 20°/秒），`kwargs` 透传给 `rotate`（如 `about_point`）。

## f_always

`f_always(method, *arg_generators, **kwargs)` 是函数版 always：每帧以各参数生成器的**当前返回值**调用 `mobject.method(*args)`。例如 `f_always(dot.move_to, lambda: tracker.get_value() * RIGHT)` 等价于一个跟随 tracker 的 updater。

四个工厂对比：

:::compare
| 函数 | 每帧动作 |
| ---- | ---- |
| `always_redraw(func)` | 重建并 `become` 整个 mobject |
| `always_shift(mob, direction, rate)` | 增量平移 `direction * rate * dt` |
| `always_rotate(mob, rate, **kwargs)` | 增量旋转 `rate * dt` 弧度 |
| `f_always(method, *gens, **kwargs)` | 以生成器返回值调用 `mob.method(...)`（绝对赋值） |
:::

:::demo examples/ch05/updater_helpers.py UpdaterHelpers
`always_redraw` 让正弦曲线随 tracker 每帧重建；`always_rotate` 让正方形持续自转；`cycle_animation` 让小圆不停转圈。
:::

:::notice warning
常见错误
`always_redraw` 的代价是**每帧完整重建** mobject。构造一个简单的 `Dot`/`FunctionGraph` 没问题，但重建带大量子对象的图形（如复杂 `VGroup`、大量文字）会明显拖慢渲染。此时应改用轻量 updater（直接改属性）而不是整对象重建。
:::

## turn_animation_into_updater

`turn_animation_into_updater(animation, cycle=False, delay=0)` 把**一个动画变成 updater**：物体的更新不再占用 `play`，而是在每次帧推进时推进动画进度。`delay` 是开始前延迟秒数。

```python
turn_animation_into_updater(animation: Animation, cycle: bool = False, delay: float = 0, **kwargs) -> Mobject
```

## cycle_animation

`cycle_animation(animation, **kwargs)` 是 `turn_animation_into_updater(animation, cycle=True)` 的简写：动画无限循环。

```python
cycle_animation(animation: Animation, **kwargs) -> Mobject
```

两者都返回 mobject 本身。典型用法：先转换、再 `self.add(mob)`，之后用 `self.wait(...)` 观察效果；非循环版本播完会自动移除 updater。

## UpdateFromFunc

`UpdateFromFunc(mobject, update_function)` 把"每帧更新"封装进 `play`：播放期间每帧调用 `f(mob)`，与 `play` 生命周期绑定（播完即停），适合一次性联动。

```python
UpdateFromFunc(mobject: Mobject, update_function: Callable[[Mobject], Any],
               suspend_mobject_updating: bool = False, **kwargs)
```

:::inheritance
UpdateFromFunc → Animation → object
:::

## UpdateFromAlphaFunc

`UpdateFromAlphaFunc(mobject, update_function)` 继承 `UpdateFromFunc`，区别是更新函数额外收到动画进度：`f(mob, alpha)`，alpha 从 0 到 1——需要做"随进度渐变"的更新时用它。

:::inheritance
UpdateFromAlphaFunc → UpdateFromFunc → Animation → object
:::

两者都有 `suspend_mobject_updating=False` 参数：为 False（默认）时播放期间会先挂起 mobject 自身的 updater，避免双重更新。

## MaintainPositionRelativeTo

`MaintainPositionRelativeTo(mobject, tracked_mobject)` 播放期间让 `mobject` 保持与 `tracked_mobject` 的**相对位置不变**——目标物体移动时，它跟着平移。常用于"标签跟着图形跑"。

:::inheritance
MaintainPositionRelativeTo → Animation → object
:::

:::notice warning
常见错误
updater 只在**有帧推进**时运行：静止等待默认会逐帧模拟（updater 正常），但 `wait(frozen_frame=True)` 期间 updater 不执行；`skip_animations` / `-n` 跳过的部分 updater 也不会补齐。另外 `suspend_updating` 之后 updater 只是"不看时钟"，恢复后若 updater 用的是 `move_to` 这类**绝对赋值**，物体会瞬间跳到当前正确位置而不是平滑追上。
:::

## 自测

:::exercise
想让一个标签始终贴着某个移动正方形的右上角，两种思路分别是什么？
:::answer
思路一：给标签加 updater，每帧 `label.next_to(square, UR)`；思路二：`self.play(MaintainPositionRelativeTo(label, square))` 让标签在动画期间跟随。需要永久跟随用前者，只在某段动画内跟随用后者。
:::
:::

:::exercise
`always_redraw(lambda: func())` 与给物体加 `lambda mob: mob.become(func())` 的 updater 有什么区别？
:::answer
没有本质区别——`always_redraw` 就是后者加了一层封装（先调用一次 `func()` 作为初始物体）。两者都是每帧完整重建，都要注意性能。
:::
:::

## 下一步

学会了"持续更新"之后，下一节看 updater 最常见的搭档：让数字平滑滚动起来的 `ChangingDecimal` 家族。
