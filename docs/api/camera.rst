==========================
API 参考：摄像机（camera）
==========================

共 **8** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

BackgroundColoredVMobjectDisplayer
----------------------------------

把 VMobject 按背景色反色显示的辅助相机组件，内部机制居多。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``camera``
        - —，Camera

API 文档
~~~~~~~~

.. autoclass:: manim.BackgroundColoredVMobjectDisplayer

Camera
------

相机基类：管理画面帧、像素坐标与 Mobject 的投影，所有渲染都从它开始。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``background_image``
        - None，str | None
      * - ``frame_center``
        - array([0., 0., 0.])，Point3D
      * - ``image_mode``
        - 'RGBA'，str
      * - ``n_channels``
        - 4，int
      * - ``pixel_array_dtype``
        - 'uint8'，str
      * - ``cairo_line_width_multiple``
        - 0.01，float
      * - ``use_z_index``
        - True，bool
      * - ``background``
        - None，PixelArray | None
      * - ``pixel_height``
        - None，int | None
      * - ``pixel_width``
        - None，int | None
      * - ``frame_height``
        - None，float | None
      * - ``frame_width``
        - None，float | None
      * - ``frame_rate``
        - None，float | None
      * - ``background_color``
        - None
      * - ``background_opacity``
        - None，float | None

快速上手
~~~~~~~~

.. code-block:: python

   self.camera.frame.set(width=10)

API 文档
~~~~~~~~

.. autoclass:: manim.Camera

MappingCamera
-------------

映射相机：局部应用变换映射后拍摄，做放大镜视窗用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Camera" -> "MappingCamera";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mapping_func``
        - <function MappingCamera.<la…
      * - ``min_num_curves``
        - 50
      * - ``allow_object_intrusion``
        - False

API 文档
~~~~~~~~

.. autoclass:: manim.MappingCamera

MovingCamera
------------

可移动相机：帧可随 updater 平移/缩放/旋转，是 MovingCameraScene 的底层。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Camera" -> "MovingCamera";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``frame``
        - None，Mobject | None
      * - ``fixed_dimension``
        - 0，int
      * - ``default_frame_stroke_color``
        - ManimColor('#FFFFFF')，ManimColor
      * - ``default_frame_stroke_width``
        - 0，int

API 文档
~~~~~~~~

.. autoclass:: manim.MovingCamera

MultiCamera
-----------

多相机合成：把多个相机画面按子矩形拼到一个画面里。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Camera" -> "MovingCamera";
     "MovingCamera" -> "MultiCamera";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``image_mobjects_from_cameras``
        - None
      * - ``allow_cameras_to_capture_their_own_display``
        - False，bool

API 文档
~~~~~~~~

.. autoclass:: manim.MultiCamera

OldMultiCamera
--------------

旧版多相机实现，已被 MultiCamera 取代，仅作兼容保留。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Camera" -> "OldMultiCamera";
   }

API 文档
~~~~~~~~

.. autoclass:: manim.OldMultiCamera

SplitScreenCamera
-----------------

分屏相机：左右分屏显示两个画面，对比演示可用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Camera" -> "OldMultiCamera";
     "OldMultiCamera" -> "SplitScreenCamera";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``left_camera``
        - —
      * - ``right_camera``
        - —

API 文档
~~~~~~~~

.. autoclass:: manim.SplitScreenCamera

ThreeDCamera
------------

三维相机：管理 phi/theta/gamma 视角参数与三维投影，ThreeDScene 的渲染核心。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Camera" -> "ThreeDCamera";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``focal_distance``
        - 20.0，float
      * - ``shading_factor``
        - 0.2，float
      * - ``default_distance``
        - 5.0，float
      * - ``light_source_start_point``
        - array([-7., -9., 10.])，Point3DLike
      * - ``should_apply_shading``
        - True，bool
      * - ``exponential_projection``
        - False，bool
      * - ``phi``
        - 0，float
      * - ``theta``
        - -1.5707963267948966，float
      * - ``gamma``
        - 0，float
      * - ``zoom``
        - 1，float

快速上手
~~~~~~~~

.. code-block:: python

   self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)

API 文档
~~~~~~~~

.. autoclass:: manim.ThreeDCamera
