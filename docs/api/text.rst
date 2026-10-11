============================
API 参考：文本与公式（text）
============================

共 **14** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

BulletedList
------------

项目符号列表：字符串数组一键排成带圆点的竖排列表，演示文稿风。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "SVGMobject";
     "SVGMobject" -> "SingleStringMathTex";
     "SingleStringMathTex" -> "MathTex";
     "MathTex" -> "Tex";
     "Tex" -> "BulletedList";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``buff``
        - 0.5，float
      * - ``dot_scale_factor``
        - 2，float
      * - ``tex_environment``
        - None，str | None
      * - ``dot_buff``
        - 0.1，float

快速上手
~~~~~~~~

.. code-block:: python

   bl = BulletedList("第一项", "第二项", "第三项")

API 文档
~~~~~~~~

.. autoclass:: manim.BulletedList

Code
----

代码高亮块：从文件或字符串渲染带语法着色的代码段，主题、字体、行号可调。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Code";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``code_file``
        - None，StrPath | None
      * - ``code_string``
        - None，str | None
      * - ``language``
        - None，str | None
      * - ``formatter_style``
        - 'vim'，str | type[Style]
      * - ``tab_width``
        - 4，int
      * - ``add_line_numbers``
        - True，bool
      * - ``line_numbers_from``
        - 1，int
      * - ``background``
        - 'rectangle'
      * - ``background_config``
        - None，dict[str, Any] | None
      * - ``paragraph_config``
        - None，dict[str, Any] | None

快速上手
~~~~~~~~

.. code-block:: python

   code = Code("script.py", language="python")

API 文档
~~~~~~~~

.. autoclass:: manim.Code

DecimalNumber
-------------

可动小数的数字文本：set_value 即重排，配 ValueTracker 做计数器。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "DecimalNumber";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``number``
        - 0，float
      * - ``num_decimal_places``
        - 2，int
      * - ``mob_class``
        - <class 'manim.mobject.text.…
      * - ``include_sign``
        - False，bool
      * - ``group_with_commas``
        - True，bool
      * - ``digit_buff_per_font_unit``
        - 0.001，float
      * - ``show_ellipsis``
        - False，bool
      * - ``unit``
        - None，str | None
      * - ``unit_buff_per_font_unit``
        - 0，float
      * - ``include_background_rectangle``
        - False，bool
      * - ``edge_to_fix``
        - array([-1.,  0.,  0.])，Vector3DLike
      * - ``font_size``
        - 48，float
      * - ``stroke_width``
        - 0，float
      * - ``fill_opacity``
        - 1.0，float

快速上手
~~~~~~~~

.. code-block:: python

   num = DecimalNumber(0, num_decimal_places=2)

API 文档
~~~~~~~~

.. autoclass:: manim.DecimalNumber

Integer
-------

整数版 DecimalNumber：无小数点，步进计数常用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "DecimalNumber";
     "DecimalNumber" -> "Integer";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``number``
        - 0，float
      * - ``num_decimal_places``
        - 0，int

API 文档
~~~~~~~~

.. autoclass:: manim.Integer

MarkupText
----------

Pango 标记语言文本：字符串里直接写 b/i/span 等标签实现富文本混排。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "SVGMobject";
     "SVGMobject" -> "MarkupText";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``text``
        - —，str
      * - ``fill_opacity``
        - 1，float
      * - ``stroke_width``
        - 0，float
      * - ``color``
        - None
      * - ``font_size``
        - 48，float
      * - ``line_spacing``
        - -1，float
      * - ``font``
        - ''，str
      * - ``slant``
        - 'NORMAL'，str
      * - ``weight``
        - 'NORMAL'，str
      * - ``justify``
        - False，bool
      * - ``gradient``
        - None
      * - ``tab_width``
        - 4，int
      * - ``height``
        - None，int | None
      * - ``width``
        - None，int | None
      * - ``should_center``
        - True，bool
      * - ``disable_ligatures``
        - False，bool
      * - ``warn_missing_font``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   mt = MarkupText('<b>bold</b> <span foreground="#FFFF00">yellow</span>')

API 文档
~~~~~~~~

.. autoclass:: manim.MarkupText

MathTex
-------

LaTeX 公式文本：每个 LaTeX 片段是独立子对象，可按下标索引做局部动画，数学视频的核心。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "SVGMobject";
     "SVGMobject" -> "SingleStringMathTex";
     "SingleStringMathTex" -> "MathTex";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``arg_separator``
        - ' '，str
      * - ``substrings_to_isolate``
        - None，Iterable[str] | None
      * - ``tex_to_color_map``
        - None
      * - ``tex_environment``
        - 'align*'，str | None

快速上手
~~~~~~~~

.. code-block:: python

   eq = MathTex(r"rac{a}{b} = \sqrt{c}")

API 文档
~~~~~~~~

.. autoclass:: manim.MathTex

MathTypst
---------

