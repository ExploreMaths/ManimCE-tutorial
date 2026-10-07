---
title: 生长与淡入淡出
---

# 生长与淡入淡出

两组最直观的进场/离场动画：Grow 家族让物体从某个基准点"生长"出来，Fade 家族让物体淡入淡出并可附带平移/缩放。两组都支持 `point_color` 之类的起点着色参数，Grow 系默认 `introducer=True`，`FadeOut` 是 `remover=True`。

## GrowFromPoint

`GrowFromPoint(mobject, point, point_color=None)` 从任意 `point` 出发把物体放大到完整尺寸，`point_color` 可指定生长起点的颜色（默认跟随物体自身颜色）。

## GrowFromCenter

`GrowFromCenter(mobject, point_color=None)` 从物体中心生长——`GrowFromPoint` 以质心为 `point` 的便捷版。

## GrowFromEdge

`GrowFromEdge(mobject, edge, point_color=None)` 从指定边缘方向（如 `LEFT`、`UP`）生长，适合做"从屏幕边缘长出"的效果。

:::compare
| 类 | 生长基准 | 适合 |
| ---- | ---- | ---- |
| `GrowFromPoint` | 任意点（必填） | 从某个参照物/位置冒出 |
| `GrowFromCenter` | 物体中心 | 通用进场 |
| `GrowFromEdge` | 指定方向的边缘 | 从边缘展开 |
| `GrowArrow` | 箭头起点 | 箭头类专用 |
| `SpinInFromNothing` | 中心 + 旋转 | 带点动感的进场 |
:::

## GrowArrow

`GrowArrow(arrow, point_color=None)` 从箭尾向箭头生长出完整箭头。它内部会调用 `arrow.scale(0, scale_tips=True, about_point=arrow.get_start())` 生成初始状态。

:::notice warning
常见错误
`GrowArrow` 只适合真正的 `Arrow`（其 `scale` 支持 `scale_tips` 参数）。对 `CurvedArrow` 使用会抛 `TypeError: VMobject.scale() got an unexpected keyword argument 'scale_tips'`（本机 v0.21.0 实测）——因为 `CurvedArrow` 继承自 `ArcBetweenPoints` 而非 `Arrow`。曲线箭头请改用 `Create` 或 `FadeIn`。
:::

## SpinInFromNothing

`SpinInFromNothing(mobject, angle=PI/2, point_color=None)` 从中心一边旋转一边放大出现，默认转 90°，比纯生长多一分动感。

:::demo examples/ch05/grow_variants.py GrowVariants
五个物体依次演示：`GrowFromPoint`（自定义点）、`GrowFromCenter`、`GrowFromEdge`、`GrowArrow` 与 `SpinInFromNothing`。
:::

## FadeIn

`FadeIn(*mobjects, shift=None, target_position=None, scale=1)` 让物体逐渐变不透明。可同时传入多个物体（内部包成 `Group`）。三个可选修饰参数来自其基类实现：

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `shift` | np.ndarray \| None | None | 淡入的同时从"当前位置 + shift"平移过来 |
| `target_position` | np.ndarray \| Mobject \| None | None | 淡入起点对齐到某点/某物体中心（与 `shift` 二选一，优先于 `shift`） |
| `scale` | float | 1 | 淡入起点的缩放倍数（如 `scale=0.2` 表示从 1/5 大小放大） |
:::

## FadeOut

`FadeOut(*mobjects, shift=None)` 渐隐出场，`remover=True` 播完移除物体。也支持 `shift`（整体向某方向滑走）与 `target_position`。注意 `FadeOut` 只接受 `shift`/`target_position`，**没有** `scale` 参数。

:::demo examples/ch05/fade_variants.py FadeVariants
普通淡入、带 `shift` 的滑入、从指定 `target_position` 飞入、从小放大（`scale=0.2`）；最后四个物体整体 `FadeOut` 并向右滑走。
:::

:::notice tip
提示
`FadeIn`/`FadeOut` 位于 `manim.animation.fading` 模块，而名字相近的 `FadeTransform`/`FadeToColor` 却在 `manim.animation.transform` 模块——检索源码时注意区分。
:::

## 自测

:::exercise
`CurvedArrow(ORIGIN, RIGHT*2)` 想用生长效果进场，`GrowArrow` 可以吗？不行的话给出替代方案。
:::answer
不行。`CurvedArrow` 不是 `Arrow` 子类，其 `scale()` 没有 `scale_tips` 参数，`GrowArrow` 初始化起始状态时会抛 `TypeError`（v0.21.0 实测）。改用 `Create`（沿弧线画出）或 `FadeIn` 即可。
:::
:::

:::exercise
想让一个圆从屏幕左上角飞入并落在中央、同时从小变大，`FadeIn` 一行怎么写？
:::answer
`self.play(FadeIn(c, target_position=LEFT * 5 + UP * 3, scale=0.2))`：`target_position` 指定淡入起点（也可用另一个 Mobject，取其中心），`scale=0.2` 让它从 1/5 尺寸放大到位。
:::
:::

## 下一步

进场和离场都齐了，最重磅的一节来了：`Transform` 家族——如何让一个物体变成另一个物体。
