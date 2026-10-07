---
title: 坐标系家族
---

# 坐标系家族

坐标系把“数据坐标”翻译成“场景位置”，是函数绘图和数据可视化的舞台。家族成员都围绕 `CoordinateSystem` 的坐标互转 API 构建，再各自叠加网格、刻度或极坐标线。

:::inheritance
CoordinateSystem → object
:::

:::inheritance
Axes → VGroup
:::

:::inheritance
NumberPlane → Axes → VGroup
:::

:::inheritance
ComplexPlane → NumberPlane → Axes
:::

:::inheritance
PolarPlane → Axes → VGroup
:::

:::inheritance
ThreeDAxes → Axes → VGroup
:::

## CoordinateSystem

`CoordinateSystem` 是**抽象基类**，本身不可实例化（`get_axis_labels()` 直接抛 `NotImplementedError`）。它的价值在于定义了所有坐标系共享的核心 API：

- **坐标互转**：`coords_to_point(*coords)`（别名 `c2p`）与 `point_to_coords(point)`（别名 `p2c`）；`NumberLine` 上的 `number_to_point`/`point_to_number` 是一维版本
- **绘图**：`plot`、`plot_parametric_curve`、`plot_implicit_curve`、`plot_polar_graph`、`plot_derivative_graph`、`plot_antiderivative_graph`、`plot_surface`（详见“函数绘图”一节）
- **辅助线**：`get_vertical_line(point)`、`get_horizontal_line(point)`、`get_line_from_axis_to_point(index, point)`（从坐标轴指向点的虚线）
- **面积与积分**：`get_area(graph, ...)`、`get_riemann_rectangles(...)`
- **标签**：`get_axis_labels()`（子类实现）、`get_graph_label(graph, label, x_val=..., dot=...)`、`get_T_label(...)`
- **切线**：`slope_of_tangent(x, graph)`、`angle_of_tangent(...)`、`get_secant_slope_group(...)`

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `x_range` | Sequence[float] \| None | None | x 轴范围 `(起, 止, 步长)` |
| `y_range` | Sequence[float] \| None | None | y 轴范围 |
| `x_length` | float \| None | None | x 轴物理长度（场景单位） |
| `y_length` | float \| None | None | y 轴物理长度 |
| `dimension` | int | 2 | 坐标系维数 |
:::

:::notice warning
常见错误
旧教程里的 `axes.get_graph(lambda x: x**2)` **在 v0.21.0 已不存在**（`Axes` 上没有 `get_graph` 方法），统一改用 `axes.plot(...)`。同理 `get_graph_label` 属于坐标系而不是图对象：`axes.get_graph_label(graph, "f(x)")`。
:::

## Axes

`Axes` 是标准的**直角坐标系**：x 轴 + y 轴（两条 `NumberLine`），默认带箭头、无网格。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `x_range` | Sequence[float] \| None | (-7.11, 7.11, 1) | x 轴范围，按 `x_length` 自动取整 |
| `y_range` | Sequence[float] \| None | (-4, 4, 1) | y 轴范围 |
| `x_length` | float \| None | 12 | x 轴长度 |
| `y_length` | float \| None | 6 | y 轴长度 |
| `axis_config` | dict \| None | None | 同时作用于两条轴的 `NumberLine` 配置 |
| `x_axis_config` / `y_axis_config` | dict \| None | None | 单轴配置，优先级高于 `axis_config` |
| `tips` | bool | True | 是否显示轴末端箭头 |
:::

`Axes` 的两个子对象可通过 `axes.get_x_axis()` / `axes.get_y_axis()` 取回（它们就是 `NumberLine`）；`axes.get_origin()` 返回原点场景位置。`axes.get_axis_labels(x_label="x", y_label="y")` 返回默认的 LaTeX 轴标签（也可传入 `Text` 等 Mobject）。

:::demo examples/ch04/axes_basic.py AxesDemo
`coords_to_point(2, 1)` 把数据坐标翻译成场景坐标；配合 `point_to_coords` 可以在几何位置与数据坐标之间自由往返。
:::

:::notice tip
提示
坐标轴本质上就是 `NumberLine`，所以数轴的所有配置都能用：给某条轴加数字只需 `axes.get_x_axis().add_numbers()`；对数坐标则用 `x_axis_config={"scaling": LogBase(base=10)}`。
:::

## NumberPlane

`NumberPlane` 在 `Axes` 基础上铺满**背景网格线**（主实线 + 次淡化线），是默认的“草稿纸”。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `x_range` / `y_range` | Sequence[float] \| None | (-7.11, 7.11, 1) / (-4, 4, 1) | 网格范围（默认与 16:9 画幅适配） |
| `x_length` / `y_length` | float \| None | None | 平面尺寸，None 时按画幅自动计算 |
| `background_line_style` | dict \| None | None | 主网格线样式（`stroke_color` / `stroke_opacity` 等） |
| `faded_line_style` | dict \| None | None | 次网格线样式 |
| `faded_line_ratio` | int | 1 | 每个主间隔中淡化线的数量 |
| `make_smooth_after_applying_functions` | bool | True | 应用函数变换后是否平滑网格 |
:::

默认**不显示数字**；需要坐标数字时调用 `plane.add_coordinates()`（走 LaTeX）或自行 `add_labels`。

:::demo examples/ch04/number_plane.py NumberPlaneDemo
`faded_line_ratio=2` 让每个主间隔出现两条淡化线；淡化线很适合营造“坐标纸”质感而不喧宾夺主。
:::

## ComplexPlane

`ComplexPlane` 把平面解释为**复平面**：`number_to_point` 接受复数（如 `2 + 1j`），`point_to_number` 返回复数。构造参数与 `NumberPlane` 完全一致（`__init__(self, **kwargs)` 全部转发），只额外提供复数语义的转换方法。

