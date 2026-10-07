---
title: 概率与图表
---

# 概率与图表

`manim.mobject.graphing.probability` 模块提供两块可视化工具：`SampleSpace` 把矩形按概率划分成若干块（面积 = 概率），`BarChart` 在 `Axes` 基础上画出柱状图。

## SampleSpace

`SampleSpace` 是一个**可按比例横向/纵向划分的矩形**，常用来表示概率论中的样本空间：每个子矩形对应一个事件，视觉面积正比于概率。

:::inheritance
SampleSpace → Rectangle → Polygon → Polygram → VMobject
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `height` | float | 3 | 矩形高度 |
| `width` | float | 3 | 矩形宽度 |
| `fill_color` | ParsableManimColor | '#444444' | 填充色 |
| `fill_opacity` | float | 1 | 填充不透明度 |
| `stroke_width` | float | 0.5 | 边框线宽 |
| `stroke_color` | ParsableManimColor | '#BBBBBB' | 边框颜色 |
| `default_label_scale_val` | float | 1 | 内置标签的缩放系数 |
:::

划分 API 是一对镜像方法：

- `space.divide_vertically(p_list, colors=[MAROON_B, YELLOW], vect=RIGHT)` —— 沿**宽度**切成竖条
- `space.divide_horizontally(p_list, colors=[GREEN, BLUE], vect=DOWN)` —— 沿**高度**切成横条

`p_list` 是**单个位置参数**（比例列表，也可只传一个浮点数），各块颜色从 `colors` 渐变生成；比例总和小于 1 时 `complete_p_list` 自动补一块“余量”，等于 1 则不补。划分结果存入动态属性 `space.vertical_parts` / `space.horizontal_parts` 并自动加入场景树。

:::demo examples/ch04/sample_space.py SampleSpaceDemo
`divide_vertically([0.5, 0.3, 0.2])` 把矩形切成三条；划分结果存在 `vertical_parts` 里，可据此用 `Brace` + `Text` 手工标注各块比例。
:::

:::notice warning
常见错误
`p_list` 不是可变参数：`space.divide_vertically(0.5, 0.3, 0.2)` 会把第二个数 `0.3` 当成 `colors` 传入并触发 `TypeError`——正确写法是传一个列表。另外比例总和**大于** 1 时余量为负，会产生朝反方向拉伸的怪块，请自行保证总和 ≤ 1。
:::

:::notice warning
版本说明
v0.21.0 中 `SampleSpace.get_subdivision_braces_and_labels(...)` **存在 bug**：它把 `min_num_quads` 传给 `Brace`，而 `Brace` 不接受该参数，调用必然抛出 `TypeError: Mobject.__init__() got an unexpected keyword argument 'min_num_quads'`。本版本请用 `Brace(part, direction)` + `Text` 手工组合代替（如上方示例）。
:::

## BarChart

`BarChart` 是**柱状图**：内部就是一台 `Axes`（x 轴为类别序号、y 轴为数值，无箭头），柱条是立在 x 轴上的矩形，`values` 决定柱高。

:::inheritance
BarChart → Axes → VGroup
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `values` | MutableSequence[float] | — | 各柱高度（必需） |
| `bar_names` | Sequence[str] \| None | None | x 轴类别名；None 则不显示 |
| `y_range` | Sequence[float] \| None | None | None 时按数据自动取（下界取 `min(0, 最小值)`） |
| `x_length` / `y_length` | float \| None | None | 图表尺寸；None 时按画幅自动 |
| `bar_colors` | Iterable[str] | 五色列表 | 柱条配色，按序循环取用 |
| `bar_width` | float | 0.6 | 柱条宽度（x 轴坐标单位） |
| `bar_fill_opacity` | float | 0.7 | 填充不透明度 |
| `bar_stroke_width` | float | 3 | 描边宽度 |
:::

:::demo examples/ch04/bar_chart.py BarChartDemo
`change_bar_values(...)` 按新数据瞬时重设柱高；`get_bar_labels(...)` 按**当前**柱高生成柱顶数值标签。
:::

本示例的类别名与数值标签默认由 `Tex` 渲染，依赖 LaTeX，由 CI 渲染。

常用操作：

- `chart.bars` —— 柱条 `VGroup`，可按索引单独着色、位移
- `chart.change_bar_values(values, update_colors=True)` —— **瞬时**更新柱高（见下方提示），数量不必与原始柱数一致，按序取 `zip` 对齐
- `chart.get_bar_labels(color=None, font_size=24, buff=0.25, label_constructor=Tex)` —— 生成数值标签 `VGroup`，调用后也可用 `chart.bar_labels` 取回；标签不会自动上屏，需 `add` 或 `play(FadeIn(...))`
- `chart.x_axis` / `chart.y_axis` —— 就是 `Axes` 的两条轴，可 `add_numbers()` 等

:::notice warning
常见错误
`change_bar_values()` **不播放动画**：它直接拉伸/移动柱条，画面瞬间跳变。想要平滑过渡，请自己对 `chart.bars` 施加 `Transform` / `.animate`，或配合 `self.play(...)` 手工编排。
:::

:::notice warning
常见错误
`get_bar_labels()` 要在 `change_bar_values(...)` **之后**调用才拿得到新值；顺序反了标签会停留在旧数值上。
:::

:::notice tip
提示
不想依赖 LaTeX 时，给 x 轴换标签构造器即可：构造时传 `x_axis_config={"label_constructor": Text}`（类别名与轴数字会改用 Pango 渲染）；`get_bar_labels(label_constructor=Text)` 同理。
:::

## 自测

:::exercise
`space.divide_vertically([0.2, 0.3])` 之后样本空间里有几块？比例各是多少？
:::answer
三块。比例总和为 0.5，小于 1 的部分由 `complete_p_list` 自动补齐为余量块：`[0.2, 0.3, 0.5]`。若总和恰好等于 1 则不会补块。
:::
:::

:::exercise
想让人物讲解时柱状图“长高”的过程平滑可见，直接把 `chart.change_bar_values([...])` 写进 `construct()` 为什么不行？应该怎么写？
:::answer
`change_bar_values()` 是瞬时更新，没有动画过程。平滑效果需要自己播动画，例如先用旧数据建图，再对柱条逐个 `Transform`：`self.play(*[Transform(old, new) for old, new in zip(chart.bars, chart.bars.copy())])` 的等价思路——更常见的做法是保存旧柱的副本，计算新高度后 `self.play(*[bar.animate.stretch_to_fit_height(h) for ...])` 逐根拉伸。
:::
:::

:::exercise
在没装 LaTeX 的机器上运行带 `bar_names` 的 `BarChart`，会在哪一步报错？如何规避？
:::answer
构造 `BarChart` 时就会报错：类别名走 `Tex`、y 轴数字也走 `Tex`，任何一处都会触发 LaTeX 编译。规避方法是传 `x_axis_config={"label_constructor": Text}` 把轴标签换成 Pango 渲染（`y_axis_config` 同理），`get_bar_labels` 传 `label_constructor=Text`。
:::
:::
