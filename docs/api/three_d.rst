=============================
API 参考：三维对象（three_d）
=============================

共 **17** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

Arrow3D
-------

三维箭头：空间中的方向向量表示。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Surface";
     "Surface" -> "Cylinder";
     "Cylinder" -> "Line3D";
     "Line3D" -> "Arrow3D";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``start``
        - array([-1.,  0.,  0.])，Point3DLike
      * - ``end``
        - array([1., 0., 0.])，Point3DLike
      * - ``thickness``
        - 0.02，float
      * - ``height``
        - 0.3，float
      * - ``base_radius``
        - 0.08，float
      * - ``color``
        - ManimColor('#FFFFFF')，ParsableManimColor
      * - ``resolution``
        - 24，int | tuple[int, int]

快速上手
~~~~~~~~

.. code-block:: python

   a3 = Arrow3D(ORIGIN, [1, 1, 1])

API 文档
~~~~~~~~

.. autoclass:: manim.Arrow3D

Cone
----

圆锥体：底面半径 + 高度，3D 几何基本体。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Surface";
     "Surface" -> "Cone";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``base_radius``
        - 1，float
      * - ``height``
        - 1，float
      * - ``direction``
        - array([0., 0., 1.])，Vector3DLike
      * - ``show_base``
        - False，bool
      * - ``v_range``
        - (0, 6.283185307179586)，tuple[float, float]
      * - ``u_min``
        - 0，float
      * - ``checkerboard_colors``
        - False

快速上手
~~~~~~~~

.. code-block:: python

   cone = Cone(direction=Z_AXIS)

API 文档
~~~~~~~~

.. autoclass:: manim.Cone

ConvexHull3D
------------

三维点集的凸包多面体，计算几何 3D 版。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Polyhedron";
     "Polyhedron" -> "ConvexHull3D";
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

.. autoclass:: manim.ConvexHull3D

Cube
----

立方体：边长指定，可显示面与棱，3D 入门第一件。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Cube";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``side_length``
        - 2，float
      * - ``fill_opacity``
        - 0.75，float
      * - ``fill_color``
        - ManimColor('#58C4DD')，ParsableManimColor
      * - ``stroke_width``
        - 0，float

快速上手
~~~~~~~~

.. code-block:: python

   cube = Cube(side_length=2)

API 文档
~~~~~~~~

.. autoclass:: manim.Cube

Cylinder
--------

圆柱体：半径 + 高度。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Surface";
     "Surface" -> "Cylinder";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``radius``
        - 1，float
      * - ``height``
        - 2，float
      * - ``direction``
        - array([0., 0., 1.])，Vector3DLike
      * - ``v_range``
        - (0, 6.283185307179586)，tuple[float, float]
      * - ``show_ends``
        - True，bool
      * - ``resolution``
        - (24, 24)，int | tuple[int, int]

快速上手
~~~~~~~~

.. code-block:: python

   cyl = Cylinder(radius=1, height=2)

API 文档
~~~~~~~~

.. autoclass:: manim.Cylinder

Dodecahedron
------------

十二面体：12 个五边形面的正多面体，Polyhedron 的预制实例。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Polyhedron";
     "Polyhedron" -> "Dodecahedron";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``edge_length``
        - 1，float

API 文档
~~~~~~~~

.. autoclass:: manim.Dodecahedron

Dot3D
-----

三维空间中的小圆点：标记空间坐标用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Surface";
     "Surface" -> "Sphere";
     "Sphere" -> "Dot3D";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``point``
        - array([0., 0., 0.])，Point3D
      * - ``radius``
        - 0.08，float
      * - ``color``
        - ManimColor('#FFFFFF')，ParsableManimColor
      * - ``resolution``
        - (8, 8)

API 文档
~~~~~~~~

.. autoclass:: manim.Dot3D

Icosahedron
-----------

二十面体：20 个三角面的正多面体。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Polyhedron";
     "Polyhedron" -> "Icosahedron";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``edge_length``
        - 1，float

API 文档
~~~~~~~~

.. autoclass:: manim.Icosahedron

Line3D
------

空间直线：两点连线，3D 构图骨架。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Surface";
     "Surface" -> "Cylinder";
     "Cylinder" -> "Line3D";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``start``
        - array([-1.,  0.,  0.])，Point3DLike
      * - ``end``
        - array([1., 0., 0.])，Point3DLike
      * - ``thickness``
        - 0.02，float
      * - ``color``
        - None
      * - ``resolution``
        - 24，int | tuple[int, int]

