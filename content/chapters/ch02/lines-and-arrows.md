---
title: 线与箭头
---

# 线与箭头

本节覆盖线段、虚线、各类箭头与角度标记。它们的共同点是：都构建在 `TipableVMobject` 机制之上，因此线段和圆弧都能“长”出箭头。

:::inheritance
Arrow → Line → TipableVMobject → VMobject
:::

## Line

`Line` 是连接 `start` 与 `end` 两点的线段（默认从 `LEFT` 到 `RIGHT`），是所有线类图形的基类。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `start` | Point3DLike \| Mobject | [-1, 0, 0] | 起点；传 Mobject 时取其中心 |
| `end` | Point3DLike \| Mobject | [1, 0, 0] | 终点；传 Mobject 时取其中心 |
| `buff` | float | 0 | 两端向内收缩的长度 |
| `path_arc` | float | 0 | 弯曲程度（弧度）；大于 0 时线段变成弧线 |
:::

```python
line = Line(LEFT, RIGHT, color=BLUE)
line = Line(circle, square)  # 两端自动吸附到两个 mobject 的中心
```

常见坑：`buff` 会让线段两端**同时**缩短；`path_arc` 是弧度而不是角度，画弯曲连线时常配合 `.animate` 或 `path_arc=PI/4` 使用。

## DashedLine

虚线段，`DashedLine` 直接继承 `Line`，所有 `Line` 参数都可用，额外控制虚线的颗粒度。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `dash_length` | float | 0.05 | 每段虚线的长度 |
| `dashed_ratio` | float | 0.5 | 虚线段与间隔的比例；0 到 1 之间 |
:::

常见坑：`dash_length` 是相对 Manim 单位的长度；线条很长而 `dash_length` 不变时会显得“密”。

## Arrow

带箭头的线段，最常用的指示工具。`Arrow` 继承 `Line`，自动在线的终点添加一个箭头尖。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `stroke_width` | float | 6 | 线身描边宽度 |
| `buff` | float | 0.25 | 箭身两端收缩量，使箭头不贴着端点 |
| `max_tip_length_to_length_ratio` | float | 0.25 | 箭头最大长度与线长的比例（限制箭头不过大） |
| `max_stroke_width_to_length_ratio` | float | 5 | 箭头最大宽度与线长比例 |
:::

额外的关键字参数（来自 `TipableVMobject` 机制）：

- `tip_shape` —— 箭头尖形状类，如 `tip_shape=StealthTip`
- `tip_style` —— 传给箭头尖构造器的样式字典，如 `tip_style={"fill_opacity": 0.5}`

:::demo examples/ch02/lines_arrows_demo.py LinesArrowsDemo
`Line` / `DashedLine` / `Arrow` / `DoubleArrow` / `Vector` 同台：注意 `Arrow` 默认 `buff=0.25`，箭身与端点之间留有缝隙；`tip_shape=StealthTip` 换成隐形战机风格的细长箭头。
:::

常见坑：v0.21.0 中 `Arrow` 的默认箭头尖是 `ArrowTriangleFilledTip`（实心三角），不是旧资料里常见的空心三角；箭头尖不会自动随 `buff` 缩放，短箭头配大 `buff` 会显得很挤。

## DoubleArrow

两端都有箭头尖的线，继承 `Arrow`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `tip_shape_start` | type[ArrowTip] | ArrowTriangleFilledTip | 起点处箭头尖形状 |
| `tip_shape_end` | type[ArrowTip] | ArrowTriangleFilledTip | 终点处箭头尖形状 |
:::

```python
DoubleArrow(LEFT, RIGHT, tip_shape_start=ArrowCircleFilledTip)
```

## Vector

从原点出发指向给定方向的箭头，继承 `Arrow`，常用于表示向量。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `direction` | Vector2DLike \| Vector3DLike | [1, 0, 0] | 向量方向（长度即箭头长度） |
| `buff` | float | 0 | 两端收缩量，默认不收缩 |
:::

```python
Vector([1, 2])          # 指向 (1, 2) 的向量
Vector(OUT)             # 指向屏幕外的 3D 向量
```

常见坑：`Vector` 的构造参数是**方向向量**而不是终点坐标，起点固定在 `ORIGIN`；想要任意起点的向量请用 `Arrow(start, end)`。

## Angle

