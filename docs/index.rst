================
ManimCE 中文教程
================

基于 **Manim Community v0.21.0** 的系统性中文教程：从安装到进阶，每个 API 配中文讲解、可交互示例视频与源码，全部例子可一键复现。

.. raw:: html

   <div id="home-progress" data-total="62"></div>

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item-card:: 🚀 开始学习
      :link: chapters/ch01/installation
      :link-type: doc

      **入门**：安装与运行环境

   .. grid-item-card:: 📚 API 索引
      :link: api-index
      :link-type: doc

      全部 259 个类与函数，按字母分组，直达中文讲解。

   .. grid-item-card:: 🧪 API 参考（全类）
      :link: api/index
      :link-type: doc

      256 个公开类逐一精讲：中文说明、继承链、参数表、上手示例与 autodoc 参考。

   .. grid-item-card:: 🧬 继承关系图
      :link: inheritance-graph
      :link-type: doc

      全部 256 个公开类的继承全景图，构建时自动遍历生成，节点可点击跳转。

   .. grid-item-card:: 📖 术语表
      :link: glossary
      :link-type: doc

      Mobject、VMobject 等核心术语的中文释义。

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 入门

   chapters/ch01/installation
   chapters/ch01/first-scene
   chapters/ch01/render-pipeline
   chapters/ch01/cli-and-sections

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 基础图形

   chapters/ch02/mobject-core
   chapters/ch02/vmobject
   chapters/ch02/groups
   chapters/ch02/basic-shapes
   chapters/ch02/lines-and-arrows
   chapters/ch02/arcs-and-curves
   chapters/ch02/dots-and-clouds
   chapters/ch02/boolean-ops
   chapters/ch02/annotations
   chapters/ch02/images-and-svg
   chapters/ch02/colors

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 文本与公式

   chapters/ch03/text-and-paragraph
   chapters/ch03/markup-text
   chapters/ch03/tex-and-mathtex
   chapters/ch03/typst
   chapters/ch03/text-compare
   chapters/ch03/numbers
   chapters/ch03/lists-and-title
   chapters/ch03/code-highlight
   chapters/ch03/tex-templates

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 坐标系与数据可视化

   chapters/ch04/number-line
   chapters/ch04/scales
   chapters/ch04/axes-family
   chapters/ch04/function-graphs
   chapters/ch04/probability-and-charts
   chapters/ch04/matrices
   chapters/ch04/tables
   chapters/ch04/vector-space-scenes

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 动画进阶

   chapters/ch05/animation-mechanism
   chapters/ch05/creation
   chapters/ch05/grow-and-fade
   chapters/ch05/transforms
   chapters/ch05/matching-transforms
   chapters/ch05/composition
   chapters/ch05/updaters
   chapters/ch05/number-animations
   chapters/ch05/tracing
   chapters/ch05/motion
   chapters/ch05/rotation
   chapters/ch05/indication
   chapters/ch05/speed
   chapters/ch05/rate-functions

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 3D 与摄像机

   chapters/ch06/three-d-scene
   chapters/ch06/three-d-mobjects
   chapters/ch06/polyhedra
   chapters/ch06/moving-camera
   chapters/ch06/zoomed-scene
   chapters/ch06/camera-internals
   chapters/ch06/renderers

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 高级主题

   chapters/ch07/custom-mobjects
   chapters/ch07/custom-animations
   chapters/ch07/plugins
   chapters/ch07/config-deep-dive
   chapters/ch07/performance
   chapters/ch07/cli-deep-dive
   chapters/ch07/scripting
   chapters/ch07/utils-overview
   chapters/ch07/misc

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 站内

   api-index
   inheritance-graph
   glossary

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: API 参考（全类）

   api/index
