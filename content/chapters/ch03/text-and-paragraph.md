---
title: Text 与段落
---

# Text 与段落

Manim 中最常用的文本类是 `Text`：它把字符串交给 Pango 排版、再转成 SVG 矢量图形，因此**无需安装 TeX 就能显示包括中文在内的 Unicode 文本**。本节覆盖 `Text` 的完整参数体系、两种索引约定、多行排版 `Paragraph`，以及自定义字体 `register_font`。

## Text

`Text` 用于渲染一段纯文本，每个可见字符对应一个子对象（submobject），可以按索引或切片单独着色、移动、替换。

:::inheritance
Text → SVGMobject → VMobject → Mobject
:::

```python
Text(
    text: str,
    fill_opacity: float = 1.0,
    stroke_width: float = 0,
    color: ParsableManimColor | None = None,
    font_size: float = 48,
    line_spacing: float = -1,
    font: str = "",
    slant: str = "NORMAL",
    weight: str = "NORMAL",
    t2c: dict[str, str] | None = None,
    t2f: dict[str, str] | None = None,
    t2g: dict[str, Iterable[ParsableManimColor]] | None = None,
    t2s: dict[str, str] | None = None,
    t2w: dict[str, str] | None = None,
    gradient: Iterable[ParsableManimColor] | None = None,
    tab_width: int = 4,
    warn_missing_font: bool = True,
    height: float | None = None,
    width: float | None = None,
    should_center: bool = True,
    disable_ligatures: bool = False,
    use_svg_cache: bool = False,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `text` | str | — | 要渲染的文本 |
| `font_size` | float | 48 | 字号（Manim 字体单位，非像素） |
| `font` | str | "" | 字体名或字体文件路径；空串用 Pango 默认字体 |
| `weight` | str | "NORMAL" | 字重：`NORMAL`/`BOLD` 等，也可用常量 `BOLD` |
| `slant` | str | "NORMAL" | 字态：`NORMAL`/`ITALIC`/`OBLIQUE` |
| `color` | ParsableManimColor \| None | None | 整体颜色 |
| `gradient` | Iterable[color] \| None | None | 渐变填充色列表，与 `t2c` 互斥 |
| `t2c` | dict \| None | None | 文本子串 → 颜色映射 |
| `t2f` | dict \| None | None | 文本子串 → 字体映射 |
| `t2g` | dict \| None | None | 文本子串 → 渐变映射 |
| `t2s` | dict \| None | None | 文本子串 → 字态映射 |
| `t2w` | dict \| None | None | 文本子串 → 字重映射 |
| `line_spacing` | float | -1 | 行距倍数，-1 时用字体默认行距 |
| `tab_width` | int | 4 | 制表符展开为空格数 |
| `disable_ligatures` | bool | False | 禁用连字，强制字符与字形一一对应 |
| `warn_missing_font` | bool | True | 字体找不到时是否告警 |
| `height` / `width` | float \| None | None | 指定后整体缩放到目标高度/宽度 |
| `should_center` | bool | True | 构造后是否居中到原点 |
| `use_svg_cache` | bool | False | 相同文本复用 SVG 缓存 |
:::

下面这个示例依次演示 `gradient` 整体渐变、`t2c` 子串着色、`weight`/`slant` 字重字态：

:::demo examples/ch03/text_basics.py TextBasics
`gradient` 接受颜色列表做线性渐变；`t2c` 按子串匹配着色；`weight` 与 `slant` 控制整段字的粗斜体。
:::

### t2c 与切片的索引约定

`t2c` 等映射的键除了子串，还可以是**作用于原始字符串的切片**（如 `"[3:7]"`）。这里有一个极易踩坑的地方：两种索引方式对空白的处理**不一致**（v0.21.0 源码中的明确行为）：

- `my_text[3:5]`：索引到**渲染出的字符**，即“去掉空白后的文本”。`Text("Hello world")` 的索引 `5` 指的是 `"w"`，而不是空格。
- `t2c={"[3:7]": RED}`：切片作用于**原始 `text` 参数**，空白也算在内。`t2c={"[3:7]": RED}` 着色的会是 `"llo W"`。

:::demo examples/ch03/text_index_slice.py TextIndexSlice
`direct_text[0:5]` 按去空白后的渲染字符计数（空格不占位），而 `t2c={"[0:3]": ...}` 按原始字符串切片——两套约定不要混用。
:::

### 常见坑

:::notice warning
常见错误
连字（ligature）会让多个字符合并成一个字形，破坏“一字符一字形”的对应关系，直接索引会错位。涉及逐字符动画时传 `disable_ligatures=True`。若排版后字形数仍少于非空白字符数，v0.21.0 会直接抛出 `ValueError`，提示选择实现连字方式不同的字体（例如带 `calt` 特性的编程连字字体 Fira Code）。
:::

:::notice warning
常见错误
`font` 传不存在的字体名不会报错，只会静默回退到默认字体并在日志告警（可用 `warn_missing_font=False` 关闭）。要确认字体是否真正生效，渲染后用 `text.submobjects[0]` 的实际字形核对，或直接指定字体文件路径。
:::

:::notice tip
提示
`gradient` 与 `t2c` 互斥：同时传入时按 `t2c` 优先处理。想“整体渐变 + 局部改色”，请先 `gradient` 再对子对象 `set_color`。
:::

## Paragraph

`Paragraph` 用于**多行段落**：每个位置参数是一行文本，整体是一个 `VGroup`，每行是一个子对象，可单独取出行做动画。

:::inheritance
Paragraph → VGroup → VMobject → Mobject
:::

```python
Paragraph(*text: str, line_spacing: float = -1, alignment: str | None = None, **kwargs)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `*text` | str | — | 每一行一个位置参数 |
| `line_spacing` | float | -1 | 行距倍数，-1 时用默认行距 |
| `alignment` | str \| None | None | 每行对齐方式：`"left"`/`"center"`/`"right"`，None 时左对齐 |
:::

