---
title: 创建家族
---

# 创建家族

创建（Creation）动画管"物体如何进场"：描边、填色、逐字、逐批、打字机……它们的共同点是 `introducer=True`——动画开始时物体进入场景。先给一张选型表，再逐个展开。

:::compare
| 需求 | 用哪个 |
| ---- | ---- |
| 图形/曲线一笔画出 | `Create` |
| 先描边再填充的厚重感 | `DrawBorderThenFill` |
| 文字沿笔画书写 | `Write` |
| 子对象一批批/一个个出现 | `ShowIncreasingSubsets` / `ShowSubmobjectsOneByOne` |
| 文字逐字符/逐词淡入 | `AddTextLetterByLetter` / `AddTextWordByWord` |
| 打字机效果（带光标） | `TypeWithCursor` |
| 成群物体螺旋飞入 | `SpiralIn` |
:::

## Create

`Create(mobject, lag_ratio=1.0)` 沿 `VMobject` 的描边逐点"画"出物体，是图形进场的主力。`lag_ratio=1.0` 让组成它的各条子路径依次绘制而非同时。

:::inheritance
Create → DrawBorderThenFill → Animation → object
:::

## Uncreate

`Uncreate` 是 `Create` 的镜像：`reverse_rate_function=True` 反转进度、`remover=True` 播完把物体移出场景——相当于沿原路径"擦除"。

:::demo examples/ch05/creation_family.py CreationFamily
三个图形分别用 `Create`、`DrawBorderThenFill` 进场；随后 `Uncreate` 把前两个擦除。
:::

## Write

`Write(vmobject, rate_func=linear, reverse=False)` 让 `VMobject`（常用于 `Text`/`MathTex`）沿笔画描出轮廓再填充。注意它的默认 `rate_func` 是 `linear` 而不是大多数动画的 `smooth`，书写节奏更均匀。

:::inheritance
Write → Draw → DrawBorderThenFill → Animation → object
:::

## Unwrite

`Unwrite(vmobject, rate_func=linear, reverse=True)` 是 `Write` 的逆过程：按 `reverse=True` 从尾到头擦除，`remover=True` 收场。英文教材中 `Write`/`Unwrite` 是演示公式推导的经典组合。

## DrawBorderThenFill

`DrawBorderThenFill(vmobject, run_time=2, rate_func=double_smooth, stroke_width=2, stroke_color=None)` 分两段：先用细线描边，再展开填充。默认 `run_time=2` 比多数动画长，自带"隆重登场"的节奏；`stroke_width`/`stroke_color` 控制前一段描边的粗细与颜色（默认取物体描边色）。

## ShowIncreasingSubsets

`ShowIncreasingSubsets(group, suspend_mobject_updating=False, int_func=floor)` 让 VGroup 的子对象**一批一批**出现：进度 α 对应前 `int_func(α × n)` 个子对象可见。`int_func` 决定取整方式（默认 `floor`，即 α=0.5、n=5 时显示前 2 个）。

## ShowSubmobjectsOneByOne

`ShowSubmobjectsOneByOne(group, int_func=ceil)` 与前者类似，但节奏是"**逐个点亮再熄灭**"：每个子对象依次短暂出现后消失，动画结束只保留最后一个——适合做扫描、点名式的强调。

:::demo examples/ch05/creation_subsets.py CreationSubsets
圆点用 `ShowIncreasingSubsets` 一批批入场；正方形用 `ShowSubmobjectsOneByOne` 逐个点亮；最后六个圆环 `SpiralIn` 螺旋飞入。
:::

## AddTextLetterByLetter

`AddTextLetterByLetter(text, rate_func=linear, time_per_char=0.1, run_time=None)` 让 `Text` 的字符**逐个淡入**。每个字符耗时 `time_per_char` 秒；不传 `run_time` 时总时长自动算为 `time_per_char × 字符数`（下限 0.1 秒）。

## RemoveTextLetterByLetter

`RemoveTextLetterByLetter` 是它的逆动画：`reverse_rate_function=True` 从后往前逐字符淡出，`remover=True` 播完移除。

## AddTextWordByWord

`AddTextWordByWord(text_mobject, time_per_char=0.06)` 按**空格**把文字切成词，逐词整体淡入。`time_per_char` 控制每个词内部的节奏。

:::notice tip
提示
中文没有天然空格：`AddTextWordByWord(Text("一词 一词 出现"))` 依赖你手动插入的空格分词；不分词的中文整句会作为一个词整体出现。纯中文逐字进场请用 `AddTextLetterByLetter`。
:::

## TypeWithCursor

`TypeWithCursor(text, cursor, buff=0.1, keep_cursor_y=True, leave_cursor_on=True, time_per_char=0.1)` 在逐字符出现的同时，把一个**光标物体**贴在已出现文字的末尾，形成打字机效果。`cursor` 是任意的 `Mobject`（常用细长 `Rectangle`）；`keep_cursor_y=True` 让光标始终与文字中线对齐；`leave_cursor_on=True` 播完后保留光标。

## UntypeWithCursor

`UntypeWithCursor(text, cursor=None, ...)` 是逆过程（打字删除），`remover=True` 播完把文字移出场景。

:::notice warning
常见错误
`UntypeWithCursor` 的 `cursor` 形参默认是 `None`，但**实际上必须显式传入**：传 None 会在动画开始阶段崩溃（本机 v0.21.0 实测抛 `AttributeError: 'NoneType' object has no attribute 'get_y'`）。建议把 `TypeWithCursor` 用过的同一个光标再传给它。
:::

:::demo examples/ch05/creation_typing.py CreationTyping
`TypeWithCursor` 带着矩形光标逐字打出文字；`UntypeWithCursor` 用同一光标把文字逐个删掉。
:::

:::notice tip
提示
这两个动画只支持 `Text`，不支持 `MathTex`（官方文档明确说明）。
:::

## SpiralIn

`SpiralIn(shapes, scale_factor=8, fade_in_fraction=0.3)` 让一组物体从远处（`scale_factor` 倍）螺旋收拢飞入，最后 `fade_in_fraction` 比例的行程内淡入收尾，适合表现"一群东西聚拢成形"。

## ShowPartial

`ShowPartial` 是 `Create` 系动画的抽象基类：按 `VMobject` 已有的部分绘制进度（`0` 到 `1`）显示物体，自己不规定进度如何推进。日常几乎不会直接实例化它，但自定义"按自定义曲线进度显示"的动画时可以继承。

:::inheritance
ShowPartial → Animation → object
:::

## 自测

:::exercise
一行 `Text("Hello World")` 想做出"逐词淡入"的效果，用哪个动画？对 `"你好世界"`（无空格）会得到什么效果？
:::answer
用 `AddTextWordByWord`：它按空格切词，`Hello` 和 `World` 会依次整体淡入。`"你好世界"` 没有空格，整句会被当作一个词一次性出现；中文逐字效果应改用 `AddTextLetterByLetter`。
:::
:::

:::exercise
`ShowIncreasingSubsets` 与 `ShowSubmobjectsOneByOne` 播完后画面有什么区别？
:::answer
`ShowIncreasingSubsets`：子对象只增不减，播完时**全部**保留；`ShowSubmobjectsOneByOne`：每个子对象闪亮后消失，播完时**只剩最后一个**。
:::
:::

## 下一步

创建家族管"从无到有"，下一节是另一组进场/离场动画：从一点"长出来"的 Grow 家族，与淡入淡出的 Fade 家族。
