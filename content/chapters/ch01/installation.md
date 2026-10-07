---
title: 安装与运行环境
---

# 安装与运行环境

Manim 社区版（ManimCE）需要 **Python 3.9 或更高版本**。本教程的所有内容都基于 `manim 0.21.0`，安装时请锁定版本号，避免不同大版本之间的 API 差异。

## pip

使用 `pip` 从 PyPI 安装，并显式指定版本：

```bash
pip install manim==0.21.0
```

建议使用虚拟环境，避免依赖冲突：

```bash
python -m venv .venv
source .venv/bin/activate  # Windows 使用 .venv\Scripts\activate
pip install manim==0.21.0
```

如果你使用 [uv](https://docs.astral.sh/uv/)，命令等价：

```bash
uv pip install manim==0.21.0
```

Manim 还提供了两个可选的附加组件：

| 附加组件 | 安装命令 | 用途 |
| ---- | ---- | ---- |
| `typst` | `pip install "manim[typst]"` | Typst 排版支持与 `MathTypst`（v0.21.0 新增） |
| `jupyterlab` | `pip install "manim[jupyterlab]"` | Jupyter Notebook / JupyterLab 环境 |

:::notice version
版本说明
不锁定版本号时，`pip install manim` 会安装当时的最新版，可能与本教程的 API 不一致。开始学习前请先运行 `manim --version` 核对版本。
:::

## 验证安装

安装完成后运行：

```bash
manim --version
manim checkhealth
```

`manim --version` 应输出 `Manim Community v0.21.0`；`manim checkhealth` 会检查可执行文件、LaTeX、dvisvgm 等组件并给出每项的 PASSED / FAILED 状态。

然后渲染官方经典示例验证整条链路：

:::demo examples/ch01/square_to_circle.py SquareToCircle
这是 Manim 的“Hello World”。如果这条命令能渲染出正方形变圆的动画，说明安装完全成功：

```bash
manim -pql examples/ch01/square_to_circle.py SquareToCircle
```
:::

## 系统依赖

自 v0.19.0 起，ffmpeg 已随 Python wheel 一起分发，`pip install manim` 之后即可直接渲染视频，无需再手动安装 ffmpeg。各平台的注意事项：

| 平台 | 需要额外做的事 |
| ---- | ---- |
| Windows | 无需额外安装，Pango / Cairo 均有预编译 wheel |
| macOS | 无需额外安装，Pango / Cairo 均有预编译 wheel |
| Linux | 少数发行版需装 Pango / Cairo 的系统库，如 `sudo apt install libpango1.0-0 libcairo2` |

:::notice tip
提示
只有需要渲染 `Tex` / `MathTex` 时才要求本地装有 LaTeX（如 TeX Live 或 MiKTeX）；纯 `Text` 场景不需要。`manim checkhealth` 会告诉你 LaTeX 是否可用。
:::

## ManimMagic

想在 Jupyter Notebook 里边写边渲染，可以使用 Manim 内置的 IPython 单元魔法（cell magic）`%%manim`，它由 `manim.utils.ipython_magic` 中的 `ManimMagic` 类提供。

在 Notebook 中只要执行过 `import manim`（或 `from manim import *`），魔法命令就会自动注册，无需手动加载扩展：

```python
from manim import *

%%manim -qm -v WARNING MyScene
class MyScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
```

- `%%manim` 后面跟的参数与 CLI 选项一致，例如 `-qm` 指定 medium 画质。
- 渲染完成后视频会直接嵌入单元格输出下方；`-v WARNING` 用于隐藏冗长的日志。
- 若尚未安装 Jupyter，可用 `pip install "manim[jupyterlab]"` 一键装好。

:::notice warning
常见错误
社区版（ManimCE，导入名 `manim`）与 3Blue1Brown 原版（`manimgl` / `manimlib`）是两个不同的包。旧教程若让你安装 `manimlib` 或继承 `Scene` 之外的 GL 风格写法，请改用 `pip install manim==0.21.0`。
:::

:::notice tip
提示
若 `manim` 命令提示找不到，通常是 Python 的 Scripts 目录不在 `PATH` 中。可以改用 `python -m manim --version` 验证，或检查虚拟环境是否已激活。
:::

## 下一步

环境就绪后，下一节写出你自己的第一个场景，并理解 `Scene`、`play()` 与 `wait()` 三个核心概念。
