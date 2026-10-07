---
title: 向量空间场景
---

# 向量空间场景

`manim.scene.vector_space_scene` 提供两个教学向的场景基类：`VectorScene` 在网格背景上**画向量、标注坐标**，`LinearTransformationScene` 把整张网格当作向量空间，**以动画演示矩阵乘法**（3Blue1Brown 线性代数系列的核心场景）。

## VectorScene

`VectorScene` 继承普通 `Scene`，额外提供网格背景与一整套向量操作：加向量、贴标签、写坐标、坐标与向量的双向演示。

:::inheritance
VectorScene → Scene
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `basis_vector_stroke_width` | float | 6.0 | 基向量（i / j 帽）的线宽 |
:::

场景辅助（默认背景**没有**网格，需要时自行添加）：

- `self.add_plane(animate=False, **kwargs)` —— 添加 `NumberPlane` 背景
- `self.add_axes(animate=False, color=WHITE)` —— 只添加 `Axes`
- `self.lock_in_faded_grid(dimness=0.7, axes_dimness=0.5)` —— 常用开场：淡化网格 + 坐标轴锁定在底层

向量操作：

- `self.add_vector(vector, color=YELLOW, animate=True, **kwargs)` —— 画向量并播放 `GrowArrow`，返回 `Arrow`；`vector` 可传坐标序列
- `self.label_vector(vector, label, animate=True, **kwargs)` —— 给向量贴标签（`Text` / `MathTex` 均可），返回标签
- `self.get_vector(numerical_vector, **kwargs)` —— 只创建不播放，返回 `Arrow`
- `self.write_vector_coordinates(vector, **kwargs)` —— 写出向量的坐标矩阵 `Matrix`
- `self.vector_to_coords(vector, integer_labels=True, clean_up=True)` —— 演示“向量 → 坐标”：返回 `(坐标矩阵, x 虚线, y 虚线)`，`clean_up=False` 保留辅助线
- `self.coords_to_vector(coords, coords_start=(2, 2, 0), clean_up=True)` —— 反向演示“坐标 → 向量”

:::demo examples/ch04/vector_scene.py VectorSceneDemo
`add_vector` 默认播放生长动画并返回 `Arrow`，返回值要接住才能继续 `label_vector`；标签用 `Text` 渲染即可，不依赖 LaTeX。
:::

:::notice tip
提示
`VectorScene` 的网格不会自动出现——`add_plane()` / `lock_in_faded_grid()` 二选一。只做向量加减讲解时 `lock_in_faded_grid()` 的淡化网格最省心；需要读坐标时再用 `add_plane()` 配合 `show_coordinates` 风格的显式网格。
:::

## LinearTransformationScene

`LinearTransformationScene` 继承 `VectorScene`，专为**线性变换动画**设计：场景自带背景网格与前景网格，以及 i 帽 / j 帽两个基向量；`apply_matrix(...)` 会把整个空间（网格、基向量、所有“可变换对象”）按矩阵逐一变换。

:::inheritance
LinearTransformationScene → VectorScene → Scene
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `include_background_plane` | bool | True | 底层淡化网格 |
| `include_foreground_plane` | bool | True | 顶层“会变形的”网格 |
| `background_plane_kwargs` / `foreground_plane_kwargs` | dict \| None | None | 两层 `NumberPlane` 的配置 |
| `show_coordinates` | bool | False | 是否显示网格坐标数字 |
| `show_basis_vectors` | bool | True | 是否显示 i 帽 / j 帽 |
| `basis_vector_stroke_width` | float | 6 | 基向量线宽 |
| `i_hat_color` | ParsableManimColor | '#83C167' | i 帽颜色（绿） |
| `j_hat_color` | ParsableManimColor | '#FC6255' | j 帽颜色（红） |
| `leave_ghost_vectors` | bool | False | 变换时是否留下基向量的“残影”轨迹 |
:::

变换方法：

