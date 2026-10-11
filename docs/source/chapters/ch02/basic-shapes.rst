
基本形状
========


Manim 的内置几何形状都在 ``manim.mobject.geometry`` 包中（arc、boolean_ops、labeled、line、polygram、shape_matchers、tips 七个子模块）。本节覆盖最常用的成员：圆与椭圆、矩形家族、多边形家族、折线图形，以及凸包与镂空。

Circle
------

.. autoclass:: manim.Circle
   :noindex:


``Circle`` 是最常用的形状：按半径生成的正圆，默认描边、无填充，默认颜色是 Manim 标志性的红色 ``#FC6255`` 。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Circle" [label="Circle", URL="/chapters/ch02/basic-shapes.html#circle"];
     "Arc" [label="Arc", URL="/chapters/ch02/arcs-and-curves.html#arc"];
     "TipableVMobject" [label="TipableVMobject", URL="/chapters/ch02/lines-and-arrows.html#tipablevmobject"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Circle" -> "Arc";
     "Arc" -> "TipableVMobject";
     "TipableVMobject" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   Circle(radius: float | None = None, color: ParsableManimColor = "#FC6255", **kwargs)


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``radius``
        - float | None
        - None
        - 半径；None 时取 1
      * - ``color``
        - `ParsableManimColor <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor>`__
        - #FC6255
        - 颜色，传给 `Arc </chapters/ch02/arcs-and-curves.html#arc>`__
      * - ``kwargs``
        - —
        - —
        - 转发给 `Arc </chapters/ch02/arcs-and-curves.html#arc>`__ / `VMobject </chapters/ch02/vmobject.html#vmobject>`__ ，如 ``stroke_width`` 、 ``fill_opacity``


与 ``Ellipse`` 的对比：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 维度
        - `Circle </chapters/ch02/basic-shapes.html#circle>`__
        - `Ellipse </chapters/ch02/basic-shapes.html#ellipse>`__
      * - 继承
        - `Circle </chapters/ch02/basic-shapes.html#circle>`__ → `Arc </chapters/ch02/arcs-and-curves.html#arc>`__ → `TipableVMobject </chapters/ch02/lines-and-arrows.html#tipablevmobject>`__
        - `Ellipse </chapters/ch02/basic-shapes.html#ellipse>`__ → `Circle </chapters/ch02/basic-shapes.html#circle>`__ → ...
      * - 尺寸参数
        - ``radius``
        - ``width=2`` 、 ``height=1``
      * - 关系
        - 正圆
        - 构造一个单位圆后拉伸得到


.. demo:: examples/ch02/circle_ellipse.py CircleEllipseDemo

   ``Circle(radius=1.2)`` 与 ``Ellipse(width=3.0, height=1.4)`` ：椭圆等价于把圆在两个方向上独立拉伸。


.. admonition:: 常见错误
   :class: warning

   ``Circle(width=3)`` 是不存在的参数——圆只有 ``radius`` 。想要宽高可独立设置的椭圆请用 ``Ellipse`` （它的参数是 ``width`` / ``height`` ，不是 ``radius`` ）。


Ellipse
-------

.. autoclass:: manim.Ellipse
   :noindex:


``Ellipse`` 是 ``Circle`` 的子类：先按 ``Circle`` 构造单位圆，再分别 ``stretch_to_fit_width`` / ``stretch_to_fit_height`` 拉伸。参数表与示例见上方 ``Circle`` 一节的对比与演示。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Ellipse" [label="Ellipse", URL="/chapters/ch02/basic-shapes.html#ellipse"];
     "Circle" [label="Circle", URL="/chapters/ch02/basic-shapes.html#circle"];
     "Arc" [label="Arc", URL="/chapters/ch02/arcs-and-curves.html#arc"];
     "TipableVMobject" [label="TipableVMobject", URL="/chapters/ch02/lines-and-arrows.html#tipablevmobject"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Ellipse" -> "Circle";
     "Circle" -> "Arc";
     "Arc" -> "TipableVMobject";
     "TipableVMobject" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


Square
------

.. autoclass:: manim.Square
   :noindex:


``Square`` 是边长相等的特殊矩形：它把 ``side_length`` 同时作为宽和高传给 ``Rectangle`` 。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Square" [label="Square", URL="/chapters/ch02/basic-shapes.html#square"];
     "Rectangle" [label="Rectangle", URL="/chapters/ch02/basic-shapes.html#rectangle"];
     "Polygon" [label="Polygon", URL="/chapters/ch02/basic-shapes.html#polygon"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Square" -> "Rectangle";
     "Rectangle" -> "Polygon";
     "Polygon" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   Square(side_length: float = 2.0, **kwargs)


矩形家族三兄弟对比：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 维度
        - `Square </chapters/ch02/basic-shapes.html#square>`__
        - `Rectangle </chapters/ch02/basic-shapes.html#rectangle>`__
        - `RoundedRectangle </chapters/ch02/basic-shapes.html#roundedrectangle>`__
      * - 专属参数
        - ``side_length=2.0``
        - ``width=4.0, height=2.0, grid_xstep, grid_ystep``
        - ``corner_radius=0.5`` （支持列表逐角指定）
      * - 外形
        - 正方形
        - 矩形，可画内部网格线
        - 圆角矩形
      * - 继承
        - 三者依次：`Square </chapters/ch02/basic-shapes.html#square>`__ → `Rectangle </chapters/ch02/basic-shapes.html#rectangle>`__ → `Polygon </chapters/ch02/basic-shapes.html#polygon>`__ → `Polygram </chapters/ch02/basic-shapes.html#polygram>`__
        - 
        - 


``Rectangle`` 的 ``grid_xstep`` / ``grid_ystep`` 会在内部画出等距网格线； ``RoundedRectangle`` 的 ``corner_radius`` 传列表时按角分别指定圆角大小。

.. demo:: examples/ch02/rect_family.py RectFamilyDemo

   上排： ``Square`` / ``Rectangle`` / ``RoundedRectangle`` ；下排： ``grid_xstep=grid_ystep=0.8`` 画出的网格矩形。


.. admonition:: 常见错误
   :class: warning

   ``Square(3, 4)`` 想画长方形是行不通的——``Square`` 只接受一个边长参数。长方形请用 ``Rectangle(width=4, height=3)`` 。


Rectangle
---------

.. autoclass:: manim.Rectangle
   :noindex:


``Rectangle`` 是两组对边平行的四边形，默认 4×2 的白色描边框。参数 ``grid_xstep`` / ``grid_ystep`` 可在内部生成网格线。完整参数表与示例见上方 ``Square`` 一节的家族对比与演示。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Rectangle" [label="Rectangle", URL="/chapters/ch02/basic-shapes.html#rectangle"];
     "Polygon" [label="Polygon", URL="/chapters/ch02/basic-shapes.html#polygon"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Rectangle" -> "Polygon";
     "Polygon" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


RoundedRectangle
----------------

.. autoclass:: manim.RoundedRectangle
   :noindex:


``RoundedRectangle`` 在 ``Rectangle`` 基础上把四个角替换为圆弧， ``corner_radius`` 控制圆角大小（也接受逐角列表）。参数与示例见 ``Square`` 一节。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "RoundedRectangle" [label="RoundedRectangle", URL="/chapters/ch02/basic-shapes.html#roundedrectangle"];
     "Rectangle" [label="Rectangle", URL="/chapters/ch02/basic-shapes.html#rectangle"];
     "Polygon" [label="Polygon", URL="/chapters/ch02/basic-shapes.html#polygon"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "RoundedRectangle" -> "Rectangle";
     "Rectangle" -> "Polygon";
     "Polygon" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


Polygon
-------

.. autoclass:: manim.Polygon
   :noindex:


``Polygon`` 是按顶点顺序连接并闭合的多边形，顶点数量任意（≥3）。它继承自 ``Polygram`` ，但只允许 **一组** 顶点，语义上是“一条闭合回路”。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Polygon" [label="Polygon", URL="/chapters/ch02/basic-shapes.html#polygon"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Polygon" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   Polygon(*vertices: Point3DLike, **kwargs)


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``*vertices``
        - `Point3DLike <https://docs.manim.community/en/v0.21.0/reference/manim.typing.html#manim.typing.Point3DLike>`__
        - —
        - 至少 3 个顶点，按顺序相连并首尾闭合
      * - ``kwargs``
        - —
        - —
        - 转发给 `Polygram </chapters/ch02/basic-shapes.html#polygram>`__ ，如 ``color`` 、 ``fill_opacity``


常用方法： ``get_vertices()`` 返回构造时传入的顶点数组，便于再做计算。

多边形家族对比：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 维度
        - `Polygon </chapters/ch02/basic-shapes.html#polygon>`__
        - `RegularPolygon </chapters/ch02/basic-shapes.html#regularpolygon>`__
        - `Triangle </chapters/ch02/basic-shapes.html#triangle>`__
      * - 参数
        - ``*vertices`` （任意顶点）
        - ``n=6`` （边数）
        - 无专属参数
      * - 形状
        - 任意简单多边形
        - n 边正多边形
        - 等边三角形
      * - 顶点方向
        - —
        - 偶数 n 从 0° 起，奇数 n 从 90° 起（顶点朝上）
        - 一个顶点朝上


.. demo:: examples/ch02/polygon_family.py PolygonDemo

   左：手写顶点的任意三角形；中： ``RegularPolygon(n=6)`` （偶数边，平顶朝右）；右： ``Triangle()`` （三边，顶点朝上）。


RegularPolygon
--------------

.. autoclass:: manim.RegularPolygon
   :noindex:


``RegularPolygon`` 是 n 边正多边形，本质是 ``RegularPolygram`` 取 ``density=1`` 。默认边数 6。参数与示例见 ``Polygon`` 一节。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "RegularPolygon" [label="RegularPolygon", URL="/chapters/ch02/basic-shapes.html#regularpolygon"];
     "RegularPolygram" [label="RegularPolygram", URL="/api/geometry.html#regularpolygram"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "RegularPolygon" -> "RegularPolygram";
     "RegularPolygram" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


Triangle
--------

.. autoclass:: manim.Triangle
   :noindex:


``Triangle`` 是无参构造的等边三角形（ ``RegularPolygon(n=3)`` ），一个顶点朝上。参数与示例见 ``Polygon`` 一节。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Triangle" [label="Triangle", URL="/chapters/ch02/basic-shapes.html#triangle"];
     "RegularPolygon" [label="RegularPolygon", URL="/chapters/ch02/basic-shapes.html#regularpolygon"];
     "RegularPolygram" [label="RegularPolygram", URL="/api/geometry.html#regularpolygram"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Triangle" -> "RegularPolygon";
     "RegularPolygon" -> "RegularPolygram";
     "RegularPolygram" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


Polygram
--------

.. autoclass:: manim.Polygram
   :noindex:


``Polygram`` 是广义多边形：接受 **多组** 顶点，每组各自闭合，允许画出互不相连的边（例如蝴蝶结、分离的岛）。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   Polygram(*vertex_groups: Point3DLike_Array, color: ParsableManimColor = "#58C4DD", **kwargs)


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``*vertex_groups``
        - `Point3DLike <https://docs.manim.community/en/v0.21.0/reference/manim.typing.html#manim.typing.Point3DLike>`__ 数组
        - —
        - 每组顶点一个闭合折线，组与组之间不连接
      * - ``color``
        - `ParsableManimColor <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor>`__
        - #58C4DD
        - 默认颜色
      * - ``kwargs``
        - —
        - —
        - 转发给 `VMobject </chapters/ch02/vmobject.html#vmobject>`__


折线图形家族对比：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 维度
        - `Polygram </chapters/ch02/basic-shapes.html#polygram>`__
        - `RegularPolygram </api/geometry.html#regularpolygram>`__
        - `Star </chapters/ch02/basic-shapes.html#star>`__
      * - 参数
        - ``*vertex_groups``
        - ``num_vertices`` 、 ``density=2`` 、 ``radius=1`` 、 ``start_angle=None``
        - ``n=5`` 、 ``outer_radius=1`` 、 ``inner_radius=None`` 、 ``density=2`` 、 ``start_angle=TAU/4``
      * - 顶点排布
        - 手写，可多组
        - 正多边形顶点，按 Schläfli 符号 ``{p/d}`` 连接
        - 内外半径交替，无交叉线
      * - 典型产物
        - 蝴蝶结、分离轮廓
        - 五角星形 {5/2}、六芒星 {6/2}
        - 实心五角星


``RegularPolygram`` 的 ``density`` 表示“每隔几个顶点连一条线”： ``{5/2}`` 是五角星， ``{6/2}`` 因 6 与 2 不互质而化为两个叠加的三角形（六芒星）。 ``Star`` 的 ``inner_radius`` 不指定时按 ``density`` 自动计算，使星形比例匀称。

.. demo:: examples/ch02/polygram_star.py PolygramDemo

   左： ``Polygram`` 两组顶点画出的蝴蝶结；中： ``RegularPolygram(num_vertices=6, density=2)`` 六芒星；右： ``Star(n=5, fill_opacity=0.5)`` 。


RegularPolygram
---------------

.. autoclass:: manim.RegularPolygram
   :noindex:


``RegularPolygram`` 按顶点数与密度生成规则折线图形（Schläfli 符号 ``{num_vertices/density}`` ）。参数与示例见 ``Polygram`` 一节的家族对比与演示。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "RegularPolygram" [label="RegularPolygram", URL="/api/geometry.html#regularpolygram"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "RegularPolygram" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


Star
----

.. autoclass:: manim.Star
   :noindex:


``Star`` 是特殊的 ``Polygon`` ：内外半径交替取顶点，画出 **没有交叉线** 的 n 角星，默认五角星且一个角朝上。参数与示例见 ``Polygram`` 一节。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Star" [label="Star", URL="/chapters/ch02/basic-shapes.html#star"];
     "Polygon" [label="Polygon", URL="/chapters/ch02/basic-shapes.html#polygon"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Star" -> "Polygon";
     "Polygon" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


ConvexHull
----------

.. autoclass:: manim.ConvexHull
   :noindex:


``ConvexHull`` 接收一堆无序点，用 quickhull 算法求出它们的 **凸包多边形**——包住所有点的最小凸形状。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "ConvexHull" [label="ConvexHull", URL="/chapters/ch02/boolean-ops.html#convexhull"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "ConvexHull" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   ConvexHull(*points: Point3DLike, tolerance: float = 1e-5, **kwargs)


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``*points``
        - `Point3DLike <https://docs.manim.community/en/v0.21.0/reference/manim.typing.html#manim.typing.Point3DLike>`__
        - —
        - 参与计算的点（至少 3 个不共线的点）
      * - ``tolerance``
        - float
        - 1e-5
        - quickhull 算法的容差


与 ``Cutout`` 的对比——二者都“基于已有形状生成新形状”，但方向相反：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 维度
        - `ConvexHull </chapters/ch02/boolean-ops.html#convexhull>`__
        - `Cutout </chapters/ch02/boolean-ops.html#cutout>`__
      * - 输入
        - 点集
        - 一个主形状 + 若干洞形状
      * - 输出
        - 包住所有点的凸多边形
        - 主形状被挖洞后的轮廓
      * - 继承
        - `Polygram </chapters/ch02/basic-shapes.html#polygram>`__
        - `VMobject </chapters/ch02/vmobject.html#vmobject>`__


.. demo:: examples/ch02/hull_cutout.py HullCutoutDemo

   上方：4 个散点的 ``ConvexHull`` 外包多边形；下方： ``Cutout(Square, Circle)`` 方块被圆挖去一块。


.. admonition:: 常见错误
   :class: warning

   ``ConvexHull`` 只接受 **点** （坐标三元组），传 mobject 会按坐标数组处理并可能报错或得到奇怪结果；请先取 ``mob.get_center()`` 等坐标再传入。


Cutout
------

.. autoclass:: manim.Cutout
   :noindex:


``Cutout`` 在一个主形状上挖出若干洞：把洞形状的环绕方向反转后拼接进主形状的点序列，利用环绕方向差异让填充在洞区域“镂空”。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Cutout" [label="Cutout", URL="/chapters/ch02/boolean-ops.html#cutout"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Cutout" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   Cutout(main_shape: VMobject, *mobjects: VMobject, **kwargs)


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``main_shape``
        - `VMobject </chapters/ch02/vmobject.html#vmobject>`__
        - —
        - 被挖洞的主形状（必填）
      * - ``*mobjects``
        - `VMobject </chapters/ch02/vmobject.html#vmobject>`__
        - —
        - 要挖掉的洞形状，可多个
      * - ``kwargs``
        - —
        - —
        - 转发给 `VMobject </chapters/ch02/vmobject.html#vmobject>`__ ，如 ``color`` 、 ``fill_opacity``


.. admonition:: 常见错误
   :class: warning

   ``Cutout`` 只影响 **填充** ：洞内的描边不会被挖掉，主形状的外轮廓线仍然完整。需要真正删除路径请使用布尔运算章节（ ``Union`` / ``Difference`` / ``Intersection`` / ``Exclusion`` ）。


自测
----


.. dropdown:: ✏️ 练习

   画一个“顶点朝上”的五边形和一个“一条边朝上”的六边形，分别怎么构造？

   .. dropdown:: ✅ 参考答案

      奇数边正多边形默认顶点朝上： ``RegularPolygon(n=5)`` 。偶数边默认从 0° 开始（一条边跨在顶部两侧）， ``RegularPolygon(n=6)`` 即符合要求；想精确控制方向时可传 ``start_angle=TAU / 4`` 。


.. dropdown:: ✏️ 练习

   ``Polygram`` 与 ``Polygon`` 是什么关系？什么场景必须用 ``Polygram`` ？

   .. dropdown:: ✅ 参考答案

      ``Polygon`` 继承自 ``Polygram`` ，只能接收一组顶点（一个闭合回路）； ``Polygram`` 接收多组顶点，每组独立闭合。需要一次画出互不相连的多段轮廓（如蝴蝶结、两个分离的三角形）时只能用 ``Polygram`` 。



ScreenRectangle
---------------

.. autoclass:: manim.ScreenRectangle
   :noindex:


``ScreenRectangle`` 是一个长宽比固定为屏幕比例（默认 16:9）的矩形，默认高度 4。常用来标注“安全区域”、模拟屏幕/画框，或作为视频叠加层的占位参照。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "ScreenRectangle" [label="ScreenRectangle", URL="/chapters/ch02/basic-shapes.html#screenrectangle"];
     "Rectangle" [label="Rectangle", URL="/chapters/ch02/basic-shapes.html#rectangle"];
     "Polygon" [label="Polygon", URL="/chapters/ch02/basic-shapes.html#polygon"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "ScreenRectangle" -> "Rectangle";
     "Rectangle" -> "Polygon";
     "Polygon" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``aspect_ratio``
        - float
        - 16/9
        - 宽除以高；传 1 即正方形
        - ``height``
        - float
        - 4
        - 矩形高度，宽度随之确定
FullScreenRectangle
-------------------

.. autoclass:: manim.FullScreenRectangle
   :noindex:


``FullScreenRectangle`` 恰好铺满整个画面（高度等于 ``FRAME_HEIGHT`` 8 个单位），是制作背景色块、遮罩、转场底色的首选：给它一个填充色并 ``fade_in`` / ``fade_out``，就是最常用的场景过渡手法。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "FullScreenRectangle" [label="FullScreenRectangle", URL="/chapters/ch02/basic-shapes.html#fullscreenrectangle"];
     "ScreenRectangle" [label="ScreenRectangle", URL="/chapters/ch02/basic-shapes.html#screenrectangle"];
     "Rectangle" [label="Rectangle", URL="/chapters/ch02/basic-shapes.html#rectangle"];
     "Polygon" [label="Polygon", URL="/chapters/ch02/basic-shapes.html#polygon"];
     "Polygram" [label="Polygram", URL="/chapters/ch02/basic-shapes.html#polygram"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "FullScreenRectangle" -> "ScreenRectangle";
     "ScreenRectangle" -> "Rectangle";
     "Rectangle" -> "Polygon";
     "Polygon" -> "Polygram";
     "Polygram" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   # 经典转场：黑幕落下再抬起
   curtain = FullScreenRectangle(fill_color=BLACK, fill_opacity=1)
   self.play(FadeIn(curtain), run_time=0.5)   # 黑幕落下
   self.play(FadeOut(curtain), run_time=0.5)  # 黑幕抬起

下一步
------


形状齐备后，下一节处理更小的东西： ``Dot`` 、 ``Point`` 与整片点云。
