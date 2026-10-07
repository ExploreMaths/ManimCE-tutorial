---
title: 圆弧与曲线
---

# 圆弧与曲线

本节覆盖圆弧家族（`Arc`、扇形、圆环）、贝塞尔曲线与曲线箭头。所有圆弧都继承 `TipableVMobject`，因此也能像直线一样挂箭头尖。

:::inheritance
CurvedDoubleArrow → CurvedArrow → ArcBetweenPoints → Arc → TipableVMobject → VMobject
:::

## Arc

`Arc` 是按圆心、半径与角度生成的一段圆弧，是所有圆弧图形的基石。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `radius` | float \| None | 1.0 | 半径；None 时由其它参数决定 |
| `start_angle` | float | 0 | 起始角（弧度） |
| `angle` | float | PI / 2 | 圆弧张角（弧度） |
| `num_components` | int | 9 | 组成圆弧的贝塞尔曲线段数 |
| `arc_center` | Point3DLike | [0, 0, 0] | 圆心位置 |
:::

```python
Arc(radius=2, start_angle=PI / 6, angle=PI * 2 / 3)
```

常见坑：`arc_center` 只在构造时生效；之后 `move_to` / `shift` 改变的是包围盒位置，`get_arc_center()` 仍是几何圆心——以圆心为基准做动画时用 `arc.get_arc_center()` 而不是 `ORIGIN`。

## ArcBetweenPoints

`ArcBetweenPoints` 生成经过指定起点、终点的圆弧，弯曲程度由圆心角 `angle` 或 `radius` 控制。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `start` | Point3DLike | — | 起点 |
| `end` | Point3DLike | — | 终点 |
| `angle` | float | PI / 2 | 圆心角；决定弯曲程度 |
| `radius` | float \| None | None | 半径；传入时优先于 angle 计算圆心 |
:::

常见坑：当 `start` 与 `end` 距离固定时，`angle` 越大弧越“鼓”；`angle=PI` 恰好是半圆，更大的角会让圆心跑到起终点连线的另一侧。

## AnnularSector

`AnnularSector`（环形扇区）是内外两个同心圆弧夹出的填充区域，`Sector` 是它的特例（内半径为 0）。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `inner_radius` | float | 1 | 内半径 |
| `outer_radius` | float | 2 | 外半径 |
| `angle` | float | PI / 2 | 张角（弧度） |
| `start_angle` | float | 0 | 起始角 |
| `fill_opacity` | float | 1 | 填充不透明度 |
| `stroke_width` | float | 0 | 描边宽度（默认不描边） |
:::

## Sector

`Sector` 是从圆心切出的实心扇形，继承 `AnnularSector`（`inner_radius=0`）。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `radius` | float | 1 | 扇形半径 |
| `angle` | float | PI / 2 | 张角（弧度），经 kwargs 传入 |
| `start_angle` | float | 0 | 起始角，经 kwargs 传入 |
:::

```python
Sector(radius=2, angle=PI / 3, start_angle=PI / 6)
```

## Annulus

`Annulus`（圆环）是两个同心圆之间的区域，继承 `Circle`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `inner_radius` | float | 1 | 内半径 |
| `outer_radius` | float | 2 | 外半径 |
| `fill_opacity` | float | 1 | 填充不透明度 |
| `stroke_width` | float | 0 | 描边宽度 |
| `mark_paths_closed` | bool | False | 是否把路径标记为闭合 |
:::

常见坑：`Annulus` 的填充区域依赖 `fill_opacity`，默认描边为 0，直接 `Create` 会看到“空心圆盘外框”而不是圆环——记得保留填充或加描边。

## AnnotationDot

`AnnotationDot` 是 3Blue1Brown 风格的注释圆点：青色填充、白色粗描边，继承 `Dot`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `radius` | float | 0.104 | 圆点半径 |
| `stroke_width` | float | 5 | 白色描边宽度 |
| `stroke_color` | ParsableManimColor | WHITE | 描边颜色 |
| `fill_color` | ParsableManimColor | #58C4DD | 填充颜色（品牌青） |
:::

