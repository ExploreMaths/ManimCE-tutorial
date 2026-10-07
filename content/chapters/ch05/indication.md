---
title: 强调与指示
---

# 强调与指示

"看这里！"——演示动画里引导注意力的 10 个常用动画：聚光、变色、闪光、圈选、扫光、波浪、扭动、眨眼、广播。它们都**不改变物体的核心数据**，只叠加临时的视觉效果。

## FocusOn

`FocusOn(focus_point, opacity=0.2, color=#888888, run_time=2)` 压暗整个画面，只在目标处留一个圆形亮区，像舞台追光。`focus_point` 可以是点坐标，也可以是 mobject（用其中心）。它是 `Transform` 子类：压暗层随动画淡入淡出。

:::inheritance
FocusOn → Transform → Animation → object
:::

## Indicate

`Indicate(mobject, scale_factor=1.2, color=YELLOW, rate_func=there_and_back)` 让物体放大到 1.2 倍并变黄，再原样返回——最轻量的"提醒看一下"。同为 `Transform` 子类，结束后物体数据不变。

:::inheritance
Indicate → Transform → Animation → object
:::

## Flash

`Flash(point, line_length=0.2, num_lines=12, flash_radius=0.1, color=YELLOW, time_width=1, run_time=1)` 从一点向外放射一簇短线，像闪光点。`point` 取坐标（如 `mob.get_center()`）。

:::inheritance
Flash → AnimationGroup → Animation → object
:::

## Circumscribe

`Circumscribe(mobject, shape=Rectangle, fade_in=False, fade_out=False, time_width=0.3, buff=0.1, color=YELLOW, run_time=1, stroke_width=4)` 沿物体外接矩形或圆逐边扫过一圈高亮，适合"圈出重点"。`shape` 只能取 `Rectangle` 或 `Circle`；`buff` 控制圈与物体的间距。

:::inheritance
Circumscribe → Succession → AnimationGroup → Animation → object
:::

:::demo examples/ch05/indication_basics.py IndicationBasics
依次演示：`FocusOn` 压暗背景聚光圆、`Indicate` 放大变黄、`Flash` 放射短线、`Circumscribe` 沿文字圈一圈。
:::

## ShowPassingFlash

`ShowPassingFlash(vmobject, time_width=0.1)` 让一道高亮沿线条扫过，原物体不受影响——是"引导视线沿路径移动"的利器。

:::inheritance
ShowPassingFlash → ShowPartial → Animation → object
:::

## ShowPassingFlashWithThinningStrokeWidth

`ShowPassingFlashWithThinningStrokeWidth(vmobject, n_segments=10, time_width=0.1, remover=True)` 扫光的同时笔画逐渐变细，默认播完自动移除。

:::inheritance
ShowPassingFlashWithThinningStrokeWidth → AnimationGroup → Animation → object
:::

## ApplyWave

`ApplyWave(mobject, direction=UP, amplitude=0.2, wave_func=smooth, time_width=1, ripples=1, run_time=2)` 让物体沿 `direction` 泛起涟漪式波动（本质是 `Homotopy` 形变），`ripples` 控制涟漪次数。

:::inheritance
ApplyWave → Homotopy → Animation → object
:::

## Wiggle

`Wiggle(mobject, scale_value=1.1, rotation_angle=0.0628, n_wiggles=6, run_time=2)` 小幅度来回缩放加旋转的"抖动"，适合表现"抖动校准"或否定语气。

:::inheritance
Wiggle → Animation → object
:::

## Blink

`Blink(mobject, time_on=0.5, time_off=0.5, blinks=1, hide_at_end=False)` 让物体按"亮 time_on 秒、灭 time_off 秒"的节奏闪烁 `blinks` 次；闪烁的是传入物体本身，结束恢复显示（`hide_at_end=True` 则停在隐藏态）。

:::inheritance
Blink → Succession → AnimationGroup → Animation → object
:::

## Broadcast

`Broadcast(mobject, focal_point=ORIGIN, n_mobs=5, initial_opacity=1, final_opacity=0, initial_width=0, remover=True, lag_ratio=0.2, run_time=3)` 从焦点向外扩散一圈圈放大渐隐的轮廓，像信号广播；`focal_point` 默认取原点，通常传 `mob.get_center()`。

:::inheritance
Broadcast → LaggedStart → AnimationGroup → Animation → object
:::

:::demo examples/ch05/indication_advanced.py IndicationAdvanced
依次演示：两道扫光扫过横线（第二道逐渐变细）、`ApplyWave` 波浪、`Wiggle` 扭动方块、`Blink` 闪点、`Broadcast` 从点向外扩散信号。
:::

:::notice warning
常见错误
带 `remover=True` 的动画（`Broadcast`、默认的 `ShowPassingFlashWithThinningStrokeWidth`）播完会把生成的临时对象移出场景，这是预期行为；若看到"特效突然消失"不要惊讶。
:::

:::notice tip
提示
强调动画重在克制：同一画面连续堆叠多种指示会互相干扰。通常一个要点配一种强调，并保持默认配色（黄/灰）以维持风格统一。
:::

## 自测

:::exercise
想引导观众看一根很长的公式里的某一项，圈选和扫光各适合什么场景？
:::answer
目标是"注意这一项本身"用 `Circumscribe(term)`；目标是"沿公式读到这一项"用 `ShowPassingFlash` 在公式底线上扫一道光，把视线引向目标位置。
:::
:::

:::exercise
`Broadcast(dot)` 播完后扩散的圆圈为什么消失了？
:::answer
`Broadcast` 默认 `remover=True`，播放结束自动移除所有扩散轮廓，只留下原物体——这正是"信号发完"想要的效果。想保留最后一圈可以传 `remover=False`。
:::
:::

## 下一步

动画的节奏不仅能靠设计，还能在播放中**实时变速**：下一节看 `ChangeSpeed` 如何给正在播放的动画挂上"油门"。
