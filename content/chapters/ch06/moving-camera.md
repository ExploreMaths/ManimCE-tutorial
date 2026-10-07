---
title: 移动摄像机
---

# 移动摄像机

`MovingCameraScene` 是 2D 场景里做“镜头运动”的标准方式：它把摄像机换成 `MovingCamera`，核心思想是**镜头框（frame）本身就是画面里的一个矩形 mobject**。移动、缩放这个矩形，就等于移动、缩放摄像机看到的范围。画面里的物体不动，动的是取景框。

## MovingCameraScene

:::inheritance
MovingCameraScene → Scene → object
:::

```python
MovingCameraScene(camera_class=MovingCamera, **kwargs)
```

摄像机框通过 `self.camera.frame` 访问，它是一个普通的 `Mobject`，支持一切 mobject 变换方法：

- `self.camera.frame.move_to(obj)` —— 镜头对准某个物体（无动画）
- `self.camera.frame.shift(...)` / `.scale(factor)` —— 平移 / 缩放取景范围
- `self.camera.frame.animate.move_to(...)` —— 以动画方式运镜
- `self.camera.frame.set(width=..., height=...)` —— 直接设定取景尺寸

:::demo examples/ch06/moving_camera_walk.py CameraWalk
`frame.move_to` 瞬时对准某个圆点；`frame.animate.move_to` 平滑运镜；`frame.scale(0.5)` 把取景范围缩小一半（画面放大 2 倍）；最后 `auto_zoom` 自动框选多个物体。
:::

:::notice tip
提示
镜头移动时，未进入取景框的物体不会渲染，但场景逻辑（updater、self.time）仍在推进。给运镜留停顿用 `self.wait(...)`，不要用长 run_time 空转。
:::

## MovingCamera

`MovingCamera` 是背后的摄像机类，也可以单独实例化用于离屏取景。

```python
MovingCamera(
    frame: Mobject | None = None,
    fixed_dimension: int = 0,
    default_frame_stroke_color: ManimColor = WHITE,
    default_frame_stroke_width: int = 0,
    **kwargs,
)
```

:::inheritance
MovingCamera → Camera → object
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `frame` | Mobject \| None | None | 取景框；None 时自动创建 |
| `fixed_dimension` | int | 0 | 调整像素尺寸时固定不变的维度（0=高，1=宽） |
| `default_frame_stroke_width` | int | 0 | 取景框默认描边宽度；>0 时画面上会显示框线 |
:::

### auto_zoom

`auto_zoom` 自动调整取景框，把给定的一组 mobjects 全部纳入画面：

```python
MovingCamera.auto_zoom(
    mobjects: Iterable[Mobject],
    margin: float = 0,
    only_mobjects_in_frame: bool = False,
    animate: bool = True,
) -> _AnimationBuilder | Mobject
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `mobjects` | Iterable[Mobject] | — | 要框住的物体 |
| `margin` | float | 0 | 取景框与物体包围盒四周留白 |
| `only_mobjects_in_frame` | bool | False | 为 True 时只考虑已在画面内的物体 |
| `animate` | bool | True | True 返回可直接 `play` 的动画；False 直接瞬时调整 |
:::

返回值是 `_AnimationBuilder`（可直接 `self.play(...)`），因此示例中写 `self.play(self.camera.auto_zoom(dots[1:4], margin=1))`。

:::notice warning
常见错误
`MovingCameraScene` 里不要用 `self.camera.frame_height` 当动画目标——改的是属性值而不是框，画面不会平滑过渡。推拉镜头请用 `frame.animate.scale(...)` 或 `auto_zoom(...)`。
:::

:::notice tip
提示
想看到取景框的实际位置（调试用），构造场景后执行 `self.camera.default_frame_stroke_width = 2`，或直接对 `frame` 设置 `stroke_width`。
:::

:::notice version
版本说明
`auto_zoom` 签名与默认值基于 `manim 0.21.0` 本机 `inspect` 核实。
:::

## 自测

:::exercise
场景里有一行 6 个圆点，想让镜头从左到右依次“扫过”它们，至少两种写法是什么？
:::answer
第一种：循环 `self.play(self.camera.frame.animate.move_to(dots[i]), run_time=0.5)` 逐个对准。第二种：先 `frame.scale(0.6)` 缩小取景范围，再一次性 `frame.animate.shift(RIGHT * 距离)` 匀速扫过。想要严格框选某几个点时，用 `auto_zoom`。
:::
:::

:::exercise
`self.play(self.camera.frame.animate.scale(0.5))` 之后，画面中的物体会显得变大还是变小？为什么？
:::answer
变大。`frame` 缩小意味着取景范围减半，同样多的像素只渲染原来一半的空间，物体被放大 2 倍显示——相当于摄像机推近。
:::
:::

## 下一步

取景框不仅可以移动缩放，还可以复制一份显示在画面角落——下一节讲 `ZoomedScene`，实现“局部放大”效果。
