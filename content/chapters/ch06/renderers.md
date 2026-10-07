---
title: 渲染器
---

# 渲染器

Manim 社区版有两个渲染器：**Cairo**（默认）与 **OpenGL**。它们执行同一套场景逻辑，但底层绘制方式完全不同：Cairo 是 CPU 上的 2D 矢量光栅化（3D 是投影后的伪 3D），OpenGL 是 GPU 上的真 3D 光栅化。本章所有 3D 示例（ThreeDScene、多面体、移动摄像机等）用 Cairo 即可完成，无需 OpenGL。

## 选择渲染器

CLI 用 `--renderer` 切换：

```bash
manim -qm --renderer cairo scene.py MyScene    # 默认，可省略
manim -qm --renderer opengl scene.py MyScene   # 需要 OpenGL 环境
```

也可以在配置文件中固定 `renderer = cairo`（或 `opengl`），省去每次传参。

## Cairo vs OpenGL

:::compare
| 维度 | Cairo（默认） | OpenGL |
| ---- | ------------- | ------ |
| 依赖 | pycairo + ffmpeg | 额外需要 `moderngl`、`moderngl-window` 及可用的 GPU 驱动 |
| 3D 实现 | 伪 3D：投影 + 着色后走 2D 矢量管线 | 真 3D：顶点/着色器管线，硬件加速 |
| 速度 | 中小场景稳定；高分辨率 3D 明显偏慢 | 复杂 3D 场景通常更快，支持实时预览 |
| 交互 | 仅输出视频 | 支持交互式嵌入（`Scene.embed()`、按键交互） |
| 特性覆盖 | 参考实现，功能最全、行为最可预期 | 个别特性与 Cairo 存在差异，遇到问题先换 Cairo 复现 |
| 适用场景 | 最终出片、教程、需要稳定复现的产出 | 调试复杂 3D、探索性交互、性能敏感的 3D 场景 |
:::

## 依赖检查

OpenGL 渲染器需要 `moderngl` 与 `moderngl-window`。安装方式：

```bash
pip install moderngl moderngl-window
```

装好后用一次小规模渲染验证：

```bash
manim -ql --renderer opengl examples/ch06/three_d_solids.py ThreeDSolids
```

:::notice tip
提示
不确定环境是否就绪时，先跑 `manim checkhealth` 看整体安装状况；OpenGL 相关问题通常表现为渲染启动时报 moderngl 相关异常，按提示补装依赖即可。Cairo 渲染器没有这些额外依赖，开箱即用。
:::

## 常见错误与建议

:::notice warning
常见错误
不要在团队协作或 CI 里默认 OpenGL：不同机器的 GPU 驱动差异会导致结果不一致。发布用的成片统一走 Cairo，OpenGL 留给本地探索。
:::

:::notice warning
常见错误
切到 OpenGL 后画面与 Cairo 不一致（如描边粗细、渐变、部分动画细节）并不一定是 bug——两个渲染器在个别视觉细节上本就有差异。以 Cairo 输出为准做视觉验收。
:::

:::notice tip
提示
3D 场景“渲染慢”多半不是渲染器的锅，而是分辨率与网格密度：先试 `-ql` + 调低 `resolution`，比换渲染器收益更直接。
:::

:::notice version
版本说明
渲染器行为基于 `manim 0.21.0`；`--renderer` 标志取值为 `cairo` / `opengl`，默认 `cairo`。
:::

## 自测

:::exercise
服务器（无 GPU、无显示器）上批量出片，应该选哪个渲染器？为什么？
:::answer
选 Cairo。它只依赖 CPU（pycairo + ffmpeg），不依赖 GPU 驱动；OpenGL 需要 moderngl 与可用的图形环境，在无头服务器上更容易失败，且视觉结果可能与本机不一致。
:::
:::

:::exercise
同一个 3D 场景，Cairo 渲染明显卡顿。在考虑换 OpenGL 之前，应该先尝试哪两个更省事的优化？
:::answer
一是降画质 `-ql` 调试验证逻辑；二是降低 3D 网格的 `resolution`（如 `Sphere(resolution=(16, 16))`）减少面片数量。两者都不改代码结构，通常比切换渲染器更快定位瓶颈。
:::
:::

## 下一步

“3D 与摄像机”板块到此结束：你已经能搭建 3D 场景、操纵镜头与取景框，并理解渲染器的选择。最后一个板块进入高级主题——自定义 mobject 与自定义动画。
