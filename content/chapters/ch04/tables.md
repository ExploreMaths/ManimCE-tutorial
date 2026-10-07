---
title: 表格
---

# 表格

`manim.mobject.table` 模块用 Mobject 网格排版二维数据：`Table` 是基类，子类只决定**单元格内容的构造函数**（整数 / 小数 / 公式 / 任意 Mobject）。表格自带行列线、行列标签与单元格定位，是数据展示与“逐项讲解”的利器。

## Table

`Table` 把嵌套列表排成带线的网格。**字符串单元格默认由 `Paragraph` 渲染（Pango，不依赖 LaTeX）**，这是它与矩阵家族最大的不同。

:::inheritance
Table → VGroup → VMobject
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `table` | Iterable[Iterable[float \| str \| VMobject]] | — | 二维数据（必需）；每行长度必须一致 |
| `row_labels` | Iterable[VMobject] \| None | None | 行标签（Mobject，常用 `Text`） |
| `col_labels` | Iterable[VMobject] \| None | None | 列标签（Mobject） |
| `top_left_entry` | VMobject \| None | None | 同时有行列标签时，左上角单元格 |
| `v_buff` / `h_buff` | float | 0.8 / 1.3 | 行 / 列间距 |
| `include_outer_lines` | bool | False | 是否绘制外框线 |
| `include_inner_lines` | bool | True | 是否绘制内部网格线 |
| `add_background_rectangles_to_entries` | bool | False | 给每个单元格加背景矩形 |
| `element_to_mobject` | Callable \| type[VMobject] | Paragraph | 单元格构造函数（子类改写的核心） |
| `element_to_mobject_config` | dict | {} | 传给单元格构造函数的参数 |
| `line_config` | dict | {} | 行列线样式（`stroke_color` / `stroke_width` 等） |
:::

定位与高亮（行列标签存在时**占第 0 行/列**，坐标随之后移）：

- `table.get_cell((行, 列))` —— 返回该单元格的 `Polygon` 边框，1 起编号、含标签行列
- `table.get_entries(pos=None)` —— 传坐标返回单个单元格内容；不传返回全部 `VGroup`
- `table.get_highlighted_cell(pos, color=YELLOW, **kwargs)` —— 返回背景 `BackgroundRectangle`，**不会自动上屏**，需 `self.add(...)`
- `table.add_highlighted_cell(pos, color=YELLOW, **kwargs)` —— 一步到位：生成并直接加入背景层
- `table.get_rows()` / `get_columns()` / `get_horizontal_lines()` / `get_vertical_lines()` —— 取回行 / 列 / 线

:::demo examples/ch04/table_highlight.py TableHighlightDemo
纯字符串表格默认 `Paragraph` 渲染，无需 LaTeX；`get_highlighted_cell(...)` 生成背景矩形，手动 `add` 到对应单元格后面。
:::

:::notice warning
常见错误
`get_highlighted_cell()` 返回的矩形**不会自动显示**，忘记 `self.add(highlight)` 就看不到任何效果；嫌两步麻烦就改用 `add_highlighted_cell()`。
:::

:::notice warning
常见错误
行 / 列标签会计入 `get_cell` / `get_entries` 的坐标：带 `col_labels` 的表格里 `get_entries((2, 2))` 指的是**数据区**第 1 行第 1 列（标签行是第 0 行）。算坐标时先想清楚标签占不占位。
:::

## IntegerTable

`IntegerTable` 把每个单元格渲染为 `Integer`（整数逐位排版，需要 LaTeX）。

:::inheritance
IntegerTable → Table → VGroup
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `table` | Iterable[Iterable[float \| str]] | — | 二维数据（必需） |
| `element_to_mobject` | … | Integer | 单元格构造函数，一般保持默认 |
:::

:::demo examples/ch04/integer_table.py IntegerTableDemo
行列标签就是普通 `Text`；`get_cell((2, 3))` 在含标签的表格里按“标签占位后”的坐标取值。数字默认由 `MathTex` 逐位排版，依赖 LaTeX，本示例由 CI 渲染。
:::

## DecimalTable

`DecimalTable` 把每个单元格渲染为 `DecimalNumber`，默认保留 **1 位**小数，可用 `element_to_mobject_config` 调整。

