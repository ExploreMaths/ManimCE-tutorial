---
title: 数值动画
---

# 数值动画

`DecimalNumber` 本身只能 `set_value` 瞬间改数。`ChangingDecimal` 家族把"改数"变成动画：计数器滚动、数值逼近目标，都靠它们。

## ChangingDecimal

`ChangingDecimal(decimal_mob, number_update_func)` 播放期间每帧重算并刷新显示的数字。

:::inheritance
ChangingDecimal → Animation → object
:::

```python
ChangingDecimal(
    decimal_mob: DecimalNumber,
    number_update_func: Callable[[float], float],
    suspend_mobject_updating: bool = False,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `decimal_mob` | DecimalNumber | — | 要驱动的数字对象 |
| `number_update_func` | Callable[[float], float] | — | 接收动画进度 alpha（0→1，已过 rate_func），返回此刻应显示的数值 |
| `suspend_mobject_updating` | bool | False | 播放期间是否挂起该数字自身的 updater |
:::

:::notice warning
常见错误
`number_update_func` 接收的是**进度 alpha**，不是"当前值"：写 `lambda a: 10 * a` 从 0 数到 10；若想"在当前值基础上累加"，请先 `start = num.get_value()` 再写 `lambda a: start + a`。把它当成"旧值→新值"的映射是新手最常见的误解。
:::

## ChangeDecimalToValue

`ChangeDecimalToValue(decimal_mob, target_number)` 是 `ChangingDecimal` 的子类：从数字当前值平滑滚动到指定目标值，不用自己写映射函数。

:::inheritance
ChangeDecimalToValue → ChangingDecimal → Animation → object
:::

```python
ChangeDecimalToValue(decimal_mob: DecimalNumber, target_number: int, **kwargs)
```

:::demo examples/ch05/number_animations.py NumberAnimations
第一段用 `ChangingDecimal` 按 `10 * alpha` 从 0 数到 10；第二段 `ChangeDecimalToValue` 从 10 平滑滚动到 42。
:::

:::notice warning
常见错误
`DecimalNumber` 默认用 `MathTex` 渲染数字，**需要 LaTeX 环境**；机器上没装 LaTeX 会在渲染时抛 `FileNotFoundError`。无 LaTeX 时请传 `mob_class=Text`（`DecimalNumber(0, mob_class=Text)`），本教程示例均用这种方式。另外 `DecimalNumber` 的位数由 `num_decimal_places` 决定，显示值会被四舍五入到该精度。
:::

:::notice tip
提示
想做成"时钟计数器"效果，把 `num_decimal_places` 设大、给数字挂 updater 读 `ValueTracker` 即可，不一定要用本节动画——`ChangingDecimal` 更适合"一次性的计数/逼近"叙事。
:::

## 自测

:::exercise
用 `ChangingDecimal` 让数字从 0 数到 100，再原路数回 0，怎么写最简洁？
:::answer
利用 `there_and_back`：把 `rate_func=there_and_back` 传给 play，更新函数写 `lambda a: 100 * a`——进度走到 1 再折返，数字自然数过去又数回来。
:::
:::

:::exercise
为什么 `self.play(ChangingDecimal(num, lambda v: v + 1))` 往往看不到数字变化？
:::answer
因为参数 `v` 是进度 alpha 而非当前显示值：`lambda v: v + 1` 只在 1.0~2.0 之间微小变化。正确写法是显式用进度映射，如 `lambda a: 100 * a`，或用 `ChangeDecimalToValue`。
:::
:::

## 下一步

数字能滚动了，下一节给运动的物体加上"轨迹"和"流动边界"：`TracedPath` 与 `AnimatedBoundary`。