`Angle` 在两条直线的交点处画出夹角弧线，可附带圆点、直角符号，并能读取角度值。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `line1` | Line | — | 第一条线 |
| `line2` | Line | — | 第二条线 |
| `radius` | float \| None | None | 弧线半径；None 时按两线长度自动取 |
| `quadrant` | AngleQuadrant | (1, 1) | 弧线所在的象限，如 (-1, 1) |
| `other_angle` | bool | False | True 时画反角（优角） |
| `dot` | bool | False | 是否在弧线中点加圆点 |
| `dot_radius` | float \| None | None | 圆点半径 |
| `dot_distance` | float | 0.55 | 圆点距交点的比例位置 |
| `dot_color` | ParsableManimColor | WHITE | 圆点颜色 |
| `elbow` | bool | False | True 时用直角折线代替弧线 |
:::

```python
angle = Angle(line1, line2, radius=0.6, dot=True)
angle.get_value()            # 弧度
angle.get_value(degrees=True)  # 角度
```

:::demo examples/ch02/angle_marks.py AngleMarks
`Angle` 带圆点并配合 `get_value(degrees=True)` 标注度数；`RightAngle` 画直角方块；`TangentLine` 在圆上 1/4 弧长处作切线。
:::

:::notice version
版本说明
在 v0.21.0 中，当两条直线**平行或共线**（无唯一交点）时，`Angle` 不再抛出 `ValueError`，而是退化为一个空 Mobject（`angle_value` 记为 0）。旧代码若依赖“平行线报错”的分支需要调整。
:::

常见坑：`quadrant` 的取值是 `(±1, ±1)` 四种组合，分别对应交点四周的四个角域；默认 `(1, 1)` 画的是两线正方向之间的角。

## RightAngle

直角的快捷写法：本质是 `Angle(line1, line2, radius=length, elbow=True)`，在交点画一个直角小方块。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `line1` | Line | — | 第一条线 |
| `line2` | Line | — | 第二条线 |
| `length` | float \| None | None | 方块边长；None 时自动 |
:::

## Elbow

`Elbow` 是一个独立的直角折角图形（两段等宽短边），继承 `VMobject`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `width` | float | 0.2 | 折角两段的宽度（边长） |
| `angle` | float | 0 | 整体旋转角度（弧度） |
:::

常见坑：`Elbow` 的角点默认在其包围盒中心附近，需要精确定位时配合 `move_to` / `shift` 调整。

## TangentLine

`TangentLine` 在任意 `VMobject` 路径的指定位置作切线段，继承 `Line`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `vmob` | VMobject | — | 目标图形（圆、曲线等） |
| `alpha` | float | — | 路径上的相对位置，0 到 1 |
| `length` | float | 1 | 切线段长度 |
| `d_alpha` | float | 1e-06 | 求导时使用的微小增量 |
:::

常见坑：`alpha` 是**归一化弧长比例**而不是角度；对闭合图形 0 和 1 都指向起点。

## TangentialArc

`TangentialArc` 过“切点”画一段与两条线都相切的圆弧，常用于表现圆角过渡；继承 `ArcBetweenPoints`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `line1` | Line | — | 第一条线 |
| `line2` | Line | — | 第二条线 |
| `radius` | float | — | 圆弧半径（圆角大小） |
| `corner` | tuple[float, float] | (1, 1) | 取两线哪一侧的夹角 |
:::

常见坑：`radius` 太大、超过两线交点附近可容纳的范围时，切点会落到线段之外，图形看起来“脱节”。

## TipableVMobject

`TipableVMobject` 是“可挂箭头尖”的 mixin 基类：`Line` 与 `Arc` 都继承它，因此直线和圆弧都能添加箭头尖（`CurvedArrow` 正是这样实现的）。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `tip_length` | float | 0.35 | 箭头尖默认长度 |
| `normal_vector` | Vector3DLike | [0, 0, 1] | 箭头尖朝向的法向量 |
| `tip_style` | dict \| None | None | 传给箭头尖构造器的默认样式 |
:::

常用方法：

```python
obj.add_tip()                                   # 终点加默认箭头尖
obj.add_tip(tip_shape=ArrowCircleTip)           # 指定形状
obj.add_tip(at_start=True)                      # 起点加箭头尖
obj.get_tip()                                   # 取终点箭头尖（可能为 None）
```

