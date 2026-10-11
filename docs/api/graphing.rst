================================
API 参考：图表与坐标（graphing）
================================

共 **15** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

Axes
----

平面直角坐标系：x/y 轴 + 刻度 + 可扩展的坐标转换（c2p/p2c），函数绘图的主舞台。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "CoordinateSystem" -> "Mobject";
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Axes";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``x_range``
        - None，Sequence[float] | None
      * - ``y_range``
        - None，Sequence[float] | None
      * - ``x_length``
        - 12，float | None
      * - ``y_length``
        - 6，float | None
      * - ``axis_config``
        - None，dict | None
      * - ``x_axis_config``
        - None，dict | None
      * - ``y_axis_config``
        - None，dict | None
      * - ``tips``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   axes = Axes(x_range=[-3, 3], y_range=[-2, 2])
   self.add(axes)
   self.play(Create(axes.plot(lambda x: x**2)))

API 文档
~~~~~~~~

.. autoclass:: manim.Axes

BarChart
--------

柱状图：数值列表一键成图，柱色、标签、方向全能调，数据可视化入门件。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "CoordinateSystem" -> "Mobject";
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Axes";
     "Axes" -> "BarChart";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``values``
        - —，MutableSequence[float]
      * - ``bar_names``
        - None，Sequence[str] | None
      * - ``y_range``
        - None，Sequence[float] | None
      * - ``x_length``
        - None，float | None
      * - ``y_length``
        - None，float | None
      * - ``bar_colors``
        - ['#003f5c', '#58508d', '#bc…，Iterable[str]
      * - ``bar_width``
        - 0.6，float
      * - ``bar_fill_opacity``
        - 0.7，float
      * - ``bar_stroke_width``
        - 3，float

快速上手
~~~~~~~~

.. code-block:: python

   chart = BarChart(values=[3, 1, 4, 1, 5])

API 文档
~~~~~~~~

.. autoclass:: manim.BarChart

ComplexPlane
------------

复平面：实轴 + 虚轴 + 复数标注，复变函数可视化的坐标底图。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "CoordinateSystem" -> "Mobject";
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Axes";
     "Axes" -> "NumberPlane";
     "NumberPlane" -> "ComplexPlane";
   }

快速上手
~~~~~~~~

.. code-block:: python

   plane = ComplexPlane()

API 文档
~~~~~~~~

.. autoclass:: manim.ComplexPlane

CoordinateSystem
----------------

一切坐标系（Axes、NumberLine、PolarPlane 等）的基类：统一提供 c2p/p2c 坐标变换与 get_graph 等接口。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``x_range``
        - None，Sequence[float] | None
      * - ``y_range``
        - None，Sequence[float] | None
      * - ``x_length``
        - None，float | None
      * - ``y_length``
        - None，float | None
      * - ``dimension``
        - 2，int

API 文档
~~~~~~~~

.. autoclass:: manim.CoordinateSystem

FunctionGraph
-------------

函数图像对象：给定 f(x) 自动生成曲线，配合 Axes 使用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "ParametricFunction";
     "ParametricFunction" -> "FunctionGraph";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``function``
        - —，Callable[[float], Any]
      * - ``x_range``
        - None
      * - ``color``
        - ManimColor('#FFFF00')，ParsableManimColor

快速上手
~~~~~~~~

.. code-block:: python

   graph = axes.plot(lambda x: np.sin(x))

API 文档
~~~~~~~~

.. autoclass:: manim.FunctionGraph

ImplicitFunction
----------------

隐函数图像：给定 F(x, y)=0 用采样方式画出曲线，如圆锥曲线。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "ImplicitFunction";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``func``
        - —
      * - ``x_range``
        - None，Sequence[float] | None
      * - ``y_range``
        - None，Sequence[float] | None
      * - ``min_depth``
        - 5，int
      * - ``max_quads``
        - 1500，int
      * - ``use_smoothing``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   imp = ImplicitFunction(lambda x, y: x**2 + y**2 - 4)

API 文档
~~~~~~~~

.. autoclass:: manim.ImplicitFunction

LinearBase
----------

线性刻度轴的刻度策略类：刻度等距分布，Axes 默认使用。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``scale_factor``
        - 1.0，float

API 文档
~~~~~~~~

.. autoclass:: manim.LinearBase

LogBase
-------

对数刻度轴的刻度策略类：数值按对数分布，画数量级差异大的数据用。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``base``
        - 10，float
      * - ``custom_labels``
        - True，bool

API 文档
~~~~~~~~

.. autoclass:: manim.LogBase

NumberLine
----------

一维数轴：范围、步长、刻度标签、单位长度全可配，数值可视化的地基。

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
     "Line" -> "NumberLine";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``x_range``
        - None，Sequence[float] | None
      * - ``length``
        - None，float | None
      * - ``unit_size``
        - 1，float
      * - ``include_ticks``
        - True，bool
      * - ``tick_size``
        - 0.1，float
      * - ``numbers_with_elongated_ticks``
        - None，Iterable[float] | None
      * - ``longer_tick_multiple``
        - 2，int
      * - ``exclude_origin_tick``
        - False，bool
      * - ``rotation``
        - 0，float
      * - ``stroke_width``
        - 2.0，float
      * - ``include_tip``
        - False，bool
      * - ``tip_width``
        - 0.35，float
      * - ``tip_height``
        - 0.35，float
      * - ``tip_shape``
        - None，type[ArrowTip] | None
      * - ``include_numbers``
        - False，bool
      * - ``font_size``
        - 36，float
      * - ``label_direction``
        - array([ 0., -1.,  0.])，Point3DLike
      * - ``label_constructor``
        - <class 'manim.mobject.text.…，type[ManimTextLabel]
      * - ``scaling``
        - <manim.mobject.graphing.sca…，_ScaleBase
      * - ``line_to_number_buff``
        - 0.25，float
      * - ``decimal_number_config``
        - None，dict | None
      * - ``numbers_to_exclude``
        - None，Iterable[float] | None
      * - ``numbers_to_include``
        - None，Iterable[float] | None

