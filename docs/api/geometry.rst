==============================
API 参考：几何图形（geometry）
==============================

共 **57** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

Angle
-----

两条线的夹角图形：自动找交点、按半径画出夹角弧，可标注度数，几何作图必备。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Angle";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``line1``
        - —，Line
      * - ``line2``
        - —，Line
      * - ``radius``
        - None，float | None
      * - ``quadrant``
        - (1, 1)，AngleQuadrant
      * - ``other_angle``
        - False，bool
      * - ``dot``
        - False，bool
      * - ``dot_radius``
        - None，float | None
      * - ``dot_distance``
        - 0.55，float
      * - ``dot_color``
        - ManimColor('#FFFFFF')，ParsableManimColor
      * - ``elbow``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   angle = Angle(line1, line2, radius=0.5)

API 文档
~~~~~~~~

.. autoclass:: manim.Angle

AnnotationDot
-------------

带描边强调的小圆点，比普通 Dot 在复杂背景上更醒目，常用于标记点。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "Circle";
     "Circle" -> "Dot";
     "Dot" -> "AnnotationDot";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``radius``
        - 0.10400000000000001，float
      * - ``stroke_width``
        - 5，float
      * - ``stroke_color``
        - ManimColor('#FFFFFF')，ParsableManimColor
      * - ``fill_color``
        - ManimColor('#58C4DD')，ParsableManimColor

API 文档
~~~~~~~~

.. autoclass:: manim.AnnotationDot

AnnularSector
-------------

扇环（圆环的一段）：内外半径 + 起止角度，饼图环图的基础件。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "AnnularSector";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``inner_radius``
        - 1，float
      * - ``outer_radius``
        - 2，float
      * - ``angle``
        - 1.5707963267948966，float
      * - ``start_angle``
        - 0，float
      * - ``fill_opacity``
        - 1，float
      * - ``stroke_width``
        - 0，float
      * - ``color``
        - ManimColor('#FFFFFF')，ParsableManimColor

快速上手
~~~~~~~~

.. code-block:: python

   s = AnnularSector(inner_radius=1, outer_radius=2, angle=PI/2)

API 文档
~~~~~~~~

.. autoclass:: manim.AnnularSector

Annulus
-------

完整圆环：内半径 + 外半径，甜甜圈形状。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "Circle";
     "Circle" -> "Annulus";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``inner_radius``
        - 1，float
      * - ``outer_radius``
        - 2，float
      * - ``fill_opacity``
        - 1，float
      * - ``stroke_width``
        - 0，float
      * - ``color``
        - ManimColor('#FFFFFF')，ParsableManimColor
      * - ``mark_paths_closed``
        - False，bool

API 文档
~~~~~~~~

.. autoclass:: manim.Annulus

Arc
---

圆弧：半径 + 起始角 + 张角，所有曲线类图形（Circle、Sector……）的祖宗。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``radius``
        - 1.0，float | None
      * - ``start_angle``
        - 0，float
      * - ``angle``
        - 1.5707963267948966，float
      * - ``num_components``
        - 9，int
      * - ``arc_center``
        - array([0., 0., 0.])，Point3DLike

快速上手
~~~~~~~~

.. code-block:: python

   arc = Arc(radius=2, start_angle=0, angle=PI)

API 文档
~~~~~~~~

.. autoclass:: manim.Arc

ArcBetweenPoints
----------------

过两点的一段圆弧：自动选半径让弧经过两点，画「连接箭头」或「跳跃路径」常用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "ArcBetweenPoints";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``start``
        - —，Point3DLike
      * - ``end``
        - —，Point3DLike
      * - ``angle``
        - 1.5707963267948966，float
      * - ``radius``
        - None，float | None

快速上手
~~~~~~~~

.. code-block:: python

   arc = ArcBetweenPoints(a.get_center(), b.get_center())

API 文档
~~~~~~~~

.. autoclass:: manim.ArcBetweenPoints

ArcPolygon
----------

边为圆弧的多边形：顶点之间用弧连接而非直线，呈现「鼓包」轮廓。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "ArcPolygon";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``angle``
        - 0.7853981633974483，float
      * - ``radius``
        - None，float | None
      * - ``arc_config``
        - None，list[dict] | None

API 文档
~~~~~~~~

.. autoclass:: manim.ArcPolygon

ArcPolygonFromArcs
------------------

