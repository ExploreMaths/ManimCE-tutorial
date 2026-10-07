---
title: Rate Functions 全解
---

# Rate Functions 全解

`rate_func` 决定动画"进度怎么走"：给定归一化时间 `t ∈ [0, 1]`，返回归一化进度。合格的速率函数满足契约 `f(0)=0, f(1)=1`；`self.play(..., rate_func=smooth)` 里的就是它。本节以 `manim.utils.rate_functions` 在 v0.21.0 的**实际导出**为准做全量速查。

## 核心速率函数

:::compare
| 函数 | 形状 | 典型用途 |
| ---- | ---- | ---- |
| `linear` | 直线 | 匀速；机械运动、倒计时 |
| `smooth` | S 形缓入缓出（sigmoid，inflection=10 可调） | 通用默认，最自然的启停 |
| `double_smooth` | 更平缓的 S 形 | 极柔和的长过渡 |
| `smoothstep` / `smootherstep` / `smoothererstep` | 经典多项式 S 形，阶数逐次升高 | 需要"钉"在端点的平滑运动 |
| `rush_from` | 起步猛、后段缓 | 物体冲入画面 |
| `rush_into` | 前段缓、收尾猛 | 物体精准落位 |
| `slow_into` | 起步极慢、后程加速 | 反差的急停变急起 |
| `running_start` | 先小幅回拉（负值）再冲出 | 投掷、起跑类预备动作 |
| `lingering` | 起点终点各留约 20% 静止段 | 强调"停稳了再走" |
| `there_and_back` | 走到 1 再折返 0 | 强调、抖动、往返 |
| `there_and_back_with_pause(t, pause_ratio=1/3)` | 去程、停留、返程三等分 | 展示—停留—收回 |
| `wiggle(t, wiggles=2)` | 波浪起伏、会跌破 0 越过 1 | 悬浮、抖动 |
:::

## ease 系列（30 个）

标准缓动家族：`ease_in_*`（慢起步）、`ease_out_*`（慢收尾）、`ease_in_out_*`（两头慢），各 10 种曲线：

:::compare
| 曲线 | ease_in | ease_out | ease_in_out |
| ---- | ---- | ---- | ---- |
| 二次 | `ease_in_quad` | `ease_out_quad` | `ease_in_out_quad` |
| 三次 | `ease_in_cubic` | `ease_out_cubic` | `ease_in_out_cubic` |
| 四次 | `ease_in_quart` | `ease_out_quart` | `ease_in_out_quart` |
| 五次 | `ease_in_quint` | `ease_out_quint` | `ease_in_out_quint` |
| 正弦 | `ease_in_sine` | `ease_out_sine` | `ease_in_out_sine` |
| 指数 | `ease_in_expo` | `ease_out_expo` | `ease_in_out_expo` |
| 圆弧 | `ease_in_circ` | `ease_out_circ` | `ease_in_out_circ` |
| 回拉 | `ease_in_back` | `ease_out_back` | `ease_in_out_back` |
| 弹性 | `ease_in_elastic` | `ease_out_elastic` | `ease_in_out_elastic` |
| 弹跳 | `ease_in_bounce` | `ease_out_bounce` | `ease_in_out_bounce` |
:::

后三种带"越过端点再回弹"的效果：`back` 小幅回冲、`elastic` 弹性振荡、`bounce` 落地弹跳。日常用 `smooth` 即可，需要"活泼感"时换 `ease_out_back` / `ease_out_elastic`。

## 修饰与组合工具

:::compare
| 工具 | 签名 | 作用 |
| ---- | ---- | ---- |
| `squish_rate_func(func, a=0.4, b=0.6)` | 函数 | 把 func 压缩到 [a, b] 区间，区间外冻结在端点值 |
| `not_quite_there(func=smooth, proportion=0.7)` | 函数 | 把终点缩到 proportion：动画"差一步到位"，f(1)=0.7 |
| `zero(function)` | 装饰器 | 包一层：t 在 [0,1] 内原样转发，之外返回 0 |
| `unit_interval(function)` | 装饰器 | 包一层：t<0 钳到 0，t>1 钳到 1（保证契约） |
| `exponential_decay(t, half_life=0.1)` | 函数 | 指数逼近 1（经 unit_interval 钳制），适合透明度/亮度衰减 |
:::

:::notice warning
常见错误
不是所有导出都满足 `f(0)=0, f(1)=1`：`sigmoid` 是原始逻辑斯蒂函数（f(0)=0.5，仅供 `smooth` 等底层调用）；`not_quite_there` 故意停在 proportion；`wiggle` 中途会跌破 0。把它们传给位移类动画可能出现"反向移动"或"不到位"，用于缩放/透明度时才安全。
:::

:::demo examples/ch05/rate_functions.py RateFunctionsRace
六个小球同时下落、各挂一种 rate_func：linear 匀速、smooth 缓入缓出、rush_from 先快后慢、rush_into 先慢后快、there_and_back 走一半折返、wiggle 波浪前进——一张图看懂曲线形状差异。
:::

:::notice tip
提示
速率函数不改变动画时长，只改变节奏；想拉长/压缩时长用 `run_time`，想在播放中途变速用上一节的 `ChangeSpeed`。
:::

## 自测

:::exercise
想要"物体先慢慢挪、越接近目标越快、最后精准停在目标点"的效果，选哪个速率函数？
:::answer
`rush_into`（前缓后急，收尾猛而准）；如果想更"俏皮"一点可以选 `ease_in_quad` / `ease_in_cubic` 系列。
:::
:::

:::exercise
`self.play(mob.animate.shift(RIGHT), rate_func=there_and_back)` 结束后 mob 在哪里？
:::answer
回到原点。`there_and_back` 的进度从 0 到 1 再折返 0，位移量同步伸缩，动画播完净位移为零——这正是它适合做"强调一下再回来"的原因。
:::
:::

## 下一步

到这里，动画进阶板块收官：机制、更新器、数值、轨迹、路径、旋转、强调、变速与速率函数都已覆盖。下一板块进入三维世界：从 `ThreeDScene` 与 3D 物体讲起。
