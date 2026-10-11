向量场可视化
============


``VectorField`` 一族把向量值函数 ``f(x, y) → (dx, dy)`` 可视化：在网格上采样并画出每个采样点处的向量或流向线，讲解微分方程、梯度场、流场时的利器。

VectorField
-----------

.. autoclass:: manim.VectorField
   :noindex:


``VectorField`` 是所有向量场的基类：传入函数 ``func`` 后按默认网格采样。``color_scheme`` 可把向量模长映射为颜色（蓝 → 绿 → 黄 → 红），``nudge()`` / ``get_nudge_updater()`` 让任意 mobject 沿场线漂移，``start_submobject_movement()`` 则让场里的所有向量自己流动起来。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "VectorField" [label="VectorField", URL="/chapters/ch04/vector-fields.html#vectorfield"];
     "VGroup" [label="VGroup", URL="/chapters/ch02/groups.html#vgroup"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "VectorField" -> "VGroup";
     "VGroup" -> "VMobject";
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
      * - ``func``
        - Callable[[Point3D], Vector3D]
        - —
        - 向量值函数
      * - ``color_scheme``
        - Callable | None
        - None
        - 向量 → [0,1] 颜色映射
      * - ``min/max_color_scheme_value``
        - float
        - 0 / 2
        - 颜色映射的值域
      * - ``colors``
        - Sequence[color]
        - 蓝→绿→黄→红
        - 渐变的取色序列

ArrowVectorField
----------------

.. autoclass:: manim.ArrowVectorField
   :noindex:


``ArrowVectorField`` 用箭头画出每个采样点的向量（``VectorField`` 的直线版更轻量，箭头版更直观）。``x_range`` / ``y_range`` / ``z_range`` 控制采样网格。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "ArrowVectorField" [label="ArrowVectorField", URL="/chapters/ch04/vector-fields.html#arrowvectorfield"];
     "VectorField" [label="VectorField", URL="/chapters/ch04/vector-fields.html#vectorfield"];
     "VGroup" [label="VGroup", URL="/chapters/ch02/groups.html#vgroup"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "ArrowVectorField" -> "VectorField";
     "VectorField" -> "VGroup";
     "VGroup" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


StreamLines
-----------

.. autoclass:: manim.StreamLines
   :noindex:


``StreamLines`` 不画向量，而是撒下一大批虚拟粒子，沿场方向积分出**流线**，用 Create 播放即可获得流体动画。``virtual_time`` / ``dt`` 控制积分步长与总时长，``noise_factor`` 给起点加扰动让线条分布更自然。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "StreamLines" [label="StreamLines", URL="/chapters/ch04/vector-fields.html#streamlines"];
     "VectorField" [label="VectorField", URL="/chapters/ch04/vector-fields.html#vectorfield"];
     "VGroup" [label="VGroup", URL="/chapters/ch02/groups.html#vgroup"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "StreamLines" -> "VectorField";
     "VectorField" -> "VGroup";
     "VGroup" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. demo:: examples/ch04/vector_fields.py VectorFieldDemo

   旋转场（``(-y, x)``）上的 ``ArrowVectorField`` 与 ``StreamLines``：箭头指方向，流线展示完整轨迹。

.. admonition:: 提示
   :class: tip

   ``StreamLines`` 的采样密度由 x/y_range 的步长决定（步长越小线越密），渲染时间也随之增长；讲解用场取步长 0.5~1 即可。
