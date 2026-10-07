---
title: 变速
---

# 变速

`ChangeSpeed` 能在**一个动画播放期间**多次改变它的播放速度——慢动作、急加速、中途暂停都可用一个 dict 描述。这是 rate_func 做不到的事：rate_func 是"一条进度映射曲线"，`ChangeSpeed` 是"分段速度倍率表"。

## ChangeSpeed

:::inheritance
ChangeSpeed → Animation → object
:::

```python
ChangeSpeed(
    anim: Animation | _AnimationBuilder,
    speedinfo: dict[float, float],
    rate_func: Callable[[float], float] | None = None,
    affects_speed_updaters: bool = True,
    **kwargs,
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `anim` | Animation \| .animate 构造器 | — | 被包裹的内层动画 |
| `speedinfo` | dict[float, float] | — | **键是内层动画进度的比例节点（0~1），值是该区间的速度倍率** |
| `rate_func` | function \| None | None | 覆盖内层动画的 rate_func，在变速之前应用 |
| `affects_speed_updaters` | bool | True | 是否同时影响通过 `ChangeSpeed.add_updater` 注册的 updater 的 dt |
:::

`speedinfo` 的关键规则：

- 键是**内层动画 run_time 的百分比节点**，不是秒。`{0.5: 0.1, 0.7: 1}` 表示"进度 50% 到 70% 之间以 0.1 倍速播放"。
- 缺 `0` 键时首段速度按 1 处理；缺 `1` 键时末段继承前一个倍率。
- 实际总时长会被自动拉长或压缩：慢放段越长，视频越长。

:::demo examples/ch05/change_speed.py ChangeSpeedDemo
`speedinfo={0: 1, 0.5: 1, 0.7: 0.15, 1: 0.15}`：圆点先全速走一半，随后进入 0.15 倍慢动作直到结束——总时长由 1 秒自动拉长到约 2.8 秒。
:::

## ChangeSpeed 与 rate_func 的区别

:::compare
| 维度 | `rate_func` | `ChangeSpeed` |
| ---- | ---- | ---- |
| 形式 | 一条 0→1 映射曲线 | 分段速度倍率表 |
| 能否中途变向 | 曲线可以任意弯折 | 只能分段变速，不能倒退 |
| 影响 updater 的 dt | 否 | 是（`affects_speed_updaters=True` 时） |
| 适用 | 单一致式节奏 | 先快后慢、慢动作回放等复合节奏 |
:::

## 让 updater 跟着变速

普通 updater（`mob.add_updater`）默认**不受** `ChangeSpeed` 影响——它们仍按真实帧时间推进。想让 updater 也"跟着慢放"，需要改用类方法 `ChangeSpeed.add_updater(mob, func)` 注册；该 updater 会遵循当前正在播放的 `ChangeSpeed` 的速度。

```python
ChangeSpeed.add_updater(dot, lambda mob, dt: mob.shift(RIGHT * dt))
self.play(
    ChangeSpeed(Wait(2), speedinfo={0.5: 1, 0.7: 0.1, 1: 0.1}),
)
```

:::notice warning
常见错误
`affects_speed_updaters=True` 时，同一时间**只能有一个** `ChangeSpeed` 在播放（源码有断言），否则抛 `AssertionError`。另外 `speedinfo` 的键是比例而不是秒，把它当秒表读是新手最容易犯的错。
:::

## 自测

:::exercise
想让一个 2 秒的移动动画"前 1 秒正常、最后 1 秒以 0.25 倍慢放"，speedinfo 怎么写？实际时长是多少？
:::answer
进度中点是 0.5：`speedinfo={0: 1, 0.5: 1, 1: 0.25}`。注意速度在节点之间是**线性渐变**的：后半段平均速度约 (1 + 0.25) / 2 = 0.625，占 1 / 0.625 = 1.6 秒，总时长约 2.6 秒（不是直觉上的 1 + 4 = 5 秒）。
:::
:::

:::exercise
`ChangeSpeed(anim, {0.3: 2, 0.6: 0.5, 1: 1})` 里缺 0 键会怎样？
:::answer
首段（0 到 0.3）速度按默认值 1 处理；中间的 0.3→0.6 以 2 倍速、0.6→1 以 0.5 倍速播放。实际时长 = 0.3×1 + 0.3×(2/(2+... )) 自动重算，总之比原 run_time 更短。
:::
:::

## 下一步

变速控制的是"时间维度上的节奏"，下一节进入最后一个进阶主题：全量 rate functions 速查——每一条曲线的形状、适用场景与组合工具。
