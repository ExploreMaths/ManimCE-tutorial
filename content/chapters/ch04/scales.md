---
title: 缩放基
---

# 缩放基

`NumberLine`（及其派生的坐标系）通过**缩放基**（scale base）决定“坐标值 → 场景位置”的映射关系。所有缩放基继承自内部基类 `_ScaleBase`；公开可用的实现只有两个：`LinearBase`（线性）和 `LogBase`（对数）。

:::inheritance
LinearBase → _ScaleBase → object
:::

:::inheritance
LogBase → _ScaleBase → object
:::

## LinearBase

`LinearBase` 是默认缩放基：位置与坐标值成正比，可选一个整体放大系数。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `scale_factor` | float | 1.0 | 坐标值到位置的线性放大系数 |
:::

三个方法构成互逆的一对映射加一个开关：

- `function(x)` —— 标签值 → 原始值（线性恒等，乘 `scale_factor`）
- `inverse_function(x)` —— 原始值 → 标签值（上面运算的逆）
- `get_custom_labels(...)` —— 是否使用自定义标签（LinearBase 返回 None，即不启用）

## LogBase

`LogBase` 把数轴变成**对数轴**：标签按指数摆放（`base^n`），位置按对数排布，适合展示跨数量级的数据。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `base` | float | 10 | 对数底 |
| `custom_labels` | bool | True | 是否生成 `base` 的幂形式的 LaTeX 自定义标签 |
:::

`function(x)` 计算 `base ** x`（标签 → 真值），`inverse_function(x)` 计算 `log(x, base)`（真值 → 标签）。

:::demo examples/ch04/log_scale.py LogScaleDemo
上下两条轴等长：上面是默认的 `LinearBase`，下面是 `LogBase(base=2)`。注意对数轴上 1、2、4、8 的间距是相等的。
:::

:::notice warning
常见错误（v0.21.0 的重要语义）
带 `LogBase` 时，**面向用户的接口传的是“真值”而不是标签**：`number_to_point(8)` 内部会先取 `log2(8) = 3` 再定位；`add_labels` 的键也必须是真值 `{1: ..., 2: ..., 4: ..., 8: ...}`。给 `add_labels` 传 `{0: ...}` 会触发 `log(0)` 直接抛 `ValueError`。同理 `point_to_number` 返回的也是真值（上例中数轴右端返回 `8.0` 而不是 `3.0`）。
:::

:::notice tip
提示
`LogBase` 默认 `custom_labels=True`：一旦 `include_numbers=True`，数字会渲染成 `10^2` 这样的 LaTeX 幂标签。不想要幂形式时传 `custom_labels=False`，再自行 `add_labels` 添加纯文本标签。
:::

## 两者对比

:::compare
| 维度 | LinearBase | LogBase |
| ---- | ---------- | ------- |
| 映射 | 位置 ∝ 坐标值 | 位置 ∝ log(坐标值) |
| 默认参数 | `scale_factor=1.0` | `base=10, custom_labels=True` |
| 典型场景 | 普通坐标轴 | 跨数量级数据、指数增长曲线 |
| 标签来源 | 数字本身 | 默认渲染为 base 的幂（LaTeX） |
:::

:::notice version
版本说明
缩放基 API 在 v0.17 左右从旧的 `number_scale_value` 等参数重构为 `_ScaleBase` 体系；v0.21.0 中旧参数已不存在，统一通过 `scaling=LogBase(...)` 传入。旧教程里的 `NumberLine(x_min=..., x_max=...)` 写法同样已废弃，请使用 `x_range=[start, end, step]`。
:::

## 自测

:::exercise
`NumberLine(x_range=[0, 4, 1], length=8, scaling=LogBase(base=2, custom_labels=False))` 上，`number_to_point(4)` 和 `number_to_point(16)` 分别在哪里？
:::answer
标签 0–4 对应真值 1–16，轴长 8、每标签单位 2 个场景单位。`number_to_point(4)` 走 `inverse_function`：`log2(4)=2`，位于标签 2 的位置，即中点（原点）；`number_to_point(16)`：`log2(16)=4`，位于轴的最右端（场景 x = +4）。
:::
:::