:::demo examples/ch04/complex_plane.py ComplexPlaneDemo
`plane.number_to_point(2 + 1j)` 一步到位；`point_to_number` 是它的逆运算，返回 `complex`。
:::

常用搭配：

- `plane.add_coordinates()` —— 同时添加实轴、虚轴数字（LaTeX）
- `plane.get_coordinate_labels(...)` —— 更精细的坐标标签控制
- `z_to_point` 的等价写法：复数可直接传给 `number_to_point`

## PolarPlane

`PolarPlane` 绘制**极坐标网格**：同心圆（半径）+ 放射线（方位角）。它同样继承 `Axes` 的 `plot` 家族，并额外提供 `polar_to_point(radius, azimuth)` / `point_to_polar(point)`（别名 `pr2pt` / `pt2pr`）。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `radius_max` | float | 4.0 | 最大半径 |
| `size` | float \| None | None | 平面直径；None 时按 `radius_max` 推算 |
| `radius_step` | float | 1 | 半径网格间隔 |
| `azimuth_step` | float \| None | None | 方位角网格间隔（None 自动） |
| `azimuth_units` | str | "PI radians" | 方位角标签单位，可选 `"PI radians"` / `"TAU radians"` / `"degrees"` / `"gradians"` / None |
| `azimuth_compact_fraction` | bool | True | 标签用 π 的紧凑分数形式 |
| `azimuth_offset` | float | 0 | 角度标签偏移 |
| `azimuth_direction` | str | "CCW" | 角度增大方向（`"CCW"` 逆时针） |
| `radius_config` | dict \| None | None | 半径轴（NumberLine）配置 |
| `background_line_style` / `faded_line_style` / `faded_line_ratio` | — | — | 同 `NumberPlane` |
:::

:::notice warning
版本说明
网上旧资料常说 PolarPlane 默认角度单位是**度**——**在 v0.21.0 不正确**。默认 `azimuth_units="PI radians"`，角度标签渲染为 `PI/4` 这样的 LaTeX；要十进制度请显式传 `azimuth_units="degrees"`。注意 `get_coordinate_labels()` 生成的标签依赖 LaTeX。
:::

:::demo examples/ch04/polar_plane.py PolarPlaneDemo
继承自 `Axes`，所以 `plot_polar_graph(r_func, theta_range=...)` 可直接使用；`r_func` 输入弧度制的 θ，输出半径。
:::

## ThreeDAxes

`ThreeDAxes` 增加一条 **z 轴**，组成三维直角坐标系。在普通 `Scene` 中它以固定的斜投影显示；真正的 3D 交互（旋转视角、设置相机）要配合 `ThreeDScene` 使用，见“3D 与摄像机”板块。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `x_range` / `y_range` / `z_range` | Sequence[float] \| None | (-6, 6, 1) / (-5, 5, 1) / (-4, 4, 1) | 三个轴的范围 |
| `x_length` / `y_length` / `z_length` | float \| None | 10.5 / 10.5 / 6.5 | 三个轴的物理长度 |
| `z_axis_config` | dict \| None | None | z 轴（`NumberLine`）配置 |
| `z_normal` | Vector3DLike | (0, -1, 0) | z 轴“朝向上方”的方向参考 |
| `num_axis_pieces` | int | 20 | 每个轴的分段数 |
:::

`coords_to_point` 在此接受**三个**坐标；`get_z_axis()` 取回 z 轴。

:::demo examples/ch04/three_d_axes.py ThreeDAxesDemo
普通 `Scene` 里 `ThreeDAxes` 以斜投影静态呈现；给它加 `Dot3D` 标记空间点，后续移入 `ThreeDScene` 即可获得完整 3D 体验。
:::

## 成员怎么选

:::compare
| 需求 | 用谁 |
| ---- | ---- |
| 只要两条轴、画函数图像 | `Axes` |
| 需要网格背景 | `NumberPlane` |
| 复数运算可视化 | `ComplexPlane` |
| 极坐标方程、角度数据 | `PolarPlane` |
| 空间曲线/曲面 | `ThreeDAxes` + `ThreeDScene`（ch06） |
| 数据柱状图 | `BarChart`（见“概率与图表”） |
:::

## 自测

:::exercise
已知 `plane = NumberPlane(x_range=[-4, 4, 1], y_range=[-3, 3, 1], x_length=8, y_length=6)`，`plane.coords_to_point(2, 1)` 大约在场景什么位置？（原点即平面中心）
:::answer
x 方向 `unit_size = 8 / 8 = 1`，y 方向 `unit_size = 6 / 6 = 1`，所以结果约为 `(2, 1, 0)`。一般地：`coords_to_point` 的结果 = 原点 + `(x * x_unit_size, y * y_unit_size)`，可用 `plane.get_x_unit_size()` / `get_y_unit_size()` 查询。
:::
:::

:::exercise
旧脚本里有一句 `graph = axes.get_graph(np.sin)`，在 v0.21.0 下如何修改？
:::answer
改为 `graph = axes.plot(np.sin)`。`get_graph` 已在重构中移除；返回值是 `ParametricFunction`，后续 `axes.get_area(graph, ...)`、`axes.get_graph_label(graph, ...)` 的用法不变。
:::
:::

:::exercise
想让 `PolarPlane` 的角度标签显示为十进制度（如 45°），怎么做？
:::answer
构造时传 `azimuth_units="degrees"`；若还想要 ° 符号或自定义格式，可传 `azimuth_units=None` 后自行用 `add_labels` 添加 `Text` 标签。
:::
:::
