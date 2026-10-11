
VMobject
========


``VMobject`` （Vectorized Mobject，矢量对象）在 ``Mobject`` 的基础上增加了矢量渲染所需的 **填充、描边与光泽** 等样式。绝大多数二维图形（圆、多边形、曲线、文字轮廓）都是它的子孙。

VMobject
--------

.. autoclass:: manim.VMobject
   :noindex:


``VMobject`` 是矢量图形的基类：它用一系列三次贝塞尔曲线（锚点 + 控制点）描述轮廓，渲染时按 **填充（fill）→ 背景描边（background stroke）→ 描边（stroke）** 的顺序绘制。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }



.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``fill_color``
        - `ParsableManimColor <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor>`__ | None
        - None
        - 填充色；None 时跟随 ``color``
      * - ``fill_opacity``
        - float
        - 0.0
        - 填充不透明度，默认 0 即 **不填充**
      * - ``stroke_color``
        - `ParsableManimColor <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor>`__ | None
        - None
        - 描边色；None 时跟随 ``color``
      * - ``stroke_opacity``
        - float
        - 1.0
        - 描边不透明度
      * - ``stroke_width``
        - float
        - 4
        - 描边宽度
      * - ``background_stroke_color``
        - `ParsableManimColor <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor>`__ | None
        - `BLACK <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.manim_colors.html>`__
        - 背景描边颜色（垫在填充下面）
      * - ``background_stroke_opacity``
        - float
        - 1.0
        - 背景描边不透明度
      * - ``background_stroke_width``
        - float
        - 0
        - 背景描边宽度，默认 0 即关闭
      * - ``sheen_factor``
        - float
        - 0.0
        - 光泽强度：颜色向白色渐变的程度
      * - ``sheen_direction``
        - `Vector3DLike <https://docs.manim.community/en/v0.21.0/reference/manim.typing.html#manim.typing.Vector3DLike>`__
        - (-1, 1, 0)
        - 光泽渐变方向
      * - ``close_new_points``
        - bool
        - False
        - 新增的点是否自动闭合成环
      * - ``cap_style``
        - `CapStyleType </api/core.html#capstyletype>`__
        - AUTO
        - 开放曲线端点的样式（AUTO/BUTT/ROUND/SQUARE）


与 ``Mobject`` 相比， ``VMobject`` 增加了三个核心样式方法：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 方法
        - 签名
        - 说明
      * - ``set_fill``
        - ``(color=None, opacity=None, family=True)``
        - 设置填充色与不透明度； ``family=True`` 时递归作用到所有子对象
      * - ``set_stroke``
        - ``(color=None, width=None, opacity=None, background=False, family=True)``
        - 设置描边； ``background=True`` 时操作背景描边
      * - ``set_opacity``
        - ``(opacity, family=True)``
        - 同时设置填充与描边的不透明度


三个对象的填充/描边对比：

.. demo:: examples/ch02/vmobject_styles.py VMobjectStyles

   左：仅填充（描边宽 0）；中：仅描边（填充透明）；右：半透明填充 + 细描边。最后一帧整组 ``set_opacity(0.4)`` 一起变淡。


.. admonition:: 常见错误
   :class: warning

   ``set_fill(BLUE)`` 只会改颜色， **不会** 让图形填上颜色——默认 ``fill_opacity`` 仍是 0。要看到填充必须给不透明度，如 ``set_fill(BLUE, opacity=0.7)`` ，或构造时传 ``fill_opacity=0.7`` 。


.. admonition:: 提示
   :class: tip

   ``background_stroke`` 常用来给文字或细线在复杂背景上“描白边”垫底：设置 ``background_stroke_color=BLACK, background_stroke_width=8`` 即可。


DashedVMobject
--------------

.. autoclass:: manim.DashedVMobject
   :noindex:


``DashedVMobject`` 把任意 ``VMobject`` 转换成 **等长的虚线段集合** ，原对象不会被修改（内部使用拷贝）。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "DashedVMobject" [label="DashedVMobject", URL="/api/types.html#dashedvmobject"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "DashedVMobject" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }



.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``vmobject``
        - `VMobject </chapters/ch02/vmobject.html#vmobject>`__
        - —
        - 要虚线化的对象（必填）
      * - ``num_dashes``
        - int
        - 15
        - 虚线段数量
      * - ``dashed_ratio``
        - float
        - 0.5
        - 虚线总长度占整个轮廓的比例（0~1）
      * - ``dash_offset``
        - float
        - 0
        - 虚线相位偏移（按 0~1 的周期比例）
      * - ``color``
        - `ManimColor </api/utils.html#manimcolor>`__
        - `WHITE <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.manim_colors.html>`__
        - 虚线颜色
      * - ``equal_lengths``
        - bool
        - True
        - 是否强制每段等长；曲线弯折处建议保持 True


.. demo:: examples/ch02/dashed_demo.py DashedDemo

   上半部分： ``Circle`` 经 ``DashedVMobject`` 变成 20 段虚线；下半部分： ``CurvesAsSubmobjects`` 把正弦曲线拆成子对象后按蓝→红渐变着色。


.. admonition:: 常见错误
   :class: warning

   虚线化后想改段数，应重新构造 ``DashedVMobject(mob, num_dashes=30)`` ，而不是修改已生成对象的 ``num_dashes`` 属性——构造函数已经把曲线切成了固定段数。


CurvesAsSubmobjects
-------------------

.. autoclass:: manim.CurvesAsSubmobjects
   :noindex:


