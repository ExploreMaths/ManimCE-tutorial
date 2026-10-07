---
title: Tex 与 MathTex
---

# Tex 与 MathTex

`Tex` 与 `MathTex` 把字符串交给 LaTeX 编译为 DVI/SVG 再导入，排版质量是五套文本方案中最高的，代价是需要安装 LaTeX（如 TeX Live）并承担编译耗时。

:::notice version
版本说明
本节所有示例依赖 LaTeX 发行版，本地无 LaTeX 时无法渲染。本站示例由 CI（安装了 TeX Live 的环境）统一渲染；请确保本机已安装 LaTeX 后再复现。
:::

## MathTex

`MathTex` 在**数学模式**下编译字符串，是渲染公式的首选。多个位置参数会按 `arg_separator` 连接成一个公式，默认用 `align*` 环境。

:::inheritance
MathTex → SingleStringMathTex → SVGMobject → VMobject
:::

```python
MathTex(
    *tex_strings: str,
    arg_separator: str = " ",
    substrings_to_isolate: Iterable[str] | None = None,
    tex_to_color_map: dict[str, ParsableManimColor] | None = None,
    tex_environment: str | None = "align*",
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `*tex_strings` | str | — | 一个或多个公式片段，按 `arg_separator` 连接 |
| `arg_separator` | str | " " | 多片段连接符 |
| `substrings_to_isolate` | Iterable[str] \| None | None | 需要隔离成独立子对象的子串 |
| `tex_to_color_map` | dict \| None | None | 子串 → 颜色映射（键自动加入隔离列表） |
| `tex_environment` | str \| None | "align*" | 包裹公式的 LaTeX 环境 |
:::

:::demo examples/ch03/tex_basic.py TexBasic
`MathTex` 直接进入数学模式；中文混排用 `Tex` 并配合 `TexTemplateLibrary.ctex` 模板（见「TeX 模板定制」一节）。本示例由 CI 渲染。
:::

### 多行行为

`tex_environment` 默认为 `"align*"`，因此**公式内显式写 `\\` 换行时会按 align 的列规则排版**；`tex_environment=None` 则不添加任何环境。传入多个字符串参数时，它们先按 `arg_separator`（默认一个空格）拼成一个字符串再编译，并不是每个参数一行——需要多行请显式写 `\\` 或使用多个公式环境。

### substrings_to_isolate 与 label 选取

`MathTex` 的每个子对象带有一个 `label`（形如 `"{a^2}"`），`get_part_by_tex()` 按 label 查找子对象。`substrings_to_isolate` 把指定子串预先隔离成独立子对象，使得嵌在复杂公式里的符号也能被精确选取：

:::demo examples/ch03/mathtex_labels.py MathTexLabels
`substrings_to_isolate=["a", "x"]` 把积分上下限里的 `a`、`x` 隔离出来，随后用 `get_part_by_tex("x")` 统一选中所有 `x` 改色。本示例由 CI 渲染。
:::

### {{ }} 双花括号分组

在单个字符串里写 `{{ ... }}` 可以把公式**就地拆成多个子对象**，分组之间以及分组内的文本各自成为独立子对象，非常适合 `TransformMatchingTex` 类动画：

```python
eq = MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}")
len(eq.submobjects)  # 5：a^2、+、b^2、=、c^2
```

:::demo examples/ch03/mathtex_groups.py MathTexGroups
`{{ }}` 分组让 `eq[0]`、`eq[2]`、`eq[4]` 直接对应三个平方项，可分别着色。本示例由 CI 渲染。
:::

识别规则：`{{` 必须出现在字符串开头或紧跟空白之后才会被当作分组符；`\frac{{{n}}}{k}`、`a^{{2}}` 这类紧贴前导字符的写法**不会**被拆分，普通嵌套花括号不受干扰。若确实想输出连续两个花括号，写成 `{ { ... } }`（中间加空格）。

:::notice warning
常见错误
`get_part_by_tex("x")` 依赖 label 的子串匹配。LaTeX 命令里的参数（如 `\frac` 的两个参数）在 label 中带有成对的**花括号**，因此按内容查找时要留意 label 实际是 `"{a^2}"` 这种带括号形式——查 `"a^2"` 可以匹配到，但对更复杂的嵌套结构，建议改用 `{{ }}` 显式分组后用整数索引，最不容易出错。
:::

:::notice warning
常见错误
编译失败时若检测到发生过 `{{ }}` 拆分，Manim 会在错误之外额外提示“可能是双花括号拆分导致的编译错误”，并给出规避写法。看到这条附加日志先检查花括号配对。
:::

## Tex

`Tex` 在**文本模式**下编译，适合排版普通文字与行内公式 `$...$`，其余行为与 `MathTex` 一致。

:::inheritance
Tex → MathTex → SingleStringMathTex → SVGMobject
:::

```python
Tex(*tex_strings: str, arg_separator: str = "", tex_environment: str | None = "center")
```

与 `MathTex` 的差异只有默认值：`arg_separator=""`、`tex_environment="center"`。中文排版需配合 `TexTemplateLibrary.ctex` 模板（默认模板只加载 `babel` + `amsmath` + `amssymb`，不支持中文）。

:::notice tip
提示
`Tex`/`MathTex` 中用 `\color`、`\textcolor` 排的颜色会保留下来，不会被 `set_color` 覆盖——这与 `Text` 的行为一致。
:::

## SingleStringMathTex

`SingleStringMathTex` 是 `MathTex` 的基类，负责真正的“单字符串 → LaTeX → SVG”编译（环境拼接、SVG 导入、子对象拆分都在这一层）。一般不需要直接使用它；`DecimalNumber` 等类的 `mob_class` 参数要求传入它的子类。

:::inheritance
SingleStringMathTex → SVGMobject → VMobject
:::

```python
SingleStringMathTex(
    tex_string: str,
    stroke_width: float = 0,
    should_center: bool = True,
    height: float | None = None,
    organize_left_to_right: bool = False,
    tex_environment: str | None = "align*",
    tex_template: TexTemplate | None = None,
    font_size: float = 48,
)
```

## MathTexPart

`MathTexPart` 是 `MathTex` 拆分后每个子对象的实际类型——一个带 `tex_string` 标注的 `VMobject` 子类。它不在 `manim` 顶层命名空间中，需要从 `manim.mobject.text.tex_mobject` 导入：

```python
from manim.mobject.text.tex_mobject import MathTexPart
```

它本身没有额外参数（构造签名与 `VMobject` 相同），了解它有两个用处：写类型标注时指认 `tex.submobjects` 的元素类型；以及在调试 label 匹配问题时打印 `part.tex_string` 观察实际拆分结果。

:::inheritance
MathTexPart → VMobject → Mobject
:::

## 自测

:::exercise
`MathTex(r"\frac{a+b}{2}")` 和 `MathTex(r"{{ \frac{a+b}{2} }}")` 的子对象数量分别是多少？为什么？
:::answer
前者只有 1 个子对象（整个公式不拆分）；后者也是 1 个子对象——`{{ }}` 把整个分数包成一个组，可通过 `eq[0]` 整体引用，便于 TransformMatchingTex 配对。要拆开分子分母，需写多个 `{{ }}` 或传多个字符串参数。
:::
:::

:::exercise
`MathTex("a^2 + b^2 = c^2", substrings_to_isolate=["b^2"]).get_part_by_tex("b^2")` 能选中目标吗？`tex_to_color_map={"b^2": RED}` 呢？
:::answer
都能。`substrings_to_isolate` 保证 `"b^2"` 被隔离成独立子对象，`get_part_by_tex` 按 label 子串匹配可以命中；`tex_to_color_map` 的键会自动并入隔离列表，构造完成后直接着色。
:::
:::

## 下一步

不想装庞大的 TeX Live？v0.21.0 新增的 `Typst` / `MathTypst` 用 Rust 实现的原生 Typst 编译器达到类似效果。
