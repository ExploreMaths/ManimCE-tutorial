---
title: MarkupText
---

# MarkupText

`MarkupText` 与 `Text` 共用 Pango 渲染管线，但输入是 **Pango 标记语言**（类似 HTML 的标签文本）：你可以在字符串里直接写 `<span>`、`<b>`、`<i>`、`<sub>` 等标签，实现富文本排版，而不必事后按索引逐个改色。

## MarkupText

`MarkupText` 用于渲染带 Pango 标记的富文本；标记标签在排版时生效，最终仍转成 SVG 矢量图形。

:::inheritance
MarkupText → SVGMobject → VMobject → Mobject
:::

```python
MarkupText(
    text: str,
    fill_opacity: float = 1,
    stroke_width: float = 0,
    color: ParsableManimColor | None = None,
    font_size: float = 48,
    line_spacing: float = -1,
    font: str = "",
    slant: str = "NORMAL",
    weight: str = "NORMAL",
    justify: bool = False,
    gradient: Iterable[ParsableManimColor] | None = None,
    tab_width: int = 4,
    height: int | None = None,
    width: int | None = None,
    should_center: bool = True,
    disable_ligatures: bool = False,
    warn_missing_font: bool = True,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `text` | str | — | 含 Pango 标记的文本 |
| `justify` | bool | False | 是否两端对齐（仅多行有效） |
| `font_size` | float | 48 | 基础字号，可被标签内 `size` 覆盖 |
| `font` / `slant` / `weight` | str | "NORMAL" | 同 `Text`，标签内的对应属性优先 |
| `gradient` | Iterable[color] \| None | None | 整体渐变填充 |
| `disable_ligatures` | bool | False | 禁用连字 |
:::

注意：`MarkupText` **没有** `t2c`/`t2f`/`t2g`/`t2s`/`t2w` 参数——颜色、字体等效果都通过标记标签实现。

### 常用标签

:::compare
| 标签 | 作用 | 示例 |
| ---- | ---- | ---- |
| `<b>` / `<i>` / `<u>` | 粗体 / 斜体 / 下划线 | `<b>加粗</b>` |
| `<sub>` / `<sup>` | 下标 / 上标 | `x<sup>2</sup>` |
| `<span foreground>` | 文字颜色（十六进制） | `<span foreground="#FFFF00">黄</span>` |
| `<span background>` | 背景色 | `<span background="blue">反白</span>` |
| `<span size>` | 字号（`x-small`~`xx-large` 或 pt） | `<span size="x-large">大</span>` |
| `<span font_family>` | 字体 | `<span font_family="serif">衬线</span>` |
| `<span rise>` | 基线升降（替代 sub/sup） | `<span rise="5000">上</span>` |
| `<span strikethrough>` | 删除线 | `<span strikethrough="true">删</span>` |
:::

:::demo examples/ch03/markup_text_demo.py MarkupTextDemo
`<span>` 的 `foreground`/`size` 控制标题颜色与字号；`<sup>`/`<sub>` 直接排出上下标；`<b>`/`<i>` 是粗斜体的简写。
:::

### 与 Text 的对比

:::compare
| | Text | MarkupText |
| - | ---- | ---------- |
| 语法 | 纯文本 | Pango 标记 |
| 局部着色 | `t2c` 子串映射 | 标签内联 |
| 上标/下标 | 不支持 | `<sup>` / `<sub>` |
| 嵌套不同字体 | `t2f` | `<span font_family>` |
| 颜色值格式 | Manim 颜色对象 | 十六进制字符串 |
| 性能 | 略快（无标记解析） | 略慢 |
| 适用场景 | 程序化批量改色 | 富文本、混排排版 |
:::

:::notice warning
常见错误
Pango 标记是 XML：文本里的 `&`、`<`、`>` 必须转义为 `&amp;`、`&lt;`、`&gt;`，否则排版直接报错。颜色属性**只认十六进制字符串**（如 `"#58C4DD"`），不要传 `RED` 之类的 Manim 颜色常量。
:::

:::notice tip
提示
标签里引号用单引号更方便在 Python 字符串中书写：用双引号包裹 Python 字符串、单引号包裹属性值。`MarkupText` 的子对象结构与 `Text` 一致，连字、`disable_ligatures` 的行为也完全相同。
:::

## 自测

:::exercise
写出渲染 `速度 v = 2 m/s，平方 v²`（其中 2 为下标、² 用上标）的 MarkupText 调用。
:::answer

```python
MarkupText('速度 v<sub>2</sub> = 2 m/s，平方 v<sup>2</sup>')
```

注意属性值不需要引号问题——标签整体在 Python 字符串内，标签属性用双引号。
:::
:::

:::exercise
想在 MarkupText 里显示 `a < b`，直接写会怎样？正确写法？
:::answer
`<` 会被当成标签起始符导致 Pango 解析失败。正确写法是转义：`MarkupText("a &lt; b")`，`&` 与 `>` 同理写成 `&amp;`、`&gt;`。
:::
:::

## 下一步

纯文本与富文本解决了“写字”，数学公式则交给基于 LaTeX 的 `Tex` 与 `MathTex`。
