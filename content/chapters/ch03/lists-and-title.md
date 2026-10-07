---
title: 列表与标题
---

# 列表与标题

`BulletedList` 快速生成圆点列表，`Title` 生成带分割线的页首标题。两者都继承自 `Tex`，因此默认走 LaTeX 排版（圆点本身也是 `MathTex(r"\cdot")` 渲染的）。

:::notice version
版本说明
本节示例依赖 LaTeX，由 CI 渲染。中文条目建议配合 `TexTemplateLibrary.ctex` 模板，见「TeX 模板定制」一节。
:::

## BulletedList

`BulletedList` 把每个位置参数排成一行，行首自动加圆点并左对齐纵向排列。

:::inheritance
BulletedList → Tex → MathTex → SingleStringMathTex
:::

```python
BulletedList(
    *items: str,
    buff: float = 0.5,
    dot_scale_factor: float = 2,
    tex_environment: str | None = None,
    dot_buff: float = 0.1,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `*items` | str | — | 每一行一个位置参数 |
| `buff` | float | 0.5 | 行间距 |
| `dot_scale_factor` | float | 2 | 圆点相对默认尺寸的比例 |
| `dot_buff` | float | 0.1 | 圆点与文字之间的间距 |
| `tex_environment` | str \| None | None | 覆盖默认的 TeX 环境 |
:::

其中 `buff` 与 `dot_buff` 取自常量 `MED_LARGE_BUFF`、`SMALL_BUFF`，随默认度量体系微调。

每个条目是 `bl[i]` 一个子对象（圆点 + 文字的组合），`fade_all_but()` 可以快速做“聚焦某一条”的效果：

:::demo examples/ch03/bulleted_list_demo.py BulletedListDemo
三条列表整体淡入，`fade_all_but("第二条要点", opacity=0.3)` 只保持目标条目全亮，适合讲解时的逐项聚焦。本示例由 CI 渲染。
:::

:::notice tip
提示
`BulletedList` 的条目走 TeX 文本模式，条目里可以直接写 `$...$` 行内公式；中文条目需通过 `tex_template=TexTemplateLibrary.ctex` 传入。需要 Pango 字体的项目符号列表，更灵活的做法是 `VGroup` + `Text` + `Dot` 手工拼。
:::

## Title

`Title` 生成置于画面顶部的标题，默认在标题下方带一条**贯穿画面的分割线**。

:::inheritance
Title → Tex → MathTex → SingleStringMathTex
:::

```python
Title(
    *text_parts: str,
    include_underline: bool = True,
    match_underline_width_to_text: bool = False,
    underline_buff: float = 0.25,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `*text_parts` | str | — | 标题文本，多个参数按 TeX 拼接 |
| `include_underline` | bool | True | 是否绘制下划线 |
| `match_underline_width_to_text` | bool | False | True 时下划线宽度匹配文字，False 时贯穿画面 |
| `underline_buff` | float | 0.25 | 标题与下划线间距 |
:::

:::demo examples/ch03/title_demo.py TitleDemo
第一个标题用默认的全宽下划线；`match_underline_width_to_text=True` 让第二个标题的下划线跟随文字宽度。本示例由 CI 渲染。
:::

关于 `Title` 的缩放行为：标题本身是一个整体 Mobject，`animate.scale(...)` 会把文字和下划线一起缩放；但下划线宽度是**构造时**按当时文字宽度计算的，之后再改变文字内容不会自动跟随。要“文字变了、线跟着变”，需手动 `title.underline.match_width(title)` 或重建 `Title`。

:::compare
| | BulletedList | Title |
| - | ------------ | ----- |
| 继承 | Tex | Tex |
| 子对象 | 每条目一个（圆点 + 文字） | 文字 + 下划线 |
| 定位 | 原点附近纵向排列 | 自动贴 `UP` 边缘 |
| 便捷方法 | `fade_all_but` | 无（`underline` 属性） |
:::

:::notice warning
常见错误
`Title` 构造后自动 `to_edge(UP)`，再用 `shift` 会基于已经贴边的位置偏移，容易超出画面。想自定义位置请用 `title.to_edge(UP, buff=...)` 重新贴边，而不是叠加大偏移。
:::

## 自测

:::exercise
如何只让第三条列表项保持高亮，其余淡出到 30% 透明度？
:::answer

```python
bl = BulletedList("一", "二", "三")
bl.fade_all_but(2, opacity=0.3)  # 按索引
# 或 bl.fade_all_but("三", opacity=0.3)  # 按文本匹配
```

`fade_all_but` 接受整数索引或条目文本字符串。
:::
:::

:::exercise
为什么 `title = Title("A")` 之后 `title.become(Title("更长的一段标题"))` 会让下划线错位？
:::answer
`become` 只对齐了子对象点集；下划线宽度在构造 `Title("A")` 时已固定为当时的文字宽度，`become` 不会重新计算它。正确做法是重建：`title_new = Title("更长的一段标题")` 后用 `Transform(title, title_new)`，或改文字后手动 `title.underline.match_width(title)`。
:::
:::

## 下一步

最后一类结构化文本是代码——下一节看 `Code` 如何用 Pygments 做语法高亮，以及 v0.21.0 的配色机制变更。