快速上手
~~~~~~~~

.. code-block:: python

   nl = NumberLine(x_range=[-5, 5, 1])

API 文档
~~~~~~~~

.. autoclass:: manim.NumberLine

NumberPlane
-----------

网格纸坐标系：Axes + 背景网格线，默认淡色网格，函数演示常用底图。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "CoordinateSystem" -> "Mobject";
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Axes";
     "Axes" -> "NumberPlane";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``x_range``
        - (-7.111111111111111, 7.1111…，Sequence[float] | None
      * - ``y_range``
        - (-4.0, 4.0, 1)，Sequence[float] | None
      * - ``x_length``
        - None，float | None
      * - ``y_length``
        - None，float | None
      * - ``background_line_style``
        - None，dict[str, Any] | None
      * - ``faded_line_style``
        - None，dict[str, Any] | None
      * - ``faded_line_ratio``
        - 1，int
      * - ``make_smooth_after_applying_functions``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   plane = NumberPlane()

API 文档
~~~~~~~~

.. autoclass:: manim.NumberPlane

ParametricFunction
------------------

参数方程曲线：传入 r(t) 自动采样成曲线，极坐标/物理轨迹必备。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "ParametricFunction";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``function``
        - —
      * - ``t_range``
        - (0, 1)
      * - ``scaling``
        - <manim.mobject.graphing.sca…，_ScaleBase
      * - ``dt``
        - 1e-08，float
      * - ``discontinuities``
        - None，Iterable[float] | None
      * - ``use_smoothing``
        - True，bool
      * - ``use_vectorized``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   curve = ParametricFunction(lambda t: np.array([np.cos(t), np.sin(t), 0]), t_range=[0, TAU])

API 文档
~~~~~~~~

.. autoclass:: manim.ParametricFunction

PolarPlane
----------

极坐标系：同心圆 + 放射线网格，极坐标方程 r(θ) 的直接画布。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "CoordinateSystem" -> "Mobject";
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Axes";
     "Axes" -> "PolarPlane";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``radius_max``
        - 4.0，float
      * - ``size``
        - None，float | None
      * - ``radius_step``
        - 1，float
      * - ``azimuth_step``
        - None，float | None
      * - ``azimuth_units``
        - 'PI radians'，str
      * - ``azimuth_compact_fraction``
        - True，bool
      * - ``azimuth_offset``
        - 0，float
      * - ``azimuth_direction``
        - 'CCW'，str
      * - ``azimuth_label_buff``
        - 0.1，float
      * - ``azimuth_label_font_size``
        - 24，float
      * - ``radius_config``
        - None，dict[str, Any] | None
      * - ``background_line_style``
        - None，dict[str, Any] | None
      * - ``faded_line_style``
        - None，dict[str, Any] | None
      * - ``faded_line_ratio``
        - 1，int
      * - ``make_smooth_after_applying_functions``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   polar = PolarPlane()

API 文档
~~~~~~~~

.. autoclass:: manim.PolarPlane

SampleSpace
-----------

概率样本空间矩形：横竖切分表示条件概率，概率论章节道具。

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
     "Rectangle" -> "SampleSpace";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``height``
        - 3，float
      * - ``width``
        - 3，float
      * - ``fill_color``
        - ManimColor('#444444')，ParsableManimColor
      * - ``fill_opacity``
        - 1，float
      * - ``stroke_width``
        - 0.5，float
      * - ``stroke_color``
        - ManimColor('#BBBBBB')，ParsableManimColor
      * - ``default_label_scale_val``
        - 1，float

API 文档
~~~~~~~~

.. autoclass:: manim.SampleSpace

ThreeDAxes
----------

三维坐标轴：x/y/z 三轴 + 可旋转视角，3D 函数绘图底座。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "CoordinateSystem" -> "Mobject";
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Axes";
     "Axes" -> "ThreeDAxes";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``x_range``
        - (-6, 6, 1)，Sequence[float] | None
      * - ``y_range``
        - (-5, 5, 1)，Sequence[float] | None
      * - ``z_range``
        - (-4, 4, 1)，Sequence[float] | None
      * - ``x_length``
        - 10.5，float | None
      * - ``y_length``
        - 10.5，float | None
      * - ``z_length``
        - 6.5，float | None
      * - ``z_axis_config``
        - None，dict[str, Any] | None
      * - ``z_normal``
        - array([ 0., -1.,  0.])，Vector3DLike
      * - ``num_axis_pieces``
        - 20，int
      * - ``light_source``
        - array([-7., -9., 10.])，Point3DLike
      * - ``depth``
        - None，Any
      * - ``gloss``
        - 0.5，float

快速上手
~~~~~~~~

.. code-block:: python

   axes3d = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3])

API 文档
~~~~~~~~

.. autoclass:: manim.ThreeDAxes

UnitInterval
------------

0 到 1 的快捷数轴：概率论单位线段场景直接取用。

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
     "Line" -> "NumberLine";
     "NumberLine" -> "UnitInterval";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``unit_size``
        - 10，float
      * - ``numbers_with_elongated_ticks``
        - None，list[float] | None
      * - ``decimal_number_config``
        - None，dict[str, Any] | None

快速上手
~~~~~~~~

.. code-block:: python

   ui = UnitInterval()

API 文档
~~~~~~~~

.. autoclass:: manim.UnitInterval