- `self.apply_matrix(matrix, **kwargs)` —— 播放线性变换动画；`matrix` 为 2×2（列是 i 帽 / j 帽的新位置）
- `self.apply_inverse(matrix, **kwargs)` / `apply_transposed_matrix(...)` / `apply_inverse_transpose(...)` —— 逆 / 转置 / 逆转置
- `self.apply_nonlinear_transformation(function, **kwargs)` —— 任意 `R² → R²` 函数变换（如 `lambda p: p + np.array([np.sin(p[1]), 0, 0])`）
- `self.add_unit_square(animate=False, **kwargs)` —— 添加单位正方形（默认不播动画）
- `self.add_transformable_mobject(*mobjects)` —— 注册自定义对象，变换时随网格一起变形
- `self.add_transformable_label(vector, label, transformation_name="L", new_label=None, **kwargs)` —— 给基向量添加会跟随变换的标注（`MathTex`）
- `self.add_title(title, scale_factor=1.5, animate=False)` —— 场景标题

:::demo examples/ch04/linear_transformation.py LinearTransformationDemo
`[[1, 1], [0, 1]]` 是切变矩阵：第一列 `(1, 0)` 是 i 帽的新位置，第二列 `(1, 1)` 是 j 帽的新位置。单位正方形随网格一起被“推斜”。
:::

:::notice warning
常见错误
`apply_matrix` 的参数是**列主序**的数学矩阵：每一列是一个基向量变换后的像（第一列 = i 帽新位置，第二列 = j 帽新位置）。想实现“x 轴不变、y 按 x 剪切”（`x' = x + y, y' = y`）应传 `[[1, 1], [0, 1]]`；而它的转置 `[[1, 0], [1, 1]]` 是“y 轴不变、x 按 y 剪切”——两者效果完全不同，对称矩阵看不出来时最容易写错。不确定就观察 i 帽 / j 帽的实际走向。
:::

:::notice tip
提示
`leave_ghost_vectors=True` 会在每次变换时留下基向量的半透明残影，多步变换的轨迹一目了然；`show_coordinates=True` 适合演示“网格线即坐标”的概念，但数字较密，正式讲解常用 `show_coordinates=False` 的干净网格。
:::

## 自测

:::exercise
`self.add_vector([2, 1])` 之后想给这个向量贴上标签 `v`，完整写法是什么？
:::answer
接住返回值再标注：

```python
v = self.add_vector([2, 1], color=YELLOW)
self.label_vector(v, Text("v", font_size=36))
```

`add_vector` 默认播放 `GrowArrow` 动画；不想播动画可传 `animate=False`。
:::
:::

:::exercise
在 `LinearTransformationScene` 中演示“先逆时针旋转 90°，再沿 x 轴剪切”的两步变换，第二步应该怎么写矩阵？（旋转矩阵 `R = [[0, -1], [1, 0]]`，剪切 `S = [[1, 1], [0, 1]]`）
:::answer
第二步直接 `self.apply_matrix([[1, 1], [0, 1]])` 即可。`LinearTransformationScene` 的每一步 `apply_matrix` 都作用在**当前**空间状态上：先 `self.apply_matrix([[0, -1], [1, 0]])` 旋转，再 `self.apply_matrix([[1, 1], [0, 1]])` 剪切，总效果即复合变换 `S @ R`。想一次到位也可合成矩阵 `self.apply_matrix(np.array([[1, 1], [0, 1]]) @ np.array([[0, -1], [1, 0]]))`。
:::
:::

:::exercise
只想保留会变形的“前景网格”，去掉底层淡化网格，怎么构造？
:::answer
`class MyScene(LinearTransformationScene): def __init__(self, **kw): super().__init__(include_background_plane=False, **kw)`——或直接在构造时传参。前景网格是变换的“主角”，背景网格只作参照；两层都关掉（`include_foreground_plane=False`）则只剩基向量和注册对象在动。
:::
:::

## 下一步

坐标系与数据可视化板块到此结束：数轴、刻度、坐标系家族、函数绘图、概率图表、矩阵、表格与向量空间场景都已就位。下一板块进入动画进阶，从 `Animation` 的内部机制讲起。
