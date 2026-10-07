---
title: 旋转
---

# 旋转

`Rotate` 和 `Rotating` 名字只差三个字母，却是两条继承链上的不同动画：前者是 `Transform` 系（改数据），后者是 `Animation` 系（每帧从快照重算）。选错会导致节奏或结果不符合预期。

## Rotate

`Rotate(mobject, angle=PI, axis=OUT, ...)` 是 **`Transform` 的子类**：按 Transform 的方式从当前状态插值到"旋转后的目标状态"，默认缓动是 `smooth`（继承自 Transform），播放结束后数据**永久改变**。

:::inheritance
Rotate → Transform → Animation → object
:::

```python
Rotate(
    mobject: Mobject,
    angle: float = PI,
    axis: Vector3DLike = OUT,
    about_point: Point3DLike | None = None,
    about_edge: Vector3DLike | None = None,
    **kwargs,
)
```

## Rotating

`Rotating(mobject, angle=TAU, axis=OUT, ..., run_time=5, rate_func=linear)` 直接继承 `Animation`：每一帧都先 `become(起始快照)` 再旋转 `rate_func(alpha) * angle`，因此是严格的匀速旋转，默认转一整圈、用时 5 秒。

:::inheritance
Rotating → Animation → object
:::

```python
Rotating(
    mobject: Mobject,
    angle: float = TAU,
    axis: Vector3DLike = OUT,
    about_point: Point3DLike | None = None,
    about_edge: Vector3DLike | None = None,
    run_time: float = 5,
    rate_func: Callable[[float], float] = linear,
    **kwargs,
)
```

## Rotate 与 Rotating 对比

:::compare
| 维度 | `Rotate` | `Rotating` |
| ---- | ---- | ---- |
| 继承链 | Transform → Animation | Animation |
| 默认角度 | `PI`（半圈） | `TAU`（整圈） |
| 默认 rate_func | `smooth`（缓入缓出） | `linear`（匀速） |
| 默认 run_time | 1.0 | 5 |
| 每帧计算 | 从当前状态向目标插值 | 从起始快照重算旋转 |
| 播放后数据 | 停在转过 angle 的状态 | 同样停在转过 angle 的状态 |
:::

:::demo examples/ch05/rotation.py RotateVsRotating
同样转 90°：左侧 `Rotate` 用 smooth 缓动先慢后快；右侧 `Rotating` 用 linear 匀速，肉眼可见节奏差异。
:::

:::notice warning
常见错误
网传"Rotate 改变数据、Rotating 只播放不动数据"的说法在 v0.21.0 **不准确**：实测两者播放结束后物体的旋转数据都会保留。真正的区别在**每帧的计算方式**——Rotating 每帧从起始快照重算，播放期间对物体的其他修改会被覆盖；而"持续自转"效果应配 `cycle_animation(Rotating(...))` 或改用 updater，而不是反复 `play`。
:::

## 自测

:::exercise
想让一个齿轮以每秒 90° 匀速不停旋转，推荐怎么写？
:::answer
`cycle_animation(Rotating(gear, angle=PI / 2, run_time=1, rate_func=linear))` 后 `self.add(gear)`；`cycle_animation` 会把动画变成循环 updater，齿轮无限自转。
:::
:::

:::exercise
为什么 `Rotating(mob, angle=PI / 2)` 播完后物体位置与 `Rotate(mob, angle=PI / 2)` 相同，观感却不同？
:::answer
两者终态确实一致，但 Rotating 每帧从起始快照匀速（linear）重算，Rotate 用 smooth 从当前状态缓动插值——同样的 90°，前者匀速、后者先慢后快，观感节奏不同。
:::
:::

## 下一步

掌握了"怎么动"，下一节解决"怎么让观众看"：10 个强调与指示动画，把观众的注意力精确引导到画面任意位置。
