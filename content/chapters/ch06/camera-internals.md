---
title: Camera 基类与扩展
---

# Camera 基类与扩展

前面所有场景类本质上都是在 `Scene` 上换不同的摄像机：`ThreeDScene` 换 `ThreeDCamera`，`MovingCameraScene` 换 `MovingCamera`，`ZoomedScene` 换 `MultiCamera`。本节解剖这个公共基类 `Camera`，以及三个较少用但值得知道的扩展。

## Camera

`Camera` 负责两件事：定义**取景范围**（帧坐标系）与**像素网格**（像素坐标系）的对应关系，以及把 mobject 渲染进像素数组。

```python
Camera(
    background_image: str | None = None,
    frame_center: Point3D = ORIGIN,
    image_mode: str = "RGBA",
    n_channels: int = 4,
    pixel_array_dtype: str = "uint8",
    cairo_line_width_multiple: float = 0.01,
    use_z_index: bool = True,
    background: PixelArray | None = None,
    pixel_height: int | None = None,
    pixel_width: int | None = None,
    frame_height: float | None = None,
    frame_width: float | None = None,
    frame_rate: float | None = None,
    background_color: ParsableManimColor | None = None,
    background_opacity: float | None = None,
    **kwargs,
)
```

:::inheritance
Camera → object
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `frame_center` | Point3D | ORIGIN | 帧坐标系原点对准的空间点 |
| `frame_height` / `frame_width` | float \| None | None | 取景范围（画面单位），None 时取 `config`（默认 8 × 14.22） |
| `pixel_height` / `pixel_width` | int \| None | None | 输出像素尺寸，None 时取 `config`（`-qm` 为 720×1280） |
| `pixel_array_dtype` | str | uint8 | 像素数组数据类型 |
| `use_z_index` | bool | True | 是否按 z_index 排序渲染 |
:::

### 帧坐标系与像素坐标系

摄像机用两组尺寸把“画面单位”换算成“像素”：

- 帧坐标系：以 `frame_center` 为中心，`frame_height`/`frame_width` 为可见范围（默认 16:9 时高 8、宽 8×16/9≈14.22）
- 像素坐标系：`pixel_height`×`pixel_width` 的数组；**像素 y 轴向下增长**（数组行号），而帧坐标 y 轴向上增长

换算关系：空间点 `p` 的像素横坐标 = `(p.x - center.x) / frame_width * pixel_width + pixel_width/2`，纵坐标方向相反。`Camera` 提供的换算工具：

- `points_to_subpixel_coords(mobject, points)` —— 空间点 → 亚像素坐标（float）
- `points_to_pixel_coords(mobject, points)` —— 空间点 → 整数像素坐标（`(N, 2)` 数组）
- `get_coords_of_all_pixels()` —— 全部像素对应的帧坐标
- `is_in_frame(mobject_or_point)` / `on_screen_pixels(...)` —— 可见性判断
- `reset_pixel_shape(pixel_height, pixel_width)` / `resize_frame_shape(fixed_dimension)` —— 改变像素尺寸时保持比例

:::demo examples/ch06/camera_pixel_coords.py PixelCoords
三个点旁边的标注是 `points_to_pixel_coords` 换算出的像素坐标：ORIGIN 对应画面正中心 (640, 360)，y 向上会让像素行号变小。
:::

### convert_pixel_array

`convert_pixel_array(pixel_array)` 把 0–1 浮点像素数组转成 0–255 的 `uint8` RGB 值（乘以 `rgb_max_val` 后按 `pixel_array_dtype` 取整），是渲染输出前的最后一步。

:::notice version
版本说明
v0.21.0 破坏性变更：`Camera.convert_pixel_array()` 的 `convert_from_floats` 参数**已移除**（本机核实当前签名为 `convert_pixel_array(pixel_array)`，函数体无条件做浮点→整数转换）。旧代码若写 `convert_pixel_array(arr, convert_from_floats=True/False)` 需删掉第二个参数；不再需要转换时改为直接使用原数组。
:::

### get_image