:::inheritance
DecimalTable → Table → VGroup
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `table` | Iterable[Iterable[float \| str]] | — | 二维数据（必需） |
| `element_to_mobject_config` | dict | {'num_decimal_places': 1} | 透传给 `DecimalNumber`，常用 `num_decimal_places` |
:::

:::demo examples/ch04/decimal_table.py DecimalTableDemo
`element_to_mobject_config={"num_decimal_places": 2}` 统一小数位；`include_inner_lines=False` 可得到简洁的三线表风格。数字同样依赖 LaTeX，本示例由 CI 渲染。
:::

:::notice tip
提示
`IntegerTable` / `DecimalTable` 的数字字符默认走 `MathTex`（`mob_class` 是 `Integer` / `DecimalNumber` 的构造参数，无法通过 config 覆盖）。要完全摆脱 LaTeX，直接用 `Table(..., element_to_mobject=lambda x: Text(str(x)))` 即可——字符串单元格本来就不需要 LaTeX。
:::

## MathTable

`MathTable` 把每个单元格当作**公式**用 `MathTex` 渲染，适合符号运算表、函数值对照表。

:::inheritance
MathTable → Table → VGroup
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `table` | Iterable[Iterable[float \| str]] | — | 二维数据（必需），单元格是 LaTeX 片段 |
| `element_to_mobject` | … | MathTex | 单元格构造函数，一般保持默认 |
:::

:::demo examples/ch04/math_table.py MathTableDemo
单元格写 `x^2` 这类 LaTeX 片段即可自动排版；`get_entries((2, 2))` 取回单个单元格做强调。本示例依赖 LaTeX，由 CI 渲染。
:::

## MobjectTable

`MobjectTable` 把**任意 Mobject 直接当作单元格**，与 `MobjectMatrix` 同理，只是容器换成了表格（带网格线与定位 API）。

:::inheritance
MobjectTable → Table → VGroup
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `table` | Iterable[Iterable[VMobject]] | — | 由 Mobject 组成的二维数据（必需） |
| `element_to_mobject` | Callable | 恒等 lambda | 元素预处理函数，可自行替换 |
:::

:::demo examples/ch04/mobject_table.py MobjectTableDemo
图形单元格配合 `h_buff` 放大避免拥挤；`get_entries((1, 1))` 可直接取回某个图形做动画。单元格是矢量图形，不依赖 LaTeX。
:::

## 子类怎么选

:::compare
| 单元格内容 | 用谁 | LaTeX |
| ---- | ---- | ---- |
| 普通文字 / 数字文本 | `Table`（默认 `Paragraph`） | 不需要 |
| 整数运算结果 | `IntegerTable` | 需要（数字走 MathTex） |
| 测量数据、小数 | `DecimalTable` | 需要（数字走 MathTex） |
| 公式、符号 | `MathTable` | 需要 |
| 图形、图标 | `MobjectTable` | 不需要 |
:::

## 自测

:::exercise
`table.get_highlighted_cell((1, 2), color=RED)` 之后画面没有任何变化，为什么？
:::answer
`get_highlighted_cell()` 只**生成**背景矩形并返回，不会自动加入场景。需要 `self.add(highlight)`（或包进 `FadeIn` 动画）才能看到；改用 `add_highlighted_cell()` 则生成并添加一步到位。
:::
:::

:::exercise
带 `col_labels` 的表格上，`get_entries((1, 1))` 与 `get_entries((2, 1))` 分别取到什么？
:::answer
列标签占第 0 行：`(1, 1)` 是**列标签行**的第一个单元格（即第一个列标签），`(2, 1)` 才是数据区第一行第一列。行标签占第 0 列时同理——用坐标前先确认标签是否占位。
:::
:::

:::exercise
要在没装 LaTeX 的机器上展示一张全数字表格，有哪些可行方案？
:::answer
两种：一是直接用基类 `Table(..., element_to_mobject=lambda x: Text(str(x)))`，字符串单元格由 Pango 渲染；二是预先把数字格式化成字符串（如 `f"{v:.2f}"）再交给默认的 `Paragraph`。`IntegerTable` / `DecimalTable` 在这类环境会失败，因为它们的数字字符默认由 `MathTex` 排版。
:::
:::
