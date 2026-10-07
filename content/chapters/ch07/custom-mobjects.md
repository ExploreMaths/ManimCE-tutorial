---
title: 自定义 Mobject
---

# 自定义 Mobject

Manim 内置的几百个 `Mobject` 子类覆盖了常见图形，但总会有不够用的时候：一个带刻度的仪表盘、一朵参数化的云、一个特殊的徽标……这时就需要扩展 Manim 的图形体系。本节介绍三条扩展路线，并给出一个完整的自定义 `VMobject` 示例。

## 三条扩展路线

按“实现成本从低到高”排列：

:::compare
| 路线 | 做法 | 适用场景 | 代价 |
| ---- | ---- | -------- | ---- |
| 组合现有对象 | 用 `Group` / `VGroup` 把已有 mobject 拼起来 | 徽标、仪表盘、复杂标注 | 零继承，最简单；成员间相对布局需要自己维护 |
| 继承 `VMobject` 重写 `generate_points` | 用 `start_new_path`、`add_line_to`、`add_cubic_bezier_curve` 等绘制轮廓 | 新形状（曲线图形、参数化轮廓） | 要理解贝塞尔点数组结构 |
| 继承 `Mobject` | 完全自定义数据与渲染行为 | 非矢量图形、特殊数据结构（如自定义点云） | 没有现成的填充/描边能力，几乎从零做起 |
:::

三条路线不是互斥的：一个自定义 `VMobject` 内部完全可以再用 `VGroup` 拼装子部件。

:::notice tip
提示
90% 的“自定义图形”需求用第一条路线（组合）就够了。先问自己：这个图形能不能由圆、线、多边形、文字拼出来？能，就不要急着继承。
:::

## 组合路线：Group 与 VGroup

`Group` 是任意 mobject 的通用容器，`VGroup` 只接受 `VMobject`（含其子孙，如 `Text`、`Axes`）。两者都继承自 `Mobject`，本身不绘制任何东西，只是把子对象组织成树。

```python
Group(*mobjects, **kwargs)    # 任意 Mobject
VGroup(*vmobjects, **kwargs)  # 仅限 VMobject
```

:::notice warning
常见错误
`VGroup` 不接受非 `VMobject` 成员，传 `ImageMobject` 之类的对象会抛 `TypeError`（提示改用 `Group`）。不确定成员类型时，用 `Group` 更保险。
:::

组合路线的关键技巧是把**相对布局封装进构造函数**，让复合对象可以像内置对象一样 `shift`、`rotate`：

```python
class Logo(VGroup):
    def __init__(self, **kwargs):
        ring = Circle(radius=1).set_stroke(BLUE, 8)
        dot = Dot().set_color(YELLOW)
        super().__init__(ring, dot, **kwargs)
```

## VMobject 路线：重写 generate_points

继承 `VMobject` 的核心是重写 `generate_points(self)`：Manim 在初始化时会调用它生成对象的轮廓点。`VMobject` 内部把轮廓存成**锚点 + 控制点**的三次贝塞尔点数组（`self.points`），绘制时逐条曲线渲染。你不需要直接操作裸数组，用这组绘图方法即可：

:::compare
| name | 签名 | 作用 |
| ---- | ---- | ---- |
| `start_new_path` | `(point)` | 抬起笔，从 `point` 开始一条新的子路径 |
| `add_line_to` | `(point)` | 从当前点连直线到 `point` |
| `add_cubic_bezier_curve` | `(anchor1, handle1, handle2, anchor2)` | 添加一条完整的三次贝塞尔曲线 |
| `add_cubic_bezier_curve_to` | `(handle1, handle2, anchor)` | 从当前点出发的三次贝塞尔曲线 |
| `add_quadratic_bezier_curve_to` | `(handle, anchor)` | 二次贝塞尔曲线 |
| `close_path` | `()` | 闭合当前子路径 |
| `set_points` | `(points)` | 直接用点数组替换全部轮廓 |
:::

:::inheritance
Gauge → VMobject → Mobject → object
:::

下面是一个完整的自定义仪表盘：外弧用折线近似，刻度是 9 条独立的短线子路径，全部在 `generate_points` 中完成：

:::demo examples/ch07/custom_gauge.py CustomGauge
`Gauge` 在 `generate_points` 里先画半圆外弧，再画 9 根刻度（每根一条子路径）；指针是独立的 `VGroup`，最后用 `Rotate` 转动它。
:::

:::notice warning
常见错误
自定义属性（如示例中的 `radius`）必须在 `super().__init__()` **之前**赋值：基类构造函数会调用 `generate_points`，而后者依赖这些属性。先调 `super()` 再设属性会得到 `AttributeError`。
:::

:::notice warning
常见错误
在 `generate_points` 里调用 `self.play()`、`self.add()` 之类的方法是不可行的——此时对象还没有进入任何场景。`generate_points` 只负责生成几何数据，动画逻辑写在场景的 `construct()` 里。
:::

## Mobject 路线：什么时候才需要

直接继承 `Mobject` 意味着放弃 `VMobject` 的填充、描边、贝塞尔轮廓体系，自行管理 `points` 并面对摄像机渲染接口。只有当你要表达的东西**本质上是点集或场**（如自定义采样粒子、热力图网格）、而矢量轮廓无法描述时，才值得走这条路。即便如此，通常的做法也是继承 `Mobject` 管理数据，同时内部挂一个 `VGroup` 负责实际绘制。

## 常见错误与建议

:::notice tip
提示
自定义对象想支持 `Create`、`Transform` 等动画无需额外工作——这些动画操作的就是 `points` 与样式属性。但 `Transform(a, b)` 要求两者的子对象结构匹配，自定义对象的子对象划分要保持稳定。
:::

:::notice tip
提示
调试自定义图形时，`manim` 命名空间里的 `index_labels(mobject)` 可以给每个子对象贴上序号标签，`print_family(mobject)` 可以把对象树打印到控制台。详见“杂项”一节。
:::

## 自测

:::exercise
自定义 `VMobject` 的子类在 `__init__` 里先调用了 `super().__init__(**kwargs)`，然后才给 `self.radius` 赋值，结果渲染时报 `AttributeError: 'MyShape' object has no attribute 'radius'`。为什么？
:::answer
基类 `VMobject.__init__` 会调用 `generate_points()`，而该方法用到了 `self.radius`。赋值发生在 `super().__init__()` 之后，导致生成点时属性还不存在。把 `self.radius = radius` 移到 `super().__init__()` 之前即可。
:::
:::

:::exercise
想在仪表盘上加一个会随数值转动的指针，应该把指针画进 `Gauge.generate_points` 里吗？
:::answer
不建议。`generate_points` 生成的几何属于对象本体，转动指针需要单独动画控制。更合理的做法是把指针做成独立的 `VGroup`（如示例中的 `needle`），用 `Rotate` 等动画操作它；若一定要封装在一个类里，可让仪表盘类继承 `VGroup`，把表盘和指针作为两个子成员分别控制。
:::
:::

## 下一步

会造新图形之后，下一节解决另一个常见扩展需求：当内置动画（FadeIn、Transform……）都不够用的时候，如何写一个自定义 `Animation`。