``CurvesAsSubmobjects`` 把一条曲线的 **每一段曲线元素拆成独立子对象** ，从而可以对同一条曲线分段着色（例如整体渐变）。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "CurvesAsSubmobjects" [label="CurvesAsSubmobjects", URL="/api/types.html#curvesassubmobjects"];
     "VGroup" [label="VGroup", URL="/chapters/ch02/groups.html#vgroup"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "CurvesAsSubmobjects" -> "VGroup";
     "VGroup" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   CurvesAsSubmobjects(vmobject: VMobject, **kwargs)


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``vmobject``
        - `VMobject </chapters/ch02/vmobject.html#vmobject>`__
        - —
        - 要拆分的曲线（必填）
      * - ``kwargs``
        - —
        - —
        - 转发给 `VGroup </chapters/ch02/groups.html#vgroup>`__ 构造


典型用法： ``CurvesAsSubmobjects(curve).set_color_by_gradient(BLUE, RED)`` 。若不拆分， ``set_color_by_gradient`` 只会按曲线上的位置插值，效果与拆分后不同；拆分成子对象后每个子对象取自己区间内的渐变色。

VectorizedPoint
---------------

.. autoclass:: manim.VectorizedPoint
   :noindex:


``VectorizedPoint`` 是一个 **不可见的定位辅助点** ：默认填充、描边全为 0，画面上看不见，但它有 ``artificial_width`` / ``artificial_height`` ，能正常参与 ``next_to`` 、 ``move_to`` 等布局计算。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "VectorizedPoint" [label="VectorizedPoint", URL="/api/types.html#vectorizedpoint"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "VectorizedPoint" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }



.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``location``
        - `Point3DLike <https://docs.manim.community/en/v0.21.0/reference/manim.typing.html#manim.typing.Point3DLike>`__
        - `ORIGIN <https://docs.manim.community/en/v0.21.0/reference/manim.constants.html#manim.constants.ORIGIN>`__
        - 点的位置
      * - ``color``
        - `ManimColor </api/utils.html#manimcolor>`__
        - `BLACK <https://docs.manim.community/en/v0.21.0/reference/manim.utils.color.manim_colors.html>`__
        - 颜色（默认不可见，改色也看不出）
      * - ``fill_opacity``
        - float
        - 0
        - 填充不透明度
      * - ``stroke_width``
        - float
        - 0
        - 描边宽度
      * - ``artificial_width``
        - float
        - 0.01
        - 参与布局计算的“假宽度”
      * - ``artificial_height``
        - float
        - 0.01
        - 参与布局计算的“假高度”


.. demo:: examples/ch02/vectorized_point_demo.py VectorizedPointDemo

   红色的 ``VectorizedPoint(2 * RIGHT)`` 在画面中不可见，但 ``Square().next_to(anchor, RIGHT)`` 以它为参照完成了定位。


.. admonition:: 常见错误
   :class: warning

   ``VectorizedPoint`` **天生不可见**——构造出来却“找不到它”不是 bug。它适合当隐藏的锚点；想要看得见的点请用 ``Dot`` 。


自测
----


.. dropdown:: ✏️ 练习

   ``set_fill(RED)`` 之后图形仍然只有边框没有红色填充，为什么？

   .. dropdown:: ✅ 参考答案

      ``set_fill`` 只设置了填充颜色， ``fill_opacity`` 仍是默认的 0（完全透明）。需要写成 ``set_fill(RED, opacity=0.7)`` 或 ``set_fill(RED, 0.7)`` 。


.. dropdown:: ✏️ 练习

   如何给一条 ``ParametricFunction`` 曲线做出“从头到尾由蓝变红”的效果？为什么直接对原曲线 ``set_color_by_gradient`` 效果不理想？

   .. dropdown:: ✅ 参考答案

      用 ``CurvesAsSubmobjects(curve)`` 把曲线拆成子对象，再 ``set_color_by_gradient(BLUE, RED)`` 。拆分前曲线是单个子对象，渐变按整条曲线的位置插值；拆分后每个曲线段是独立子对象，各自取渐变中对应区间的颜色，分段效果更细腻。



CapStyleType
------------

.. autoclass:: manim.CapStyleType
   :noindex:


``CapStyleType`` 是描边**端点**样式的枚举，作为 ``VMobject`` 的 ``cap_style`` 参数（或 ``set_cap_style()`` 方法）取值：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 成员
        - 效果
      * - ``AUTO``
        - 按渲染器默认值（Cairo 下为 BUTT）
      * - ``ROUND``
        - 端点为半圆，线条末端更圆润
      * - ``BUTT``
        - 端点齐平，线条精确止于端点
      * - ``SQUARE``
        - 端点外扩半个线宽的正方形

LineJointType
-------------

.. autoclass:: manim.LineJointType
   :noindex:


``LineJointType`` 是描边**拐角**样式的枚举，作为 ``VMobject`` 的 ``joint_type`` 参数（或 ``set_joint_type()`` 方法）取值，影响折线在顶点处如何衔接：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 成员
        - 效果
      * - ``AUTO``
        - 按渲染器默认值
      * - ``ROUND``
        - 圆角衔接
      * - ``BEVEL``
        - 切角衔接
      * - ``MITER``
        - 尖角衔接（锐角会向外延伸）

下一步
------


学会了给图形上色，下一节看如何把它们组织起来： ``Group`` 、 ``VGroup`` 与键值容器 ``VDict`` 。
