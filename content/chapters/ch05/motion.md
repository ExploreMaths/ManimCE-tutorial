---
title: 运动变形
---

# 运动变形

本节处理两类"自定义运动"：`MoveAlongPath` 让物体贴着任意曲线走；`Homotopy` 家族让你写出**任意空间形变函数**，对物体每个点做个性化映射。最后补充 `manim.utils.paths` 的路径函数，它们决定 `Transform` 系动画中点如何从起点走到终点。

## MoveAlongPath

`MoveAlongPath(mobject, path)` 让物体沿一条 `VMobject` 路径运动，方向始终沿路径切线，进度由 rate_func 控制。

:::inheritance
MoveAlongPath → Animation → object
:::

```python
MoveAlongPath(mobject: Mobject, path: VMobject, suspend_mobject_updating: bool = False, **kwargs)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `path` | VMobject | — | 运动路径（`Circle`、`ArcBetweenPoints`、自定义曲线等） |
| `suspend_mobject_updating` | bool | False | 播放期间是否挂起物体自身 updater |
:::

## Homotopy

`Homotopy(homotopy, mobject, run_time=3)` 是**按函数逐点形变**的动画：`homotopy(x, y, z, t)` 把 t 时刻空间点 `(x, y, z)` 映射到新位置。`t` 从 0（原状）到 1（终态）。

:::inheritance
Homotopy → Animation → object
:::

```python
Homotopy(
    homotopy: Callable[[float, float, float, float], tuple[float, float, float]],
    mobject: Mobject,
    run_time: float = 3,
    apply_function_kwargs: dict | None = None,
    **kwargs,
)
```

两个子类覆盖两种常见特化：

## SmoothedVectorizedHomotopy

`SmoothedVectorizedHomotopy(homotopy, mobject, run_time=3, ...)` 是 `Homotopy` 的子类：在通用逐点映射之外，对 `VMobject` 相邻点之间的位移做平滑插值，缓解逐点独立映射导致的边缘撕裂，形变视觉上更顺滑。

:::inheritance
SmoothedVectorizedHomotopy → Homotopy → Animation → object
:::

## ComplexHomotopy

`ComplexHomotopy(complex_homotopy, mobject, **kwargs)` 也是 `Homotopy` 的子类：形变函数用复数形式 `f(z: complex, t: float) -> complex` 描述，写共形映射（如 `z * np.exp(t * PI * 1j)` 的整体旋转缩放）比三元组形式简洁得多。

:::inheritance
ComplexHomotopy → Homotopy → Animation → object
:::

## PhaseFlow

`PhaseFlow(function, mobject, virtual_time=1)` 沿**向量场**推进物体：每一点按 `function(point)` 给出的速度方向运动 `virtual_time` 个虚拟秒，默认 `rate_func=linear`。常用来可视化微分方程的流。

:::inheritance
PhaseFlow → Animation → object
:::

```python
PhaseFlow(
    function: Callable[[np.ndarray], np.ndarray],
    mobject: Mobject,
    virtual_time: float = 1,
    suspend_mobject_updating: bool = False,
    rate_func: RateFunction = linear,
    **kwargs,
)
```

## manim.utils.paths 路径函数

这组函数不是动画，而是 **`Transform` 系动画的 `path_func` 参数**：它决定每个点从起点到终点走什么路线。全部为**工厂函数**，调用后返回真正的路径函数。

:::compare
| 函数 | 签名 | 路线形状 |
| ---- | ---- | ---- |
| `straight_path()` | — | 直线（默认） |
| `path_along_arc(arc_angle, axis=OUT)` | 弧度，轴向 | 绕指定轴沿弧线走 `arc_angle` |
| `clockwise_path()` | — | 顺时针半圆弧（等价 `path_along_arc(-PI)`） |
| `counterclockwise_path()` | — | 逆时针半圆弧（等价 `path_along_arc(PI)`） |
| `path_along_circles(arc_angle, circles_centers, axis=OUT)` | 两段圆心 | 各点分别绕给定圆心转 `arc_angle` |
| `spiral_path(angle, axis=OUT)` | 弧度 | 螺旋线，旋转的同时收缩 |
:::

典型用法：

```python
self.play(
    Transform(a, b, path_func=path_along_arc(PI / 2)),
    run_time=2,
)
```

:::demo examples/ch05/motion.py MotionAndHomotopy
圆点沿下半圆弧 `MoveAlongPath` 到右侧；随后正方形被自定义 `Homotopy` 纵向压扁并带正弦波纹。
:::

:::notice warning
常见错误
`Transform` 的 `path_func` 影响的是**运动路线**，不改变起止状态：无论绕多大的弧，动画结束物体都精确落在目标状态。另外 `clockwise_path()` / `counterclockwise_path()` 是无参工厂，注意写 `path_func=counterclockwise_path()` 而不是传函数本身时漏了调用。
:::

## 自测

:::exercise
想写"正方形被压成一条水平波浪线"的效果，应该用哪个动画、函数怎么写？
:::answer
用 `Homotopy`：函数返回 `(x, y * (1 - t) + t * A * np.sin(k * x), z)`，t 从 0 到 1 时 y 坐标被逐渐压到正弦曲线上。
:::
:::

:::exercise
`MoveAlongPath` 与给物体加 updater `lambda m, dt: m.shift(...)` 手写运动有什么区别？
:::answer
`MoveAlongPath` 保证物体**严格贴路径**、进度与 rate_func 绑定、播完停在路径终点；手写 updater 需要自己积分速度和方向，容易偏离曲线，但适合不受固定路径约束的运动。
:::
:::

## 下一步

路径和形变解决了"怎么走"，下一节回到最基本的刚体运动——旋转：`Rotate` 与 `Rotating` 只有一词之差，行为却大不相同。
