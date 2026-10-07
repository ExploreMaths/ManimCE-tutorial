---
title: 标注与装饰
---

# 标注与装饰

本节覆盖“给已有内容加标注”的一族工具：包围框、背景框、叉号、下划线、标签、大括号。它们大多不改变被标注对象本身，而是作为独立的 mobject 叠加在画面上。

## SurroundingRectangle

`SurroundingRectangle` 画一个紧贴目标外围的矩形框，是最常用的强调手段。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `*mobjects` | Mobject | — | 被包围的对象（多个时取整体包围盒） |
| `color` | ParsableManimColor | YELLOW | 框线颜色 |
| `buff` | float \| tuple[float, float] | 0.1 | 与目标的间距，可分别指定横向/纵向 |
| `corner_radius` | float | 0.0 | 圆角半径；大于 0 时边角变圆 |
:::

:::inheritance
SurroundingRectangle → RoundedRectangle → Rectangle → Polygon → VMobject
:::

常见坑：矩形框是**静态快照**——目标随后移动时框不会跟随，需要配合 updater 或每帧重算。

## BackgroundRectangle

`BackgroundRectangle` 画一个填充的“背景垫”，常垫在文字下方提高可读性。继承 `SurroundingRectangle`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `*mobjects` | Mobject | — | 被垫底的对象 |
| `color` | ParsableManimColor \| None | None | 填充色；None 时取 `config.background_color` |
| `stroke_width` | float | 0 | 描边宽度（默认无） |
| `fill_opacity` | float | 0.75 | 填充不透明度 |
| `buff` | float \| tuple[float, float] | 0 | 与目标的间距（默认贴紧） |
:::

常见坑：在浅背景上把 `color` 留 None 会得到“背景色垫”，等于隐形；需要深色垫时显式传 `color=BLACK`。

## Cross

`Cross` 在目标位置画一个“X”形叉号，表示否定、删除或错误。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `mobject` | Mobject \| None | None | 叉号中心对齐的目标；None 时画在原点附近的小叉 |
| `stroke_color` | ParsableManimColor | #FC6255 | 叉号线颜色 |
| `stroke_width` | float | 6.0 | 线宽 |
| `scale_factor` | float | 1.0 | 相对目标尺寸的缩放 |
:::

:::inheritance
Cross → VGroup
:::

常见坑：`Cross` 是一个 `VGroup`（两条线），对它整体 `set_color` 只影响默认色，若已显式传过 `stroke_color` 需要 `set_stroke` 修改。

## Underline

`Underline` 在目标正下方画一条下划线，继承 `Line`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `mobject` | Mobject | — | 被划线的对象 |
| `buff` | float | 0.1 | 线与目标底边的间距 |
:::

```python
underline = Underline(formula, buff=0.15, color=BLUE)
```

## Label

`Label` 是 v0.21 标签三件套（`Label` / `LabeledLine` / `LabeledArrow` / `LabeledPolygram`）的基类：一个文本外加背景垫与边框组成的 `VGroup`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `label` | str \| ManimTextLabel | — | 文本；str 时默认用 `MathTex` 渲染，也可直接传 `Text` / `MathTex` / `Typst` 实例 |
| `label_config` | dict \| None | None | 文本构造参数（如 `font_size`、`color`） |
| `box_config` | dict \| None | None | 背景垫 `BackgroundRectangle` 的参数 |
| `frame_config` | dict \| None | None | 边框 `SurroundingRectangle` 的参数 |
:::

```python
Label("x+y", label_config={"font_size": 36})
Label(Text("速度", font_size=36), box_config={"fill_opacity": 0})
```

常用属性：`label.rendered_label`（文本本体）、`label.background_rect`（背景垫）、`label.frame`（边框）。

## LabeledLine

带标签的线段：标签沿线段按 `label_position` 比例定位。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `label` | str \| ManimTextLabel | — | 标签文本（同 Label） |
| `label_position` | float | 0.5 | 标签在线段上的比例位置，0 起点、1 终点 |
| `label_config` | dict \| None | None | 文本样式 |
| `box_config` | dict \| None | None | 背景垫样式 |
| `frame_config` | dict \| None | None | 边框样式 |
| `*args, **kwargs` | Any | — | 其余参数同 `Line`（`start`、`end`、`color` 等） |
:::

```python
LabeledLine(label="a", label_position=0.3, start=LEFT * 3, end=RIGHT * 3)
```

:::inheritance
LabeledLine → Line → TipableVMobject → VMobject
:::

## LabeledArrow

`LabeledArrow` 多重继承 `LabeledLine` 与 `Arrow`：既是一根带箭头尖的线，又带沿线定位的标签。参数同 `LabeledLine`，可直接传 `Text` 实例作标签。

```python
LabeledArrow(label=Text("v", font_size=36), start=LEFT, end=RIGHT)
```

:::inheritance
LabeledArrow → LabeledLine → Line
:::

## LabeledPolygram

