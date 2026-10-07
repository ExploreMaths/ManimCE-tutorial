---
title: 杂项
---

# 杂项

最后收拢三个不易归类但实用的主题：给视频配音的 `add_sound`、交互式调试的 `interactive_embed`，以及一组调试小工具。

## add_sound

`Scene.add_sound()` 在视频时间轴的当前位置插入一段音效，最终由 ffmpeg 混流进输出视频。

```python
Scene.add_sound(
    sound_file: str,
    time_offset: float = 0,
    gain: float | None = None,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `sound_file` | str | — | 音效文件路径；会在 `assets_dir`（默认 `./`）下按 `.wav`、`.mp3` 扩展名搜索 |
| `time_offset` | float | 0 | 相对偏移：实际播放时刻 = 调用时的 `self.time + time_offset`；正值延后，负值提前（声音在调用之前就开始） |
| `gain` | float \| None | None | 增益（放大倍数）；None 为不调整 |
:::

典型用法：

```python
class ClickScene(Scene):
    def construct(self):
        dot = Dot()
        self.add_sound("click.wav")      # 此刻插入音效
        self.play(FadeIn(dot))
        self.add_sound("click.wav", time_offset=0.2)  # 再延后 0.2 秒补一声
        self.wait()
```

:::notice warning
常见错误
`add_sound` 依赖 ffmpeg：混流在写视频文件时进行。`--dry_run`、只出 PNG（`-s` / `--format png`）的模式下没有视频容器，声音不会被写入。找不到文件时会抛错——确认文件名在 `assets_dir` 下可解析（可用 `config.assets_dir` 指定素材目录）。
:::

:::notice tip
提示
音效的播放时刻以**调用 `add_sound` 时的场景时间**为准，而不是动画结束时间。放在 `self.play(...)` 之前调用，声音就落在动画开始处。
:::

## interactive_embed

`interactive_embed()` 在场景执行到一半时打开一个 IPython 交互终端，让你在现场手动操作场景里的 mobject，验证坐标、试验动画参数，退出后继续渲染。

```python
Scene.interactive_embed() -> None
```

无参数。前置条件（源码中直接断言）：

:::compare
| 条件 | 说明 |
| ---- | ---- |
| OpenGL 渲染器 | 必须是 `--renderer opengl`（断言 `camera` 为 `OpenGLCamera`、`renderer` 为 `OpenGLRenderer`），Cairo 下会直接断言失败 |
| IPython 环境 | 内部导入 `IPython.terminal.embed.InteractiveShellEmbed`，未安装 IPython 时不可用 |
| 交互窗口 | 配合 `--force_window` 或 `-p` 使用，需要能打开窗口的环境 |
:::

进入终端时，整个 `manim` 与 `manim.opengl` 命名空间已注入，可直接操作场景变量：

```python
class EmbedScene(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.interactive_embed()   # 进入 IPython，敲 dot.shift(LEFT) 实时看效果
        self.play(dot.animate.shift(RIGHT * 2))
```

终端里还内置了一个 `rerun()` 函数：调用它会整体重跑场景，是交互调试复杂动画的利器。

:::notice warning
常见错误
在默认的 Cairo 渲染器下调用 `interactive_embed()` 会立即触发 `AssertionError`。它不是通用的“暂停调试”手段——Cairo 管道下想逐段检查，请用 `-n` 分段渲染加 `-s` 出帧。
:::

## 调试工具

`manim.utils.debug` 提供两个小工具，`from manim import *` 后可直接用：

:::compare
| name | 签名 | 作用 |
| ---- | ---- | ---- |
| `index_labels` | `(mobject, label_height=0.15, background_stroke_width=5, background_stroke_color=BLACK, **kwargs) -> VGroup` | 给 mobject 的每个子对象贴上序号标签（0、1、2……），返回由标签组成的 `VGroup`，可 `self.add(...)` 查看或加进场景 |
| `print_family` | `(mobject, n_tabs=0) -> None` | 把 mobject 的子对象树打印到控制台，带缩进层级 |
:::

```python
group = VGroup(Square(), Circle(), Triangle())
print_family(group)          # 控制台输出层级树
self.add(group, index_labels(group))   # 画面上标注子对象序号
```

调试 `Transform` 不匹配、自定义对象子对象结构异常时，这两个工具几乎总是第一步。

## 常见错误与建议

:::notice warning
常见错误
`index_labels` 返回的是**新的** `VGroup`，不会自动进场景；忘了 `self.add(labels)` 就看不到任何标签。标签本身也是 mobject，会参与后续 `Transform`——检查完及时移除。
:::

## 自测

:::exercise
`self.add_sound("click.wav", time_offset=-0.5)` 放在 `self.play(...)` 之前调用，声音会在什么时候响起？
:::answer
在调用 `add_sound` 那一刻的场景时间**提前 0.5 秒**开始播放——如果场景开始不到 0.5 秒，实际效果取决于混流处理（声音会被截断到视频起点附近）。负偏移适合让长音效的前奏对齐动画。注意声音只在输出视频文件时混流，预览 PNG 或 dry run 听不到。
:::
:::

:::exercise
想在渲染中途暂停、手动试试某个 `VGroup` 的排布再决定后续动画，该用哪个方法？有什么前提？
:::answer
用 `self.interactive_embed()`。前提：必须用 `--renderer opengl` 渲染（源码断言 OpenGL 渲染器与摄像机）、环境装有 IPython、且能打开交互窗口。进入后可直接操作场景对象，内置 `rerun()` 可重跑场景；Cairo 渲染器下请改用 `-n` + `-s` 分段出帧调试。
:::
:::

## 下一步

到这里，九个板块的内容全部走完。回到教程首页，挑一个感兴趣的板块开始动手吧——最好的学习方式是边看边改示例代码。
