====================
API 参考：核心与其他
====================

共 **4** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

CairoRenderer
-------------

Cairo 渲染器：默认的 2D 矢量光栅化后端，把 VMobject 画成帧。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``file_writer_class``
        - <class 'manim.scene.scene_f…，type[SceneFileWriter]
      * - ``camera_class``
        - None，type[Camera] | None
      * - ``skip_animations``
        - False，bool

API 文档
~~~~~~~~

.. autoclass:: manim.CairoRenderer

CapStyleType
------------

线帽样式枚举：butt/round/square，控制线段端点形状。

API 文档
~~~~~~~~

.. autoclass:: manim.CapStyleType

LineJointType
-------------

线连接样式枚举：miter/round/bevel，控制折角处形状。

API 文档
~~~~~~~~

.. autoclass:: manim.LineJointType

RendererType
------------

渲染器类型枚举：选择 cairo 或 OpenGL 渲染后端。

API 文档
~~~~~~~~

.. autoclass:: manim.RendererType
