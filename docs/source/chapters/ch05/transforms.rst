
Transform 家族
==============


``Transform`` 是 Manim 的灵魂：让物体 A 逐步"变成"物体 B。本节覆盖三个常用变换三兄弟、两组状态记忆（ ``MoveToTarget``/``Restore`` ）、一组方法动画（ ``Apply*`` ）、位置交换与渐隐变换。

Transform
---------

.. autoclass:: manim.Transform
   :noindex:


``Transform(mobject, target_mobject, ...)`` 把物体原地变形为目标的样子： **结束后场景里是原物体** （已变成目标的形态），目标物体本身并不加入场景。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Transform" [label="Transform", URL="/chapters/ch05/transforms.html#transform"];
     "Animation" [label="Animation", URL="/chapters/ch05/animation-mechanism.html#animation"];
     "object" [label="object"];
     "Transform" -> "Animation";
     "Animation" -> "object";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``target_mobject``
        - `Mobject </chapters/ch02/mobject-core.html#mobject>`__ | None
        - None
        - 要变成的目标
      * - ``path_func``
        - Callable | None
        - None
        - 每个点的运动路线函数；None 时由 ``path_arc`` 决定
      * - ``path_arc``
        - float
        - 0
        - 路线为圆弧时的弧度；非 0 时各点沿圆弧走
      * - ``path_arc_axis``
        - np.ndarray
        - `OUT <https://docs.manim.community/en/v0.21.0/reference/manim.constants.html#manim.constants.OUT>`__
        - 圆弧轴向
      * - ``path_arc_centers``
        - :class:`manim.typing.Point3DLike` 等 | None
        - None
        - 各点分别绕指定圆心转弧
      * - ``replace_mobject_with_target_in_scene``
        - bool
        - False
        - True 时结束后用目标物替换原物入场景


``path_func`` 决定点从起点到终点"走哪条路"，常用取值是 ``manim.utils.paths`` 里的路径函数（ ``straight_path`` 、 ``path_along_arc`` 、 ``clockwise_path`` 等），它们在"运动变形"一节有完整表格。改变路线不改变起止状态：绕多大的弧，终点都精确落在目标态。

ReplacementTransform
--------------------

.. autoclass:: manim.ReplacementTransform
   :noindex:


``ReplacementTransform(mobject, target_mobject)`` ：场景效果与 ``Transform`` 几乎一致，区别在于 **结束后场景里保留的是目标物体** （原物体被移除）。想继续操作变换结果时用更顺手——拿到的就是 ``target_mobject`` 本身。

TransformFromCopy
-----------------

.. autoclass:: manim.TransformFromCopy
   :noindex:


``TransformFromCopy(mobject, target_mobject)`` ：以 ``mobject`` 为模板 **复制出一份** 变成目标，原物体原封不动留在场景。等于 ``Transform`` + "保留原件"，常用于"由已知推出新结论"的推导演示。

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 类
        - 结束后场景里是谁
        - 原物体
        - 典型场景
      * - `Transform </chapters/ch05/transforms.html#transform>`__
        - 原物体（已变形）
        - 变形为目标
        - 一般变形
      * - `ReplacementTransform </chapters/ch05/transforms.html#replacementtransform>`__
        - 目标物体
        - 被替换移除
        - 要继续操作结果
      * - `TransformFromCopy </api/animation.html#transformfromcopy>`__
        - 原物体 + 新生成的目标
        - 保留
        - 推导、复制出新对象


.. demo:: examples/ch05/transform_basics.py TransformBasics

   正方形 ``Transform`` 成圆、 ``ReplacementTransform`` 成三角形、 ``TransformFromCopy`` 复制出第二个圆；随后 ``MoveToTarget`` 就位与 ``Restore`` 还原。


ClockwiseTransform
------------------

.. autoclass:: manim.ClockwiseTransform
   :noindex:


``ClockwiseTransform(mobject, target_mobject, path_arc=-PI)`` ： ``Transform`` 的变体，各点沿 **顺时针** 半圆弧到达目标（默认 ``path_arc=-PI`` ，可改弧度）。

CounterclockwiseTransform
-------------------------

.. autoclass:: manim.CounterclockwiseTransform
   :noindex:


``CounterclockwiseTransform(mobject, target_mobject, path_arc=PI)`` ：同上，方向为 **逆时针** 。两者常用于强调"翻过去"的变换感，也可通过 ``Transform(..., path_arc=...)`` 等效实现。

MoveToTarget
------------

