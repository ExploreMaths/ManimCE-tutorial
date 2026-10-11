===============================
API 参考：OpenGL 对象（opengl）
===============================

共 **5** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

DotCloud
--------

大量点组成的点云：PMobject 的高效批量渲染版，可视化散点/粒子。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "OpenGLPMobject" -> "DotCloud";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``color``
        - ManimColor('#FFFF00')，ParsableManimColor
      * - ``stroke_width``
        - 2.0，float
      * - ``radius``
        - 2.0，float
      * - ``density``
        - 10，float

API 文档
~~~~~~~~

.. autoclass:: manim.DotCloud

OpenGLPGroup
------------

OpenGL 渲染下 PMobject 的分组容器（实验性）。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "OpenGLPMobject" -> "OpenGLPGroup";
   }

API 文档
~~~~~~~~

.. autoclass:: manim.OpenGLPGroup

OpenGLPMPoint
-------------

OpenGL 渲染下的单点对象（实验性）。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "OpenGLPMobject" -> "OpenGLPMPoint";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``location``
        - array([0., 0., 0.])
      * - ``stroke_width``
        - 4.0

API 文档
~~~~~~~~

.. autoclass:: manim.OpenGLPMPoint

OpenGLPMobject
--------------

OpenGL 渲染管线的点集基类（实验性），与 cairo 版的 PMobject 平行。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``stroke_width``
        - 2.0，float
      * - ``color``
        - ManimColor('#FFFF00')，ParsableManimColor
      * - ``render_primitive``
        - 0，int

API 文档
~~~~~~~~

.. autoclass:: manim.OpenGLPMobject

TrueDot
-------

严格按点渲染的 Dot：无最小尺寸限制，配合 DotCloud 做精确散点。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "OpenGLPMobject" -> "DotCloud";
     "DotCloud" -> "TrueDot";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``center``
        - array([0., 0., 0.])，Point3DLike
      * - ``stroke_width``
        - 2.0，float

API 文档
~~~~~~~~

.. autoclass:: manim.TrueDot