## CubicBezier

`CubicBezier` 用四个控制点生成一段三次贝塞尔曲线：起点锚点、起点手柄、终点手柄、终点锚点。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `start_anchor` | Point3DLike | — | 曲线起点 |
| `start_handle` | Point3DLike | — | 起点方向手柄 |
| `end_handle` | Point3DLike | — | 终点方向手柄 |
| `end_anchor` | Point3DLike | — | 曲线终点 |
:::

```python
CubicBezier(LEFT * 2, LEFT * 2 + UP, RIGHT * 2 + DOWN, RIGHT * 2)
```

常见坑：手柄离锚点越远曲线越“拗”；多段平滑曲线请用多段 `CubicBezier` 或 `VMobject` 的 `start_new_path`，不要把多段硬拼成一个 `CubicBezier`。

## CurvedArrow

`CurvedArrow` 是带箭头尖的 `ArcBetweenPoints`，箭头画在终点切线方向上。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `start_point` | Point3DLike | — | 起点 |
| `end_point` | Point3DLike | — | 终点 |
| `angle` | float | PI / 2 | 圆心角（kwargs） |
| `tip_shape` | type[ArrowTip] | ArrowTriangleFilledTip | 箭头尖形状 |
:::

:::demo examples/ch02/arcs_showcase.py ArcsShowcase
`Arc`、`Sector`、`AnnularSector`、`Annulus` 同框；下方是 `CubicBezier` 与 `CurvedArrow` / `CurvedDoubleArrow`。曲线箭头用 `Create` 入场，因为 `GrowArrow` 依赖 `scale_tips`，对圆弧系不适用。
:::

## CurvedDoubleArrow

两端都带箭头尖的曲线箭头，继承 `CurvedArrow`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `tip_shape_start` | type[ArrowTip] | ArrowTriangleFilledTip | 起点箭头尖 |
| `tip_shape_end` | type[ArrowTip] | ArrowTriangleFilledTip | 终点箭头尖 |
:::

## TipableVMobject

`TipableVMobject` 是 `Line` 与 `Arc` 共同的基类，提供“可挂箭头尖”的机制：`tip_length`、`normal_vector`、`tip_style` 三个构造参数与 `add_tip()`、`get_tip()` 等方法。`CurvedArrow` 就是在 `ArcBetweenPoints` 构造后调用 `self.add_tip()` 实现的。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `tip_length` | float | 0.35 | 箭头尖默认长度 |
| `normal_vector` | Vector3DLike | [0, 0, 1] | 箭头尖法向量（决定朝向） |
| `tip_style` | dict \| None | None | 箭头尖默认样式字典 |
:::

```python
arc = Arc(angle=PI, tip_style={"fill_opacity": 0.5})
arc.add_tip(tip_shape=StealthTip, tip_length=0.5)
```

## 常见错误与建议

:::notice warning
常见错误
圆弧族的 `angle` 一律是**弧度**。传角度制数值（如 90）会得到绕很多圈的乱弧；用 `90 * DEGREES` 转换。
:::

:::notice tip
提示
`num_components` 控制圆弧的贝zier 分段数：需要让圆弧与直线 `Transform` 时提高分段数能让变形更平滑，代价是略慢的构造速度。
:::

## 自测

:::exercise
画一段从 `LEFT*2` 到 `RIGHT*2`、向上鼓起的半圆弧，并把箭头尖装在起点（朝左）。
:::answer
半圆对应圆心角 `PI`；箭头尖装在起点用 `add_tip(at_start=True)`：

```python
arc = ArcBetweenPoints(LEFT * 2, RIGHT * 2, angle=PI)
arc.add_tip(at_start=True)
```
:::
:::

## 下一步

有了基础图形，下一节介绍如何用布尔运算（并、交、差、异或）组合出复杂的填充形状。
