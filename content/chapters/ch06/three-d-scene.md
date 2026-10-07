---
title: ThreeDScene
---

# ThreeDScene

`ThreeDScene` 是 Manim 中编写 3D 内容的场景基类：它把默认摄像机换成 `ThreeDCamera`，并提供了一组控制摄像机方位、环绕旋转与对焦的方法。3D 几何体（如 `Cube`、`Sphere`）在普通 `Scene` 里只能“平视”，而 `ThreeDScene` 让你从任意角度观察它们。

## ThreeDScene

继承链与构造签名：

:::inheritance
ThreeDScene → Scene → object
:::

```python
ThreeDScene(
    camera_class=ThreeDCamera,
    ambient_camera_rotation=None,
    default_angled_camera_orientation_kwargs=None,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `camera_class` | type[Camera] | ThreeDCamera | 场景摄像机类；固定为 3D 摄像机才能使用方位控制 |
| `ambient_camera_rotation` | dict \| None | None | 若给出 `{"rate": ..., "about": ...}`，construct 结束后自动开始环绕 |
| `default_angled_camera_orientation_kwargs` | dict \| None | None | 传给 `set_to_default_angled_camera_orientation()` 的默认方位 |
:::

3D 摄像机用球坐标描述方位，三个核心角度（弧度制）：

- `phi`：极角，摄像机与 Z 轴的夹角（0 表示正上方俯视，PI/2 表示水平）
- `theta`：方位角，摄像机绕 Z 轴旋转的角度
- `gamma`：摄像机绕“原点→摄像机”轴的自转

:::demo examples/ch06/three_d_scene_orbit.py ThreeDOrbit
`set_camera_orientation` 瞬间设定初始视角；`begin_ambient_camera_rotation` 让摄像机以给定角速度持续环绕；`move_camera` 则以动画方式过渡到新视角。
:::

### set_camera_orientation

`set_camera_orientation(...)` 立即（无动画）设定摄像机方位：

```python
ThreeDScene.set_camera_orientation(
    phi=None,
    theta=None,
    gamma=None,
    zoom=None,
    focal_distance=None,
    frame_center=None,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `phi` | float \| None | None | 极角（弧度） |
| `theta` | float \| None | None | 方位角（弧度） |
| `gamma` | float \| None | None | 自转角（弧度） |
| `zoom` | float \| None | None | 缩放因子 |
| `focal_distance` | float \| None | None | 焦距，影响透视强度 |
| `frame_center` | Mobject \| Sequence[float] \| None | None | 画面中心对准的坐标或物体 |
:::

### begin_ambient_camera_rotation

`begin_ambient_camera_rotation(rate=0.02, about="theta")` 启动持续的环绕旋转，之后每个 `wait`/`play` 期间摄像机都会转动；用 `stop_ambient_camera_rotation(about="theta")` 停止。`about` 可取 `"phi"`、`"theta"`、`"gamma"`。

:::notice warning
常见错误
`begin_ambient_camera_rotation` 是“从此以后一直转”，不是一次动画。忘记调用 `stop_ambient_camera_rotation` 的话，后续所有画面都会继续旋转。
:::

### move_camera

`move_camera(...)` 以动画方式改变摄像机方位，参数与 `set_camera_orientation` 完全一致，额外支持：

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `added_anims` | Iterable[Animation] | [] | 与摄像机运动同时播放的其他动画 |
| `run_time` | float | — | 经由 `**kwargs` 传给 `self.play` |
:::

### set_to_default_angled_camera_orientation

`set_to_default_angled_camera_orientation(**kwargs)` 把摄像机设为构造时 `default_angled_camera_orientation_kwargs` 指定的默认斜视角度（可临时覆盖）。

:::notice deprecated
废弃提醒
旧教程中的 `get_default_camera_orientation` 在 v0.21.0 **已不存在**（本机 `inspect` 验证：`ThreeDScene` 上无此方法）。查询默认方位请直接读构造参数 `default_angled_camera_orientation_kwargs`；恢复默认视角用 `set_to_default_angled_camera_orientation()`。
:::

### add_fixed_orientation_mobjects

3D 场景中还有一个常见需求：让 2D 标注始终面朝摄像机。`add_fixed_orientation_mobjects(*mobjects, **kwargs)` 让文本等 mobject 不随摄像机旋转（始终面向观众），`add_fixed_in_frame_mobjects` 则让 mobject 完全固定在画面上（如同 2D 场景）。

## SpecialThreeDScene

`SpecialThreeDScene` 继承 `ThreeDScene`，预置了 3D 坐标轴、球体的默认配置和默认斜视角度，并提供 `get_axes()`、`get_sphere()` 等工厂方法。它源自 3b1b 的教学视频配置。

:::inheritance
SpecialThreeDScene → ThreeDScene → Scene → object
:::

:::notice warning
已知问题
在 v0.21.0 中 `SpecialThreeDScene` **无法实例化**：其 `__init__` 在调用父类之前访问 `self.renderer`，直接抛出 `AttributeError: 'SpecialThreeDScene' object has no attribute 'renderer'`（本机实测，含 CLI 渲染路径）。它没有标记 `@deprecated`，但等价于事实不可用。需要它的效果时，请改用 `ThreeDScene` + `ThreeDAxes` + `Sphere` 手动组合：

```python
class MyScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-110 * DEGREES)
        axes = ThreeDAxes()
        sphere = Sphere(radius=2, resolution=(24, 48))
        self.add(axes, sphere)
```
:::

## 常见错误与建议

:::notice warning
常见错误
在 `ThreeDScene` 里直接用 `self.camera.frame` 做 2D 推拉是无效的——3D 视角由 `phi`/`theta`/`zoom` 等参数控制，请使用 `move_camera(zoom=...)` 或 `set_camera_orientation`。
:::

:::notice tip
提示
3D 渲染比 2D 慢得多。调试时先用 `-ql` 低画质快速出片，确认镜头运动后再用 `-qm`/`-qh` 出正式版；Cairo 渲染器完全可以渲染本章所有 3D 效果，不强制要求 OpenGL。
:::

:::notice version
版本说明
本节签名与行为均基于 `manim 0.21.0` 本机核实。
:::

## 自测

:::exercise
想让摄像机从水平视角（phi≈70°）绕场景缓慢转一圈再停下来，应该用哪几个方法？速率参数是什么含义？
:::answer
先用 `set_camera_orientation(phi=70*DEGREES, theta=...)` 设定初始方位，然后 `begin_ambient_camera_rotation(rate=r, about="theta")` 开始环绕，`rate` 是角速度（弧度/秒，默认 0.02），最后用 `stop_ambient_camera_rotation()` 停止。想精确转到某个角度时，改用 `move_camera(theta=..., run_time=...)` 一次到位。
:::
:::

:::exercise
旧脚本里写了 `self.get_default_camera_orientation()`，在 v0.21.0 会发生什么？如何迁移？
:::answer
会抛 `AttributeError`——该方法在 v0.21.0 已移除。迁移方式：需要默认值时读 `self.default_angled_camera_orientation_kwargs`；需要恢复默认斜视角度时调用 `self.set_to_default_angled_camera_orientation()`。
:::
:::

## 下一步

3D 场景的舞台已经搭好。下一节认识舞台上的演员：立方体、球体、曲面等 3D 几何体。
