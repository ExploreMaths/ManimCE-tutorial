---
title: 3D 几何
---

# 3D 几何

Manim 的 3D 几何体全部可以用 Cairo 渲染器绘制（伪 3D 投影 + 着色），无需 OpenGL。它们分两个家族：由 `Surface` 参数化生成的曲面家族，以及由面片拼成的多面体家族（多面体在下一节专门介绍）。

先看最常用的六个实体：

:::demo examples/ch06/three_d_solids.py ThreeDSolids
六个基本实体一字排开：`Cube`、`Sphere`、`Cone`、`Cylinder`、`Torus`、`Prism`。默认角度下它们看起来像压扁的 2D 图形，配合 `set_camera_orientation` 才有立体感。
:::

## Cone

圆锥面（侧面为参数化曲面，默认无底面）。

```python
Cone(
    base_radius: float = 1,
    height: float = 1,
    direction: Vector3DLike = Z_AXIS,
    show_base: bool = False,
    v_range: tuple[float, float] = (0, 2*PI),
    u_min: float = 0,
    checkerboard_colors=False,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `base_radius` | float | 1 | 底面半径 |
| `height` | float | 1 | 高 |
| `direction` | Vector3DLike | [0,0,1] | 锥体朝向，默认沿 Z 轴 |
| `show_base` | bool | False | 是否显示底面圆盘 |
:::

## Cube

立方体，由 6 个正方形面片组成（因此是 `VGroup`，见下文 `Prism`）。

```python
Cube(
    side_length: float = 2,
    fill_opacity: float = 0.75,
    fill_color: ParsableManimColor = "#58C4DD",
    stroke_width: float = 0,
    **kwargs,
)
```

:::inheritance
Cube → VGroup → VMobject → Mobject
:::

## Cylinder

圆柱面。

```python
Cylinder(
    radius: float = 1,
    height: float = 2,
    direction: Vector3DLike = Z_AXIS,
    v_range: tuple[float, float] = (0, 2*PI),
    show_ends: bool = True,
    resolution: int | tuple[int, int] = (24, 24),
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `radius` | float | 1 | 半径 |
| `height` | float | 2 | 高 |
| `direction` | Vector3DLike | [0,0,1] | 轴向 |
| `show_ends` | bool | True | 是否封闭上下底 |
| `resolution` | int \| tuple | (24, 24) | 网格分辨率 |
:::

## Sphere

球面。

```python
Sphere(
    center: Point3DLike = ORIGIN,
    radius: float = 1,
    resolution: int | Sequence[int] | None = None,
    u_range: tuple[float, float] = (0, 2*PI),
    v_range: tuple[float, float] = (0, PI),
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `center` | Point3DLike | ORIGIN | 球心 |
| `radius` | float | 1 | 半径 |
| `resolution` | int \| Sequence \| None | None | 网格分辨率，None 时取配置默认值 |
:::

## Torus

圆环面（救生圈形状）。

```python
Torus(
    major_radius: float = 3,
    minor_radius: float = 1,
    u_range: tuple[float, float] = (0, 2*PI),
    v_range: tuple[float, float] = (0, 2*PI),
    resolution: int | tuple[int, int] | None = None,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `major_radius` | float | 3 | 中心到管中心的距离 |
| `minor_radius` | float | 1 | 管半径 |
:::

:::notice tip
提示
`Torus` 默认 `major_radius=3`，在小场景中显得很大，演示时通常显式传 `Torus(major_radius=1, minor_radius=0.4)` 之类的值。
:::

## Prism

长方体（矩形棱柱），继承 `Cube`。

```python
Prism(dimensions: Vector3DLike = [3, 2, 1], **kwargs)
```

:::inheritance
Prism → Cube → VGroup → VMobject
:::

`dimensions` 是 `[宽, 高, 深]` 三个方向的长度。`Prism([2, 2, 2])` 等价于 `Cube(side_length=2)`。

## Dot3D

3D 点：一个极小的球。

```python
Dot3D(
    point: Point3D = ORIGIN,
    radius: float = 0.08,
    color: ParsableManimColor = WHITE,
    resolution: int | tuple[int, int] | None = (8, 8),
    **kwargs,
)
```

:::inheritance
Dot3D → Sphere → Surface → VGroup
:::

## Line3D

3D 线段：一根很细的圆柱。

```python
Line3D(
    start: Point3DLike = [-1, 0, 0],
    end: Point3DLike = [1, 0, 0],
    thickness: float = 0.02,
    color: ParsableManimColor | None = None,
    resolution: int | tuple[int, int] = 24,
    **kwargs,
)
```

:::inheritance
Line3D → Cylinder → Surface → VGroup
:::

## Arrow3D

3D 箭头：细圆柱 + 圆锥头。

```python
Arrow3D(
    start: Point3DLike = [-1, 0, 0],
    end: Point3DLike = [1, 0, 0],
    thickness: float = 0.02,
    height: float = 0.3,
    base_radius: float = 0.08,
    color: ParsableManimColor = WHITE,
    resolution: int | tuple[int, int] = 24,
    **kwargs,
)
```

:::inheritance
Arrow3D → Line3D → Cylinder → Surface
:::

下面这个示例把 `Line3D`、`Arrow3D`、`Dot3D` 和自定义 `Surface` 放在一起：

:::demo examples/ch06/three_d_lines_surface.py ThreeDLinesAndSurface
`saddle(u, v)` 返回 `[u, v, 0.5*u*v]` 定义一张马鞍面；`Line3D`/`Arrow3D` 本质上是细圆柱，所以它们继承 `Cylinder` 的参数。
:::

## Surface

一切参数化 3D 曲面的基类：给一个 `(u, v) -> [x, y, z]` 函数，再指定参数范围和网格分辨率，Manim 把它切成小面片拼出来。

```python
Surface(
    func: Callable[[float, float], np.ndarray],
    u_range: tuple[float, float] = (0, 1),
    v_range: tuple[float, float] = (0, 1),
    resolution: int | Sequence[int] = 32,
    surface_piece_config: dict = {},
    fill_color: ParsableManimColor = BLUE_D,
    fill_opacity: float = 1.0,
    checkerboard_colors=[BLUE_D, BLUE_E],
    stroke_color: ParsableManimColor = LIGHT_GREY,
    stroke_width: float = 0.5,
    should_make_jagged: bool = False,
    pre_function_handle_to_anchor_scale_factor: float = 1e-5,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `func` | Callable | — | 参数化函数 `(u, v) -> np.ndarray([x, y, z])` |
| `u_range` | tuple[float, float] | (0, 1) | u 参数范围 |
| `v_range` | tuple[float, float] | (0, 1) | v 参数范围 |
| `resolution` | int \| Sequence | 32 | 每维网格份数，越高越平滑越慢 |
| `checkerboard_colors` | Iterable \| False | [BLUE_D, BLUE_E] | 棋盘格双色；传 False 关闭 |
| `should_make_jagged` | bool | False | 是否让面片边缘锯齿化（着色更硬） |
:::

:::inheritance
Surface → VGroup → VMobject → Mobject
:::

注意继承关系：`Surface` 不是 `VMobject` 的直接子类，而是 **`VGroup`**——每个小面片是 `ThreeDVMobject`，整个曲面是面片的组合。因此可以用 `VGroup` 的所有方法（`arrange`、`scale` 等）操作曲面。

## ThreeDVMobject

单个 3D 面片（`Surface` 的内部组成单元），也可单独用于自定义 3D 图形。

```python
ThreeDVMobject(shade_in_3d: bool = True, **kwargs)
```

:::inheritance
ThreeDVMobject → VMobject → Mobject
:::

`shade_in_3d=True` 时按 3D 法线方向参与光照着色；设 False 则按普通 2D 图形平涂。

## 常用类对比

:::compare
| 类 | 继承 | 一句话用途 | 关键参数 |
| ---- | ---- | --------- | -------- |
| `Sphere` | Surface → VGroup | 球面 | `center`、`radius`、`resolution` |
| `Cone` | Surface → VGroup | 圆锥 | `base_radius`、`height`、`show_base` |
| `Cylinder` | Surface → VGroup | 圆柱 | `radius`、`height`、`show_ends` |
| `Torus` | Surface → VGroup | 圆环 | `major_radius`、`minor_radius` |
| `Cube` | VGroup | 立方体 | `side_length` |
| `Prism` | Cube → VGroup | 长方体 | `dimensions=[x,y,z]` |
| `Dot3D` | Sphere → Surface | 3D 点 | `point`、`radius` |
| `Line3D` | Cylinder → Surface | 3D 线段 | `start`、`end`、`thickness` |
| `Arrow3D` | Line3D → Cylinder | 3D 箭头 | `height`、`base_radius`（箭头头部） |
:::

## 常见错误与建议

:::notice warning
常见错误
不要用 2D 的 `Line`/`Arrow` 在 3D 场景里连接两个 z 坐标不同的点——它们只画 XY 平面的投影。跨深度的连线请用 `Line3D`/`Arrow3D`。
:::

:::notice warning
常见错误
`Surface` 的 `func` 必须返回长度为 3 的 `np.ndarray`（如 `np.array([u, v, u*v])`）。返回 list 或形状不对会在构造时直接报错。
:::

:::notice tip
提示
`resolution` 是渲染速度的主要开关。`-ql` 下调低分辨率（如 `(8, 8)`）调试，出正式片再恢复 `(32, 32)` 或更高。
:::

:::notice version
版本说明
本节签名与默认值均基于 `manim 0.21.0` 本机 `inspect` 核实（如 `Sphere` 有 `center` 参数、`Surface` 直接继承 `VGroup`）。
:::

## 自测

:::exercise
想画一张高度为 `z = sin(x) + cos(y)`、范围 x,y∈[-2,2] 的曲面，该怎么写？
:::answer
用 `Surface` 显式写出参数化函数：

```python
def func(u, v):
    return np.array([u, v, np.sin(u) + np.cos(v)])

surface = Surface(func, u_range=(-2, 2), v_range=(-2, 2), resolution=(24, 24))
```
:::
:::

:::exercise
`Cube` 是 `VMobject` 吗？`solids.arrange(RIGHT)` 为什么能直接用在六个不同类型的实体组合上？
:::answer
`Cube` 直接继承 `VGroup`（再由 `VGroup` → `VMobject`），而 `Cone`/`Sphere` 等经 `Surface` 也继承 `VGroup`。因此所有 3D 实体都具有 `VGroup`/`Mobject` 的变换与布局方法，可以放进同一个 `VGroup` 后统一 `arrange`。
:::
:::

## 下一步

基本 3D 几何体已经齐备。下一节看多面体家族：正多面体、任意自定义多面体，以及从点集自动求凸包的 `ConvexHull3D`。
