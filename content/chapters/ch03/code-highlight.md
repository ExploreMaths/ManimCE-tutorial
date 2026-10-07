---
title: Code 代码高亮
---

# Code 代码高亮

`Code` 把一段源代码交给 **Pygments** 做词法分析与语法高亮，再用 Pango（`Paragraph`）排版，因此**不需要 LaTeX**，也能正确渲染中文注释。

## Code

`Code` 用于在场景中展示带语法高亮的代码块，支持两种来源：`code_file` 从文件读取，`code_string` 直接传字符串（二者必选其一）。

:::inheritance
Code → VMobject → Mobject
:::

```python
Code(
    code_file: StrPath | None = None,
    code_string: str | None = None,
    language: str | None = None,
    formatter_style: str | type[Style] = "vim",
    tab_width: int = 4,
    add_line_numbers: bool = True,
    line_numbers_from: int = 1,
    background: Literal["rectangle", "window"] = "rectangle",
    background_config: dict[str, Any] | None = None,
    paragraph_config: dict[str, Any] | None = None,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `code_file` / `code_string` | — | None | 代码来源，二选一 |
| `language` | str \| None | None | 语言名（Pygments lexer）；None 时自动猜测 |
| `formatter_style` | str \| type[Style] | "vim" | Pygments 配色方案名，或 `Style` 子类 |
| `tab_width` | int | 4 | 制表符展开宽度 |
| `add_line_numbers` | bool | True | 是否加行号 |
| `line_numbers_from` | int | 1 | 起始行号 |
| `background` | str | "rectangle" | `"rectangle"` 纯色底板 / `"window"` 圆角窗口 |
| `background_config` | dict \| None | None | 底板样式（`fill_color`、`fill_opacity`、`stroke_color` 等） |
| `paragraph_config` | dict \| None | None | 透传给内部 `Paragraph` 的文本参数（见下方版本说明） |
:::

:::demo examples/ch03/code_demo.py CodeDemo
`language="python"` 指定 lexer，`background="window"` 换成圆角窗口外观；中文注释照常渲染。
:::

### 自定义配色：formatter_style

`formatter_style` 除了传 Pygments 内置方案名（`"vim"`、`"monokai"`、`"github-dark"` 等），还可以直接传 **`pygments.style.Style` 的子类**，完全自定义每种 token 的颜色：

```python
from pygments.style import Style
from pygments.token import Keyword, Name, String

class NordLike(Style):
    background_color = "#2E3440"
    styles = {
        Keyword: "#81A1C1",
        Name.Function: "#88C0D0",
        String: "#A3BE8C",
    }

code = Code(code_string="...", language="python", formatter_style=NordLike)
```

:::demo examples/ch03/code_formatter_style.py CodeFormatterStyle
`NordLike` 是一个 `Style` 子类：`background_color` 决定底板色，`styles` 字典按 token 类型指定颜色，传入 `formatter_style` 即生效。
:::

:::notice version
版本说明
v0.21.0 重大变更：`Code` 的颜色处理**整体委托给 Pygments**。此前 `paragraph_config={"color": ...}` 可以覆盖文字颜色，现在源码会显式丢弃 `paragraph_config` 里的 `color` 键——改文字颜色请通过 `formatter_style` 的 `Text` token 颜色（或换配色方案）。行号颜色不受 formatter 控制，仍走 `paragraph_config` 其余键。
:::

:::compare
| 配色方式 | 写法 | 适用 |
| -------- | ---- | ---- |
| 内置方案 | `formatter_style="monokai"` | 快速出片 |
| 自定义 Style 子类 | `formatter_style=MyStyle` | 品牌色、暗色主题 |
| paragraph_config 其余键 | 字号、行距等 | 只影响排版，不影响颜色 |
:::

:::notice warning
常见错误
`language` 拼错会抛 `ClassNotFound`（Pygments 找不到 lexer）；`language=None` 时靠猜测，短代码片段可能猜错语言导致高亮异常。不确定时显式指定。另外 `Code` 的每行是 `Paragraph` 的独立子对象，整体 `scale` 正常，但逐字符索引没有语义，选中某一行用 `code[2]` 这类行级索引。
:::

## 自测

:::exercise
v0.21.0 之前能用的 `Code(..., paragraph_config={"color": YELLOW})` 现在为什么无效？正确改法？
:::answer
v0.21.0 起颜色由 Pygments 全权负责，构造时 `paragraph_config` 中的 `color` 键被显式移除。正确做法是自定义配色：`formatter_style` 传一个 `Style` 子类，在 `styles` 中设置 `Token`（普通文本）等 token 的颜色。
:::
:::

:::exercise
`Code(code_string="print('你好')", language=None)` 在 CI 上高亮异常，可能是什么原因？
:::answer
`language=None` 时 Pygments 对代码内容做语言猜测，`print('你好')` 这类短片段线索不足，可能猜成别的语言，高亮规则随之错乱。显式写 `language="python"` 即可消除不确定性。
:::
:::

## 下一步

需要 LaTeX 却又嫌默认模板不够用（比如中文排版）？最后一节看 `TexTemplate` 如何定制编译模板。
