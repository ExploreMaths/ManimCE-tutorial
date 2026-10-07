---
title: 匹配变换
---

# 匹配变换

普通 `Transform` 把整个物体糊成一团渐变。匹配变换（Matching Transforms）则先**拆解**两个物体的组成部分、按规则配对，相同的部件原地不动，不同的部件精准对换——公式变形、字母重排（Anagram）因此干净利落。

## TransformMatchingAbstractBase

两个具体类的共同基类，本身继承 `AnimationGroup`：匹配变换内部就是"一个整体 `Transform` + 若干子动画"的组合。

:::inheritance
TransformMatchingAbstractBase → AnimationGroup → Animation → object
:::

工作机制分三步：

1. **拆分**：`get_mobject_parts(mobject)` 把两边拆成部件列表（子类决定粒度）。
2. **配对**：`get_mobject_key(part)` 给每个部件算一个 key，key 相同的部件配成一对。
3. **组动画**：key 相同的部件 `Transform` 互变；key 对不上的部分按下述参数处理。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `transform_mismatches` | bool | False | 不匹配的部件互相做 `Transform` 变形 |
| `fade_transform_mismatches` | bool | False | 不匹配的部件互相做 `FadeTransformPieces` 淡入淡出变换 |
| `key_map` | dict \| None | None | 手动指定"源部件 key → 目标部件 key"的映射，强制把不相同的两个部件配成一对 |
:::

不匹配部件的默认行为（两个参数都保持 False）：源侧不匹配的部件朝目标侧不匹配部件的方向 `FadeOut`，目标侧不匹配的部件从源侧的方向 `FadeIn`——位置上有交代，但不变形。

:::notice warning
常见错误
`key_map` 的方向是**源 → 目标**（官方 docstring：把起始物体子对象的 key 映射到目标物体子对象的 key）。写反了不会报错，只是静默不生效（源码里 key 不存在时直接跳过该条映射）。两部分的 key 都要真实存在，建议先用 `get_mobject_key` 打印确认。
:::

## TransformMatchingShapes

`TransformMatchingShapes(mobject, target_mobject, ...)`：按**形状**匹配。key 是部件点坐标归一化（移到原点、高度缩到 1、坐标保留三位小数）后的哈希值——形状相同即匹配，颜色、大小、位置不影响。

```python
src = VGroup(Circle(), Square(), Triangle())   # 排成一行
tar = VGroup(Square(), Triangle(), Circle())   # 换个顺序
self.play(TransformMatchingShapes(src, tar))   # 每个图形飞到新位置，而不是整体糊掉
```

:::demo examples/ch05/matching_shapes.py MatchingShapesDemo
上排三个图形按形状一一对应飞到重排后的位置；下排两个圆变成四个圆，多出的部分用 `fade_transform_mismatches=True` 淡入。
:::

## TransformMatchingTex

`TransformMatchingTex(mobject, target_mobject, ...)`：按 `tex_string` 匹配，专用于 `MathTex`（或 `Tex`）。相同的符号原地保留，不同符号交叉换位，是公式推导演示的标配。

```python
eq1 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
eq2 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")
self.play(TransformMatchingTex(eq1, eq2))   # a²、b²、c² 各自飞去新位置
```

:::notice version
版本说明
v0.21.0 起 `MathTex` 的 `{{ ... }}` 双花括号写法会把 `{{a}}^2` 拆成 `"a"` 与 `"^2"` **两个独立部分**，key 是不含花括号的 `tex_string`（如 `"a"`、`"^2"`、`"+"`）。因此 `key_map` 要写成 `{"x": "a"}` 这种形式，旧教程里的 `"{x}^{2}"` 写法在本版本不会产生任何匹配。
:::

:::demo examples/ch05/matching_tex.py MatchingTexDemo
第一段把 `a²+b²=c²` 重排成 `a²=c²-b²`，相同平方项各自飞去新位置；第二段用 `key_map={"x": "a", ...}` 把 `x²+y²=z²` 强行对到上一式的 `a/b/c` 上。本示例需要本机安装 LaTeX，请在 CI 环境渲染。
:::

:::notice tip
提示
匹配粒度受 `MathTex(...)` 的逗号分段控制：分段越细、配对生活越精确，但过细的段会增加编译开销。调试时先 `self.add(eq)` 暂停一帧，确认每个符号确实是独立子对象，再播放匹配变换。
:::

## 自测

:::exercise
`TransformMatchingShapes` 为什么能认出"两个圆是同一个图形"，即使它们大小颜色不同？
:::answer
它的 key 来自部件**归一化后的点坐标哈希**：先把部件移到原点、高度缩放到 1、坐标四舍五入到三位小数，再对字节串取哈希。颜色、位置、缩放都不参与计算，只有形状（轮廓）决定 key。
:::
:::

:::exercise
`TransformMatchingTex(eq1, eq2)` 里某个符号两边拼写不同（如源里是 `x`、目标里是 `a`），但你想让它原地变形过去，该怎么做？方向注意什么？
:::answer
用 `key_map`：`TransformMatchingTex(eq1, eq2, key_map={"x": "a"})`。注意方向是**源 key → 目标 key**（`x` 在 eq1、`a` 在 eq2）；写反不会报错但静默失效。v0.21.0 中双花括号会把 `{{x}}^2` 拆成 `"x"` 与 `"^2"`，key 是不带花括号的 `tex_string`。
:::
:::

## 下一步

单个动画再丰富也只是一条时间线。下一节把多个动画编排成并行、串行、错峰的复合结构：`AnimationGroup` 与它的三个子类。
