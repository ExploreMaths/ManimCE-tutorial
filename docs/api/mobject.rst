======================
API 参考：Mobject 核心
======================

共 **21** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

ArrowVectorField
----------------

把向量场画成带箭头的网格：每个采样点一支方向箭头，随场强缩放，是微分方程可视化的主力。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "VectorField";
     "VectorField" -> "ArrowVectorField";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``func``
        - —
      * - ``color``
        - None
      * - ``color_scheme``
        - None
      * - ``min_color_scheme_value``
        - 0，float
      * - ``max_color_scheme_value``
        - 2，float
      * - ``colors``
        - [ManimColor('#236B8E'), Man…
      * - ``x_range``
        - None，Sequence[float]
      * - ``y_range``
        - None，Sequence[float]
      * - ``z_range``
        - None，Sequence[float]
      * - ``three_dimensions``
        - False，bool
      * - ``length_func``
        - <function ArrowVectorField.…，Callable[[float], float]
      * - ``opacity``
        - 1.0，float
      * - ``vector_config``
        - None，dict | None

快速上手
~~~~~~~~

.. code-block:: python

   field = ArrowVectorField(lambda p: np.array([-p[1], p[0], 0]))
   self.add(field)

API 文档
~~~~~~~~

.. autoclass:: manim.ArrowVectorField

ComplexValueTracker
-------------------

追踪复数的 ValueTracker：set_value 传复数，get_value 返回 complex，实部虚部同步插值。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "ValueTracker";
     "ValueTracker" -> "ComplexValueTracker";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``value``
        - 0，float

快速上手
~~~~~~~~

.. code-block:: python

   z = ComplexValueTracker(1 + 2j)
   z.set_value(3 - 1j)

API 文档
~~~~~~~~

.. autoclass:: manim.ComplexValueTracker

DecimalMatrix
-------------

矩阵 + 每个元素都是可动 DecimalNumber：数值变化动画可直接播在矩阵上。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Matrix";
     "Matrix" -> "DecimalMatrix";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``matrix``
        - —，Iterable[Iterable[Any]]
      * - ``element_to_mobject``
        - <class 'manim.mobject.text.…
      * - ``element_to_mobject_config``
        - {'num_decimal_places': 1}，dict[str, Any]

API 文档
~~~~~~~~

.. autoclass:: manim.DecimalMatrix

DecimalTable
------------

表格 + 可动的十进制数字单元格，做数据表动态更新最方便。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Table";
     "Table" -> "DecimalTable";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``table``
        - —
      * - ``element_to_mobject``
        - <class 'manim.mobject.text.…
      * - ``element_to_mobject_config``
        - {'num_decimal_places': 1}，dict

快速上手
~~~~~~~~

.. code-block:: python

   table = DecimalTable([[3.14, 2.71], [1.41, 1.73]])

API 文档
~~~~~~~~

.. autoclass:: manim.DecimalTable

DiGraph
-------

有向图对象：顶点 + 带箭头的边，支持自动布局与顶点/边样式定制。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "DiGraph";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vertices``
        - —，Sequence[Hashable]
      * - ``edges``
        - —
      * - ``labels``
        - False，bool | dict
      * - ``label_fill_color``
        - ManimColor('#000000')，str
      * - ``layout``
        - 'spring'
      * - ``layout_scale``
        - 2
      * - ``layout_config``
        - None，dict | None
      * - ``vertex_type``
        - <class 'manim.mobject.geome…，type[Mobject]
      * - ``vertex_config``
        - None，dict | None
      * - ``vertex_mobjects``
        - None，dict | None
      * - ``edge_type``
        - <class 'manim.mobject.geome…，type[Mobject]
      * - ``partitions``
        - None
      * - ``root_vertex``
        - None，Hashable | None
      * - ``edge_config``
        - None，dict | None

快速上手
~~~~~~~~

.. code-block:: python

   g = DiGraph([1, 2, 3], [(1, 2), (2, 3)])

API 文档
~~~~~~~~

.. autoclass:: manim.DiGraph

FullScreenRectangle
-------------------

恰好铺满整个画面（含边距）的矩形，常作背景板或全屏遮罩。

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
     "Rectangle" -> "ScreenRectangle";
     "ScreenRectangle" -> "FullScreenRectangle";
   }

快速上手
~~~~~~~~

.. code-block:: python

   bg = FullScreenRectangle(fill_color=BLACK, fill_opacity=0.8)

API 文档
~~~~~~~~

.. autoclass:: manim.FullScreenRectangle

Graph
-----

