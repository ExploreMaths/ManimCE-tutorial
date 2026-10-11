=======================
API 参考：场景（scene）
=======================

共 **10** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

DefaultSectionType
------------------

章节类型枚举：normal/skip/speedup，控制分节导出时该节的处理方式。

API 文档
~~~~~~~~

.. autoclass:: manim.DefaultSectionType

LinearTransformationScene
-------------------------

线性变换演示场景：自带基向量网格与 apply_matrix 快捷方法，线代可视化开箱即用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Scene" -> "VectorScene";
     "VectorScene" -> "LinearTransformationScene";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``include_background_plane``
        - True，bool
      * - ``include_foreground_plane``
        - True，bool
      * - ``background_plane_kwargs``
        - None，dict[str, Any] | None
      * - ``foreground_plane_kwargs``
        - None，dict[str, Any] | None
      * - ``show_coordinates``
        - False，bool
      * - ``show_basis_vectors``
        - True，bool
      * - ``basis_vector_stroke_width``
        - 6，float
      * - ``i_hat_color``
        - ManimColor('#83C167')，ParsableManimColor
      * - ``j_hat_color``
        - ManimColor('#FC6255')，ParsableManimColor
      * - ``leave_ghost_vectors``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   class Demo(LinearTransformationScene):
       def construct(self):
           self.apply_matrix([[1, 1], [0, 1]])

API 文档
~~~~~~~~

.. autoclass:: manim.LinearTransformationScene

MovingCameraScene
-----------------

镜头运动场景：self.camera.frame 自由推拉摇移，适合走遍整张图的讲解。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Scene" -> "MovingCameraScene";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``camera_class``
        - <class 'manim.camera.moving…，type[Camera]

快速上手
~~~~~~~~

.. code-block:: python

   self.play(self.camera.frame.animate.scale(0.5).shift(RIGHT))

API 文档
~~~~~~~~

.. autoclass:: manim.MovingCameraScene

Scene
-----

场景基类：一切动画的主入口。construct() 里用 add/play 编排，掌握 Scene 就掌握了 Manim 的导演椅。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``renderer``
        - None
      * - ``camera_class``
        - <class 'manim.camera.camera…，type[Camera]
      * - ``always_update_mobjects``
        - False，bool
      * - ``random_seed``
        - None，int | None
      * - ``skip_animations``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   class Demo(Scene):
       def construct(self):
           self.play(Write(Text("Hello")))

API 文档
~~~~~~~~

.. autoclass:: manim.Scene

SceneFileWriter
---------------

负责把场景帧编码输出为视频/图片文件：分辨率、帧率、分段导出都由它落盘。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``renderer``
        - —
      * - ``scene_name``
        - —，str

API 文档
~~~~~~~~

.. autoclass:: manim.SceneFileWriter

Section
-------

场景分节：把 construct 切成带类型的片段，配合 CLI 可导出分节视频清单。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``type_``
        - —，str
      * - ``video``
        - —，str | None
      * - ``name``
        - —，str
      * - ``skip_animations``
        - —，bool

API 文档
~~~~~~~~

.. autoclass:: manim.Section

SpecialThreeDScene
------------------

固定相机参数的三维演示场景：低多边形默认配置，快速出 3D 效果。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Scene" -> "ThreeDScene";
     "ThreeDScene" -> "SpecialThreeDScene";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``cut_axes_at_radius``
        - True
      * - ``camera_config``
        - {'should_apply_shading': Tr…
      * - ``three_d_axes_config``
        - {'num_axis_pieces': 1, 'axi…
      * - ``sphere_config``
        - {'radius': 2, 'resolution':…
      * - ``default_angled_camera_position``
        - {'phi': 1.2217304763960306,…
      * - ``low_quality_config``
        - {'camera_config': {'should_…

API 文档
~~~~~~~~

.. autoclass:: manim.SpecialThreeDScene

ThreeDScene
-----------

三维场景：自带相机朝向设置与 3D 动画辅助（如球面移动），3D 内容入口。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Scene" -> "ThreeDScene";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``camera_class``
        - <class 'manim.camera.three_…
      * - ``ambient_camera_rotation``
        - None
      * - ``default_angled_camera_orientation_kwargs``
        - None

快速上手
~~~~~~~~

.. code-block:: python

   class Demo(ThreeDScene):
       def construct(self):
           self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
           self.play(Create(Sphere()))

API 文档
~~~~~~~~

.. autoclass:: manim.ThreeDScene

VectorScene
-----------

向量演示场景：坐标系 + 向量工具方法，线性代数课场景。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Scene" -> "VectorScene";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``basis_vector_stroke_width``
        - 6.0，float

API 文档
~~~~~~~~

.. autoclass:: manim.VectorScene

ZoomedScene
-----------

局部放大场景：自带放大镜窗口，主画面 + 缩放插页同时呈现细节。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Scene" -> "MovingCameraScene";
     "MovingCameraScene" -> "ZoomedScene";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``camera_class``
        - <class 'manim.camera.multi_…，type[Camera]
      * - ``zoomed_display_height``
        - 3，float
      * - ``zoomed_display_width``
        - 3，float
      * - ``zoomed_display_center``
        - None，Point3DLike | None
      * - ``zoomed_display_corner``
        - array([1., 1., 0.])，Vector3D
      * - ``zoomed_display_corner_buff``
        - 0.5，float
      * - ``zoomed_camera_config``
        - {'default_frame_stroke_widt…，dict[str, Any]
      * - ``zoomed_camera_image_mobject_config``
        - {}，dict[str, Any]
      * - ``zoomed_camera_frame_starting_position``
        - array([0., 0., 0.])，Point3DLike
      * - ``zoom_factor``
        - 0.15，float
      * - ``image_frame_stroke_width``
        - 3，float
      * - ``zoom_activated``
        - False，bool

API 文档
~~~~~~~~

.. autoclass:: manim.ZoomedScene
