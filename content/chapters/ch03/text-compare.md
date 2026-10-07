---
title: 文本方案对比
---

# 文本方案对比

板块三介绍了五套文本方案：`Text`（Pango 纯文本）、`MarkupText`（Pango 富文本）、`Tex`/`MathTex`（LaTeX）、`Typst`/`MathTypst`（v0.21.0 新增）。本节把它们放在同一张表里正面对比，并给出选型决策树。

## 总对比表

:::compare
| | Text | MarkupText | Tex / MathTex | Typst / MathTypst |
| - | ---- | ---------- | ------------- | ----------------- |
| 渲染引擎 | Pango → SVG | Pango → SVG | LaTeX → DVI/SVG | typst (Rust) → SVG |
| 外部依赖 | ManimPango | ManimPango | TeX Live / MiKTeX | Python `typst` 包 |
| 安装成本 | 零 | 零 | 数 GB | 一条 pip 命令 |
| 文本语法 | 纯文本 | Pango 标记 | LaTeX 文本/数学模式 | Typst 标记/数学模式 |
| 中文支持 | 直接支持 | 直接支持 | 需 ctex 模板 + XeLaTeX | 直接支持 |
| 数学公式 | 不支持 | 仅上下标 | 完整（amsmath） | 完整（Typst math） |
| 逐字/逐组动画 | 字符级子对象 | 字符级子对象 | `substrings_to_isolate` / `{{ }}` | `{{ }}` + `select` |
| 富文本（粗斜体/颜色/字号） | `t2c`/`t2w` 等映射 | 内联标签 | `\textbf` 等命令 | Typst `#set`/`_ _` |
| 首次渲染耗时 | 快 | 快 | 慢（秒级编译） | 中等（毫秒级编译） |
| 缓存 | SVG 缓存可选 | SVG 缓存可选 | 部分视频缓存 | SVG 缓存可选 |
| 排版质量 | 良 | 良 | 最优 | 优 |
| 适用场景 | 中文标注、简单文字 | 富文本混排 | 正式数学公式 | 轻量公式、免 TeX 环境 |
:::

几点补充说明：

- **性能**：`Text`/`MarkupText` 只做一次 Pango 排版，最快；`Tex`/`MathTex` 每次都要调起 LaTeX 编译，几十个公式场景会明显拖慢迭代；`Typst` 编译在毫秒级，介于两者之间。
- **颜色机制**：`Text` 系与 `Tex` 系都是 SVG 导入，Manim 颜色对象直接可用；`MarkupText` 的 `<span foreground>` 与 Typst 内联颜色则用各自语法（十六进制 / Typst 颜色函数），`Typst(color=...)` 会整体覆盖 Typst 内部 fill。
- **子对象粒度**：`Text` 按字符拆分，做逐字动画最自然；`MathTex` 默认整式一个子对象，需要 `substrings_to_isolate` 或 `{{ }}` 主动拆分；`MathTypst` 的 `{{ }}` + `select` 是三者中最接近“按语义分组”的。

## 选型决策树

```text
要渲染的内容是什么？
├─ 数学公式
│   ├─ 已装 LaTeX，追求最高排版质量 ──→ MathTex（中文混排用 Tex + ctex 模板）
│   ├─ 不想装 TeX / CI 环境受限 ────→ MathTypst
│   └─ 只有简单上下标 ──────────────→ MarkupText（<sup>/<sub>）
└─ 普通文字
    ├─ 含中文 ──────────────────────→ Text（无需任何额外依赖）
    ├─ 需要粗斜体、多字号混排 ────────→ MarkupText
    ├─ 需要整段文档式排版（标题/列表/强调）→ Typst
    └─ 需要 LaTeX 文本排版质量 ───────→ Tex
```

再叠加两条约束：

- **逐字/逐组动画需求强** → 优先 `Text`（字符天然是子对象）或 `MathTypst`（`{{ }}` 语义分组）；`MathTex` 要先规划隔离子串。
- **渲染环境不可控**（观众复现、CI、插件分发）→ 优先 Pango 系或 Typst，避免把数 GB 的 LaTeX 作为隐形依赖。

## 常见坑

:::notice warning
常见错误
不要在中途换引擎：同一个场景里 `Text` 和 `MathTex` 的字体、基线、笔画宽度体系完全不同，`Transform` 跨引擎变形会得到难看的中间帧。跨方案切换用 `FadeOut`/`FadeIn` 或 `ReplacementTransform`。
:::

:::notice tip
提示
混排公式 + 中文标注的最省心组合是：`MathTex` 出公式、`Text` 出中文注释，用 `next_to`/`arrange` 手工对齐。两者都是成熟路径，CI 与本地行为一致。
:::

## 自测

:::exercise
目标：渲染中文标题“牛顿-莱布尼茨公式”和公式 `∫_a^b f(x)dx = F(b)-F(a)`，机器没装 LaTeX。选哪套方案？写出关键代码。
:::answer
公式用 `MathTypst`（免 TeX），标题用 `Text`：

```python
title = Text("牛顿-莱布尼茨公式")
formula = MathTypst(r"integral_a^b f(x) dif x = F(b) - F(a)")
formula.next_to(title, DOWN)
```
:::
:::

:::exercise
为什么大量公式场景推荐预渲染或缓存策略？Tex/MathTex 与其他方案比瓶颈在哪？
:::answer
`Tex`/`MathTex` 每个（或每组）公式都要启动一次外部 LaTeX 进程编译，秒级耗时且进程启动开销固定；Pango 与 Typst 都在进程内完成排版，毫秒级。公式多时 LaTeX 路径成为主要瓶颈，可利用 Manim 的部分视频缓存（默认开启）跳过未修改片段，或把静态公式预渲染为 SVG/图片。
:::
:::

## 下一步

对比完引擎，回到具体对象：下一节看数字相关类 `DecimalNumber`、`Integer` 与 `Variable`——它们让数值本身成为可动画的对象。
