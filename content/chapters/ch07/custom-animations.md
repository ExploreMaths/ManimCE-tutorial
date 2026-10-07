---
title: 自定义 Animation
---

# 自定义 Animation

`FadeIn`、`Transform`、`Rotate` 都继承自同一个基类 `Animation`（见 ch05 的“Animation 机制”一节）。本节讲解这个基类的工作机制，以及如何继承它写出自己的动画。

## Animation 基类

一个 `Animation` 的生命周期由渲染器驱动，核心步骤：

1. `begin()`：动画开始前调用。基类在这里把目标 mobject 拷贝为 `self.starting_mobject`（起始状态快照），并暂停目标对象自身的 updater，最后调用 `interpolate(0)`。
2. 每一帧渲染器调用 `interpolate(alpha)`，`alpha ∈ [0, 1]` 表示动画进度（已经过 `rate_func` 处理），内部转交给 `interpolate_mobject`。
3. `finish()`：动画结束后的收尾（默认恢复 updater 状态）。

:::inheritance
Animation → object
:::

```python
Animation(
    mobject, lag_ratio=0.0, run_time=1.0, rate_func=smooth,
    reverse_rate_function=False, name=None, remover=False,
    suspend_mobject_updating=True, introducer=False, ...
)
```

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `mobject` | Mobject \| None | — | 被动画驱动的目标对象 |
| `lag_ratio` | float | 0.0 | 子对象之间的错峰比例（见 `AnimationGroup`） |
| `run_time` | float | 1.0 | 动画时长（秒） |
| `rate_func` | callable | `smooth` | 速率函数，把线性时间映射为动画进度 |
| `reverse_rate_function` | bool | False | 播放时反转 rate_func 的方向 |
| `remover` | bool | False | 结束后把目标对象移出场景（如 `FadeOut`） |
| `suspend_mobject_updating` | bool | True | 动画期间暂停目标对象自身的 updater |
| `introducer` | bool | False | 标记该动画会把目标对象引入场景 |
:::

## 两个插值钩子

自定义动画的本质就是重写插值钩子。有两层：

- **`interpolate_mobject(alpha)`**：接收整个对象的进度，负责驱动目标 mobject。想整体生效（颜色、透明度、整体形变）时重写它。
- **`interpolate_submobject(submobject, starting_submobject, alpha)`**：基类按 `get_all_families_zipped()` 把目标与起始快照的子对象两两配对，对每个子对象调用一次。想让子对象**逐个**响应动画（错落、各自插值）时重写它。

基类的 `interpolate_mobject` 只做一件事：遍历子对象对并调用 `interpolate_submobject`；而基类的 `interpolate_submobject` 是空实现（`pass`）。所以重写任意一个即可，另一个保持默认。

## 完整示例：变色 + 抖动

下面是一个自定义动画 `ColorJitter`：颜色从起始色渐变到目标色，同时叠加一个“中间大、两端为零”的随机抖动（用 `4α(1−α)` 作权重，动画结束图形自然归位）：

:::demo examples/ch07/color_jitter.py CustomAnimationDemo
`ColorJitter` 重写了 `begin()`（预生成随机噪声，保证每帧抖动方向一致）和 `interpolate_mobject()`（按 alpha 插值颜色、按 `4α(1−α)` 叠加位移）。正方形先从蓝变红抖动，再从红变绿加大振幅抖动。
:::

三个值得注意的实现细节：

- 随机噪声在 `begin()` 里预生成，而不是每帧现取随机数——否则每帧抖动方向乱跳，视觉上变成噪声闪烁。
- `begin()` 里**先**生成噪声再调 `super().begin()`：基类的 `begin` 会立即调用 `interpolate(0)`，此时 `interpolate_mobject` 已经需要读取 `self.noise`。
- 位移基于 `starting_mobject.points`（起始快照），不是当前帧的 `points`，避免误差逐帧累积。

## 自定义 Animation 还是 updater？

两者都能让对象随时间变化，选择标准：

:::compare
| | 自定义 Animation | mobject updater |
| - | ---------------- | --------------- |
| 组织方式 | `self.play(MyAnim(mob))`，有明确起止 | `mob.add_updater(func)` 挂到对象上，跨多个动画持续生效 |
| 与场景时间轴 | 属于时间轴上的一个片段，有 run_time | 每帧都被调用，直到 `remove_updater` |
| 起始快照 | `starting_mobject` 自动拷贝 | 需要自己保存状态 |
| 缓存 | 参与部分视频缓存（见“性能与缓存”一节） | updater 期间缓存通常被跳过 |
| 典型场景 | 一次性效果（变色、抖动、特殊形变） | 持续行为（跟随、数值联动、物理模拟） |
:::

:::notice tip
提示
规则很简单：**有明确开始和结束的一次性效果写成 Animation；需要持续到某个条件才停止的行为写成 updater**。一个效果既要在 play 期间发生、又要在此前持续运行，就两者都用。
:::

## 常见错误与建议

:::notice warning
常见错误
在 `interpolate_submobject` 里直接返回新对象没有意义——这个方法靠**就地修改** `submobject` 起作用（基类实现就是 `pass`）。忘记修改、只 `return` 一个值，动画会“什么都不做”也不报错。
:::

:::notice warning
常见错误
重写 `begin()` 时忘了调 `super().begin()`。基类在这里创建 `starting_mobject` 快照并调用 `interpolate(0)`，跳过它会导致 `AttributeError`（找不到 `starting_mobject`）或首帧状态错误。
:::

:::notice tip
提示
`Transform` 家族的 `interpolate_submobject` 签名多了一个 `target_copy` 参数（目标快照），与基类不同。如果你的自定义动画被 `Transform` 风格的逻辑困扰，检查是否混用了这两套签名。
:::

## 自测

:::exercise
自定义动画里想“记住动画开始前的状态”，应该在哪一步、用什么方式保存？
:::answer
在 `begin()` 中（或重写 `create_starting_mobject`）。基类 `begin()` 会自动把目标对象拷贝成 `self.starting_mobject`，重写 `begin()` 时先调 `super().begin()` 即可直接用这个快照，不要手动 `deepcopy` 整个对象树。
:::
:::

:::exercise
什么时候应该重写 `interpolate_submobject` 而不是 `interpolate_mobject`？
:::answer
当希望效果的粒度落到**子对象**上时：基类会把目标与其起始快照的子对象一一配对，逐个传入 `interpolate_submobject`，配合 `lag_ratio` 还能让子对象错峰响应。若效果是针对对象整体的（如整体变色、整体位移），重写 `interpolate_mobject` 更简单。
:::
:::

## 下一步

掌握了图形与动画两条扩展路线后，下一节看向生态层面：如何用插件机制把自定义成果分享给他人、以及如何使用社区插件。