.. autoclass:: manim.MoveToTarget
   :noindex:


``MoveToTarget(mobject)`` 把物体变换到它的 ``target`` 属性所记录的状态。 ``target`` 不会自动出现，必须先调用：

.. code-block:: python

   circle.generate_target()        # 生成一份副本存到 circle.target
   circle.target.shift(RIGHT * 2).scale(0.5)  # 在这份副本上布置终态
   self.play(MoveToTarget(circle))


.. admonition:: 常见错误
   :class: warning

   忘记 ``generate_target()`` 就直接 ``MoveToTarget(m)`` 会在渲染时崩溃（本机 v0.21.0 实测报 ``NotImplementedError: get_point_mobject not implemented for Mobject`` ；官方 docstring 声明的校验是 ``ValueError`` ）。养成"先 ``generate_target`` 、改 ``target`` 、再播放"的三步习惯。


Restore
-------

.. autoclass:: manim.Restore
   :noindex:


``Restore(mobject)`` 把物体还原到 ``save_state()`` 时记录的状态：

.. code-block:: python

   square.save_state()
   self.play(square.animate.shift(RIGHT * 2))   # 随便折腾
   self.play(Restore(square))                   # 一键还原


``save_state()`` 把当前状态副本存进 ``saved_state`` 属性，可反复 ``Restore`` 。

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 机制
        - 记录什么
        - 怎么改终态
        - 还原/变换
      * - ``generate_target`` + `MoveToTarget </api/animation.html#movetotarget>`__
        - 一份可编辑的目标副本
        - 直接改 ``m.target`` 的属性
        - 只去不回
      * - ``save_state`` + `Restore </api/animation.html#restore>`__
        - 当前状态的快照
        - 不需要（快照即终态）
        - 去了还能回


ApplyMethod
-----------

.. autoclass:: manim.ApplyMethod
   :noindex:


``ApplyMethod(method, *args, **kwargs)`` 以"方法 + 参数"的形式播放任意 mobject 方法动画，等价于 ``.animate`` 的前身写法：

.. code-block:: python

   self.play(ApplyMethod(square.shift, LEFT * 2, run_time=1))
   # 等价于
   self.play(square.animate.shift(LEFT * 2), run_time=1)


新方法优先用 ``.animate`` ； ``ApplyMethod`` 适合方法名在运行时才确定的场景。

ApplyFunction
-------------

.. autoclass:: manim.ApplyFunction
   :noindex:


``ApplyFunction(function, mobject)`` 把 ``function(m)`` 的返回值作为终态做平滑变换——适合"目标状态不方便用链式方法表达"的自定义形变，如 ``lambda m: m.scale(1.5).set_color(YELLOW)`` 。

ApplyMatrix
-----------

.. autoclass:: manim.ApplyMatrix
   :noindex:


``ApplyMatrix(matrix, mobject, about_point=ORIGIN)`` 让每个点左乘 ``matrix`` 到达新位置，默认绕原点。旋转 90° 就是 ``np.array([[0,-1,0],[1,0,0],[0,0,1]])`` 。

ApplyComplexFunction
--------------------

.. autoclass:: manim.ApplyComplexFunction
   :noindex:


``ApplyComplexFunction(function, mobject)`` ： ``ApplyFunction`` 的复数特化， ``function(z: complex) -> complex`` 把每个点当作复平面上的数做共形映射（如 ``lambda z: z**2`` ），保角不变形好看。

ApplyPointwiseFunction
----------------------

.. autoclass:: manim.ApplyPointwiseFunction
   :noindex:


``ApplyPointwiseFunction(function, mobject, run_time=3.0)`` ：对每个点独立施加 ``function(point) -> point`` 。注意默认 ``run_time=3.0`` 明显偏长，且逐点独立映射可能撕裂轮廓，复杂形变可考虑 ``Homotopy`` （见"运动变形"一节）。

ApplyPointwiseFunctionToCenter
------------------------------

.. autoclass:: manim.ApplyPointwiseFunctionToCenter
   :noindex:


``ApplyPointwiseFunctionToCenter(function, mobject)`` ：只把 ``function`` 施加到物体中心，物体整体平移过去、内部形状保持不变——相当于"由中心决定的自定义 ``shift``"。

.. demo:: examples/ch05/transform_path_func.py TransformPathFunc

   ``ApplyMethod`` 播方法、 ``ApplyFunction`` 自定义终态、 ``ApplyMatrix`` 旋转 90°；最后 ``Swap`` 两物换位、 ``CyclicReplace`` 三物循环换。