`LabeledPolygram` 在任意多边形（`Polygram`）中心放置标签。标签位置不是简单的几何中心，而是多边形的**不可达极点**（pole of inaccessibility，距离所有边最远的内点），对凹多边形也能把标签放在“最深处”。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `*vertex_groups` | Point3DLike_Array | — | 顶点组，同 `Polygram`（每组自动首尾闭合） |
| `label` | str \| ManimTextLabel | — | 标签文本 |
| `precision` | float | 0.01 | 极点求解精度 |
| `label_config` | dict \| None | None | 文本样式 |
:::

常用属性：`poly.pole`（极点坐标）、`poly.radius`（极点到边界的最小距离）。

:::demo examples/ch02/annotations_demo.py AnnotationsDemo
`SurroundingRectangle` / `BackgroundRectangle` / `Underline` 强调公式，`Cross` 表示否定后消失；下方依次是 `LabeledLine`（标签在 30% 处）、`LabeledArrow`（Text 标签）与 `LabeledPolygram`（标签位于三角形极点）。
:::

## Brace

`Brace` 在一侧画一个大括号 `{`，常用于标注长度、配文字说明。它继承 `VMobjectFromSVGPath`——内部把大括号当作一段 SVG 路径解析。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `mobject` | Mobject | — | 被标注的对象 |
| `direction` | Vector3DLike | [0, -1, 0] | 大括号开口朝向（默认向下） |
| `buff` | float | 0.2 | 与目标的间距 |
| `sharpness` | float | 2 | 大括号的尖锐程度 |
| `stroke_width` | float | 0 | 描边宽度（默认纯填充） |
| `fill_opacity` | float | 1.0 | 填充不透明度 |
:::

配套方法：`brace.get_text("...")`、`brace.get_tex("...")` 可快速生成放在大括号旁的文字。

常见坑：大括号不会随目标自动伸缩——目标尺寸变化后需要重新构造 `Brace` 或手动 `brace.scale_to_fit_width(...)`；`get_text`/`get_tex` 返回的文字也要自己 `next_to(brace, ...)` 定位。

## BraceBetweenPoints

`BraceBetweenPoints` 在两个点之间画大括号，不用先有 mobject。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `point_1` | Point3DLike | — | 起点 |
| `point_2` | Point3DLike | — | 终点 |
| `direction` | Vector3DLike | [0, 0, 0] | 开口方向；零向量时自动取垂直方向 |
:::

:::inheritance
BraceBetweenPoints → Brace → VMobjectFromSVGPath → VMobject
:::

## BraceLabel

`BraceLabel` 是“大括号 + 文字”的组合：构造后文字自动放在大括号外侧。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `obj` | Mobject | — | 被标注的对象 |
| `text` | str | — | 标注文字 |
| `brace_direction` | Vector3DLike | [0, -1, 0] | 大括号开口方向 |
| `label_constructor` | type | MathTex | 文字构造器（`MathTex` 或 `Text`） |
| `font_size` | float | 48 | 文字字号 |
| `buff` | float | 0.2 | 文字与大括号的间距 |
| `brace_config` | dict \| None | None | 传给 `Brace` 的参数 |
:::

常用属性：`bl.brace`（大括号）、`bl.label`（文字）。

## BraceText

`BraceText` 继承 `BraceLabel`，唯一区别是 `label_constructor` 默认是 `Text` 而非 `MathTex`——标注纯文本时少写一个参数。

```python
BraceText(rectangle, "width = 4")            # 用 Text 渲染
BraceLabel(rectangle, "w=4")                 # 用 MathTex 渲染
```

## ArcBrace

`ArcBrace` 沿一段 `Arc` 画大括号（常用于标注角度或弧长），继承 `Brace`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `arc` | Arc \| None | None | 被标注的圆弧；None 时默认一段单位圆弧 |
| `direction` | Vector3DLike | [1, 0, 0] | 大括号整体朝向 |
| `**kwargs` | Any | — | 其余参数同 `Brace` |
:::

```python
arc = Arc(radius=1.5, start_angle=PI / 4, angle=PI / 2)
arc_brace = ArcBrace(arc)
```

:::demo examples/ch02/braces_demo.py BracesDemo
上方是 `Brace` + `BraceText` 标注矩形宽度；左下是 `BraceBetweenPoints` 与 `BraceLabel`（MathTex 标签）标注两点间距离；右下是 `ArcBrace` 标注圆弧。
:::

## 常见错误与建议

:::notice warning
常见错误
所有标注类都是**独立 mobject**，不会跟随目标。给移动中的目标加框请用 updater：`box.add_updater(lambda b: b.become(SurroundingRectangle(target)))`。
:::

:::notice tip
提示
`Label` 家族的文本默认用 `MathTex` 渲染，传普通中文或句子时请直接传 `Text(...)` 实例，或设置 `label_constructor`（`BraceLabel` 系列），否则特殊字符会按 LaTeX 语法解析报错。
:::

## 自测

:::exercise
一个正方形在画面中左右往返移动，如何让它外围的黄色矩形框始终贴着它？
:::answer
给包围框加 updater，每帧重建自身：

```python
frame = SurroundingRectangle(square, color=YELLOW)
frame.add_updater(lambda f: f.become(SurroundingRectangle(square, color=YELLOW)))
self.add(frame)
```
:::
:::

## 下一步

下一节介绍如何加载位图与 SVG 图形：`ImageMobject` 与 `SVGMobject`。