通用图论对象：无向图，自动布局（如 spring/circular），顶点标签、边粗细颜色全能调。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Graph";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vertices``
        - —，Sequence[Hashable]
      * - ``edges``
        - —
      * - ``labels``
        - False，bool | dict
      * - ``label_fill_color``
        - ManimColor('#000000')，str
      * - ``layout``
        - 'spring'
      * - ``layout_scale``
        - 2
      * - ``layout_config``
        - None，dict | None
      * - ``vertex_type``
        - <class 'manim.mobject.geome…，type[Mobject]
      * - ``vertex_config``
        - None，dict | None
      * - ``vertex_mobjects``
        - None，dict | None
      * - ``edge_type``
        - <class 'manim.mobject.geome…，type[Mobject]
      * - ``partitions``
        - None
      * - ``root_vertex``
        - None，Hashable | None
      * - ``edge_config``
        - None，dict | None

快速上手
~~~~~~~~

.. code-block:: python

   g = Graph([1, 2, 3], [(1, 2), (2, 3), (3, 1)])

API 文档
~~~~~~~~

.. autoclass:: manim.Graph

Group
-----

Mobject 的通用容器：把任意对象打包统一管理（移动、淡入、整体动画）。注意 Group 不保证子对象是 VMobject。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "Group";
   }

快速上手
~~~~~~~~

.. code-block:: python

   group = Group(dot, label, square)
   self.play(FadeIn(group))

API 文档
~~~~~~~~

.. autoclass:: manim.Group

IntegerMatrix
-------------

元素为整数的矩阵 Mobject，和 DecimalMatrix 类似但用固定整数显示。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Matrix";
     "Matrix" -> "IntegerMatrix";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``matrix``
        - —，Iterable[Iterable[Any]]
      * - ``element_to_mobject``
        - <class 'manim.mobject.text.…

API 文档
~~~~~~~~

.. autoclass:: manim.IntegerMatrix

IntegerTable
------------

整数单元格表格，适合计数类数据展示。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Table";
     "Table" -> "IntegerTable";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``table``
        - —
      * - ``element_to_mobject``
        - <class 'manim.mobject.text.…

API 文档
~~~~~~~~

.. autoclass:: manim.IntegerTable

ManimBanner
-----------

官方 Logo 动画横幅：自带展开、收拢等现成动画方法，适合视频片头片尾。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "ManimBanner";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``dark_theme``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   banner = ManimBanner()
   self.play(banner.expand())

API 文档
~~~~~~~~

.. autoclass:: manim.ManimBanner

MathTable
---------

单元格为 MathTex 的表格：每个格子都是公式，排版数学矩阵类内容用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Table";
     "Table" -> "MathTable";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``table``
        - —
      * - ``element_to_mobject``
        - <class 'manim.mobject.text.…

API 文档
~~~~~~~~

.. autoclass:: manim.MathTable

Matrix
------

通用矩阵对象：元素可以是任意 Mobject，括号、行距列距可调，线性代数章节的核心道具。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Matrix";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``matrix``
        - —
      * - ``v_buff``
        - 0.8，float
      * - ``h_buff``
        - 1.3，float
      * - ``bracket_h_buff``
        - 0.25，float
      * - ``bracket_v_buff``
        - 0.25，float
      * - ``add_background_rectangles_to_entries``
        - False，bool
      * - ``include_background_rectangle``
        - False，bool
      * - ``element_to_mobject``
        - <class 'manim.mobject.text.…
      * - ``element_to_mobject_config``
        - {}，dict[str, Any]
      * - ``element_alignment_corner``
        - array([ 1., -1.,  0.])，Vector3DLike
      * - ``left_bracket``
        - '['，str
      * - ``right_bracket``
        - ']'，str
      * - ``stretch_brackets``
        - True，bool
      * - ``bracket_config``
        - {}，dict

快速上手
~~~~~~~~

.. code-block:: python

   m = Matrix([[1, 2], [3, 4]])

API 文档
~~~~~~~~

.. autoclass:: manim.Matrix

Mobject
-------

一切可见对象的基类。掌握它的 transform、shift、scale、fade 族方法与子对象树，就掌握了 Manim 的对象模型。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``color``
        - ManimColor('#FFFFFF')
      * - ``name``
        - None，str | None
      * - ``dim``
        - 3，int
      * - ``target``
        - None，Mobject | None
      * - ``z_index``
        - 0，float

快速上手
~~~~~~~~

.. code-block:: python

   mob = Mobject()
   mob.shift(UP).scale(2)

API 文档
~~~~~~~~

.. autoclass:: manim.Mobject

MobjectMatrix
-------------