用现成 Arc 对象拼成多边形，边完全由你给的弧决定。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "ArcPolygonFromArcs";
   }

API 文档
~~~~~~~~

.. autoclass:: manim.ArcPolygonFromArcs

Arrow
-----

带箭头的直线：start/end + 箭尖样式 buff 可调，是最常用的指向性图形。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Line";
     "Line" -> "Arrow";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``stroke_width``
        - 6，float
      * - ``buff``
        - 0.25，float
      * - ``max_tip_length_to_length_ratio``
        - 0.25，float
      * - ``max_stroke_width_to_length_ratio``
        - 5，float

快速上手
~~~~~~~~

.. code-block:: python

   arrow = Arrow(LEFT, RIGHT, buff=0.1)

API 文档
~~~~~~~~

.. autoclass:: manim.Arrow

ArrowCircleFilledTip
--------------------

圆形实心箭尖样式类：配合 Arrow 的 tip_shape 使用（ArrowCircleTip 的实心版）。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "Circle";
     "Circle" -> "ArrowTip";
     "ArrowTip" -> "ArrowCircleTip";
     "ArrowCircleTip" -> "ArrowCircleFilledTip";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``fill_opacity``
        - 1，float
      * - ``stroke_width``
        - 0，float

API 文档
~~~~~~~~

.. autoclass:: manim.ArrowCircleFilledTip

ArrowCircleTip
--------------

空心圆形箭尖样式类：把箭头末端换成小圆圈，思维导图风。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "Circle";
     "Circle" -> "ArrowTip";
     "ArrowTip" -> "ArrowCircleTip";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``fill_opacity``
        - 0，float
      * - ``stroke_width``
        - 3，float
      * - ``length``
        - 0.35，float
      * - ``start_angle``
        - 3.141592653589793，float

API 文档
~~~~~~~~

.. autoclass:: manim.ArrowCircleTip

ArrowSquareFilledTip
--------------------

方形实心箭尖样式类。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "Polygon";
     "Polygon" -> "Rectangle";
     "Rectangle" -> "Square";
     "Square" -> "ArrowTip";
     "ArrowTip" -> "ArrowSquareTip";
     "ArrowSquareTip" -> "ArrowSquareFilledTip";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``fill_opacity``
        - 1，float
      * - ``stroke_width``
        - 0，float

API 文档
~~~~~~~~

.. autoclass:: manim.ArrowSquareFilledTip

ArrowSquareTip
--------------

空心方形箭尖样式类。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "Polygon";
     "Polygon" -> "Rectangle";
     "Rectangle" -> "Square";
     "Square" -> "ArrowTip";
     "ArrowTip" -> "ArrowSquareTip";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``fill_opacity``
        - 0，float
      * - ``stroke_width``
        - 3，float
      * - ``length``
        - 0.35，float
      * - ``start_angle``
        - 3.141592653589793，float

API 文档
~~~~~~~~

.. autoclass:: manim.ArrowSquareTip

ArrowTip
--------

所有箭尖样式的基类：自定义箭尖就继承它实现 set_points()，length/width 属性定义尺寸。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "ArrowTip";
   }

API 文档
~~~~~~~~

.. autoclass:: manim.ArrowTip

ArrowTriangleFilledTip
----------------------

三角实心箭尖（默认样式），一般不直接实例化。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "RegularPolygram";
     "RegularPolygram" -> "RegularPolygon";
     "RegularPolygon" -> "Triangle";
     "Triangle" -> "ArrowTip";
     "ArrowTip" -> "ArrowTriangleTip";
     "ArrowTriangleTip" -> "ArrowTriangleFilledTip";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``fill_opacity``
        - 1，float
      * - ``stroke_width``
        - 0，float

API 文档
~~~~~~~~

.. autoclass:: manim.ArrowTriangleFilledTip

ArrowTriangleTip
----------------

空心三角箭尖样式类。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "RegularPolygram";
     "RegularPolygram" -> "RegularPolygon";
     "RegularPolygon" -> "Triangle";
     "Triangle" -> "ArrowTip";
     "ArrowTip" -> "ArrowTriangleTip";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``fill_opacity``
        - 0，float
      * - ``stroke_width``
        - 3，float
      * - ``length``
        - 0.35，float
      * - ``width``
        - 0.35，float
      * - ``start_angle``
        - 3.141592653589793，float

API 文档
~~~~~~~~

.. autoclass:: manim.ArrowTriangleTip

BackgroundRectangle
-------------------

