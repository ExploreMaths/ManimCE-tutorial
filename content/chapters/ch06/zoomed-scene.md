---
title: 局部放大
---

# 局部放大

`ZoomedScene` 在 `MovingCameraScene` 的基础上叠加“画中画”：一个小的取景框（`zoomed_camera`）对准画面局部，并把它的画面实时显示在角落的小窗口（`zoomed_display`）里，实现放大镜效果。

## ZoomedScene

:::inheritance
ZoomedScene → MovingCameraScene → Scene
:::

```python
ZoomedScene(
    camera_class=MultiCamera,
    zoomed_display_height: float = 3,
    zoomed_display_width: float = 3,
    zoomed_display_center: Point3DLike | None = None,
    zoomed_display_corner: Vector3D = UR,
    zoomed_display_corner_buff: float = 0.5,
    zoomed_camera_config={"default_frame_stroke_width": 2, "background_opacity": 1},
    zoomed_camera_image_mobject_config={},
    zoomed_camera_frame_starting_position=ORIGIN,
    zoom_factor: float = 0.15,
    image_frame_stroke_width: int = 3,
    zoom_activated: bool = False,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `zoomed_display_height` / `zoomed_display_width` | float | 3 | 角落放大窗口的尺寸（画面单位） |
| `zoomed_display_corner` | Vector3D | [1,1,0] | 窗口所在角落（如 UR、DL） |
| `zoomed_display_center` | Point3D \| None | None | 若给出则按中心定位窗口，覆盖 corner |
| `zoom_factor` | float | 0.15 | 小取景框相对主画面的缩放比 |
| `zoom_activated` | bool | False | 是否一开始就激活放大 |
| `zoomed_camera_frame_starting_position` | Point3DLike | ORIGIN | 小取景框初始位置 |
:::

场景在 `setup()` 阶段创建两个关键实例属性：

- `self.zoomed_camera`：一个 `MovingCamera`，它的 `frame` 就是画面中的小方框
- `self.zoomed_display`：一个 `ImageMobjectFromCamera`，实时显示小取景框捕获的画面

### activate_zooming

`activate_zooming(animate: bool = False)` 激活放大：把小取景框和窗口加入前景。`animate=True` 时依次播放 `get_zoom_in_animation()` 和 `get_zoomed_display_pop_out_animation()`（框弹出 + 窗口弹出）。

### get_zoom_factor

`get_zoom_factor() -> float` 返回实际放大倍率，定义为 `zoomed_camera.frame.height / zoomed_display.height`（通常接近 `1 / zoom_factor` 构造值）。

:::demo examples/ch06/zoomed_scene_demo.py ZoomDemo
`activate_zooming(animate=True)` 弹出小框与窗口；`zoomed_camera.frame.animate.move_to(...)` 让小取景框转向黄点，窗口内容实时跟随。
:::

### 取消放大显示

v0.21.0 中**没有** `remove_zoom_animated_effect` 方法（本机 `dir(ZoomedScene)` 验证）。要撤掉放大窗口，直接从场景移除相关 mobject 即可：

```python
self.remove(self.zoomed_display, self.zoomed_camera.frame)
```

窗口移除后小取景框不再被渲染；如需重新显示，再次 `self.add(...)` 或重新调用 `activate_zooming()`。

:::notice deprecated
废弃提醒
旧教程中的 `remove_zoom_animated_effect` 在 v0.21.0 已不存在，请改用 `self.remove(self.zoomed_display, self.zoomed_camera.frame)`。旧方法名属于更早期版本的 API。
:::

## MultiCamera

`ZoomedScene` 的默认摄像机：它在普通摄像机之外维护一组“子摄像机 + 显示窗口”对，每帧先让子摄像机捕获画面，再把结果显示到对应的 `ImageMobjectFromCamera` 上。

```python
MultiCamera(
    image_mobjects_from_cameras: Iterable[ImageMobjectFromCamera] | None = None,
    allow_cameras_to_capture_their_own_display: bool = False,
    **kwargs,
)
```

:::inheritance
MultiCamera → MovingCamera → Camera
:::

相关方法：

- `add_image_mobject_from_camera(imfc)` —— 注册一个显示窗口（`activate_zooming` 内部会调用）
- `update_sub_cameras()` —— 按主画面比例调整子摄像机像素尺寸（每帧自动调用）

`allow_cameras_to_capture_their_own_display=True` 允许子摄像机把放大窗口自身也拍进去（默认排除，防止画面递归）。

## ImageMobjectFromCamera

把一台 `MovingCamera` 的画面当作位图显示在场景里的 mobject，即放大窗口的本体。

```python
ImageMobjectFromCamera(
    camera: MovingCamera,
    default_display_frame_config: dict | None = None,
    **kwargs,
)
```

:::inheritance
ImageMobjectFromCamera → AbstractImageMobject → Mobject
:::

`default_display_frame_config` 默认 `{"stroke_width": 3, "stroke_color": WHITE, "buff": 0}`，即窗口的白色边框；`add_display_frame()` 会按此配置给窗口加边框。

## 常见错误与建议

:::notice warning
常见错误
放大窗口里“只剩填充、描边消失”：子摄像机画面以位图方式直接贴出，Cairo 渲染下**纯描边对象**（如默认 `Square`）在窗口中显示为黑色。被放大的物体请给填充（`fill_opacity` 大于 0）或改用 `Dot` 等有填充的对象。本教程所有 ZoomedScene 示例均经本机实渲验证此行为。
:::

:::notice warning
常见错误
`zoomed_camera` 与 `zoomed_display` 是 `setup()` 里创建的**实例属性**，在 `construct` 里直接可用；但如果在 `setup()` 之前（如类属性定义处）引用它们会得到 `AttributeError`。
:::

:::notice tip
提示
`zoom_factor` 越小，小取景框越大、放大倍率越低。常用值 0.1–0.2；倍率可用 `get_zoom_factor()` 在运行时读取并标注在画面上。
:::

:::notice version
版本说明
本节签名基于 `manim 0.21.0` 本机 `inspect` 核实；`remove_zoom_animated_effect` 的缺失已经本机 `dir()` 与实渲双重验证。
:::

## 自测

:::exercise
想把放大倍率从默认提高一倍，应该改哪个构造参数？改完后如何确认实际倍率？
:::answer
把 `zoom_factor` 从 0.15 调小到约 0.075（小取景框更小、放大更强）。实际倍率受显示窗口尺寸影响，运行时用 `self.get_zoom_factor()` 读取才是准确值。
:::
:::

:::exercise
激活放大后想在中途撤掉窗口，v0.21.0 该怎么写？旧脚本里的 `remove_zoom_animated_effect()` 会发生什么？
:::answer
写 `self.remove(self.zoomed_display, self.zoomed_camera.frame)`。旧方法 `remove_zoom_animated_effect` 在 v0.21.0 已移除，直接调用会抛 `AttributeError`。
:::
:::

## 下一步

放大窗口背后是“多台摄像机协同工作”的机制。再往下钻一层：下一节解剖 `Camera` 基类与它的扩展（坐标换算、`MappingCamera`、分屏摄像机）。