元素为任意 Mobject 的矩阵：把图形本身排成矩阵布局展示。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Matrix";
     "Matrix" -> "MobjectMatrix";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``matrix``
        - —，Iterable[Iterable[Any]]
      * - ``element_to_mobject``
        - <function MobjectMatrix.<la…

API 文档
~~~~~~~~

.. autoclass:: manim.MobjectMatrix

MobjectTable
------------

单元格为任意 Mobject 的通用表格，最自由的表格形态。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Table";
     "Table" -> "MobjectTable";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``table``
        - —
      * - ``element_to_mobject``
        - <function MobjectTable.<lam…

快速上手
~~~~~~~~

.. code-block:: python

   t = MobjectTable([[dot, circle], [square, star]])

API 文档
~~~~~~~~

.. autoclass:: manim.MobjectTable

ScreenRectangle
---------------

按 16:9 屏幕比例裁出的矩形，适合作画中画框或参考取景框。

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
     "Rectangle" -> "ScreenRectangle";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``aspect_ratio``
        - 1.7777777777777777，float
      * - ``height``
        - 4，float

快速上手
~~~~~~~~

.. code-block:: python

   frame = ScreenRectangle(height=3)

API 文档
~~~~~~~~

.. autoclass:: manim.ScreenRectangle

StreamLines
-----------

沿向量场绘出流线族（积分曲线），比 ArrowVectorField 更能表现场的整体走势。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "VectorField";
     "VectorField" -> "StreamLines";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``func``
        - —
      * - ``color``
        - None
      * - ``color_scheme``
        - None
      * - ``min_color_scheme_value``
        - 0，float
      * - ``max_color_scheme_value``
        - 2，float
      * - ``colors``
        - [ManimColor('#236B8E'), Man…
      * - ``x_range``
        - None，Sequence[float]
      * - ``y_range``
        - None，Sequence[float]
      * - ``z_range``
        - None，Sequence[float]
      * - ``three_dimensions``
        - False，bool
      * - ``noise_factor``
        - None，float | None
      * - ``n_repeats``
        - 1
      * - ``dt``
        - 0.05
      * - ``virtual_time``
        - 3
      * - ``max_anchors_per_line``
        - 100
      * - ``padding``
        - 3
      * - ``stroke_width``
        - 1
      * - ``opacity``
        - 1

快速上手
~~~~~~~~

.. code-block:: python

   lines = StreamLines(lambda p: np.array([-p[1], p[0], 0]))

API 文档
~~~~~~~~

.. autoclass:: manim.StreamLines

Table
-----

表格基类：字符串单元格 + 行列标签 + 边框样式，add_highlighted_cell 可做聚光单元格。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Table";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``table``
        - —
      * - ``row_labels``
        - None
      * - ``col_labels``
        - None
      * - ``top_left_entry``
        - None，VMobject | None
      * - ``v_buff``
        - 0.8，float
      * - ``h_buff``
        - 1.3，float
      * - ``include_outer_lines``
        - False，bool
      * - ``include_inner_lines``
        - True，bool
      * - ``add_background_rectangles_to_entries``
        - False，bool
      * - ``entries_background_color``
        - ManimColor('#000000')，ParsableManimColor
      * - ``include_background_rectangle``
        - False，bool
      * - ``background_rectangle_color``
        - ManimColor('#000000')，ParsableManimColor
      * - ``element_to_mobject``
        - <class 'manim.mobject.text.…
      * - ``element_to_mobject_config``
        - {}，dict
      * - ``arrange_in_grid_config``
        - {}，dict
      * - ``line_config``
        - {}，dict

快速上手
~~~~~~~~

.. code-block:: python

   t = Table([["a", "b"], ["c", "d"]], row_labels=[1, 2])

API 文档
~~~~~~~~

.. autoclass:: manim.Table

ValueTracker
------------

不可见数值容器：本身不渲染，配合 get_value/set_value 与 add_updater 驱动一切「数值驱动的动画」。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "ValueTracker";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``value``
        - 0，float

快速上手
~~~~~~~~

.. code-block:: python

   vt = ValueTracker(0)
   number.add_updater(lambda d: d.set_value(vt.get_value()))
   self.play(vt.animate.set_value(10))

API 文档
~~~~~~~~

.. autoclass:: manim.ValueTracker

VectorField
-----------

向量场基类：ArrowVectorField 与 StreamLines 的共同父类，负责采样与归一化逻辑。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "VectorField";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``func``
        - —
      * - ``color``
        - None
      * - ``color_scheme``
        - None
      * - ``min_color_scheme_value``
        - 0，float
      * - ``max_color_scheme_value``
        - 2，float
      * - ``colors``
        - [ManimColor('#236B8E'), Man…

API 文档
~~~~~~~~

.. autoclass:: manim.VectorField