自动包裹目标对象的背景色矩形：给文字图形加底色衬垫，防止与背景混淆。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "Polygon";
     "Polygon" -> "Rectangle";
     "Rectangle" -> "RoundedRectangle";
     "RoundedRectangle" -> "SurroundingRectangle";
     "SurroundingRectangle" -> "BackgroundRectangle";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``color``
        - None
      * - ``stroke_width``
        - 0，float
      * - ``stroke_opacity``
        - 0，float
      * - ``fill_opacity``
        - 0.75，float
      * - ``buff``
        - 0

快速上手
~~~~~~~~

.. code-block:: python

   bg = BackgroundRectangle(label, fill_opacity=0.7)

API 文档
~~~~~~~~

.. autoclass:: manim.BackgroundRectangle

Circle
------

圆：radius 或 diameter 指定大小，提供 from_three_points、point_at_angle、surround 等几何工厂方法。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "Circle";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``radius``
        - None，float | None
      * - ``color``
        - ManimColor('#FC6255')，ParsableManimColor

快速上手
~~~~~~~~

.. code-block:: python

   c = Circle(radius=2, color=BLUE)

API 文档
~~~~~~~~

.. autoclass:: manim.Circle

ConvexHull
----------

一组点的凸包多边形：自动计算外轮廓，计算几何可视化。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "ConvexHull";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``tolerance``
        - 1e-05，float

API 文档
~~~~~~~~

.. autoclass:: manim.ConvexHull

Cross
-----

叉号（×）图形：stroke_width 和比例可调，标记错误或否定语义。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Cross";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - None，Mobject | None
      * - ``stroke_color``
        - ManimColor('#FC6255')，ParsableManimColor
      * - ``stroke_width``
        - 6.0，float
      * - ``scale_factor``
        - 1.0，float

快速上手
~~~~~~~~

.. code-block:: python

   cross = Cross(mob)

API 文档
~~~~~~~~

.. autoclass:: manim.Cross

CubicBezier
-----------

三次贝塞尔曲线：两个锚点 + 两个控制点，是矢量绘图的最小单元。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "CubicBezier";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``start_anchor``
        - —，Point3DLike
      * - ``start_handle``
        - —，Point3DLike
      * - ``end_handle``
        - —，Point3DLike
      * - ``end_anchor``
        - —，Point3DLike

快速上手
~~~~~~~~

.. code-block:: python

   b = CubicBezier(a1, h1, h2, a2)

API 文档
~~~~~~~~

.. autoclass:: manim.CubicBezier

CurvedArrow
-----------

弯曲的箭头：ArcBetweenPoints + 箭尖的组合体，流程图里绕过障碍的连线。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "ArcBetweenPoints";
     "ArcBetweenPoints" -> "CurvedArrow";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``start_point``
        - —，Point3DLike
      * - ``end_point``
        - —，Point3DLike

API 文档
~~~~~~~~

.. autoclass:: manim.CurvedArrow

CurvedDoubleArrow
-----------------

两端都带箭尖的弯弧，双向关系专用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "ArcBetweenPoints";
     "ArcBetweenPoints" -> "CurvedArrow";
     "CurvedArrow" -> "CurvedDoubleArrow";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``start_point``
        - —，Point3DLike
      * - ``end_point``
        - —，Point3DLike

API 文档
~~~~~~~~

.. autoclass:: manim.CurvedDoubleArrow

Cutout
------

带镂空的多边形：外部轮廓减内部孔洞，fill 模式下孔洞透明。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Cutout";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``main_shape``
        - —，VMobject

快速上手
~~~~~~~~

.. code-block:: python

   c = Cutout(square, circle)

API 文档
~~~~~~~~

.. autoclass:: manim.Cutout

DashedLine
----------

虚线直线：DashedVMobject 的直线便捷版，辅助线首选。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Line";
     "Line" -> "DashedLine";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``dash_length``
        - 0.05，float
      * - ``dashed_ratio``
        - 0.5，float

快速上手
~~~~~~~~

.. code-block:: python

   d = DashedLine(LEFT, RIGHT)

API 文档
~~~~~~~~

.. autoclass:: manim.DashedLine

Difference
----------

布尔差集：从主体图形中挖掉重叠部分，属于 VMobject 布尔运算家族。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Difference";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``subject``
        - —，VMobject
      * - ``clip``
        - —，VMobject

快速上手
~~~~~~~~

