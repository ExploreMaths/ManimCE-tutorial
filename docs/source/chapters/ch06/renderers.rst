
渲染器
======


Manim 社区版有两个渲染器： **Cairo** （默认）与 **OpenGL** 。它们执行同一套场景逻辑，但底层绘制方式完全不同：Cairo 是 CPU 上的 2D 矢量光栅化（3D 是投影后的伪 3D），OpenGL 是 GPU 上的真 3D 光栅化。本章所有 3D 示例（ThreeDScene、多面体、移动摄像机等）用 Cairo 即可完成，无需 OpenGL。

选择渲染器
----------


CLI 用 ``--renderer`` 切换：

.. code-block:: bash

   manim -qm --renderer cairo scene.py MyScene    # 默认，可省略
   manim -qm --renderer opengl scene.py MyScene   # 需要 OpenGL 环境


也可以在配置文件中固定 ``renderer = cairo`` （或 ``opengl`` ），省去每次传参。

Cairo vs OpenGL
---------------


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 维度
        - Cairo（默认）
        - OpenGL
      * - 依赖
        - pycairo + ffmpeg
        - 额外需要 ``moderngl`` 、 ``moderngl-window`` 及可用的 GPU 驱动
      * - 3D 实现
        - 伪 3D：投影 + 着色后走 2D 矢量管线
        - 真 3D：顶点/着色器管线，硬件加速
      * - 速度
        - 中小场景稳定；高分辨率 3D 明显偏慢
        - 复杂 3D 场景通常更快，支持实时预览
      * - 交互
        - 仅输出视频
        - 支持交互式嵌入（ ``Scene.embed()`` 、按键交互）
      * - 特性覆盖
        - 参考实现，功能最全、行为最可预期
        - 个别特性与 Cairo 存在差异，遇到问题先换 Cairo 复现
      * - 适用场景
        - 最终出片、教程、需要稳定复现的产出
        - 调试复杂 3D、探索性交互、性能敏感的 3D 场景


依赖检查
--------


OpenGL 渲染器需要 ``moderngl`` 与 ``moderngl-window`` 。安装方式：

.. code-block:: bash

   pip install moderngl moderngl-window


装好后用一次小规模渲染验证：

.. code-block:: bash

   manim -ql --renderer opengl examples/ch06/three_d_solids.py ThreeDSolids


.. admonition:: 提示
   :class: tip

   不确定环境是否就绪时，先跑 ``manim checkhealth`` 看整体安装状况；OpenGL 相关问题通常表现为渲染启动时报 moderngl 相关异常，按提示补装依赖即可。Cairo 渲染器没有这些额外依赖，开箱即用。


常见错误与建议
--------------


.. admonition:: 常见错误
   :class: warning

   不要在团队协作或 CI 里默认 OpenGL：不同机器的 GPU 驱动差异会导致结果不一致。发布用的成片统一走 Cairo，OpenGL 留给本地探索。


.. admonition:: 常见错误
   :class: warning

   切到 OpenGL 后画面与 Cairo 不一致（如描边粗细、渐变、部分动画细节）并不一定是 bug——两个渲染器在个别视觉细节上本就有差异。以 Cairo 输出为准做视觉验收。


.. admonition:: 提示
   :class: tip

   3D 场景“渲染慢”多半不是渲染器的锅，而是分辨率与网格密度：先试 ``-ql`` + 调低 ``resolution`` ，比换渲染器收益更直接。


.. admonition:: 版本说明
   :class: notice-version

   渲染器行为基于 ``manim 0.21.0`` ； ``--renderer`` 标志取值为 ``cairo`` / ``opengl`` ，默认 ``cairo`` 。


自测
----


.. dropdown:: ✏️ 练习

   服务器（无 GPU、无显示器）上批量出片，应该选哪个渲染器？为什么？

   .. dropdown:: ✅ 参考答案

      选 Cairo。它只依赖 CPU（pycairo + ffmpeg），不依赖 GPU 驱动；OpenGL 需要 moderngl 与可用的图形环境，在无头服务器上更容易失败，且视觉结果可能与本机不一致。


.. dropdown:: ✏️ 练习

   同一个 3D 场景，Cairo 渲染明显卡顿。在考虑换 OpenGL 之前，应该先尝试哪两个更省事的优化？

   .. dropdown:: ✅ 参考答案

      一是降画质 ``-ql`` 调试验证逻辑；二是降低 3D 网格的 ``resolution`` （如 ``Sphere(resolution=(16, 16))`` ）减少面片数量。两者都不改代码结构，通常比切换渲染器更快定位瓶颈。



