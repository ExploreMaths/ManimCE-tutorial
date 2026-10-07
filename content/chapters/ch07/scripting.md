---
title: 脚本化调用
---

# 脚本化调用

前几节的渲染入口都是 CLI：`manim scene.py MyScene`。但 Manim 本质是一个 Python 库——场景类完全可以像普通类一样在脚本里实例化并渲染。当你需要批量出图、在 Web 服务里渲染、或做单元测试时，这就成了刚需。

## Scene.render

渲染一个场景的底层入口是 `Scene.render()`：

```python
Scene.render(preview: bool = False) -> bool
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `preview` | bool | False | 渲染完成后打开预览（等价于 CLI 的 `-p`） |
| 返回值 | bool | — | 场景请求“重跑”时为 True（`RerunSceneException` 机制），正常完成为 False |
:::

:::notice version
版本说明
本机 v0.21.0 的 `Scene.render()` **没有** `quiet` 参数——早期资料里的 `quiet` 是老版本 3b1 的 API，社区版从未提供过。想安静输出，用 `config.verbosity = "WARNING"`（或更低）降低日志级别。
:::

`render()` 内部依次执行 `setup() → construct() → tear_down()`，与 CLI 渲染完全同一条路径。

## 最小脚本化渲染

```python
from manim import *

config.quality = "medium_quality"   # 等价于 CLI -qm
config.media_dir = "./media_out"
config.verbosity = "WARNING"        # 减少日志输出

class MyScene(Scene):
    def construct(self):
        self.play(FadeIn(Square()))
        self.wait(0.5)

if __name__ == "__main__":
    scene = MyScene()
    scene.render()
```

保存为 `render_demo.py`，直接 `python render_demo.py` 即可，不需要 `manim` 命令。输出位置与 CLI 一致：`./media_out/videos/render_demo/720p30/MyScene.mp4`。

批量渲染多个场景 / 多个参数组合也一样：

```python
for color in (RED, GREEN, BLUE):
    class S(Scene):
        def construct(self):
            self.play(FadeIn(Square(color=color)))
            self.wait(0.5)
    S().render()
```

## 与 CLI 渲染的等价关系

:::compare
| 方面 | CLI 渲染 | 脚本化渲染 |
| ---- | -------- | ---------- |
| 入口 | `manim -qm scene.py MyScene` | `MyScene().render()` |
| 画质/输出目录 | `-qm`、`--media_dir` | `config.quality`、`config.media_dir` |
| 配置文件 | 自动读取三层 `manim.cfg` | 同样读取（`import manim` 时消化） |
| 预览 | `-p` 标志 | `render(preview=True)` |
| 场景选择 | 命令行场景名参数 | 实例化哪个类就渲染哪个 |
| 日志级别 | `-v` | `config.verbosity` |
| 额外能力 | `cfg`、`checkhealth`、`init` 等子命令 | 无（自行实现） |
:::

CLI 本质就是“解析参数 → 写进 `config` → 找到场景类 → 调用 `render()`”的一层薄壳。脚本化时这层壳由你接管，配置文件仍然生效，行为一致。

:::notice tip
提示
两者也可以混用：`manim render` 渲染的同时，同一个文件里保留 `if __name__ == "__main__":` 脚本入口，调试时 `python scene.py` 直接跑，发布时走 CLI 精确控制参数。
:::

## 常见错误与建议

:::notice warning
常见错误
在脚本入口实例化多个场景时，前一个场景的 mobject / updater 不会自动清干净——每个场景实例有自己的 `mobjects` 列表，但 `config` 是全局的。循环渲染时若改了 `config`（如 `background_color`），会影响后续所有场景。
:::

:::notice warning
常见错误
`render()` 返回 True 表示场景通过 `RerunSceneException` 请求重跑（交互模式的 `rerun()`），脚本里忽略返回值通常没问题；但如果你在自己的循环里渲染，注意这个信号，否则重跑语义会丢失。
:::

## 自测

:::exercise
写一个没有 CLI、双击即可运行的脚本，渲染 `Circle` 淡入 1 秒后停留 0.5 秒，输出到 `./out`。
:::answer
```python
from manim import *

config.quality = "medium_quality"
config.media_dir = "./out"

class CircleScene(Scene):
    def construct(self):
        self.play(FadeIn(Circle()), run_time=1.0)
        self.wait(0.5)

if __name__ == "__main__":
    CircleScene().render()
```

`python` 直接运行即可；等价 CLI 是 `manim -qm --media_dir ./out scene.py CircleScene`。
:::
:::

:::exercise
想在脚本渲染时完全静音 Manim 的日志，有 `render(quiet=True)` 吗？应该怎么做？
:::answer
没有。v0.21.0 的 `render()` 只接受 `preview`。静音方式是把日志级别调低：`config.verbosity = "ERROR"`（或 `"CRITICAL"`），这同时影响终端输出与 ffmpeg 日志级别。
:::
:::

## 下一步

最后一节是工具箱：`manim.utils` 里那些被各章节反复用到、却很少被正眼看待的工具函数。
