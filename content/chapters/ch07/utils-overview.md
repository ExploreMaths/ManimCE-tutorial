---
title: 实用工具速览
---

# 实用工具速览

`manim.utils` 是 Manim 的“工具箱”命名空间：五族函数（颜色、空间运算、迭代工具、路径、贝塞尔）支撑了内置 mobject 与动画的全部底层计算。写自定义对象和自定义动画时（见本板块前两节），你会频繁用到它们。以下导出名清单均以本机 v0.21.0 的实际导出为准。

## manim.utils.color

`ManimColor` 与全部颜色常量的家，ch02“颜色”一节已详细介绍核心类，这里补工具函数。

导出清单：

- 核心：`ManimColor`、`ParsableManimColor`、`ManimColorDType`、`RGBA`、`HSV`、`RandomColorGenerator`
- 常量：`WHITE`、`BLACK`、`GRAY/GREY` 系列、`RED/GREEN/BLUE/YELLOW/ORANGE/PURPLE/TEAL/MAROON/GOLD/PINK` 及各自 `_A`~`_E` 明度变体、`PURE_*`、`LOGO_*`、`DARK_*`、`LIGHT_*`
- 色板模块：`X11`、`XKCD`、`SVGNAMES`、`DVIPSNAMES`、`AS2700`、`BS381`（如 `X11.LIGHTSKYBLUE`）
- 工具函数：`interpolate_color`、`average_color`、`color_gradient`、`invert_color`、`random_color`、`random_bright_color`、`get_shaded_rgb`、`color_to_rgb`、`color_to_rgba`、`color_to_int_rgb`、`color_to_int_rgba`、`rgb_to_color`、`rgba_to_color`、`rgb_to_hex`、`hex_to_rgb`

```python
from manim import *

# 三种颜色等分渐变，取中间值
colors = color_gradient([BLUE, YELLOW, RED], 5)
interpolate_color(BLUE, RED, 0.3)   # 按 30% 插值

# 十六进制与 ManimColor 互转
rgb_to_hex(BLUE.to_rgb())           # '#58C4DD'
```

## manim.utils.space_ops

三维向量、角度与旋转的运算库，自定义几何计算的第一选择。

导出清单（27 个）：

`quaternion_mult`、`quaternion_from_angle_axis`、`angle_axis_from_quaternion`、`quaternion_conjugate`、`rotate_vector`、`thick_diagonal`、`rotation_matrix`、`rotation_about_z`、`z_to_vector`、`angle_of_vector`、`angle_between_vectors`、`normalize`、`get_unit_normal`、`compass_directions`、`regular_vertices`、`complex_to_R3`、`R3_to_complex`、`complex_func_to_R3_func`、`center_of_mass`、`midpoint`、`find_intersection`、`line_intersection`、`get_winding_number`、`shoelace`、`shoelace_direction`、`cross2d`、`earclip_triangulation`、`cartesian_to_spherical`、`spherical_to_cartesian`、`perpendicular_bisector`

```python
from manim import *

v = normalize(np.array([3.0, 4.0, 0.0]))        # [0.6, 0.8, 0]
a = angle_of_vector(RIGHT)                       # 0
rot = rotation_matrix(PI / 2, OUT)               # 绕 z 轴 90° 的 3x3 矩阵
w = rotate_vector(RIGHT, PI / 2)                 # 直接旋转向量
pts = regular_vertices(6, radius=2)              # 正六边形顶点
```

注意这些函数吃 NumPy 数组（`NDArray`），不吃 mobject——配合 `mob.get_center()`、`mob.get_vertices()` 使用。

## manim.utils.iterables

列表与序列的小工具，写 `generate_points` 或数据处理时很顺手。

导出清单（13 个）：`adjacent_n_tuples`、`adjacent_pairs`、`all_elements_are_instances`、`concatenate_lists`、`list_difference_update`、`list_update`、`listify`、`make_even`、`make_even_by_cycling`、`remove_list_redundancies`、`remove_nones`、`stretch_array_to_length`、`tuplify`

```python
from manim import *

adjacent_pairs([1, 2, 3, 4])
# [(1, 2), (2, 3), (3, 4)] —— 画折线、逐段动画时常用

make_even_by_cycling([1, 2, 3], 8)
# [1, 2, 3, 1, 2, 3, 1, 2] —— 把短列表循环补足到目标长度
```

## manim.utils.paths

`MoveAlongPath`、`.animate.path_arc` 等的路径函数来源，ch05“运动变形”一节已用到。

导出清单（4 个）：`straight_path`、`path_along_arc`、`clockwise_path`、`counterclockwise_path`

```python
from manim import *

# MoveAlongPath 默认走直线；path_along_arc 让点沿圆弧走
self.play(MoveAlongPath(dot, path), run_time=2)

# 给 .animate 指定弧线半径
self.play(dot.animate.path_arc(PI / 2).move_to(2 * UP))
```

`path_along_arc(arc_height)` 返回一个路径函数，也可以手动传给 `MoveAlongPath(mob, vmobject, path_func=...)` 风格的底层 API 或自定义动画。

## manim.utils.bezier

贝塞尔曲线计算内核：`VMobject.points` 的锚点/控制点语义就是这里定义的。

导出清单（14 个）：`bezier`、`partial_bezier_points`、`split_bezier`、`subdivide_bezier`、`bezier_remap`、`interpolate`、`integer_interpolate`、`mid`、`inverse_interpolate`、`match_interpolate`、`get_smooth_cubic_bezier_handle_points`、`is_closed`、`proportions_along_bezier_curve_for_point`、`point_lies_on_bezier`

```python
from manim import *

# bezier(points, t)：对任意阶贝塞尔曲线在参数 t 处求值
curve_pts = np.array([[0, 0, 0], [1, 2, 0], [3, 2, 0], [4, 0, 0]])
p = bezier(curve_pts, 0.5)      # t=0.5 处的点

# subdivide_bezier：把一条三次曲线一分为二，用于自适应加密
left, right = subdivide_bezier(curve_pts, 3)
```

## 常见错误与建议

:::notice warning
常见错误
`space_ops` 的函数不吃 `Mobject`。传 `Square()` 而不是 `square.get_center()` 会得到难以理解的广播错误。这是工具层与对象层的边界：对象层（`Mobject` 方法）处理 mobject，工具层处理裸数组。
:::

:::notice tip
提示
`from manim import *` 会把这些常用工具一并导入（`normalize`、`interpolate_color`、`bezier` 等都在顶层命名空间），不必写 `from manim.utils.space_ops import ...`。写库代码（插件）时才建议显式从 `manim.utils.*` 导入。
:::

## 自测

:::exercise
自定义动画里需要让一个点绕原点匀速转 90°，用 `manim.utils.space_ops` 里的哪个函数最直接？
:::answer
`rotate_vector(vector, angle)`：直接返回旋转向量，配合 `interpolate` 或在插值钩子里按 alpha 计算角度即可。若需要旋转矩阵（例如同时转多个向量），用 `rotation_matrix(angle, OUT)`。
:::
:::

:::exercise
`adjacent_pairs` 和 `make_even_by_cycling` 各适合什么场景？
:::answer
`adjacent_pairs` 返回相邻元素对，适合“逐段处理”的任务：给折线每段着色、对相邻顶点连线等。`make_even_by_cycling` 把列表循环复制到指定长度，适合两组数据点数不对齐时（例如两组顶点一一配对前先把短的一组补齐）。
:::
:::

## 下一步

工具箱盘点完毕。最后一节收拢散落各处的杂项：`add_sound`、`interactive_embed` 两个场景方法，以及一组调试小工具。