.. code-block:: python

   diff = Difference(square, circle)

API 文档
~~~~~~~~

.. autoclass:: manim.Difference

Dot
---

小圆点：radius 很小且 fill 为主，标记坐标、描点画图的基本单元。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "Circle";
     "Circle" -> "Dot";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``point``
        - array([0., 0., 0.])，Point3DLike
      * - ``radius``
        - 0.08，float
      * - ``stroke_width``
        - 0，float
      * - ``fill_opacity``
        - 1.0，float
      * - ``color``
        - ManimColor('#FFFFFF')，ParsableManimColor

快速上手
~~~~~~~~

.. code-block:: python

   dot = Dot(point, color=RED)

API 文档
~~~~~~~~

.. autoclass:: manim.Dot

DoubleArrow
-----------

两端都有箭头的直线，表示双向映射或区间。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Line";
     "Line" -> "Arrow";
     "Arrow" -> "DoubleArrow";
   }

快速上手
~~~~~~~~

.. code-block:: python

   d = DoubleArrow(LEFT, RIGHT)

API 文档
~~~~~~~~

.. autoclass:: manim.DoubleArrow

Elbow
-----

直角弯头线：两条垂直短线段，管道图、直角坐标标记用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Elbow";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``width``
        - 0.2，float
      * - ``angle``
        - 0，float

API 文档
~~~~~~~~

.. autoclass:: manim.Elbow

Ellipse
-------

椭圆：width/height 分别指定两轴，圆形的长轴版。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "Circle";
     "Circle" -> "Ellipse";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``width``
        - 2，float
      * - ``height``
        - 1，float

快速上手
~~~~~~~~

.. code-block:: python

   e = Ellipse(width=4, height=2)

API 文档
~~~~~~~~

.. autoclass:: manim.Ellipse

Exclusion
---------

布尔异或：只保留两个图形不重叠的部分。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Exclusion";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``subject``
        - —，VMobject
      * - ``clip``
        - —，VMobject

API 文档
~~~~~~~~

.. autoclass:: manim.Exclusion

Intersection
------------

布尔交集：只保留两个图形重叠的区域。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Intersection";
   }

快速上手
~~~~~~~~

.. code-block:: python

   i = Intersection(square, circle)

API 文档
~~~~~~~~

.. autoclass:: manim.Intersection

Label
-----

几何图形上的标签：自带背景框的小文本，跟随目标位置摆放。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Label";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``label``
        - —，str | ManimTextLabel
      * - ``label_config``
        - None，dict[str, Any] | None
      * - ``box_config``
        - None，dict[str, Any] | None
      * - ``frame_config``
        - None，dict[str, Any] | None

API 文档
~~~~~~~~

.. autoclass:: manim.Label

LabeledArrow
------------

带文字标签的箭头：label 自动置于箭身中点，省去手动对位。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Line";
     "Line" -> "Arrow";
     "Arrow" -> "LabeledLine";
     "LabeledLine" -> "LabeledArrow";
   }

API 文档
~~~~~~~~

.. autoclass:: manim.LabeledArrow

LabeledDot
----------

带文字标签的圆点：标签居中于点内，图论顶点标注专用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "Circle";
     "Circle" -> "Dot";
     "Dot" -> "LabeledDot";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``label``
        - —
      * - ``radius``
        - None，float | None
      * - ``buff``
        - 0.1，float

API 文档
~~~~~~~~

.. autoclass:: manim.LabeledDot

LabeledLine
-----------

带标签的直线：标签自动放在线段中点。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Line";
     "Line" -> "LabeledLine";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``label``
        - —，str | ManimTextLabel
      * - ``label_position``
        - 0.5，float
      * - ``label_config``
        - None，dict[str, Any] | None
      * - ``box_config``
        - None，dict[str, Any] | None
      * - ``frame_config``
        - None，dict[str, Any] | None

API 文档
~~~~~~~~

.. autoclass:: manim.LabeledLine

LabeledPolygram
---------------

带顶点标签的折线/多边形：每个顶点自动编号。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "LabeledPolygram";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``label``
        - —，str | ManimTextLabel
      * - ``precision``
        - 0.01，float
      * - ``label_config``
        - None，dict[str, Any] | None
      * - ``box_config``
        - None，dict[str, Any] | None
      * - ``frame_config``
        - None，dict[str, Any] | None

API 文档
~~~~~~~~

.. autoclass:: manim.LabeledPolygram