常见坑：`add_tip()` 返回的是 mobject 自身（链式调用安全），但箭头尖是**子 mobject**，`remove` 它请用 `obj.remove(obj.get_tip())`。

## ArrowTip

所有箭头尖的抽象基类，定义了箭头尖与线身衔接的接口（`base`、`tip_point`、`get_length` 等）。一般不直接实例化，而是通过 `tip_shape=` 传给 `Arrow`/`add_tip()`。

:::inheritance
ArrowTip → VMobject
:::

## ArrowTriangleTip

空心三角形箭头尖（默认描边、不填充），继承 `ArrowTip` 与 `Triangle`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `fill_opacity` | float | 0 | 填充不透明度（0 即空心） |
| `stroke_width` | float | 3 | 描边宽度 |
| `length` | float | 0.35 | 箭头尖长度 |
| `width` | float | 0.35 | 箭头尖宽度 |
| `start_angle` | float | PI | 箭头尖自身旋转角 |
:::

## ArrowTriangleFilledTip

实心三角形箭头尖，只改默认样式（填充 1、描边 0），行为与 `ArrowTriangleTip` 完全一致。

:::notice tip
提示
v0.21.0 中 `Arrow`、`Vector`、`DoubleArrow`、`CurvedArrow` 的默认箭头尖都是 `ArrowTriangleFilledTip`，不是它空心的兄弟类 `ArrowTriangleTip`。
:::

## ArrowCircleTip

空心圆形箭头尖，继承 `ArrowTip` 与 `Circle`。参数与 `ArrowTriangleTip` 相同（`fill_opacity=0`、`stroke_width=3`、`length=0.35`）。

## ArrowCircleFilledTip

实心圆形箭头尖，`ArrowCircleTip` 的实心版本（`fill_opacity=1`、`stroke_width=0`）。

## ArrowSquareTip

空心方形箭头尖，继承 `ArrowTip` 与 `Square`。参数与 `ArrowTriangleTip` 相同。

## ArrowSquareFilledTip

实心方形箭头尖，`ArrowSquareTip` 的实心版本。

## StealthTip

隐形战机（stealth）风格的箭头尖：更细长、默认填充，适合科技感的图示。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `length` | float | 0.175 | 箭头尖长度（比三角尖默认短） |
:::

```python
Arrow(LEFT, RIGHT, tip_shape=StealthTip)
```

:::compare
| 箭头尖 | 形状 | 默认填充 | 典型场景 |
| ------ | ---- | -------- | -------- |
| `ArrowTriangleTip` | 三角 | 空心 | 描边风格图示 |
| `ArrowTriangleFilledTip` | 三角 | 实心 | 默认箭头 |
| `ArrowCircleTip` | 圆形 | 空心 | 特殊标记 |
| `ArrowCircleFilledTip` | 圆形 | 实心 | 端点强调 |
| `ArrowSquareTip` | 方形 | 空心 | 工程图风格 |
| `ArrowSquareFilledTip` | 方形 | 实心 | 端点强调 |
| `StealthTip` | 细长多边形 | 实心 | 简约/科技感箭头 |
:::

## 常见错误与建议

:::notice warning
常见错误
箭头尖是子 mobject：对 `Arrow` 整体 `scale` 时箭头尖会跟着缩放，但对 `arrow.get_tip()` 单独 `scale` 后再 `add_tip` 会叠加缩放。需要固定尺寸箭头时设置 `max_tip_length_to_length_ratio`。
:::

:::notice tip
提示
`GrowArrow` 动画依赖 `scale(scale_tips=True)`，只适用于 `Arrow` / `Line` 系；对 `CurvedArrow` 请改用 `Create` 或 `FadeIn`。
:::

## 自测

:::exercise
如何把一根普通 `Line` 变成双头箭头，并且两端用不同形状的箭头尖？
:::answer
`Line` 继承自 `TipableVMobject`，直接调用 `add_tip()` 两次（其中一次 `at_start=True`）并分别指定 `tip_shape`：

```python
line = Line(LEFT, RIGHT)
line.add_tip(tip_shape=ArrowTriangleFilledTip)
line.add_tip(at_start=True, tip_shape=StealthTip)
```
:::
:::

## 下一步

下一节介绍圆弧与曲线家族：`Arc`、`CubicBezier` 以及由它们衍生的扇形、圆环与曲线箭头。
