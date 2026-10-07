---
title: 组合与编排
---

# 组合与编排

`play()` 传多个动画默认同时开始；要表达"并行、串行、错峰"，需要把动画装进**组合动画**。本节四个类都基于 `AnimationGroup`，区别只在 `lag_ratio` 一个参数。

## AnimationGroup

`AnimationGroup(*animations, group=None, run_time=None, rate_func=linear, lag_ratio=0)` 把多个动画打包成一个，整体可像普通动画一样传入 `play()`、设置时长与速率。

:::inheritance
AnimationGroup → Animation → object
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `group` | Group \| VGroup \| None | None | 组合动画所依附的物体；None 时自动收集各子动画的非 introducer 物体 |
| `run_time` | float \| None | None | 总时长；None 时自动取所有子动画的最晚结束时间 |
| `rate_func` | Callable | `linear` | 注意：组合动画默认 `linear`，而非 `Animation` 的 `smooth` |
| `lag_ratio` | float | 0 | 子动画之间的错峰比例，见下文语义 |
:::

### lag_ratio 语义

`AnimationGroup` 的排布算法（`build_animations_with_timings`）：第 i 个子动画的开始时间 = 前面所有子动画 `run_time × lag_ratio` 的累加。即：

- `lag_ratio=0`：全部同时开始（默认，纯并行）
- `lag_ratio=1`：每个都在上一个**结束后**才开始（`Succession` 的默认值）
- `0 < lag_ratio < 1`：按上一个子动画时长的固定比例依次错开（`LaggedStart` 的默认值 0.05）

总时长自动取所有子动画的最晚结束时刻；手动传 `run_time` 时会覆盖为指定值。

### 嵌套规则

组合动画可以互相嵌套（`AnimationGroup` 里放 `LaggedStart`，`Succession` 里放 `Succession` 等），渲染器会按组递归展开。注意两点：

- **同一物体不要同时被两个并行子动画驱动**（行为未定义，常见症状是物体"闪"到终态）；要错开就调 `lag_ratio` 或改用 `Succession`。
- 子动画的 `rate_func` 各自生效；外层的 `rate_func`/`run_time` 作用于整个组合的时间轴。

:::notice warning
常见错误
`AnimationGroup` 的默认 `rate_func` 是 `linear`：如果你发现组合动画比单独播放时"手感"不同，多半是速率函数差异，不是 bug。追求统一手感可显式传 `rate_func=smooth`。
:::

## Succession

`Succession(*animations, lag_ratio=1)`：严格**一个接一个**播放的子类，lag_ratio 写死为 1。前一个结束后一个才开始，总时长为各子动画之和。适合表达"先出现、再移动、再消失"这类有严格先后依赖的流程。

```python
self.play(
    Succession(
        GrowFromCenter(c, run_time=0.5),
        c.animate.shift(DOWN).set_run_time(0.5),
        FadeOut(c, run_time=0.5),
    )
)
```

## LaggedStart

`LaggedStart(*animations, lag_ratio=0.05)`：所有子动画都播**完整时长**，但按 `lag_ratio` 依次晚开始——后一个比前一个晚 `0.05 × 前一个run_time`。默认 0.05 很温和；想让节奏明显可把 `lag_ratio` 调大（如 0.3），形成"波浪式"入场。

## LaggedStartMap

`LaggedStartMap(animation_class, mobject, arg_creator=None, run_time=2, lag_ratio=0.05)`：对 `mobject` 的**每个子对象**用同一个动画类批量生成子动画，再按 `LaggedStart` 错峰播放。`arg_creator(submob)` 决定每个子动画的位置参数（默认把子对象本身作为唯一参数）。

```python
# 对 5 个方块逐个 FadeIn，每个都带同样的 shift 修饰
self.play(LaggedStartMap(FadeIn, squares, shift=UP * 0.8, lag_ratio=0.2))
```

:::compare
| 类 | lag_ratio 默认 | 语义 |
| ---- | ---- | ---- |
| `AnimationGroup` | 0 | 并行（可同时整体调 run_time/rate_func） |
| `Succession` | 1 | 严格串行 |
| `LaggedStart` | 0.05 | 错峰并行，各播完整时长 |
| `LaggedStartMap` | 0.05 | 对一组子对象批量套用并错峰 |
:::

:::demo examples/ch05/composition.py CompositionDemo
`AnimationGroup` 两点并行淡入；`Succession` 让方块先生长、再移动、最后消失；`LaggedStart` 让五个圆点波浪式长出；`LaggedStartMap` 对一排方块批量 `FadeIn` 并错峰。
:::

## 自测

:::exercise
`AnimationGroup(a, b, lag_ratio=0.5)` 里 a、b 的 `run_time` 都是 1 秒，b 什么时候开始？总时长是多少？
:::answer
按排布算法，b 的开始时间 = a 的 `run_time × lag_ratio` = 0.5 秒；b 播到 1.5 秒，故组合总时长为 **1.5 秒**。`lag_ratio` 乘的是**前一个子动画自己的时长**并累加，不是乘组合总时长。
:::
:::

:::exercise
五个圆点想"依次出现，一个完全出现后下一个才出现"，用哪个组合类？如果希望它们节奏更紧凑（下一个在前一个播到一半时就开始）呢？
:::answer
严格依次用 `Succession`（lag_ratio=1）；紧凑错峰用 `LaggedStart(*anims, lag_ratio=0.5)`——lag_ratio=0.5 时每个动画在前一个进行到一半时开始。
:::
:::

## 下一步

到这里，单个动画与组合编排都齐了。下一节进入更动态的领域：`ValueTracker` 与 updater 系统，让动画脱离"固定时间轴"、由数值实时驱动。