快速上手
~~~~~~~~

.. code-block:: python

   l3 = Line3D(ORIGIN, [2, 2, 2])

API 文档
~~~~~~~~

.. autoclass:: manim.Line3D

Octahedron
----------

八面体：8 个三角面的正多面体。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Polyhedron";
     "Polyhedron" -> "Octahedron";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``edge_length``
        - 1，float

API 文档
~~~~~~~~

.. autoclass:: manim.Octahedron

Polyhedron
----------

通用多面体：顶点列表 + 面列表定义任意凸多面体，正多面体家族由此派生。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Polyhedron";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vertex_coords``
        - —，Point3DLike_Array
      * - ``faces_list``
        - —，list[list[int]]
      * - ``faces_config``
        - {}
      * - ``graph_config``
        - {}，dict[str, Any]

API 文档
~~~~~~~~

.. autoclass:: manim.Polyhedron

Prism
-----

棱柱：正多边形底面沿法向拉伸而成。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Cube";
     "Cube" -> "Prism";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``dimensions``
        - [3, 2, 1]，Vector3DLike

API 文档
~~~~~~~~

.. autoclass:: manim.Prism

Sphere
------

球体：半径指定，可设分辨率，3D 最常用实体。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Surface";
     "Surface" -> "Sphere";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``center``
        - array([0., 0., 0.])，Point3DLike
      * - ``radius``
        - 1，float
      * - ``resolution``
        - None
      * - ``u_range``
        - (0, 6.283185307179586)，tuple[float, float]
      * - ``v_range``
        - (0, 3.141592653589793)，tuple[float, float]

快速上手
~~~~~~~~

.. code-block:: python

   s = Sphere(radius=2, resolution=(24, 24))

API 文档
~~~~~~~~

.. autoclass:: manim.Sphere

Surface
-------

参数化曲面：uv 网格生成任意曲面，如抛物面，3D 函数可视化核心。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Surface";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``func``
        - —
      * - ``u_range``
        - (0, 1)，tuple[float, float]
      * - ``v_range``
        - (0, 1)，tuple[float, float]
      * - ``resolution``
        - 32，int | Sequence[int]
      * - ``surface_piece_config``
        - {}，dict
      * - ``fill_color``
        - ManimColor('#29ABCA')，ParsableManimColor
      * - ``fill_opacity``
        - 1.0，float
      * - ``checkerboard_colors``
        - [ManimColor('#29ABCA'), Man…
      * - ``stroke_color``
        - ManimColor('#BBBBBB')，ParsableManimColor
      * - ``stroke_width``
        - 0.5，float
      * - ``should_make_jagged``
        - False，bool
      * - ``pre_function_handle_to_anchor_scale_factor``
        - 1e-05，float

快速上手
~~~~~~~~

.. code-block:: python

   surf = Surface(lambda u, v: [u, v, u*u + v*v], u_range=[-1, 1], v_range=[-1, 1])

API 文档
~~~~~~~~

.. autoclass:: manim.Surface

Tetrahedron
-----------

四面体：4 个三角面的正多面体。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Polyhedron";
     "Polyhedron" -> "Tetrahedron";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``edge_length``
        - 1，float

API 文档
~~~~~~~~

.. autoclass:: manim.Tetrahedron

ThreeDVMobject
--------------

三维矢量对象基类：兼容 2D 渲染的 3D 图形祖先。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "ThreeDVMobject";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``shade_in_3d``
        - True，bool

API 文档
~~~~~~~~

.. autoclass:: manim.ThreeDVMobject

Torus
-----

圆环体（救生圈面）：主半径 + 管半径。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Surface";
     "Surface" -> "Torus";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``major_radius``
        - 3，float
      * - ``minor_radius``
        - 1，float
      * - ``u_range``
        - (0, 6.283185307179586)，tuple[float, float]
      * - ``v_range``
        - (0, 6.283185307179586)，tuple[float, float]
      * - ``resolution``
        - None

快速上手
~~~~~~~~

.. code-block:: python

   t = Torus(major_radius=2, minor_radius=0.5)

API 文档
~~~~~~~~

.. autoclass:: manim.Torus
