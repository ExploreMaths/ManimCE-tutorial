---
title: 布尔运算
---

# 布尔运算

布尔运算把多个 `VMobject` 的填充区域按集合规则组合成新形状：并集、交集、差集、异或。它们定义在 `manim.mobject.geometry.boolean_ops` 模块，底层由 skia-pathops 完成路径运算，无需额外安装 shapely。

:::inheritance
Union → _BooleanOps → VMobject
:::

:::notice version
版本说明
布尔运算类在 v0.21.0 位于模块 `manim.mobject.geometry.boolean_ops`（`manim.mobject.geometry.bool_ops` 是旧路径）。顶级命名空间 `from manim import Union` 仍然有效，但写文档、插件或自动补全时请以新模块路径为准。
:::

## Union

`Union` 取所有输入图形填充区域的**并集**。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `*vmobjects` | VMobject | — | 任意多个参与运算的图形 |
| `**kwargs` | Any | — | 传给 VMobject 的样式，如 `fill_opacity`、`color` |
:::

```python
Union(circle, square, fill_opacity=1, color=GREEN)
```

常见坑：样式（颜色、填充）取结果对象的 `kwargs`，不会继承输入图形的样式；不设置 `fill_opacity` 时结果默认不可见（继承 VMobject 默认 fill_opacity=0）。

## Intersection

`Intersection` 取所有输入图形填充区域的**交集**：只有被所有图形共同覆盖的部分会保留。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `*vmobjects` | VMobject | — | 任意多个参与运算的图形 |
| `**kwargs` | Any | — | 结果样式 |
:::

常见坑：只有两个以上图形重叠时结果才非空；完全不相交的输入会得到空图形，渲染时不报错但“什么也看不见”。

## Difference

`Difference` 从 `subject` 中减去 `clip` 覆盖的区域（`subject - clip`）。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `subject` | VMobject | — | 被裁剪的主体 |
| `clip` | VMobject | — | 减去的部分 |
| `**kwargs` | Any | — | 结果样式 |
:::

```python
Difference(square, circle)  # 正方形挖掉圆
```

## Exclusion

`Exclusion` 取**对称差**（异或）：只保留恰好被一个图形覆盖的区域，重叠部分被挖掉。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `subject` | VMobject | — | 第一个图形 |
| `clip` | VMobject | — | 第二个图形 |
| `**kwargs` | Any | — | 结果样式 |
:::

:::compare
| 运算 | 语义 | 参数形式 | 形象理解 |
| ---- | ---- | -------- | -------- |
| `Union` | 覆盖任一图形的区域 | `*vmobjects` 多输入 | 图形“溶”在一起 |
| `Intersection` | 同时被所有图形覆盖的区域 | `*vmobjects` 多输入 | 只留下重叠 Lens |
| `Difference` | 主体减去裁剪 | `subject, clip` 两个 | 饼干模子抠洞 |
| `Exclusion` | 恰好被一个图形覆盖的区域 | `subject, clip` 两个 | 两图形互相挖掉重叠 |
:::

:::demo examples/ch02/boolean_ops_demo.py BooleanOpsDemo
正方形与圆先做原始展示，随后淡出，换成四个布尔结果：并集、交集、差集、异或。注意四个结果都显式传了 `fill_opacity=1`，否则默认填充为 0 不可见。
:::

## 常见错误与建议

:::notice warning
常见错误
布尔运算作用于**填充路径**：纯描边（`fill_opacity=0`）的图形没有可运算的内部，结果会退化或为空。参与运算前确保输入有实际填充，或者接受结果按 `kwargs` 重新设置填充。
:::

:::notice tip
提示
布尔运算结果仍是普通 `VMobject`，可以继续 `set_fill`、参与 `Transform`、或作为下一个布尔运算的输入。复杂路径的运算较慢，调试时先用 `-ql` 低画质快速迭代。
:::

## 自测

:::exercise
想画一个“圆角矩形挖掉中间圆形”的甜甜圈状图形，但 `Difference(rounded_rect, circle)` 的结果一片空白，最可能的原因是什么？
:::answer
结果对象的 `fill_opacity` 默认是 0（不继承输入图形）。给 `Difference` 显式传 `fill_opacity=1`（以及想要的颜色）即可看到结果。
:::
:::

## 下一步

下一节介绍标注与装饰：包围框、背景框、删除线、带标签的线与多边形，以及大括号族。