`get_image(pixel_array=None) -> PIL.Image` 把像素数组转成 PIL 图像，便于截图、后处理或保存自定义背景。

## MappingCamera

`MappingCamera` 在渲染前对所有点应用一个自定义映射函数，可做出局部扭曲、放大、反演等特效。

```python
MappingCamera(
    mapping_func=<恒等映射>,
    min_num_curves=50,
    allow_object_intrusion=False,
    **kwargs,
)
```

:::inheritance
MappingCamera → Camera
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `mapping_func` | Callable | 恒等 | 对显示点施加的映射 `(x, y, z) -> (x', y', z')` |
| `min_num_curves` | int | 50 | 映射前把曲线细分的最小段数，保证弯曲效果平滑 |
| `allow_object_intrusion` | bool | False | 是否允许物体侵入被映射区域 |
:::

```python
class WarpScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(
            camera_class=lambda **kw: MappingCamera(
                mapping_func=lambda p: p * np.exp(-np.linalg.norm(p) ** 2 / 8),
                **kw,
            ),
            **kwargs,
        )
```

:::notice tip
提示
自定义 `camera_class` 时若需要额外构造参数，用 `lambda **kw: MyCamera(..., **kw)` 包装，因为渲染器只会以关键字形式传入 `camera_config`。
:::

## SplitScreenCamera

把两台摄像机左右拼接成一块画面（左相机占左半、右相机占右半）。

```python
SplitScreenCamera(left_camera, right_camera, **kwargs)
```

:::inheritance
SplitScreenCamera → OldMultiCamera → Camera
:::

典型用途：同一 mobject 列表用两种不同视角/映射同时展示。注意左右两台相机需要预先自行构造。

## OldMultiCamera

`SplitScreenCamera` 的父类，接受任意多台摄像机及各自的起始位置，是更通用的“多机位”基类。名字里的 “Old” 是历史遗留——它仍受支持，但新代码若只需画中画，优先用 `MultiCamera`（见上一节）。

```python
OldMultiCamera(*cameras_with_start_positions, **kwargs)
```

:::inheritance
OldMultiCamera → Camera
:::

## 常见错误与建议

:::notice warning
常见错误
像素坐标不是“中心为原点、向上为正”。像素数组的 (0, 0) 在**左上角**且 y 向下；做像素级计算时务必用 `points_to_pixel_coords` 换算，不要手推公式后忘记翻转 y。
:::

:::notice warning
常见错误
`Camera` 的 `frame_width` 默认按 16:9 由 `frame_height` 推出；用自定义分辨率（如 `-r 1000,1000` 方形）时，如需精确控制取景范围，请显式传 `frame_width` 与 `frame_height`，不要假设宽是高的 16/9。
:::

:::notice version
版本说明
本节签名与 `convert_pixel_array` 参数移除均基于 `manim 0.21.0` 本机 `inspect` 核实。
:::

## 自测

:::exercise
`-qm` 画质下 `pixel_width=1280, pixel_height=720`，默认 `frame_height=8`。点 `(2, 1, 0)` 的像素坐标大约是多少？
:::answer
横向：`(2 / (8*16/9)) * 1280 + 640 ≈ 820`；纵向因 y 轴向上而像素向下：`-(1/8)*720 + 360 = 270`。也可以用 `self.camera.points_to_pixel_coords(dot, [point])` 直接得到精确整数。对照本节示例：(3, 2, 0) 对应 (910, 180)，比例一致。
:::
:::

:::exercise
升级到 v0.21.0 后，自定义摄像机子类里的 `self.convert_pixel_array(arr, convert_from_floats=True)` 报 TypeError，怎么修？
:::answer
删除第二个参数：改为 `self.convert_pixel_array(arr)`。v0.21.0 移除了 `convert_from_floats`，现在该函数总是执行浮点到整数的转换；原意为“跳过转换”的调用点应不再调用此函数。
:::
:::

## 下一步

摄像机决定“怎么看”，渲染器决定“怎么画”。最后一节对比 Cairo 与 OpenGL 两个渲染器：能力差异、性能特征与选型建议。