其余 `**kwargs`（`font_size`、`t2c`、`font` 等）原样传给内部的 `Text`。

:::demo examples/ch03/paragraph_demo.py ParagraphDemo
`Paragraph` 每行是一个子对象，`para[2]` 直接取出行设置颜色；`alignment="center"` 让每行居中。
:::

`Text` 与 `Paragraph` 的分工：

:::compare
| | Text | Paragraph |
| - | ---- | --------- |
| 输入 | 单个字符串（含 `\n`） | 每行一个参数 |
| 结构 | 每个字符一个子对象 | 每行一个子对象 |
| 逐字动画 | 直接支持 `text[3]` | 需先取行再索引 |
| 逐行对齐 | 不支持（整体对齐） | 支持 `alignment` |
| 适用场景 | 标题、标注、逐字效果 | 正文段落、行级动画 |
:::

## register_font

`register_font` 把字体文件临时加入 Pango 搜索路径，让 `Text(..., font=...)` 能用未安装到系统的字体。**必须用上下文管理器 `with` 使用**，退出后字体即从搜索路径移除。

```python
from manim import *

class CustomFont(Scene):
    def construct(self):
        with register_font("assets/MyFont.ttf"):
            text = Text("自定义字体", font="My Font Name")
        self.play(Write(text))
```

文件查找顺序：绝对路径 → `assets/fonts/` → `fonts/` → 当前目录。找不到文件抛 `FileNotFoundError`。

:::notice warning
平台注意
`register_font` 在 macOS 上依赖 `ManimPango>=0.2.3`，更早版本会抛 `AttributeError`。Windows 与 Linux 无此限制。CI 环境若缺字体，渲染结果会回退为默认字体——建议把字体文件随仓库放在 `assets/fonts/` 下。
:::

## remove_invisible_chars

`remove_invisible_chars(mobject)` 返回一个去掉不可见字符（空格等宽度为零的占位）的副本，常用于 `TransformMatchingShapes` 等需要“按可见字形配对”的场景，避免空白占位干扰匹配。

```python
def remove_invisible_chars(mobject: VMobject) -> VMobject
```

:::notice version
版本说明
v0.21.0 起，字形缺失/不对应时的报错信息显著改进：错误信息会明确指出是连字（含 `calt` 类编程连字）导致字符与字形无法一一对应，并建议更换字体。另外空白与换行**从不成为子对象**，索引约定与文档字符串中的描述完全一致（见上文「t2c 与切片的索引约定」）。
:::

## 自测

:::exercise
`Text("Hello World")[6]` 选中的是哪个字符？`t2c={"[6:11]": RED}` 着色的又是哪段？
:::answer
`text[6]` 按去空白后的渲染字符计数，`"HelloWorld"` 索引 6 是 `"o"`（World 的第二个字母）。`t2c` 切片按原始字符串计空白，`"[6:11]"` 着色的是 `"World"`。
:::
:::

:::exercise
要对 `"efficient"` 中的 `ffi` 连字做逐字变色动画，只按索引取子对象会发生什么？怎么避免？
:::answer
默认情况下 `ffi` 可能被排成一个连字字形，索引与子对象错位。构造时传 `disable_ligatures=True` 强制一字符一字形，再按索引操作；若字形数仍对不上，v0.21.0 会抛 `ValueError` 并提示换用连字实现方式不同的字体。
:::
:::

## 下一步

纯文本之外，`MarkupText` 让你用 Pango 标记语言直接控制字号、颜色、上下标等富文本效果。