CairoRenderer
-------------

.. autoclass:: manim.CairoRenderer
   :noindex:


``CairoRenderer`` 是默认渲染器：把矢量图形光栅化为帧序列再编码成视频。稳定、对全部 mobject 类型兼容，是日常使用的首选；``skip_animations`` 可用于快速导出最后一帧的静态预览。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "CairoRenderer" [label="CairoRenderer", URL="/chapters/ch06/renderers.html#cairorenderer"];
     "object" [label="object"];
     "CairoRenderer" -> "object";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``file_writer_class``
        - type[SceneFileWriter]
        - SceneFileWriter
        - 输出视频/图片的写入器
        - ``camera_class``
        - type[Camera] | None
        - None
        - 使用的相机类；None 取默认
        - ``skip_animations``
        - bool
        - False
        - 跳过所有动画，只输出末帧
RendererType
------------

.. autoclass:: manim.RendererType
   :noindex:


``RendererType`` 是渲染器选择的枚举，对应配置项 ``renderer``：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 成员
        - 含义
      * - ``CAIRO``
        - Cairo 渲染器（默认）
      * - ``OPENGL``
        - OpenGL 渲染器（更快，支持 ``TrueDot`` / ``DotCloud`` 等 GL 对象）
OpenGLPMobject
--------------

.. autoclass:: manim.OpenGLPMobject
   :noindex:


``OpenGLPMobject`` 是 OpenGL 点集对象的基类，相当于点云家族在 GL 一侧的 “PMobject”：以点集为渲染原语，``stroke_width`` 控制点尺寸。它本身很少直接用，常见的是其子类 ``DotCloud``、``OpenGLPMPoint``。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "OpenGLPMobject" [label="OpenGLPMobject", URL="/chapters/ch06/renderers.html#openglpmobject"];
     "OpenGLMobject" [label="OpenGLMobject"];
     "object" [label="object"];
     "OpenGLPMobject" -> "OpenGLMobject";
     "OpenGLMobject" -> "object";
   }


.. admonition:: 注意
   :class: warning

   该类需要 ``--renderer=opengl``；在 Cairo 渲染器下添加到场景不会正常显示。
OpenGLPGroup
------------

.. autoclass:: manim.OpenGLPGroup
   :noindex:


``OpenGLPGroup`` 是多个 ``OpenGLPMobject`` 的组合容器（对应 Cairo 侧的 ``PGroup``）：把若干 GL 点集对象作为一个整体参与变换。需要 **OpenGL 渲染器**。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "OpenGLPGroup" [label="OpenGLPGroup", URL="/chapters/ch06/renderers.html#openglpgroup"];
     "OpenGLPMobject" [label="OpenGLPMobject", URL="/chapters/ch06/renderers.html#openglpmobject"];
     "OpenGLMobject" [label="OpenGLMobject"];
     "object" [label="object"];
     "OpenGLPGroup" -> "OpenGLPMobject";
     "OpenGLPMobject" -> "OpenGLMobject";
     "OpenGLMobject" -> "object";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``*pmobs``
        - OpenGLPMobject
        - —
        - 要组合的点集对象
OpenGLPMPoint
-------------

.. autoclass:: manim.OpenGLPMPoint
   :noindex:


``OpenGLPMPoint`` 是单个 GL 点：``OpenGLPMobject`` 的最小特化，``location`` 指定点位。需要 **OpenGL 渲染器**；Cairo 侧画单点请用 ``Dot`` / ``Point``。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "OpenGLPMPoint" [label="OpenGLPMPoint", URL="/chapters/ch06/renderers.html#openglpmpoint"];
     "OpenGLPMobject" [label="OpenGLPMobject", URL="/chapters/ch06/renderers.html#openglpmobject"];
     "OpenGLMobject" [label="OpenGLMobject"];
     "object" [label="object"];
     "OpenGLPMPoint" -> "OpenGLPMobject";
     "OpenGLPMobject" -> "OpenGLMobject";
     "OpenGLMobject" -> "object";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``location``
        - `Point3DLike <https://docs.manim.community/en/v0.21.0/reference/manim.typing.html#manim.typing.Point3DLike>`__
        - `ORIGIN <https://docs.manim.community/en/v0.21.0/reference/manim.constants.html#manim.constants.ORIGIN>`__
        - 点的位置
        - ``stroke_width``
        - float
        - 4.0
        - 点的尺寸

下一步
------


“3D 与摄像机”板块到此结束：你已经能搭建 3D 场景、操纵镜头与取景框，并理解渲染器的选择。最后一个板块进入高级主题——自定义 mobject 与自定义动画。