Typst 排版的公式对象（v0.21 新增）：用 Typst 语法替代 LaTeX，需安装 typst。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "SVGMobject";
     "SVGMobject" -> "Typst";
     "Typst" -> "MathTypst";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``math_expression``
        - —，str

API 文档
~~~~~~~~

.. autoclass:: manim.MathTypst

Paragraph
---------

多段落文本块：长文字自动分行成段，排文章类内容用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "Paragraph";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``line_spacing``
        - -1，float
      * - ``alignment``
        - None，str | None

API 文档
~~~~~~~~

.. autoclass:: manim.Paragraph

SingleStringMathTex
-------------------

单个 LaTeX 字符串的公式对象：不做分词切片，MathTex 的底层形式。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "SVGMobject";
     "SVGMobject" -> "SingleStringMathTex";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``tex_string``
        - —，str
      * - ``stroke_width``
        - 0，float
      * - ``should_center``
        - True，bool
      * - ``height``
        - None，float | None
      * - ``organize_left_to_right``
        - False，bool
      * - ``tex_environment``
        - 'align*'，str | None
      * - ``tex_template``
        - None，TexTemplate | None
      * - ``font_size``
        - 48，float
      * - ``color``
        - None

API 文档
~~~~~~~~

.. autoclass:: manim.SingleStringMathTex

Tex
---

LaTeX 完整文档模式：可加载宏包与自定义导言区，出整个 LaTeX 页面效果。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "SVGMobject";
     "SVGMobject" -> "SingleStringMathTex";
     "SingleStringMathTex" -> "MathTex";
     "MathTex" -> "Tex";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``arg_separator``
        - ''，str
      * - ``tex_environment``
        - 'center'，str | None

API 文档
~~~~~~~~

.. autoclass:: manim.Tex

Text
----

Pango 渲染的系统字体文本：中文、emoji 原生支持，t2c/t2f 子串改色改字体，文字类内容首选。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "SVGMobject";
     "SVGMobject" -> "Text";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``text``
        - —，str
      * - ``fill_opacity``
        - 1.0，float
      * - ``stroke_width``
        - 0，float
      * - ``color``
        - None
      * - ``font_size``
        - 48，float
      * - ``line_spacing``
        - -1，float
      * - ``font``
        - ''，str
      * - ``slant``
        - 'NORMAL'，str
      * - ``weight``
        - 'NORMAL'，str
      * - ``t2c``
        - None，dict[str, str] | None
      * - ``t2f``
        - None，dict[str, str] | None
      * - ``t2g``
        - None
      * - ``t2s``
        - None，dict[str, str] | None
      * - ``t2w``
        - None，dict[str, str] | None
      * - ``gradient``
        - None
      * - ``tab_width``
        - 4，int
      * - ``warn_missing_font``
        - True，bool
      * - ``height``
        - None，float | None
      * - ``width``
        - None，float | None
      * - ``should_center``
        - True，bool
      * - ``disable_ligatures``
        - False，bool
      * - ``use_svg_cache``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   t = Text("你好，Manim！", t2c={"Manim": YELLOW})

API 文档
~~~~~~~~

.. autoclass:: manim.Text

Title
-----

居中放大加下划线的标题文本：章节标题专用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "SVGMobject";
     "SVGMobject" -> "SingleStringMathTex";
     "SingleStringMathTex" -> "MathTex";
     "MathTex" -> "Tex";
     "Tex" -> "Title";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``include_underline``
        - True，bool
      * - ``match_underline_width_to_text``
        - False，bool
      * - ``underline_buff``
        - 0.25，float

快速上手
~~~~~~~~

.. code-block:: python

   self.add(Title("第三章：动画进阶"))

API 文档
~~~~~~~~

.. autoclass:: manim.Title

Typst
-----

Typst 文档模式文本（v0.21 新增）：整个文档用 Typst 排版，类似 Tex 的定位。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "SVGMobject";
     "SVGMobject" -> "Typst";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``typst_code``
        - —，str
      * - ``font_size``
        - 48，float
      * - ``typst_preamble``
        - ''，str
      * - ``color``
        - None
      * - ``stroke_width``
        - None，float | None
      * - ``font_paths``
        - None，list[str | Path] | None
      * - ``track_baselines``
        - False，bool
      * - ``should_center``
        - True，bool
      * - ``height``
        - None，float | None

API 文档
~~~~~~~~

.. autoclass:: manim.Typst

Variable
--------

名字 + 数值的组合显示：变量名在上数值在下，配 ValueTracker 实时联动。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "Variable";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``var``
        - —，float
      * - ``label``
        - —
      * - ``var_type``
        - <class 'manim.mobject.text.…
      * - ``num_decimal_places``
        - 2，int

快速上手
~~~~~~~~

.. code-block:: python

   v = Variable(0, "x", num_decimal_places=2)

API 文档
~~~~~~~~

.. autoclass:: manim.Variable
