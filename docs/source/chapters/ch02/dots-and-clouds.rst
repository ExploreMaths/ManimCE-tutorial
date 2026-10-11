
点与点云
========


除了矢量轮廓，Manim 还提供一套基于 **离散点集** 的 mobject： ``Dot`` 是日常的实心圆点， ``Point`` 是逻辑单点， ``PointCloudDot`` 则用成百上千个小点拼出圆盘。点云家族的基类 ``PMobject`` 与矢量家族 ``VMobject`` 是 **并列** 关系，能力差异很大。

Dot
---

.. autoclass:: manim.Dot
   :noindex:


``Dot`` 是一个半径很小的实心圆（ ``Circle`` 的子类），默认无描边、完全填充，是标记位置、画散点图的第一选择。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Dot" [label="Dot", URL="/chapters/ch02/basic-shapes.html#dot"];
     "Circle" [label="Circle", URL="/chapters/ch02/basic-shapes.html#circle"];
     "Arc" [label="Arc", URL="/chapters/ch02/arcs-and-curves.html#arc"];
     "TipableVMobject" [label="TipableVMobject", URL="/chapters/ch02/lines-and-arrows.html#tipablevmobject"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Dot" -> "Circle";
     "Circle" -> "Arc";
     "Arc" -> "TipableVMobject";
     "TipableVMobject" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }



.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``point``
        - :class:`manim.typing.Point3DLike`
        - `ORIGIN <https://docs.manim.community/en/v0.21.0/reference/manim.constants.html#manim.constants.ORIGIN>`__
        - 圆点中心位置
      * - ``radius``
        - float
        - 0.08
        - 半径；比 `Circle </chapters/ch02/basic-shapes.html#circle>`__ 默认小得多
      * - ``stroke_width``
        - float
        - 0
        - 描边宽度，默认无描边
      * - ``fill_opacity``
        - float
        - 1.0
        - 填充不透明度，默认实心
      * - ``color``
        - :class:`manim.utils.color.core.ParsableManimColor`
        - `WHITE <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.manim_colors.html>`__
        - 颜色
      * - ``kwargs``
        - —
        - —
        - 转发给 `Circle </chapters/ch02/basic-shapes.html#circle>`__


与 ``LabeledDot`` 的对比：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 维度
        - `Dot </chapters/ch02/basic-shapes.html#dot>`__
        - `LabeledDot </api/geometry.html#labeleddot>`__
      * - 参数
        - ``point`` / ``radius`` / ``stroke_width`` / ``fill_opacity`` / ``color``
        - ``label`` 、 ``radius=None`` 、 ``buff=0.1``
      * - 标签
        - 无
        - 圆心处渲染一段文字
      * - ``radius=None`` 时
        - —
        - 按标签大小加 ``buff`` 自动计算


.. demo:: examples/ch02/dots_demo.py DotsDemo

   红色的普通 ``Dot`` 与蓝色的 ``LabeledDot(Text("A"))`` ；后者圆点尺寸随标签自动适配。


.. admonition:: 常见错误
   :class: warning

   ``Dot(RED)`` 把 ``RED`` 当成了 **位置** 参数（第一个参数是 ``point`` ）——正确写法是 ``Dot(color=RED)`` 或 ``Dot().set_color(RED)`` 。同理 ``Dot(LEFT * 2)`` 是把点放到左侧 2 个单位。


LabeledDot
----------

.. autoclass:: manim.LabeledDot
   :noindex:


