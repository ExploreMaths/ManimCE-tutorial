=======================
API 参考：工具（utils）
=======================

共 **8** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

DictAsObject
------------

把字典包成属性访问的小工具类：d.key 替代 d[键]，配置读取更便捷。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``dictin``
        - —，dict[str, Any]

API 文档
~~~~~~~~

.. autoclass:: manim.DictAsObject

HSV
---

HSV 颜色：色相/饱和度/明度三元组，做色轮、渐变等色彩动画用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "ManimColor" -> "HSV";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``hsv``
        - —
      * - ``alpha``
        - 1.0，float

API 文档
~~~~~~~~

.. autoclass:: manim.HSV

ManimColor
----------

v0.19 起的新颜色基类：RGB(A) 统一封装，hex/HSV/内置色互转，颜色运算的中枢。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``value``
        - —
      * - ``alpha``
        - 1.0，float

快速上手
~~~~~~~~

.. code-block:: python

   c = ManimColor("#FFFF00").interpolate(BLUE, 0.5)

API 文档
~~~~~~~~

.. autoclass:: manim.ManimColor

RGBA
----

带透明度的颜色表示：r/g/b/a 四通道，ManimColor 的底层载体。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``value``
        - —
      * - ``alpha``
        - 1.0，float

API 文档
~~~~~~~~

.. autoclass:: manim.RGBA

RandomColorGenerator
--------------------

随机颜色生成器：按配色策略批量产色，做随机配色演示用。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``seed``
        - None，int | None
      * - ``sample_colors``
        - None，list[ManimColor] | None

API 文档
~~~~~~~~

.. autoclass:: manim.RandomColorGenerator

TexFontTemplates
----------------

Tex 字体模板集合：pdfLaTeX 各字体配置的现成模板。

API 文档
~~~~~~~~

.. autoclass:: manim.TexFontTemplates

TexTemplate
-----------

LaTeX 导言区模板：自定义宏包、字体、命令，Tex/MathTex 渲染的编译配置。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``tex_compiler``
        - 'latex'，str | list[str]
      * - ``description``
        - ''，str
      * - ``output_format``
        - '.dvi'，str
      * - ``documentclass``
        - '\\documentclass[preview]{s…，str
      * - ``preamble``
        - '\\usepackage[english]{babe…，str
      * - ``placeholder_text``
        - 'YourTextHere'，str
      * - ``post_doc_commands``
        - ''，str

快速上手
~~~~~~~~

.. code-block:: python

   tpl = TexTemplate()
   tpl.add_to_preamble("\usepackage{amsmath}")

API 文档
~~~~~~~~

.. autoclass:: manim.TexTemplate

TexTemplateLibrary
------------------

常用 TexTemplate 的预置库：ctex、standalone 等开箱模板。

API 文档
~~~~~~~~

.. autoclass:: manim.TexTemplateLibrary
