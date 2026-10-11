
追踪与边界
==========


"拖尾轨迹"和"流动边框"是讲解演示中最常用的两类装饰效果： ``TracedPath`` 记录一个点的运动轨迹， ``AnimatedBoundary`` 给图形加上不断流动的彩色描边。

TracedPath
----------

.. autoclass:: manim.TracedPath
   :noindex:


``TracedPath(traced_point_func)`` 是一条特殊的 ``VMobject`` ：内部维护一个 updater，每帧取 **当前点** 追加到自身点列，从而把"某个点的运动路径"画出来。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "TracedPath" [label="TracedPath", URL="/chapters/ch05/tracing.html#tracedpath"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "TracedPath" -> "VMobject";
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
      * - ``traced_point_func``
        - Callable
        - —
        - 返回一个点坐标的函数；通常传 **方法引用** 如 ``dot.get_center`` （不要加括号）
      * - ``stroke_width``
        - float
        - 2
        - 轨迹线宽
      * - ``stroke_color``
        - color | None
        - :class:`manim.utils.color.manim_colors.WHITE`
        - 轨迹颜色；None 表示不描边
      * - ``dissipating_time``
        - float | None
        - None
        - 消散时长：超过该时间的轨迹段逐渐消失；None 表示永久保留


AnimatedBoundary
----------------

.. autoclass:: manim.AnimatedBoundary
   :noindex:


``AnimatedBoundary(vmobject)`` 给目标图形生成一圈 **流动的彩色描边** ：多层颜色不同的描边依次显现、消失，形成"边界在流动"的视觉效果。它本身是一个 ``VGroup`` ，由若干描边副本组成。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "AnimatedBoundary" [label="AnimatedBoundary", URL="/chapters/ch05/tracing.html#animatedboundary"];
     "VGroup" [label="VGroup", URL="/chapters/ch02/groups.html#vgroup"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "AnimatedBoundary" -> "VGroup";
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
      * - ``colors``
        - Sequence[color]
        - 四种蓝灰色
        - 参与流动的描边颜色
      * - ``max_stroke_width``
        - float
        - 3
        - 描边最大线宽
      * - ``cycle_rate``
        - float
        - 0.5
        - 每层颜色完成一次显现/消失的速率
      * - ``back_and_forth``
        - bool
        - True
        - 线宽是否来回脉动


.. demo:: examples/ch05/tracing.py TracingAndBoundary

   ``TracedPath`` 让黄点绕圆一周的轨迹留下 2 秒渐散的拖尾； ``AnimatedBoundary`` 给右侧正方形加上流动的蓝灰描边。


.. admonition:: 常见错误
   :class: warning

   ``TracedPath`` 必须先 ``self.add(...)`` 进场景，否则它的 updater 不会执行，画面里只有运动、没有轨迹。另外传点函数时写成 ``dot.get_center`` （方法引用）而不是 ``dot.get_center()`` （调用结果）——后者只记录了添加那一刻的位置，轨迹变成一条死线。


.. admonition:: 提示
   :class: tip

   ``TracedPath`` 常与 ``MoveAlongPath`` 、Rotating 或 updater 驱动的点搭配：先创建会动的点，再让轨迹跟随它。 ``dissipating_time`` 适合表现"最近路径"，设为 ``None`` 则适合保留完整轨迹（如几何作图）。


自测
----


.. dropdown:: ✏️ 练习

   想记录一个点的完整运动轨迹并永久保留， ``TracedPath`` 应该怎么配置？

   .. dropdown:: ✅ 参考答案

      ``self.add(TracedPath(dot.get_center, dissipating_time=None))`` （ ``dissipating_time`` 默认就是 None，即永久保留），确保轨迹对象被 add 进场景即可。


.. dropdown:: ✏️ 练习

   为什么 ``TracedPath(dot.get_center())`` 画不出轨迹？

   .. dropdown:: ✅ 参考答案

      ``dot.get_center()`` 是 **调用** ，传入的是添加那一刻的一个坐标值，不是"每帧取点"的函数。应传方法引用 ``dot.get_center`` ，轨迹对象每帧自己调用它取当前位置。


下一步
------


轨迹让"走过的路"可见，下一节让物体沿任意路径运动、或被任意形变： ``MoveAlongPath`` 与 ``Homotopy`` 家族。
