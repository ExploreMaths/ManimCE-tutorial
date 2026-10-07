---
title: 你的第一个场景
---

# 你的第一个场景

欢迎来到 Manim 社区版（ManimCE）教程。本节带你写出第一个可渲染的场景，并理解三个最核心的概念：`Scene`、`play()` 与 `wait()`。

## Scene

`Scene` 是 Manim 中一切场景的基类：**编写场景就是继承 `Scene` 并实现 `construct()` 方法**。渲染器负责实例化场景，并依次调用生命周期方法 `setup() → construct() → tear_down()`，其中 `construct()` 是你写动画逻辑的地方。渲染入口是 `render(preview=False)`，通常由 CLI 自动调用，不必手动执行。

:::inheritance
Scene → object
:::

注意 `Scene` 与摄像机是**组合**关系而非继承关系：场景通过构造函数持有 `camera_class`（默认 `Camera`）实例，访问方式为 `self.camera`。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `renderer` | CairoRenderer \| OpenGLRenderer \| None | None | 渲染器；None 时按 `config.renderer` 自动创建 |
| `camera_class` | type[Camera] | Camera | 场景使用的摄像机类 |
| `always_update_mobjects` | bool | False | 为 True 时即使无动画也每帧更新 mobject |
| `random_seed` | int \| None | None | 随机种子；设置后随机效果可复现 |
| `skip_animations` | bool | False | 跳过所有动画，只走逻辑（配合 `-n` 使用） |
:::

最小可运行示例：

```python
from manim import *


class MyScene(Scene):
    def construct(self):
        self.play(FadeIn(Text("你好，Manim！")))
```

用 CLI 渲染它：

```bash
manim -pqm scene.py MyScene
```

约定与注意事项：

- 每个 `.py` 示例文件只包含**一个**场景类，类名就是输出视频的文件名。
- `construct()` 由渲染器自动调用，不需要手动执行。
- 文件中必须有 `from manim import *`（或等价的显式导入）。

### construct 方法

`construct(self)` 是场景的入口。场景中所有的 `self.add(...)`、`self.play(...)`、`self.wait(...)` 都写在这里。

#### self 是什么

`self` 就是当前场景实例。通过它访问场景上的方法，例如 `self.camera.frame_center`、`self.mobjects` 等。

下面这个示例演示了 `Scene` 的两组基础操作——无动画的 `add` / `remove` 与有动画的 `play` / `wait`：

:::demo examples/ch01/scene_basics.py SceneBasics
`add` 与 `remove` 瞬间改变画面，不产生任何动画；`play` 才有逐帧的动画过程。
:::

## play

`self.play()` 用来播放动画。签名中 `*args` 接收 `Animation` 或 `.animate` 构造器（`_AnimationBuilder`），多个动画默认同时开始：

- `self.play(FadeIn(circle))` —— 播放单个动画
- `self.play(FadeIn(circle), Write(label))` —— 两个动画同时播放
- `self.play(circle.animate.shift(LEFT))` —— 由 `.animate` 生成方法动画
- 用 `lag_ratio` 可以让多个动画错峰开始

### play 的参数

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `*args` | Animation \| _AnimationBuilder | — | 要播放的动画，可传入多个 |
| `run_time` | float | 1.0 | 动画时长（秒） |
| `rate_func` | function | `smooth` | 速率函数，见 Rate Functions 章节 |
| `lag_ratio` | float | 0.0 | 多动画之间的错峰比例 |
| `subcaption` | str \| None | None | 播放期间写入的字幕内容（输出 .srt） |
:::

## wait

`self.wait()` 让画面静止一段时间，常用来给观众留出阅读时间，例如 `self.wait(2)` 停顿 2 秒。

### wait 的参数

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `duration` | float | 1.0 | 静止时长（秒），可以是小数 |
| `stop_condition` | callable \| None | None | 返回 True 时提前结束等待 |
| `frozen_frame` | bool \| None | None | 强制按“静止帧”处理；None 时自动判断 |
:::

