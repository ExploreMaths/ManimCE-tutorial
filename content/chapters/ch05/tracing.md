---
title: 追踪与边界
---

# 追踪与边界

"拖尾轨迹"和"流动边框"是讲解演示中最常用的两类装饰效果：`TracedPath` 记录一个点的运动轨迹，`AnimatedBoundary` 给图形加上不断流动的彩色描边。

## TracedPath

`TracedPath(traced_point_func)` 是一条特殊的 `VMobject`：内部维护一个 updater，每帧取**当前点**追加到自身点列，从而把"某个点的运动路径"画出来。

:::inheritance
TracedPath → VMobject → Mobject → object
:::

```python
TracedPath(
    traced_point_func: Callable,
    stroke_width: float = 2,
    stroke_color: ParsableManimColor | None = WHITE,
    dissipating_time: float | None = None,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `traced_point_func` | Callable | — | 返回一个点坐标的函数；通常传**方法引用**如 `dot.get_center`（不要加括号） |
| `stroke_width` | float | 2 | 轨迹线宽 |
| `stroke_color` | color \| None | WHITE | 轨迹颜色；None 表示不描边 |
| `dissipating_time` | float \| None | None | 消散时长：超过该时间的轨迹段逐渐消失；None 表示永久保留 |
:::

## AnimatedBoundary

`AnimatedBoundary(vmobject)` 给目标图形生成一圈**流动的彩色描边**：多层颜色不同的描边依次显现、消失，形成"边界在流动"的视觉效果。它本身是一个 `VGroup`，由若干描边副本组成。

:::inheritance
AnimatedBoundary → VGroup → VMobject → Mobject → object
:::

```python
AnimatedBoundary(
    vmobject: VMobject,
    colors: Sequence[color] = [#29ABCA, #9CDCEB, #236B8E, #736357],
    max_stroke_width: float = 3,
    cycle_rate: float = 0.5,
    back_and_forth: bool = True,
    draw_rate_func: RateFunction = smooth,
    fade_rate_func: RateFunction = smooth,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `colors` | Sequence[color] | 四种蓝灰色 | 参与流动的描边颜色 |
| `max_stroke_width` | float | 3 | 描边最大线宽 |
| `cycle_rate` | float | 0.5 | 每层颜色完成一次显现/消失的速率 |
| `back_and_forth` | bool | True | 线宽是否来回脉动 |
:::

:::demo examples/ch05/tracing.py TracingAndBoundary
`TracedPath` 让黄点绕圆一周的轨迹留下 2 秒渐散的拖尾；`AnimatedBoundary` 给右侧正方形加上流动的蓝灰描边。
:::

:::notice warning
常见错误
`TracedPath` 必须先 `self.add(...)` 进场景，否则它的 updater 不会执行，画面里只有运动、没有轨迹。另外传点函数时写成 `dot.get_center`（方法引用）而不是 `dot.get_center()`（调用结果）——后者只记录了添加那一刻的位置，轨迹变成一条死线。
:::

:::notice tip
提示
`TracedPath` 常与 `MoveAlongPath`、Rotating 或 updater 驱动的点搭配：先创建会动的点，再让轨迹跟随它。`dissipating_time` 适合表现"最近路径"，设为 `None` 则适合保留完整轨迹（如几何作图）。
:::

## 自测

:::exercise
想记录一个点的完整运动轨迹并永久保留，`TracedPath` 应该怎么配置？
:::answer
`self.add(TracedPath(dot.get_center, dissipating_time=None))`（`dissipating_time` 默认就是 None，即永久保留），确保轨迹对象被 add 进场景即可。
:::
:::

:::exercise
为什么 `TracedPath(dot.get_center())` 画不出轨迹？
:::answer
`dot.get_center()` 是**调用**，传入的是添加那一刻的一个坐标值，不是"每帧取点"的函数。应传方法引用 `dot.get_center`，轨迹对象每帧自己调用它取当前位置。
:::
:::

## 下一步

轨迹让"走过的路"可见，下一节让物体沿任意路径运动、或被任意形变：`MoveAlongPath` 与 `Homotopy` 家族。
