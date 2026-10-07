---
title: Typst 与 MathTypst (v0.21.0 新增)
---

# Typst 与 MathTypst (v0.21.0 新增)

v0.21.0 引入了一套基于 **Typst** 的文本方案：通过 Python 包 `typst`（Rust 实现的原生编译器，自带于 `manim[typst]` 可选依赖）把 Typst 标记编译为 SVG，再经 `SVGMobject` 导入。**无需安装任何 TeX 发行版**，也不用 Pango。

:::notice version
版本说明
`Typst` 与 `MathTypst` 是 v0.21.0 新增类，属于可选依赖。安装方式：`pip install "manim[typst]"`（或直接 `pip install typst`）。未安装 `typst` 包时使用这两个类会抛出导入错误。
:::

## Typst

`Typst` 接收一段 Typst 标记源码，编译为 SVG 后导入。源码会被原样放入一个最小 Typst 文档的正文，因此 `= 标题`、`#set`、`#import` 等 Typst 语法全部可用。

:::inheritance
Typst → SVGMobject → VMobject
:::

```python
Typst(
    typst_code: str,
    *,
    font_size: float = 48,
    typst_preamble: str = "",
    color: ParsableManimColor | None = None,
    stroke_width: float | None = None,
    font_paths: list[str | Path] | None = None,
    track_baselines: bool = False,
    should_center: bool = True,
    height: float | None = None,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `typst_code` | str | — | Typst 标记源码 |
| `font_size` | float | 48 | Manim 字号单位；实际缩放发生在 SVG 导入之后 |
| `typst_preamble` | str | "" | 正文之前插入的 `#set`/`#import`/`#show` 规则 |
| `color` | color \| None | None | 覆盖整段文字颜色（会覆盖 Typst 内的 fill） |
| `stroke_width` | float \| None | None | SVG 描边宽度覆盖；None 保留 Typst 输出 |
| `font_paths` | list \| None | None | 附加字体搜索目录 |
| `track_baselines` | bool | False | 记录基线参考，供 `get_baseline_frame()` 使用 |
:::

:::demo examples/ch03/typst_demo.py TypstDemo
`#set text(size: ...)` 控制 Typst 侧字号，`= 标题` 是 Typst 的标题语法，下划线 `_..._` 表示强调。Typst 原生编译，无需 TeX。
:::

## MathTypst

`MathTypst` 是 `Typst` 的便捷包装：输入**不带 `$` 定界符**的数学表达式，自动包成显示级公式 `$ ... $`。

:::inheritance
MathTypst → Typst → SVGMobject
:::

```python
MathTypst(math_expression: str, **kwargs)
```

`**kwargs` 原样转发给 `Typst`。

### {{ }} 分组与 label 选择

`MathTypst` 支持 `{{ content }}` 双花括号分组：每个分组被包进带标签的 `manimgrp`，编译后的 SVG 中对应可识别的组。分组可以显式命名——`{{ content : label }}`，不写名字则自动编号为 `_grp-0`、`_grp-1`…… 用 `select(key)` 选取，`key` 可以是标签名（str）或自动分组的整数序号：

```python
eq = MathTypst("{{ a^2 + b^2 : lhs }} = {{ c^2 : rhs }}")
eq.select("lhs")   # 按标签
eq.select(1)       # 按自动分组序号
```

:::demo examples/ch03/mathtypst_groups.py MathTypstGroups
`{{ a^2 + b^2 : lhs }}` 与 `{{ c^2 : rhs }}` 把等式两侧分成两个命名组，`select("lhs")` / `select("rhs")` 选中后分别着色。
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `key`（`select`） | str \| int | — | 标签名，或自动分组 `_grp-N` 的整数序号 N |
:::

`select` 找不到标签抛 `KeyError`，整数序号越界抛 `IndexError`。

:::notice warning
常见错误
`MathTypst` 的 `{{ }}` 与 `MathTex` 的双花括号拆分是两套独立机制：前者产生 Typst 侧的 `manimgrp` 标签组，后者在 Python 侧把字符串拆成多个子对象。混用两套文本方案时不要把习惯从一个照搬到另一个。
:::

:::notice tip
提示
Typst 数学语法与 LaTeX 有差异：上标是 `x^2`（同），分数写作 `a/b` 或 `frac(a, b)`，根号是 `sqrt(x)`，希腊字母是 `alpha`、`pi` 等裸标识符。写 `MathTypst` 时按 Typst 语法书写。
:::

## 自测

:::exercise
本机没有安装 TeX Live，能使用 `MathTypst` 渲染 `x^2 + y^2` 吗？需要装什么？
:::answer
可以。`MathTypst` 走 Python `typst` 包（Rust 二进制扩展），与系统 TeX 无关。需要 `pip install "manim[typst]"` 或 `pip install typst`；装好即可渲染。
:::
:::

:::exercise
`MathTypst("{{ a+b : x }} = {{ c }}")` 中，`eq.select(1)` 选中的是哪一部分？`eq.select("x")` 呢？
:::answer
`select(1)` 按自动分组 `_grp-N` 的整数序号选取，只统计**未命名**的分组：这里只有 `{{ c }}` 一个未命名组，所以 `select(1)` 越界抛 `IndexError`（`select(0)` 选中 `c` 部分）。`select("x")` 按显式标签选中 `a+b` 部分。
:::
:::

## 下一步

五套文本方案各有拥趸，下一节把它们放在一张表里正面对比，并给出选型决策树。
