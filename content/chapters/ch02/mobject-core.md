---
title: Mobject 核心
---

# Mobject 核心

Manim 中的一切可见对象都继承自 `Mobject`（Mathematical Object，数学对象）。本节讲清 `Mobject` 的职责边界：它管理**子对象树、位置、样式状态**，但本身**没有外观**——真正能被渲染出来的是它的子类。

## Mobject

`Mobject` 是所有屏幕对象的基类：**写自定义图形就是继承 `Mobject`（或其子类）**。它约有一百多个公开成员，下面按用途分组介绍最常用的部分。

:::inheritance
Mobject → object
:::

```python
Mobject(
    color: ParsableManimColor | list[ParsableManimColor] = WHITE,
    name: str | None = None,
    dim: int = 3,
    target: Mobject | None = None,
    z_index: float = 0,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `color` | ParsableManimColor \| list[ParsableManimColor] | WHITE | 基础颜色，作为描边、填充的默认取值 |
| `name` | str \| None | None | 调试显示名；None 时自动生成 `Mobject_xxxx` |
| `dim` | int | 3 | 点坐标的维度，通常保持 3（x, y, z） |
| `target` | Mobject \| None | None | 预留的 Transform 目标占位，一般用不到 |
| `z_index` | float | 0 | 层级，数值大的后绘制（视觉上更靠前） |
:::

### 结构操作

管理子对象与整体替换：

:::compare
| 方法 | 说明 |
| ---- | ---- |
| `add(*mobjects)` | 追加子对象；同一个对象重复添加会被忽略 |
| `remove(*mobjects)` | 移除子对象；移除不存在的对象不会报错 |
| `copy()` | 返回深拷贝；要对同一图形用两次必须先拷贝 |
| `become(mobject, match_height=False, match_width=False, match_center=False, stretch=False)` | 把自身的数据与样式替换成另一个 mobject（原地修改） |
| `get_family()` | 返回 `[自身, 全部后代]` 的扁平列表 |
:::

### 定位方法

`shift` / `move_to` / `next_to` / `align_to` / `to_edge` / `to_corner` / `center` 是最常用的布局七件套：

:::compare
| 方法 | 签名（常用部分） | 说明 |
| ---- | ---------------- | ---- |
| `shift(*vectors)` | — | 按向量平移，如 `.shift(2 * LEFT + UP)` |
| `move_to(point_or_mobject)` | `aligned_edge=ORIGIN` | 把**中心**移到目标点或目标对象中心 |
| `next_to(mobject_or_point, direction=RIGHT, buff=0.25)` | `aligned_edge=ORIGIN` | 沿 `direction` 方向排到目标旁边，留 `buff` 间距 |
| `align_to(mobject_or_point, direction=ORIGIN)` | — | 只对齐指定方向的边缘，不移动其他轴 |
| `to_edge(edge=LEFT, buff=0.5)` | — | 贴到画面某条边 |
| `to_corner(corner=DL, buff=0.5)` | — | 贴到画面某个角 |
| `center()` | — | 移回画面中心 |
| `set_x(x)` / `set_y(y)` | — | 直接设定某一轴坐标 |
:::

### 变换方法

:::compare
| 方法 | 签名（常用部分） | 说明 |
| ---- | ---------------- | ---- |
| `rotate(angle, axis=OUT)` | `about_point=None` | 绕 `axis` 轴旋转 `angle` 弧度，默认绕纸面法线 |
| `scale(scale_factor)` | `about_point=None` | 等比缩放；`about_point` 可指定缩放中心 |
| `flip(axis=UP)` | `about_point=None` | 沿轴镜像翻转 |
| `stretch(factor, dim)` | — | 只沿某一维拉伸 |
| `scale_to_fit_width(width)` / `scale_to_fit_height(height)` | — | 缩放到指定宽高 |
:::

### 状态保存与查询

:::compare
| 成员 | 说明 |
| ---- | ---- |
| `save_state()` / `restore()` | 快照当前位置与样式；`restore` 也可以配合 `.animate` 播放成动画 |
| `set(**kwargs)` | 批量设属性，如 `.set(z_index=5)`，常与 `.animate` 配合 |
| `get_center()` / `get_x()` / `get_y()` | 查询中心坐标 |
| `get_top()` / `get_bottom()` / `get_left()` / `get_right()` | 查询包围盒四边中点 |
| `width` / `height` | 只读属性：当前包围盒宽高（只读，不能赋值） |
:::

下面这个示例串联了定位、变换与状态保存：

:::demo examples/ch02/mobject_methods.py MobjectMethods
`save_state()` 在旋转缩放前打快照，`animate.restore()` 再把它平滑地变回来；`next_to` 让正方形贴到圆左侧。
:::

几乎所有变换/定位方法都返回 `self`，因此可以链式书写：`Square().set_fill(BLUE).shift(LEFT).rotate(PI / 4)`。

### 与其他章节的关系

- 下一节的 `VMobject` 在 `Mobject` 之上增加描边、填充等矢量样式。
- 之后的 `Group`（Mobject 子类）与 `VGroup`（VMobject 子类）用于把多个对象当一个整体操作。

:::notice warning
常见错误
`Mobject` 本身**没有任何点，渲染出来是不可见的**——`self.play(FadeIn(Mobject()))` 不会报错，但画面什么都没有。需要可见图形时请用具体子类（`Square`、`Circle` 等）。
:::

:::notice warning
常见错误
`width` / `height` 是只读属性：`square.width = 2` 会抛 `AttributeError`。要改变大小请用 `scale()` 或 `scale_to_fit_width()`。同理，`set_fill` / `set_stroke` / `set_opacity` 定义在 `VMobject` 上，纯 `Mobject`（如 `Point`）没有这些方法。
:::

:::notice deprecated
废弃提醒
`Mobject` 保留了 `get_*` / `set_*` 兼容层：未显式定义的方法（如 `mob.set_foo(0)`）会退化为普通属性读写并给出 `DeprecationWarning`。新代码请直接写 `mob.foo = 0` 或用 `mob.set(foo=0)`。
:::

## 自测

:::exercise
`move_to(other)` 和 `next_to(other, RIGHT)` 有什么本质区别？
:::answer
`move_to` 把**自身中心**对齐到目标的中心（或 `aligned_edge` 指定的边缘），两个物体重叠；`next_to` 则把自身整体放到目标的一侧，中间留出 `buff` 间距，二者不重叠。
:::
:::

:::exercise
想让一个三角形先旋转 90° 再变回去，如何用 `save_state` / `restore` 实现为一个平滑动画？
:::answer
先 `tri.save_state()` 快照，再 `self.play(tri.animate.rotate(PI / 2))`，最后 `self.play(tri.animate.restore())`——`restore` 也可以挂在 `.animate` 后面播放成动画。
:::
:::

## 下一步

掌握了 `Mobject` 的树结构与定位变换后，下一节看真正能“上色”的矢量基类 `VMobject`。