CyclicReplace
-------------

.. autoclass:: manim.CyclicReplace
   :noindex:


``CyclicReplace(*mobjects, path_arc=PI/2)`` 让多个物体沿圆弧 **循环** 交换位置：A→B 的位置、B→C 的位置、……最后一只回到 A 的位置（默认各绕 90° 弧）。

Swap
----

.. autoclass:: manim.Swap
   :noindex:


``Swap(*mobjects, path_arc=PI/2)`` 是 ``CyclicReplace`` 的别名同族，语义相同——多只物体沿弧轮换位置。两只物体时就是最常见的"对调"。

ScaleInPlace
------------

.. autoclass:: manim.ScaleInPlace
   :noindex:


``ScaleInPlace(mobject, scale_factor)`` 绕物体自身中心缩放，等价于 ``m.animate.scale(factor)`` 但可嵌入组合动画。

ShrinkToCenter
--------------

.. autoclass:: manim.ShrinkToCenter
   :noindex:


``ShrinkToCenter(mobject)`` 缩向中心的离场动画，等价于"以中心为基准缩到 0"的 ``ScaleInPlace(m, 0)`` 。

TransformAnimations
-------------------

.. autoclass:: manim.TransformAnimations
   :noindex:


``TransformAnimations(start_anim, end_anim, rate_func=squish_rate_func(smooth, 0.25, 1))`` 把 **一段动画变成另一段动画** ：不是变形物体，而是把两个动画本身当作变换两端（常用于开场镜头转换）。默认速率函数会把前 25% 的时间压掉，让衔接更利落。

FadeTransform
-------------

.. autoclass:: manim.FadeTransform
   :noindex:


``FadeTransform(mobject, target_mobject, stretch=True, dim_to_match=1)`` ：与 ``Transform`` 的"原地变形"不同，它是 **先淡出原物、再淡入目标物** 的交叉过渡，两个状态差异很大时（例如形状、子结构完全不同）比 ``Transform`` 更自然。 ``stretch`` 控制是否拉伸对齐尺寸， ``dim_to_match`` 指定按哪个维度对齐。

.. admonition:: 提示
   :class: tip

   ``FadeTransform``/``FadeTransformPieces``/``FadeToColor`` 都在 ``manim.animation.transform`` 模块，不在 ``fading`` 模块——按名字找源码时容易找错地方。


FadeTransformPieces
-------------------

.. autoclass:: manim.FadeTransformPieces
   :noindex:


``FadeTransformPieces(mobject, target_mobject, ...)`` ：按 **子对象一一对应** 做淡入淡出变换（内部用 ``FadeTransform`` 配对），VGroup 结构相似但成员不同时比整体 ``Transform`` 效果更好。

FadeToColor
-----------

.. autoclass:: manim.FadeToColor
   :noindex:


``FadeToColor(mobject, color)`` 把物体颜色平滑过渡到目标色的便捷动画（ ``Transform`` 到"同色副本"的封装）。

.. demo:: examples/ch05/fade_transform.py FadeTransformDemo

   ``FadeTransform`` 让方块交叉过渡成圆； ``FadeTransformPieces`` 让四个方块逐个变成圆；最后 ``FadeToColor`` 整体换色。


自测
----


.. dropdown:: ✏️ 练习

   ``self.play(Transform(a, b))`` 之后，场景里保存的是 a 还是 b？如果后面想继续对"变换结果"做动画，用哪个更合适？

   .. dropdown:: ✅ 参考答案

      场景里是 **a** （a 已变形为 b 的样子），b 本身没有进场景。若后续要操作结果，用 ``ReplacementTransform(a, b)`` 更顺手——结束后场景里就是 b，直接对它继续 ``play`` 即可。


.. dropdown:: ✏️ 练习

   ``save_state``/``Restore`` 与 ``generate_target``/``MoveToTarget`` 都能"让物体去到某个状态"，什么情况下必须用前者？

   .. dropdown:: ✅ 参考答案

      需要 **去了又回** 的场景：先 ``save_state()`` 留快照，任意折腾后用 ``Restore`` 一键还原。 ``MoveToTarget`` 是单向的，且终态要事先在 ``target`` 副本上摆好； ``Restore`` 的快照就是"回去的终点"，无需再编辑。


下一步
------


整体变形之外，还有一类"有脑子的变换"——能自动匹配两物体的组成部分，让相同的部分原地保留、不同的部分精准对换：匹配变换。