Line
----

两点之间的直线：buff 让端点留白不压对象，put_start_and_end_on 可动画化，是构图的骨架。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Line";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``start``
        - array([-1.,  0.,  0.])，Point3DLike | Mobject
      * - ``end``
        - array([1., 0., 0.])，Point3DLike | Mobject
      * - ``buff``
        - 0，float
      * - ``path_arc``
        - 0，float

快速上手
~~~~~~~~

.. code-block:: python

   line = Line(ORIGIN, RIGHT * 3)

API 文档
~~~~~~~~

.. autoclass:: manim.Line

Polygon
-------

多边形：顶点列表连线闭合，一切直边图形（三角形、矩形……）的基类。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "Polygon";
   }

快速上手
~~~~~~~~

.. code-block:: python

   p = Polygon(ORIGIN, RIGHT, UP)

API 文档
~~~~~~~~

.. autoclass:: manim.Polygon

Polygram
--------

折线组：可以含多个不闭合顶点组（组 = 一条折线），比 Polygon 更自由的连点工具。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``color``
        - ManimColor('#58C4DD')，ParsableManimColor

API 文档
~~~~~~~~

.. autoclass:: manim.Polygram

Rectangle
---------

矩形：width/height 与角半径可调，包围、对齐、底衬的主力图形。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "Polygon";
     "Polygon" -> "Rectangle";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``color``
        - ManimColor('#FFFFFF')，ParsableManimColor
      * - ``height``
        - 2.0，float
      * - ``width``
        - 4.0，float
      * - ``grid_xstep``
        - None，float | None
      * - ``grid_ystep``
        - None，float | None
      * - ``mark_paths_closed``
        - True，bool
      * - ``close_new_points``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   r = Rectangle(width=4, height=2)

API 文档
~~~~~~~~

.. autoclass:: manim.Rectangle

RegularPolygon
--------------

正多边形：n 指定边数，内切圆半径可调。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "RegularPolygram";
     "RegularPolygram" -> "RegularPolygon";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``n``
        - 6，int

快速上手
~~~~~~~~

.. code-block:: python

   hexagon = RegularPolygon(n=6)

API 文档
~~~~~~~~

.. autoclass:: manim.RegularPolygon

RegularPolygram
---------------

正多角星：n 顶点按密度跳着连线（如五角星 density=2）。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "RegularPolygram";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``num_vertices``
        - —，int
      * - ``density``
        - 2，int
      * - ``radius``
        - 1，float
      * - ``start_angle``
        - None，float | None

API 文档
~~~~~~~~

.. autoclass:: manim.RegularPolygram

RightAngle
----------

直角标记：两条线垂直时的小方框角标，几何证明标配。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Angle";
     "Angle" -> "RightAngle";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``line1``
        - —，Line
      * - ``line2``
        - —，Line
      * - ``length``
        - None，float | None

快速上手
~~~~~~~~

.. code-block:: python

   ra = RightAngle(line1, line2, length=0.3)

API 文档
~~~~~~~~

.. autoclass:: manim.RightAngle

RoundedRectangle
----------------

圆角矩形：corner_radius 控制圆角，卡片式 UI 元素的首选。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "Polygon";
     "Polygon" -> "Rectangle";
     "Rectangle" -> "RoundedRectangle";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``corner_radius``
        - 0.5，float | list[float]

快速上手
~~~~~~~~

.. code-block:: python

   card = RoundedRectangle(corner_radius=0.2, width=4, height=2)

API 文档
~~~~~~~~

.. autoclass:: manim.RoundedRectangle

Sector
------

扇形：圆 + 张角，饼图的组成单元。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "AnnularSector";
     "AnnularSector" -> "Sector";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``radius``
        - 1，float

快速上手
~~~~~~~~

.. code-block:: python

   s = Sector(angle=PI/3)

API 文档
~~~~~~~~

.. autoclass:: manim.Sector

Square
------

正方形：Rectangle 的等边便捷版，边长用 side_length。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "Polygon";
     "Polygon" -> "Rectangle";
     "Rectangle" -> "Square";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``side_length``
        - 2.0，float

快速上手
~~~~~~~~

.. code-block:: python

   sq = Square(side_length=2)

API 文档
~~~~~~~~

.. autoclass:: manim.Square

Star
----

