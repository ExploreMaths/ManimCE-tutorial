---
title: 函数绘图
---

# 函数绘图

Manim 提供三种“画曲线”的 mobject，恰好覆盖函数图像的三种描述方式：**显函数** `y = f(x)`、**参数方程** `(x(t), y(t))`、**隐函数** `F(x, y) = 0`。三者都是 `VMobject` 的子类，可以像任何图形一样 `Create`、`FadeIn`、施加 `.animate`。

:::inheritance
FunctionGraph → ParametricFunction → VMobject
:::

:::inheritance
ImplicitFunction → VMobject
:::

日常使用中你很少直接构造它们——坐标系的 `plot` 家族方法会自动把曲线放进坐标系并处理好比例。下表先给出三者的直接构造参数：

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| FunctionGraph: `function` | Callable[[float], Any] | — | 显函数 `y = f(x)` |
| FunctionGraph: `x_range` | tuple \| None | None | x 取值范围（三段式可带步长） |
| ParametricFunction: `function` | Callable[[float], Point3DLike] | — | 参数方程，输入 t 输出点 |
| ParametricFunction: `t_range` | tuple | (0, 1) | 参数范围 |
| ParametricFunction: `use_vectorized` | bool | False | function 是否支持向量化（numpy）输入 |
| ParametricFunction: `discontinuities` | Iterable[float] \| None | None | 已知间断点列表，采样时会绕开 |
| ParametricFunction: `use_smoothing` | bool | True | 是否对采样点做平滑 |
| ImplicitFunction: `func` | Callable[[float, float], float] | — | `F(x, y)`，绘制其零等值线 |
| ImplicitFunction: `x_range` / `y_range` | Sequence[float] \| None | None | 搜索范围 |
| ImplicitFunction: `min_depth` | int | 5 | 四叉树最小递归深度 |
| ImplicitFunction: `max_quads` | int | 1500 | 四叉树最大节点数 |
:::

:::compare
| 维度 | FunctionGraph | ParametricFunction | ImplicitFunction |
| ---- | ------------- | ------------------ | ---------------- |
| 曲线描述 | `y = f(x)` | `(x(t), y(t))` | `F(x, y) = 0` |
| 输入函数签名 | `f(x) -> y` | `f(t) -> [x, y, z]` | `f(x, y) -> float` |
| 能否表示竖直线 | 不能 | 能 | 能 |
| 典型用途 | 普通函数图像 | 圆、摆线、利萨茹图形 | 圆锥曲线、等值线 |
| 坐标系入口 | `axes.plot(...)` | `axes.plot_parametric_curve(...)` | `axes.plot_implicit_curve(...)` |
| 底层算法 | 均匀采样 + 平滑 | 均匀采样 + 平滑 | 自适应四叉树 |
:::

## FunctionGraph

:::demo examples/ch04/function_graph.py FunctionGraphDemo
`axes.plot(np.sin)` 返回一个 `ParametricFunction`（`FunctionGraph` 家族），`get_area` 填充它与 `bounded_graph` 之间的区域，`input_to_graph_point`（别名 `i2gp`）取曲线上指定 x 的点。
:::

## ParametricFunction

:::demo examples/ch04/parametric_implicit.py ParametricImplicitDemo
蓝色的单位圆来自参数方程，黄色的圆来自隐函数 `x² + y² - 4 = 0`——同一个形状，两种描述。
:::

:::notice warning
常见错误
三者的坐标语义不同：`plot` 的函数工作在**坐标系坐标**里（y=2 就是数据坐标 2），而 `ParametricFunction` 的函数直接输出**场景坐标**——`Circle()` 就是 `ParametricFunction(lambda t: np.array([np.cos(t), np.sin(t), 0]), t_range=[0, TAU], use_smoothing=True)`，半径是 1 个场景单位，与坐标系无关。所以画数据曲线请走 `axes.plot_parametric_curve`，不要直接构造 `ParametricFunction` 再指望它自动对齐坐标轴。
:::

:::notice deprecated
废弃提醒
旧版教程中的 `ParametricSurface` **在 v0.21.0 已被移除**（`manim.ParametricSurface` 不存在）。3D 参数曲面的继任者是 `three_d` 模块中的 `Surface` 及其便捷子类，见“3D 与摄像机”板块。参数**曲线**不受影响：`ParametricFunction` 依然健在。
:::

## ImplicitFunction

`ImplicitFunction(func, x_range, y_range, min_depth=5, max_quads=1500)` 用自适应四叉树追踪 `F(x, y) = 0` 的零等值线，上面的 demo 中黄色的圆就是它画出的。坐标系入口是 `axes.plot_implicit_curve(...)`。

常见坑：曲线在狭窄弯曲处断断续续时，提高 `min_depth`（如 8–12）并视情况提高 `max_quads`，代价是生成时间变长。

## 常用配套方法（定义在 CoordinateSystem 上）

- `axes.get_area(graph, x_range=None, bounded_graph=None, opacity=0.3, ...)` —— 填充 `graph` 与 x 轴（或 `bounded_graph`）之间的区域
- `axes.get_riemann_rectangles(graph, x_range, dx=0.1, ...)` —— 黎曼求和矩形
- `axes.get_graph_label(graph, label="f(x)", x_val=None, direction=RIGHT, dot=False, ...)` —— 贴在图上的标签
- `axes.input_to_graph_point(x, graph)`（别名 `i2gp`）—— 图上取点；坐标版是 `input_to_graph_coords`（`i2gc`）
- `axes.get_vertical_line(point)` / `get_horizontal_line(point)` —— 过点作坐标轴平行线
- `axes.plot_derivative_graph(graph)` / `plot_antiderivative_graph(graph)` —— 数值导数 / 原函数图像
- `axes.get_secant_slope_group(x, graph, dx)`、`axes.slope_of_tangent(x, graph)` —— 割线 / 切线斜率

`plot` 还有两个进阶参数：`use_vectorized=True` 要求函数支持 numpy 数组输入（大提速）；`colorscale=[color1, color2]` 按 y 值给曲线上色。

## 自测

:::exercise
用 `Axes.plot_parametric_curve` 画一个中心在坐标 `(1, 2)`、半径为 1.5 的圆，并思考：为什么不能直接用 `Circle().move_to(axes.c2p(1, 2))` 替代？
:::answer
```python
circle = axes.plot_parametric_curve(
    lambda t: axes.c2p(1 + 1.5 * np.cos(t), 2 + 1.5 * np.sin(t)),
    t_range=(0, TAU),
)
```
`Circle().move_to(...)` 只是平移一个几何圆：它的“半径”是场景单位而不是数据单位，y 轴与 x 轴的 `unit_size` 一旦不等就会变椭圆，也不会跟着坐标系 `plot` 的范围/颜色参数走。参数曲线则始终在数据坐标系里定义。
:::
:::

:::exercise
`axes.plot_implicit_curve(lambda x, y: x * y - 1)` 画出的双曲线断断续续，应该调整哪个参数？
:::answer
提高 `min_depth`（如 8–12）并视情况提高 `max_quads`。隐函数曲线由自适应四叉树追踪零等值线，`min_depth` 控制最小细分深度，深度不足时曲线在狭窄弯曲处会断裂；代价是生成时间变长。
:::
:::