``LabeledDot`` 是带居中标签的 ``Dot`` ： ``label`` 传字符串时按 ``MathTex`` 渲染（ **需要本机 LaTeX** ），也可以直接传入 ``Text`` / ``Tex`` 实例；不传 ``radius`` 时圆点半径由标签尺寸加 ``buff`` 推出。参数表与示例见上方 ``Dot`` 一节的对比与演示。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "LabeledDot" [label="LabeledDot", URL="/api/geometry.html#labeleddot"];
     "Dot" [label="Dot", URL="/chapters/ch02/basic-shapes.html#dot"];
     "Circle" [label="Circle", URL="/chapters/ch02/basic-shapes.html#circle"];
     "Arc" [label="Arc", URL="/chapters/ch02/arcs-and-curves.html#arc"];
     "TipableVMobject" [label="TipableVMobject", URL="/chapters/ch02/lines-and-arrows.html#tipablevmobject"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "LabeledDot" -> "Dot";
     "Dot" -> "Circle";
     "Circle" -> "Arc";
     "Arc" -> "TipableVMobject";
     "TipableVMobject" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. admonition:: 常见错误
   :class: warning

   无 LaTeX 环境下 ``LabeledDot("A")`` 会直接报错。改用 pango 文本： ``LabeledDot(Text("A"))`` 。


Point
-----

.. autoclass:: manim.Point
   :noindex:


``Point`` 是表示 **单个位置** 的 mobject：数据上只有一个坐标点，渲染时显示为极小的方块，默认黑色、几乎不可见。它适合做纯逻辑锚点（记录位置但不希望干扰画面）。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Point" [label="Point", URL="/chapters/ch02/dots-and-clouds.html#point"];
     "PMobject" [label="PMobject", URL="/chapters/ch02/dots-and-clouds.html#pmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Point" -> "PMobject";
     "PMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   Point(location: Point3DLike = ORIGIN, color: ManimColor = BLACK, **kwargs)


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``location``
        - :class:`manim.typing.Point3DLike`
        - `ORIGIN <https://docs.manim.community/en/v0.21.0/reference/manim.constants.html#manim.constants.ORIGIN>`__
        - 点的位置
      * - ``color``
        - `ManimColor </api/utils.html#manimcolor>`__
        - `BLACK <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.manim_colors.html>`__
        - 颜色，默认黑色
      * - ``kwargs``
        - —
        - —
        - 转发给 `PMobject </chapters/ch02/dots-and-clouds.html#pmobject>`__ ，如 ``stroke_width``


.. admonition:: 常见错误
   :class: warning

   两点需要留意：其一， ``Point`` 默认 **黑色** ，在黑背景上完全看不见，这不是 bug；其二， ``Point`` 继承自 ``PMobject`` 而非 ``VMobject`` ， **没有** ``set_fill`` / ``set_stroke`` / ``set_opacity`` 方法，调了要么报错要么落入 ``Mobject`` 的 ``set_*`` 兼容层只改属性不影响渲染。


PointCloudDot
-------------

.. autoclass:: manim.PointCloudDot
   :noindex:


``PointCloudDot`` 在指定半径的圆盘内随机撒出一片小点，拼出“点云圆盘”。它属于 ``PMobject`` 家族：没有矢量填充，每个点按 ``stroke_width`` 渲染为小方块。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "PointCloudDot" [label="PointCloudDot", URL="/chapters/ch02/dots-and-clouds.html#pointclouddot"];
     "Mobject1D" [label="Mobject1D", URL="/api/types.html#mobject1d"];
     "PMobject" [label="PMobject", URL="/chapters/ch02/dots-and-clouds.html#pmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "PointCloudDot" -> "Mobject1D";
     "Mobject1D" -> "PMobject";
     "PMobject" -> "Mobject";
     "Mobject" -> "object";
   }



.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``center``
        - :class:`manim.typing.Point3DLike`
        - `ORIGIN <https://docs.manim.community/en/v0.21.0/reference/manim.constants.html#manim.constants.ORIGIN>`__
        - 圆盘中心
      * - ``radius``
        - float
        - 2.0
        - 圆盘半径
      * - ``stroke_width``
        - int
        - 2
        - 每个点的渲染尺寸
      * - ``density``
        - int
        - 10
        - 点密度，越大点越多（每单位约 density² 量级）
      * - ``color``
        - `ManimColor </api/utils.html#manimcolor>`__
        - `PURE_YELLOW <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.manim_colors.html>`__
        - 点云颜色


.. demo:: examples/ch02/point_cloud_demo.py PointCloudDemo

   两片 ``PointCloudDot`` ： ``density=15`` 的大云与 ``density=25`` 的小云；点的位置是随机生成的。


.. admonition:: 提示
   :class: tip

   点云的随机分布 **每次渲染都不同** 。需要可复现的结果时，用 CLI ``--seed`` 或 ``Scene(random_seed=42)`` 固定随机种子。


PMobject
--------

.. autoclass:: manim.PMobject
   :noindex:


点集基类：所有点成员共用一个 ``points`` 数组，无矢量填充（ ``stroke_width=4`` ）。四个点云基类的对比与继承链见下表。

Mobject1D
---------

.. autoclass:: manim.Mobject1D
   :noindex:


一维采样基类（ ``density=10`` ， ``epsilon = 1/density`` ），用于沿曲线等距采样点。

Mobject2D
---------

.. autoclass:: manim.Mobject2D
   :noindex:


二维采样基类（ ``density=25`` ， ``epsilon = 1/density`` ），用于在曲面上采样点。

PGroup
------

.. autoclass:: manim.PGroup
   :noindex:


``PMobject`` 的组合容器（成员非 ``PMobject`` 时抛 ``ValueError`` ），用于把多片点云当一个整体变换；对应 ``VMobject`` 侧的 ``VGroup`` 。

点云家族四基类对比：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 类
        - 签名（默认参数）
        - 一句话用途
      * - `PMobject </chapters/ch02/dots-and-clouds.html#pmobject>`__
        - ``(stroke_width=4)``
        - 点集基类：所有点成员一个 ``points`` 数组，无矢量填充
      * - `Mobject1D </api/types.html#mobject1d>`__
        - ``(density=10)``
        - 一维采样基类（曲线）， ``epsilon = 1/density``
      * - `Mobject2D </api/types.html#mobject2d>`__
        - ``(density=25)``
        - 二维采样基类（曲面）， ``epsilon = 1/density``
      * - `PGroup </api/types.html#pgroup>`__
        - ``(*pmobs)``
        - `PMobject </chapters/ch02/dots-and-clouds.html#pmobject>`__ 的组合容器；成员非 `PMobject </chapters/ch02/dots-and-clouds.html#pmobject>`__ 时抛 ``ValueError``


各成员的继承链：

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "PMobject" [label="PMobject", URL="/chapters/ch02/dots-and-clouds.html#pmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "PMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Mobject1D" [label="Mobject1D", URL="/api/types.html#mobject1d"];
     "PMobject" [label="PMobject", URL="/chapters/ch02/dots-and-clouds.html#pmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Mobject1D" -> "PMobject";
     "PMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Mobject2D" [label="Mobject2D", URL="/api/types.html#mobject2d"];
     "PMobject" [label="PMobject", URL="/chapters/ch02/dots-and-clouds.html#pmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Mobject2D" -> "PMobject";
     "PMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "PGroup" [label="PGroup", URL="/api/types.html#pgroup"];
     "PMobject" [label="PMobject", URL="/chapters/ch02/dots-and-clouds.html#pmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "PGroup" -> "PMobject";
     "PMobject" -> "Mobject";
     "Mobject" -> "object";
   }


日常使用中，只有 ``PointCloudDot`` （现成可看的点云）和 ``Point`` 需要直接构造； ``PMobject`` / ``Mobject1D`` / ``Mobject2D`` 更多是继承与扩展的基类， ``PGroup`` 用于把多片点云当一个整体变换。

.. admonition:: 常见错误
   :class: warning

   不要把 ``PMobject`` 家族的成员塞进 ``VGroup``——``VGroup`` 只收 ``VMobject`` ，应改用 ``PGroup`` ；反过来 ``Dot`` 是 ``Circle`` 子类，属于 ``VMobject`` ，不要塞进 ``PGroup`` 。


自测
----


.. dropdown:: ✏️ 练习

   下面两行代码各画出了什么？ ``Dot(LEFT * 2)`` 与 ``Dot(color=RED)`` 的参数分别落在了哪个形参上？

   .. dropdown:: ✅ 参考答案

      ``Dot(LEFT * 2)`` 把位置参数 ``point`` 设为 ``LEFT * 2`` ，画出一个位于左侧 2 个单位的白色（默认色）圆点； ``Dot(color=RED)`` 用关键字传入 ``color`` ，画出一个位于原点的红色圆点。若误写 ``Dot(RED)`` ， ``RED`` 会被当成 ``point`` 而报错。


.. dropdown:: ✏️ 练习

   想让画面上有一个“带字母标签的圆点”，但机器没有安装 LaTeX，应该怎样构造 ``LabeledDot`` ？如果还需要第二片点云与它一起整体移动，又该用什么容器组合？

   .. dropdown:: ✅ 参考答案

      标签用 pango 文本实例传入： ``LabeledDot(Text("A"))`` ，避免字符串触发的 ``MathTex`` 渲染。第二片点云用 ``PointCloudDot`` 构造；二者类型不同（ ``LabeledDot`` 是 ``VMobject`` ，点云是 ``PMobject`` ），不能用 ``VGroup`` 也不能用 ``PGroup`` 混装，请用不校验类型的 ``Group`` 组合后再整体 ``shift`` / ``scale`` 。



TrueDot
-------

.. autoclass:: manim.TrueDot
   :noindex:


``TrueDot`` 是 ``Dot`` 的 OpenGL 版本：用 GL 点图元绘制，无论半径多小都是标准圆点，也不会出现 Cairo 版 ``Dot`` 在多边形近似下的棱角。需要 **OpenGL 渲染器** 才能显示：``manim render -pql --renderer=opengl``。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "TrueDot" [label="TrueDot", URL="/chapters/ch02/dots-and-clouds.html#truedot"];
     "DotCloud" [label="DotCloud", URL="/chapters/ch02/dots-and-clouds.html#dotcloud"];
     "OpenGLPMobject" [label="OpenGLPMobject", URL="/chapters/ch06/renderers.html#openglpmobject"];
     "OpenGLMobject" [label="OpenGLMobject"];
     "object" [label="object"];
     "TrueDot" -> "DotCloud";
     "DotCloud" -> "OpenGLPMobject";
     "OpenGLPMobject" -> "OpenGLMobject";
     "OpenGLMobject" -> "object";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``center``
        - :class:`manim.typing.Point3DLike`
        - `ORIGIN <https://docs.manim.community/en/v0.21.0/reference/manim.constants.html#manim.constants.ORIGIN>`__
        - 圆点中心位置
      * - ``stroke_width``
        - float
        - 2.0
        - 点的描边宽度

DotCloud
--------

.. autoclass:: manim.DotCloud
   :noindex:


``DotCloud`` 是 OpenGL 点云家族的基类（Cairo 一侧的对应物是 ``PMobject``）：内部维护一个点集，用 GL 点图元整体绘制。``TrueDot`` 就是它的单点特化。需要 **OpenGL 渲染器**。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "DotCloud" [label="DotCloud", URL="/chapters/ch02/dots-and-clouds.html#dotcloud"];
     "OpenGLPMobject" [label="OpenGLPMobject", URL="/chapters/ch06/renderers.html#openglpmobject"];
     "OpenGLMobject" [label="OpenGLMobject"];
     "object" [label="object"];
     "DotCloud" -> "OpenGLPMobject";
     "OpenGLPMobject" -> "OpenGLMobject";
     "OpenGLMobject" -> "object";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``color``
        - :class:`manim.utils.color.core.ParsableManimColor`
        - ``PURE_YELLOW``
        - 点云颜色
      * - ``stroke_width``
        - float
        - 2.0
        - 点的大小相关参数
      * - ``radius``
        - float
        - 2.0
        - 点云分布半径
      * - ``density``
        - float
        - 10
        - 点的密度

下一步
------


到这里，二维图形的基础工具已经齐全。下一节进入“线与箭头”，看看 ``Line`` 、 ``Arrow`` 和带端点的曲线。
