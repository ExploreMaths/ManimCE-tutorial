===================================
API 参考：Mobject 基类类型（types）
===================================

共 **14** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

CurvesAsSubmobjects
-------------------

把多段曲线拆成独立子对象的 VMobject 容器，方便对每一段单独上色或动画。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "CurvesAsSubmobjects";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vmobject``
        - —，VMobject

API 文档
~~~~~~~~

.. autoclass:: manim.CurvesAsSubmobjects

DashedVMobject
--------------

把任意 VMobject 变成虚线版：dash_length 与间距可调，常用来表示辅助线或预期位置。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "DashedVMobject";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vmobject``
        - —，VMobject
      * - ``num_dashes``
        - 15，int
      * - ``dashed_ratio``
        - 0.5，float
      * - ``dash_offset``
        - 0，float
      * - ``color``
        - ManimColor('#FFFFFF')，ManimColor
      * - ``equal_lengths``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   dashed = DashedVMobject(circle)

API 文档
~~~~~~~~

.. autoclass:: manim.DashedVMobject

ImageMobject
------------

把本地图片文件（PNG/JPG）作为 Mobject 摆进画面，可缩放、旋转、裁剪。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "ImageMobject";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``filename_or_array``
        - —，StrPath | npt.NDArray
      * - ``scale_to_resolution``
        - 1080，int
      * - ``invert``
        - False，bool
      * - ``image_mode``
        - 'RGBA'，str

快速上手
~~~~~~~~

.. code-block:: python

   img = ImageMobject("photo.png").scale(2)

API 文档
~~~~~~~~

.. autoclass:: manim.ImageMobject

ImageMobjectFromCamera
----------------------

捕获另一个相机画面作为图像的 Mobject，用于画中画或场景缩略预览。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "ImageMobjectFromCamera";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``camera``
        - —，MovingCamera
      * - ``default_display_frame_config``
        - None，dict[str, Any] | None

API 文档
~~~~~~~~

.. autoclass:: manim.ImageMobjectFromCamera

Mobject1D
---------

一维对象基类（v0.21 标记为内部实验类型），普通教程较少直接使用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "PMobject";
     "PMobject" -> "Mobject1D";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``density``
        - 10，int

API 文档
~~~~~~~~

.. autoclass:: manim.Mobject1D

Mobject2D
---------

二维对象基类（内部实验类型），面片类对象的祖先。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "PMobject";
     "PMobject" -> "Mobject2D";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``density``
        - 25，int

API 文档
~~~~~~~~

.. autoclass:: manim.Mobject2D

PGroup
------

PMobject 的专用容器：把点集对象分组统一管理。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "PMobject";
     "PMobject" -> "PGroup";
   }

API 文档
~~~~~~~~

.. autoclass:: manim.PGroup

PMobject
--------

点云式 Mobject：只含离散点、无填充笔画，是 DotCloud 等实验性渲染类型的基类。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "PMobject";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``stroke_width``
        - 4，int

API 文档
~~~~~~~~

.. autoclass:: manim.PMobject

Point
-----

表示坐标点的轻量 Mobject：不渲染任何可见图形，只承载位置，常作动画的锚点参数。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "PMobject";
     "PMobject" -> "Point";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``location``
        - array([0., 0., 0.])，Point3DLike
      * - ``color``
        - ManimColor('#000000')，ManimColor

快速上手
~~~~~~~~

.. code-block:: python

   self.play(GrowFromPoint(mob, Point().get_center()))

API 文档
~~~~~~~~

.. autoclass:: manim.Point

PointCloudDot
-------------

把点集渲染成一群小圆点的 PMobject 显示形式，适合散点可视化。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "PMobject";
     "PMobject" -> "Mobject1D";
     "Mobject1D" -> "PointCloudDot";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``center``
        - array([0., 0., 0.])，Point3DLike
      * - ``radius``
        - 2.0，float
      * - ``stroke_width``
        - 2，int
      * - ``density``
        - 10，int
      * - ``color``
        - ManimColor('#FFFF00')，ManimColor

API 文档
~~~~~~~~

.. autoclass:: manim.PointCloudDot

VDict
-----

「键值对版 VGroup」：按键名索引子对象，方便在公式字典里做局部替换。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VDict";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mapping_or_iterable``
        - {}
      * - ``show_keys``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   d = VDict({"a": MathTex("x^2"), "b": MathTex("y^2")})

API 文档
~~~~~~~~

.. autoclass:: manim.VDict

VGroup
------

VMobject 专用容器：子对象都是 VMobject，可使用只有矢量对象才有的整体方法（如 set_stroke），是日常最常用组合器。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
   }

快速上手
~~~~~~~~

.. code-block:: python

   vg = VGroup(circle, square, dot)
   vg.arrange(RIGHT)

API 文档
~~~~~~~~

.. autoclass:: manim.VGroup

VMobject
--------

矢量对象基类：一切「用路径曲线定义」的图形（圆、线、文字）都继承它。set_stroke/set_fill、贝塞尔操作都从这里来。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``fill_color``
        - None
      * - ``fill_opacity``
        - 0.0，float
      * - ``stroke_color``
        - None
      * - ``stroke_opacity``
        - 1.0，float
      * - ``stroke_width``
        - 4，float
      * - ``background_stroke_color``
        - ManimColor('#000000')
      * - ``background_stroke_opacity``
        - 1.0，float
      * - ``background_stroke_width``
        - 0，float
      * - ``sheen_factor``
        - 0.0，float
      * - ``joint_type``
        - None，LineJointType | None
      * - ``sheen_direction``
        - array([-1.,  1.,  0.])，Vector3DLike
      * - ``close_new_points``
        - False，bool
      * - ``pre_function_handle_to_anchor_scale_factor``
        - 0.01，float
      * - ``make_smooth_after_applying_functions``
        - False，bool
      * - ``background_image``
        - None，Image | str | None
      * - ``shade_in_3d``
        - False，bool
      * - ``tolerance_for_point_equality``
        - 1e-06，float
      * - ``n_points_per_cubic_curve``
        - 4，int
      * - ``cap_style``
        - <CapStyleType.AUTO: 0>，CapStyleType

快速上手
~~~~~~~~

.. code-block:: python

   vm = VMobject()
   vm.set_points_as_corners([ORIGIN, RIGHT, UP])

API 文档
~~~~~~~~

.. autoclass:: manim.VMobject

VectorizedPoint
---------------

带矢量渲染能力的点对象（Point 的 VMobject 版本），内部实验用途居多。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VectorizedPoint";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``location``
        - array([0., 0., 0.])，Point3DLike
      * - ``color``
        - ManimColor('#000000')，ManimColor
      * - ``fill_opacity``
        - 0，float
      * - ``stroke_width``
        - 0，float
      * - ``artificial_width``
        - 0.01，float
      * - ``artificial_height``
        - 0.01，float

API 文档
~~~~~~~~

.. autoclass:: manim.VectorizedPoint
