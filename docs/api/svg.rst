===========================
API 参考：SVG 与位图（svg）
===========================

共 **7** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

ArcBrace
--------

贴合圆弧的大括号标注：沿曲线中点展开的弧形括号。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VMobjectFromSVGPath";
     "VMobjectFromSVGPath" -> "Brace";
     "Brace" -> "ArcBrace";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``arc``
        - None，Arc | None
      * - ``direction``
        - array([1., 0., 0.])，Vector3DLike

API 文档
~~~~~~~~

.. autoclass:: manim.ArcBrace

Brace
-----

贴合图形边缘的大括号：自动缩放适应目标宽度，配合标签写标注公式。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VMobjectFromSVGPath";
     "VMobjectFromSVGPath" -> "Brace";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``direction``
        - array([ 0., -1.,  0.])，Vector3DLike
      * - ``buff``
        - 0.2，float
      * - ``sharpness``
        - 2，float
      * - ``stroke_width``
        - 0，float
      * - ``fill_opacity``
        - 1.0，float
      * - ``background_stroke_width``
        - 0，float
      * - ``background_stroke_color``
        - ManimColor('#000000')，ParsableManimColor

快速上手
~~~~~~~~

.. code-block:: python

   brace = Brace(group, DOWN, label="sum")

API 文档
~~~~~~~~

.. autoclass:: manim.Brace

BraceBetweenPoints
------------------

两点之间的括号：不依附具体对象，任意位置放标注。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VMobjectFromSVGPath";
     "VMobjectFromSVGPath" -> "Brace";
     "Brace" -> "BraceBetweenPoints";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``point_1``
        - —，Point3DLike
      * - ``point_2``
        - —，Point3DLike
      * - ``direction``
        - array([0., 0., 0.])，Vector3DLike

API 文档
~~~~~~~~

.. autoclass:: manim.BraceBetweenPoints

BraceLabel
----------

括号 + 标签的组合体：一行代码完成这组等于某公式的标注。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "BraceLabel";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``obj``
        - —，Mobject
      * - ``text``
        - —，str
      * - ``brace_direction``
        - array([ 0., -1.,  0.])，Vector3DLike
      * - ``label_constructor``
        - <class 'manim.mobject.text.…
      * - ``font_size``
        - 48，float
      * - ``buff``
        - 0.2，float
      * - ``brace_config``
        - None，dict[str, Any] | None

API 文档
~~~~~~~~

.. autoclass:: manim.BraceLabel

BraceText
---------

Brace 的 Text 标签便捷版：标签自动用 Text 渲染。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "BraceLabel";
     "BraceLabel" -> "BraceText";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``obj``
        - —，Mobject
      * - ``text``
        - —，str
      * - ``label_constructor``
        - <class 'manim.mobject.text.…

API 文档
~~~~~~~~

.. autoclass:: manim.BraceText

SVGMobject
----------

把 SVG 矢量文件解析成矢量路径的 Mobject：图标、自定义图形直接导入，可控每个子路径。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "SVGMobject";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``file_name``
        - None，str | os.PathLike | None
      * - ``should_center``
        - True，bool
      * - ``height``
        - 2，float | None
      * - ``width``
        - None，float | None
      * - ``color``
        - None
      * - ``opacity``
        - None，float | None
      * - ``fill_color``
        - None
      * - ``fill_opacity``
        - None，float | None
      * - ``stroke_color``
        - None
      * - ``stroke_opacity``
        - None，float | None
      * - ``stroke_width``
        - None，float | None
      * - ``svg_default``
        - None，dict | None
      * - ``path_string_config``
        - None，dict | None
      * - ``use_svg_cache``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   icon = SVGMobject("logo.svg")

API 文档
~~~~~~~~

.. autoclass:: manim.SVGMobject

VMobjectFromSVGPath
-------------------

由单个 SVG path 数据字符串构造 VMobject 的底层工具，可程序化生成路径。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VMobjectFromSVGPath";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``path_obj``
        - —，se.Path
      * - ``long_lines``
        - False，bool
      * - ``should_subdivide_sharp_curves``
        - False，bool
      * - ``should_remove_null_curves``
        - False，bool

API 文档
~~~~~~~~

.. autoclass:: manim.VMobjectFromSVGPath
