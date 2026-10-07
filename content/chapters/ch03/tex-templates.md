---
title: TeX 模板定制
---

# TeX 模板定制

`Tex`/`MathTex` 的编译行为由 `TexTemplate` 决定： preamble 里加载哪些宏包、用什么编译器、输出什么格式。模板不改，你就只能用 `amsmath` + `amssymb` 的基础能力；模板一改，中文排版、学校试卷模板、自定义宏都不是问题。

:::notice version
版本说明
本节示例依赖 LaTeX（中文示例需 XeLaTeX），由 CI 渲染。
:::

## TexTemplate

`TexTemplate` 是一个 dataclass，每个字段对应 LaTeX 文档的一部分。

```python
TexTemplate(
    tex_compiler: str | list[str] = "latex",
    description: str = "",
    output_format: str = ".dvi",
    documentclass: str = "\\documentclass[preview]{standalone}",
    preamble: str = "\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}",
    placeholder_text: str = "YourTextHere",
    post_doc_commands: str = "",
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `tex_compiler` | str \| list[str] | "latex" | 编译器；传 list 时按顺序**多趟编译**（如 `["lualatex", "pdflatex"]`） |
| `description` | str | "" | 模板描述 |
| `output_format` | str | ".dvi" | 编译输出格式 |
| `documentclass` | str | standalone | 文档类，`preview` 选项裁掉页边距 |
| `preamble` | str | babel+amsmath+amssymb | 导言区宏包 |
| `placeholder_text` | str | "YourTextHere" | 公式占位符 |
| `post_doc_commands` | str | "" | 文档结束后的命令 |
:::

常用方法：

```python
tpl = TexTemplate()
tpl.add_to_preamble(r"\usepackage{physics}")   # 追加导言区内容
tpl.add_to_document(r"\setlength{\parindent}{0pt}")  # 追加正文设置
code = tpl.get_texcode_for_expression(r"\dv{x} f(x)")  # 预览完整 tex 源码
```

使用方式：构造 `Tex`/`MathTex` 时传 `tex_template=...`，或写入全局配置。

:::notice version
版本说明
v0.21.0 起 `tex_compiler` 支持传入**编译器列表**实现多趟编译：如目录、交叉引用、TikZ 外部化等需要多次跑编译器的场景，写 `TexTemplate(tex_compiler=["lualatex", "lualatex"], output_format=".pdf")`，Manim 会按顺序执行并在日志中打印 `Compiling 1 of 2: ...`。
:::

:::demo examples/ch03/tex_template_ctex.py TexTemplateCtex
`TexTemplateLibrary.ctex` 是内置的中文模板（ctex 宏包 + 相应编译器），直接传给 `tex_template` 即可排版中文。本示例由 CI 渲染。
:::

中文排版最小模板（手动构造版）：

```python
from manim import *

ctex = TexTemplate(
    tex_compiler="xelatex",
    output_format=".xdv",
    preamble=r"""
\usepackage[UTF8]{ctex}
\usepackage{amsmath}
\usepackage{amssymb}
""",
)

class ChineseTex(Scene):
    def construct(self):
        self.play(Write(Tex("你好，$a^2+b^2=c^2$", tex_template=ctex)))
```

:::notice warning
常见错误
模板三件套必须互相匹配：中文 + `xelatex` + `ctex` 宏包缺一不可；`output_format` 要和编译器输出一致（`.dvi` / `.xdv` / `.pdf`）。编译报错先打印 `tpl.get_texcode_for_expression(...)` 检查生成的完整 tex 文件，再手动跑编译器看原始错误——Manim 的报错只截取了末尾。
:::

## TexTemplateLibrary

`TexTemplateLibrary` 是预置模板的命名空间，按需取属性即可。

:::compare
| 模板 | 内容 | 适用 |
| ---- | ---- | ---- |
| `default` | babel + amsmath + amssymb | 英文公式默认 |
| `simple` | 极简：仅文档类 | 自定义从零开始 |
| `ctex` | ctex 宏包 + xelatex | 中文排版 |
| `threeb1b` | 3Blue1Brown 视频同款宏包集 | 复刻官方视频风格 |
:::

```python
Tex(r"勾股定理 $a^2+b^2=c^2$", tex_template=TexTemplateLibrary.ctex)
```

## TexFontTemplates

`TexFontTemplates` 预置了一批**字体主题模板**（antykwa、biolinum、comfortaa、comic_sans 等），把整组字体宏包封装成一个模板：

```python
from manim import TexFontTemplates

tpl = TexFontTemplates.comic_sans.copy()  # 拷贝后再修改，避免污染共享模板
text = Tex(r"Funny $e^{i\pi}+1=0$", tex_template=tpl)
```

:::notice tip
提示
`TexTemplateLibrary` 与 `TexFontTemplates` 的属性是**共享实例**：改它的 preamble 会影响后续所有使用处。要定制请先 `.copy()`。
:::

## 自测

:::exercise
渲染中文“正弦定理”加公式 `\frac{a}{\sin A}=2R`，需要哪三样东西？
:::answer
`ctex` 宏包（或 `TexTemplateLibrary.ctex` 模板）、`xelatex` 编译器、与编译器匹配的输出格式。最省事的写法：`Tex(r"正弦定理 $\frac{a}{\sin A}=2R$", tex_template=TexTemplateLibrary.ctex)`。
:::
:::

:::exercise
TikZ 图形需要跑两遍 `lualatex` 才能定位正确，如何配置模板？
:::answer
传编译器列表，按顺序多趟编译：

```python
tpl = TexTemplate(
    tex_compiler=["lualatex", "lualatex"],
    output_format=".pdf",
)
tpl.add_to_preamble(r"\usepackage{tikz}")
```

渲染日志会显示 `Compiling 1 of 2: lualatex` / `Compiling 2 of 2: lualatex`。
:::
:::

## 下一步

「文本与公式」板块到此结束：五套文本方案、数字动画、列表标题、代码高亮与模板定制都已齐备。下一板块进入坐标系与数据可视化，从 `NumberLine` 开始。