相关便捷方法：

- `self.pause(duration=1.0)` —— `wait` 的别名，语义完全相同
- `self.wait_until(stop_condition, max_time=60)` —— 等到条件满足为止，最多等 `max_time` 秒

静止等待默认只写一帧再按时长延展，几乎不占渲染时间；如果场景里有 updater，默认会逐帧模拟，此时传 `frozen_frame=True` 可强制按静止帧处理（代价是 updater 不会运行）。

下面是一个完整的官方风格示例——正方形变换成圆，随后停顿：

:::demo examples/ch01/square_to_circle.py SquareToCircle
`Transform` 让正方形**逐步变形**为圆，最后的 `wait()` 让成品画面停留一秒。
:::

同一个示例也可以用不带扩展名的路径引用，二者等价：

:::demo examples/ch02/circle_intro CircleIntro
`CircleIntro` 演示了 `FadeIn` 与 `Write` 的组合。
:::

## 渲染质量对比

不同质量标志对应的输出：

:::compare
| 标志 | 分辨率 | 帧率 | 用途 |
| ---- | ------ | ---- | ---- |
| `-ql` | 854×480 | 15 | 快速预览 |
| `-qm` | 1280×720 | 30 | 日常调试 |
| `-qh` | 1920×1080 | 60 | 正式发布 |
:::

普通管道表格（不在 `:::` 容器中）同样有效：

| 命令 | 作用 |
| ---- | ---- |
| `manim -p` | 渲染结束后预览 |
| `manim -f` | 渲染结束后打开输出目录 |

## 常见错误与建议

:::notice warning
常见错误
`construct()` 只能有 `self` 一个参数。写 `def construct(self, t):` 之类的签名，渲染时会被静默忽略或报错——需要参数时请改用 `self.time`、updater 或构造时把值存到实例属性上。
:::

:::notice warning
常见错误
不要把 `Mobject` 直接传给 `play()`：`self.play(Square())` 会抛 `TypeError: Unexpected argument`。正确写法是 `self.play(FadeIn(Square()))` 或 `self.play(Square().animate.shift(LEFT))`。旧版支持的“把 mobject 方法当参数传”也已被移除，统一使用 `.animate`。
:::

:::notice tip
提示
`wait()` 只是“画面静止”，updater 与 `self.time` 仍在推进。若想让某个带随机效果的场景每次渲染结果一致，用 CLI `--seed` 或构造参数 `Scene(random_seed=42)` 固定随机种子。
:::

:::notice version
版本说明
本教程所有示例均基于 `manim 0.21.0`，与其他大版本的 API 可能存在差异。
:::

:::notice deprecated
废弃提醒
旧教程中的 `self.add_foreground_mobjects` 已被 `self.add_foreground_mobject` 取代，请使用新写法。
:::

## 自测

:::exercise
如何让一个动画播放完毕后停顿 2 秒，再播放下一个动画？
:::answer
在两次 `play` 之间调用 `self.wait(2)`。`wait` 的参数单位是秒，可以是小数。
:::
:::

:::exercise
`self.play(a, b)` 与先后写两行 `self.play(a)`、`self.play(b)` 有什么区别？
:::answer
前者两个动画**同时**开始（总时长取两者较大值）；后者串行执行，总时长为两者之和。
:::
:::

:::exercise
场景里有一个 updater 在不停移动圆点，此时 `self.wait(2, frozen_frame=True)` 会发生什么？
:::answer
这 2 秒会按静止帧处理：圆点停在原地、不随 updater 移动，但视频时长仍然延长 2 秒。想要 updater 生效就不要传 `frozen_frame=True`。
:::
:::

## 场景类的继承关系

常见场景子类的两条继承链：

:::inheritance
Scene → MovingCameraScene → ZoomedScene
:::

:::inheritance
Scene → ThreeDScene
:::

这些子类会在“3D 与摄像机”板块详细介绍。

## 下一步

到这里你已经掌握了最小工作流。下一节将拆解一次渲染背后的完整流程与输出目录结构。