五角星样式的正多角星：n 与密度决定角数，外内半径比决定胖瘦。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "Polygon";
     "Polygon" -> "Star";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``n``
        - 5，int
      * - ``outer_radius``
        - 1，float
      * - ``inner_radius``
        - None，float | None
      * - ``density``
        - 2，int
      * - ``start_angle``
        - 1.5707963267948966，float | None

快速上手
~~~~~~~~

.. code-block:: python

   star = Star(n=5, fill_color=YELLOW)

API 文档
~~~~~~~~

.. autoclass:: manim.Star

StealthTip
----------

隐形战斗机风格的箭尖（默认箭尖），一般不直接实例化。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "ArrowTip";
     "ArrowTip" -> "StealthTip";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``fill_opacity``
        - 1，float
      * - ``stroke_width``
        - 3，float
      * - ``length``
        - 0.175，float
      * - ``start_angle``
        - 3.141592653589793，float

API 文档
~~~~~~~~

.. autoclass:: manim.StealthTip

SurroundingRectangle
--------------------

围绕目标的矩形框：自动留边距包围对象，强调、圈选必备。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "Polygon";
     "Polygon" -> "Rectangle";
     "Rectangle" -> "RoundedRectangle";
     "RoundedRectangle" -> "SurroundingRectangle";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``color``
        - ManimColor('#FFFF00')，ParsableManimColor
      * - ``buff``
        - 0.1
      * - ``corner_radius``
        - 0.0，float

快速上手
~~~~~~~~

.. code-block:: python

   box = SurroundingRectangle(formula, color=YELLOW)

API 文档
~~~~~~~~

.. autoclass:: manim.SurroundingRectangle

TangentLine
-----------

曲线在指定参数处的切线：微分几何可视化直接可用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Line";
     "Line" -> "TangentLine";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vmob``
        - —，VMobject
      * - ``alpha``
        - —，float
      * - ``length``
        - 1，float
      * - ``d_alpha``
        - 1e-06，float

快速上手
~~~~~~~~

.. code-block:: python

   t = TangentLine(circle, alpha=0.3)

API 文档
~~~~~~~~

.. autoclass:: manim.TangentLine

TangentialArc
-------------

以一点为端点、与曲线相切的弧：强调方向变化的小装饰。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Arc";
     "Arc" -> "ArcBetweenPoints";
     "ArcBetweenPoints" -> "TangentialArc";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``line1``
        - —，Line
      * - ``line2``
        - —，Line
      * - ``radius``
        - —，float
      * - ``corner``
        - (1, 1)，Any

API 文档
~~~~~~~~

.. autoclass:: manim.TangentialArc

TipableVMobject
---------------

「可装箭尖」线段的基类：Arrow、Line 继承它获得 add_tip/tip 配置能力。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``tip_length``
        - 0.35，float
      * - ``normal_vector``
        - array([0., 0., 1.])，Vector3DLike
      * - ``tip_style``
        - None，dict | None

API 文档
~~~~~~~~

.. autoclass:: manim.TipableVMobject

Triangle
--------

等边三角形：RegularPolygon(n=3) 的便捷版。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Polygram";
     "Polygram" -> "RegularPolygram";
     "RegularPolygram" -> "RegularPolygon";
     "RegularPolygon" -> "Triangle";
   }

快速上手
~~~~~~~~

.. code-block:: python

   tri = Triangle()

API 文档
~~~~~~~~

.. autoclass:: manim.Triangle

Underline
---------

下划线：贴住目标底部的横线，强调文本用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Line";
     "Line" -> "Underline";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``buff``
        - 0.1，float

快速上手
~~~~~~~~

.. code-block:: python

   u = Underline(text)

API 文档
~~~~~~~~

.. autoclass:: manim.Underline

Union
-----

布尔并集：合并两个图形为一个轮廓。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Union";
   }

快速上手
~~~~~~~~

.. code-block:: python

   u = Union(square, circle)

API 文档
~~~~~~~~

.. autoclass:: manim.Union

Vector
------

从原点出发的箭头（向量）：direction 与长度构造，线性代数可视化核心对象。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TipableVMobject";
     "TipableVMobject" -> "Line";
     "Line" -> "Arrow";
     "Arrow" -> "Vector";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``direction``
        - array([1., 0., 0.])
      * - ``buff``
        - 0，float

快速上手
~~~~~~~~

.. code-block:: python

   v = Vector(RIGHT * 2, color=RED)

API 文档
~~~~~~~~

.. autoclass:: manim.Vector
