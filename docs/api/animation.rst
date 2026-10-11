===========================
API 参考：动画（animation）
===========================

共 **76** 个类，按字母排序。每个类含中文说明、继承链、参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；带完整中文精讲的类见 `API 索引 <../api-index.html>`__。

Add
---

把 Mobject 加入场景播放序列的动画：与其他动画组合时控制「何时真正把对象放上来」，常与 Succession 搭配精排时序。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Add";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``run_time``
        - 0.0，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Add(dot))

API 文档
~~~~~~~~

.. autoclass:: manim.Add

AddTextLetterByLetter
---------------------

让 Text 逐字母浮现，每个字母带微小放大效果，模拟打字机输入，可设置每字符耗时。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ShowIncreasingSubsets";
     "ShowIncreasingSubsets" -> "AddTextLetterByLetter";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``text``
        - —，Text
      * - ``suspend_mobject_updating``
        - False，bool
      * - ``int_func``
        - <ufunc 'ceil'>
      * - ``rate_func``
        - <function linear at 0x00000…，Callable[[float], float]
      * - ``time_per_char``
        - 0.1，float
      * - ``run_time``
        - None，float | None
      * - ``reverse_rate_function``
        - False
      * - ``introducer``
        - True

快速上手
~~~~~~~~

.. code-block:: python

   self.play(AddTextLetterByLetter(text))

API 文档
~~~~~~~~

.. autoclass:: manim.AddTextLetterByLetter

AddTextWordByWord
-----------------

让 Text 逐词浮现，按空格分词，适合字幕式进场。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "Succession";
     "Succession" -> "AddTextWordByWord";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``text_mobject``
        - —，Text
      * - ``run_time``
        - None，float
      * - ``time_per_char``
        - 0.06，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(AddTextWordByWord(text))

API 文档
~~~~~~~~

.. autoclass:: manim.AddTextWordByWord

AnimatedBoundary
----------------

围绕 VMobject 持续流动的虚线边界动画，常用于高亮某个对象「正在被讨论」。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "VGroup";
     "VGroup" -> "AnimatedBoundary";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vmobject``
        - —，VMobject
      * - ``colors``
        - [ManimColor('#29ABCA'), Man…
      * - ``max_stroke_width``
        - 3，float
      * - ``cycle_rate``
        - 0.5，float
      * - ``back_and_forth``
        - True，bool
      * - ``draw_rate_func``
        - <function smooth at 0x00000…，RateFunction
      * - ``fade_rate_func``
        - <function smooth at 0x00000…，RateFunction

快速上手
~~~~~~~~

.. code-block:: python

   self.add(AnimatedBoundary(circle))

API 文档
~~~~~~~~

.. autoclass:: manim.AnimatedBoundary

Animation
---------

一切动画的基类。自定义动画时继承它并实现 interpolate()：给定 alpha（0 到 1）描述画面状态。

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —
      * - ``lag_ratio``
        - 0.0，float
      * - ``run_time``
        - 1.0，float
      * - ``rate_func``
        - <function smooth at 0x00000…，Callable[[float], float]
      * - ``reverse_rate_function``
        - False，bool
      * - ``name``
        - None，str
      * - ``remover``
        - False，bool
      * - ``suspend_mobject_updating``
        - True，bool
      * - ``introducer``
        - False，bool
      * - ``_on_finish``
        - <function Animation.<lambda…，Callable[[Scene], None]
      * - ``use_override``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   class Fade(Animation):
       def interpolate(self, alpha):
           self.mobject.set_opacity(alpha)

API 文档
~~~~~~~~

.. autoclass:: manim.Animation

AnimationGroup
--------------

把多个动画打包同时播放，可用 lag_ratio 让组内动画依次错开，是最常用的复合动画容器。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``group``
        - None
      * - ``run_time``
        - None，float | None
      * - ``rate_func``
        - <function linear at 0x00000…，Callable[[float], float]
      * - ``lag_ratio``
        - 0，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(AnimationGroup(FadeIn(a), GrowFromCenter(b), lag_ratio=0.5))

API 文档
~~~~~~~~

.. autoclass:: manim.AnimationGroup

ApplyComplexFunction
--------------------

把复变函数作用到每个点的复坐标上，适合做共形变换等复分析可视化。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ApplyMethod";
     "ApplyMethod" -> "ApplyComplexFunction";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``function``
        - —，types.MethodType
      * - ``mobject``
        - —，Mobject

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ApplyComplexFunction(lambda z: z**2, plane))

API 文档
~~~~~~~~

.. autoclass:: manim.ApplyComplexFunction

ApplyFunction
-------------

用任意函数逐点变形 Mobject：先复制再插值到新形状，直观展示函数对图形的变换效果。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ApplyFunction";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``function``
        - —，types.MethodType
      * - ``mobject``
        - —，Mobject

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ApplyFunction(lambda m: m.shift(UP), mob))

API 文档
~~~~~~~~

.. autoclass:: manim.ApplyFunction

ApplyMatrix
-----------

用 2×2 矩阵对平面做线性变换，传入 numpy 矩阵即可，线性代数课的标配。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ApplyMethod";
     "ApplyMethod" -> "ApplyPointwiseFunction";
     "ApplyPointwiseFunction" -> "ApplyMatrix";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``matrix``
        - —，np.ndarray
      * - ``mobject``
        - —，Mobject
      * - ``about_point``
        - array([0., 0., 0.])，np.ndarray

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ApplyMatrix([[1, 1], [0, 1]], square))

API 文档
~~~~~~~~

.. autoclass:: manim.ApplyMatrix

ApplyMethod
-----------

把任意 Mobject 方法（如 shift、set_color）包装成动画播放，是 mobject.animate 语法的底层实现。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ApplyMethod";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``method``
        - —，Callable

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ApplyMethod(dot.shift, UP))

API 文档
~~~~~~~~

.. autoclass:: manim.ApplyMethod

ApplyPointwiseFunction
----------------------

对曲线上每个点应用 R³ 向量函数，比 ApplyFunction 更底层，直接操作点集。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ApplyMethod";
     "ApplyMethod" -> "ApplyPointwiseFunction";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``function``
        - —，types.MethodType
      * - ``mobject``
        - —，Mobject
      * - ``run_time``
        - 3.0，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ApplyPointwiseFunction(lambda p: p + UP, line))

API 文档
~~~~~~~~

.. autoclass:: manim.ApplyPointwiseFunction

ApplyPointwiseFunctionToCenter
------------------------------

以对象中心为原点应用逐点函数，避免整体平移，适合「原地扭曲」效果。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ApplyMethod";
     "ApplyMethod" -> "ApplyPointwiseFunction";
     "ApplyPointwiseFunction" -> "ApplyPointwiseFunctionToCenter";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``function``
        - —，types.MethodType
      * - ``mobject``
        - —，Mobject

API 文档
~~~~~~~~

.. autoclass:: manim.ApplyPointwiseFunctionToCenter

ApplyWave
---------

让 VMobject 产生沿路径传播的波浪形变，给静态曲线注入流动感。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Homotopy";
     "Homotopy" -> "ApplyWave";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``direction``
        - array([0., 1., 0.])，Vector3DLike
      * - ``amplitude``
        - 0.2，float
      * - ``wave_func``
        - <function smooth at 0x00000…，RateFunction
      * - ``time_width``
        - 1，float
      * - ``ripples``
        - 1，int
      * - ``run_time``
        - 2，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ApplyWave(sine_curve))

API 文档
~~~~~~~~

.. autoclass:: manim.ApplyWave

Blink
-----

让 Mobject 快速闪现再恢复，模拟眨眼或提示性闪烁。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "Succession";
     "Succession" -> "Blink";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``time_on``
        - 0.5，float
      * - ``time_off``
        - 0.5，float
      * - ``blinks``
        - 1，int
      * - ``hide_at_end``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Blink(dot))

API 文档
~~~~~~~~

.. autoclass:: manim.Blink

Broadcast
---------

从中心向外扩散一圈圈涟漪的强调动画，类似水波或雷达扩散。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "LaggedStart";
     "LaggedStart" -> "Broadcast";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``focal_point``
        - array([0., 0., 0.])，Sequence[float]
      * - ``n_mobs``
        - 5，int
      * - ``initial_opacity``
        - 1，float
      * - ``final_opacity``
        - 0，float
      * - ``initial_width``
        - 0.0，float
      * - ``remover``
        - True，bool
      * - ``lag_ratio``
        - 0.2，float
      * - ``run_time``
        - 3，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Broadcast(dot))

API 文档
~~~~~~~~

.. autoclass:: manim.Broadcast

ChangeDecimalToValue
--------------------

把 DecimalNumber 从当前值滚动变化到目标值的动画，数字变动平滑自然。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ChangingDecimal";
     "ChangingDecimal" -> "ChangeDecimalToValue";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``decimal_mob``
        - —，DecimalNumber
      * - ``target_number``
        - —，int

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ChangeDecimalToValue(number, 3.14))

API 文档
~~~~~~~~

.. autoclass:: manim.ChangeDecimalToValue

ChangeSpeed
-----------

包裹一个动画并动态改变其播放速度，speed_func 接收运行进度返回速度倍率。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ChangeSpeed";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``anim``
        - —
      * - ``speedinfo``
        - —，dict[float, float]
      * - ``rate_func``
        - None
      * - ``affects_speed_updaters``
        - True，bool

API 文档
~~~~~~~~

.. autoclass:: manim.ChangeSpeed

ChangingDecimal
---------------

持续变化的数字动画：每次显示当前 ValueTracker 的值，配合 updater 可做实时计数。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ChangingDecimal";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``decimal_mob``
        - —，DecimalNumber
      * - ``number_update_func``
        - —，Callable[[float], float]
      * - ``suspend_mobject_updating``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   number.add_updater(lambda d: d.set_value(tracker.get_value()))

API 文档
~~~~~~~~

.. autoclass:: manim.ChangingDecimal

Circumscribe
------------

在 Mobject 周围画一个强调框（矩形或圆角），默认黄色，用于「注意这里」。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "Succession";
     "Succession" -> "Circumscribe";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``shape``
        - <class 'manim.mobject.geome…
      * - ``fade_in``
        - False，bool
      * - ``fade_out``
        - False，bool
      * - ``time_width``
        - 0.3，float
      * - ``buff``
        - 0.1，float
      * - ``color``
        - ManimColor('#FFFF00')，ParsableManimColor
      * - ``run_time``
        - 1，float
      * - ``stroke_width``
        - 4，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Circumscribe(formula))

API 文档
~~~~~~~~

.. autoclass:: manim.Circumscribe

ClockwiseTransform
------------------

ReplacementTransform 的顺时针变体：路径按顺时针方向插值，适合旋转感的形态变化。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ClockwiseTransform";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``target_mobject``
        - —，Mobject
      * - ``path_arc``
        - -3.141592653589793，float

API 文档
~~~~~~~~

.. autoclass:: manim.ClockwiseTransform

ComplexHomotopy
---------------

复同伦动画：随 t 从 0 到 1 把复平面连续变形，复分析可视化的利器。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Homotopy";
     "Homotopy" -> "ComplexHomotopy";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``complex_homotopy``
        - —
      * - ``mobject``
        - —，Mobject

API 文档
~~~~~~~~

.. autoclass:: manim.ComplexHomotopy

CounterclockwiseTransform
-------------------------

ReplacementTransform 的逆时针变体，与 ClockwiseTransform 对应。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "CounterclockwiseTransform";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``target_mobject``
        - —，Mobject
      * - ``path_arc``
        - 3.141592653589793，float

API 文档
~~~~~~~~

.. autoclass:: manim.CounterclockwiseTransform

Create
------

沿路径绘出 VMobject 的「一笔画」动画，是 ShowPartial 的便捷封装。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ShowPartial";
     "ShowPartial" -> "Create";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —
      * - ``lag_ratio``
        - 1.0，float
      * - ``introducer``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Create(circle))

API 文档
~~~~~~~~

.. autoclass:: manim.Create

CyclicReplace
-------------

把一组 Mobject 沿环置换：A 移到 B 的位置、B 移到 C……最后回到 A，可循环往复。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "CyclicReplace";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``path_arc``
        - 1.5707963267948966，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(CyclicReplace(a, b, c))

API 文档
~~~~~~~~

.. autoclass:: manim.CyclicReplace

DrawBorderThenFill
------------------

先描边再填充的两段式入场动画，兼具 Create 和 FadeIn 的效果，适合大面积图形。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "DrawBorderThenFill";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vmobject``
        - —
      * - ``run_time``
        - 2，float
      * - ``rate_func``
        - <function double_smooth at …，Callable[[float], float]
      * - ``stroke_width``
        - 2，float
      * - ``stroke_color``
        - None，str
      * - ``introducer``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   self.play(DrawBorderThenFill(polygon))

API 文档
~~~~~~~~

.. autoclass:: manim.DrawBorderThenFill

FadeIn
------

淡入动画。可指定 shift、scale、target_position，让对象从某处「长」进画面，是最常用的入场方式。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "FadeIn";
   }

快速上手
~~~~~~~~

.. code-block:: python

   self.play(FadeIn(mob, shift=UP))

API 文档
~~~~~~~~

.. autoclass:: manim.FadeIn

FadeOut
-------

淡出动画，出场首选；常配合 target_position 让对象朝某个点消散。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "FadeOut";
   }

快速上手
~~~~~~~~

.. code-block:: python

   self.play(FadeOut(mob))

API 文档
~~~~~~~~

.. autoclass:: manim.FadeOut

FadeToColor
-----------

平滑地把 Mobject 颜色过渡到目标色，set_color 的动画版。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ApplyMethod";
     "ApplyMethod" -> "FadeToColor";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``color``
        - —，str

快速上手
~~~~~~~~

.. code-block:: python

   self.play(FadeToColor(circle, RED))

API 文档
~~~~~~~~

.. autoclass:: manim.FadeToColor

FadeTransform
-------------

把一个 Mobject 淡出、另一个淡入并占据其位置与样式，介于替换与交叉淡化之间。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "FadeTransform";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``target_mobject``
        - —，Mobject
      * - ``stretch``
        - True，bool
      * - ``dim_to_match``
        - 1，int

API 文档
~~~~~~~~

.. autoclass:: manim.FadeTransform

FadeTransformPieces
-------------------

FadeTransform 的逐子对象版本：按子对象配对交叉淡化，适合家族整体换形。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "FadeTransform";
     "FadeTransform" -> "FadeTransformPieces";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``target_mobject``
        - —，Mobject
      * - ``stretch``
        - True，bool
      * - ``dim_to_match``
        - 1，int

API 文档
~~~~~~~~

.. autoclass:: manim.FadeTransformPieces

Flash
-----

在点或 Mobject 上打出一圈闪光线条的强调动画，视觉焦点效果强。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "Flash";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``point``
        - —，Point3DLike | Mobject
      * - ``line_length``
        - 0.2，float
      * - ``num_lines``
        - 12，int
      * - ``flash_radius``
        - 0.1，float
      * - ``line_stroke_width``
        - 3，int
      * - ``color``
        - ManimColor('#FFFF00')，ParsableManimColor
      * - ``time_width``
        - 1，float
      * - ``run_time``
        - 1.0，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Flash(point))

API 文档
~~~~~~~~

.. autoclass:: manim.Flash

FocusOn
-------

暗化全屏、用光圈聚焦目标点的提示动画，讲解时引导视线。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "FocusOn";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``focus_point``
        - —，Point3DLike | Mobject
      * - ``opacity``
        - 0.2，float
      * - ``color``
        - ManimColor('#888888')，ParsableManimColor
      * - ``run_time``
        - 2，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(FocusOn(dot))

API 文档
~~~~~~~~

.. autoclass:: manim.FocusOn

GrowArrow
---------

让 Arrow 沿自身方向从头生长出来的动画。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "GrowFromPoint";
     "GrowFromPoint" -> "GrowArrow";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``arrow``
        - —，Arrow
      * - ``point_color``
        - None

快速上手
~~~~~~~~

.. code-block:: python

   self.play(GrowArrow(arrow))

API 文档
~~~~~~~~

.. autoclass:: manim.GrowArrow

GrowFromCenter
--------------

从中心向外长大的入场动画，可用于任意 Mobject。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "GrowFromPoint";
     "GrowFromPoint" -> "GrowFromCenter";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``point_color``
        - None

快速上手
~~~~~~~~

.. code-block:: python

   self.play(GrowFromCenter(square))

API 文档
~~~~~~~~

.. autoclass:: manim.GrowFromCenter

GrowFromEdge
------------

从指定边缘向对侧生长的入场动画。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "GrowFromPoint";
     "GrowFromPoint" -> "GrowFromEdge";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``edge``
        - —，Vector3DLike
      * - ``point_color``
        - None

快速上手
~~~~~~~~

.. code-block:: python

   self.play(GrowFromEdge(dot, LEFT))

API 文档
~~~~~~~~

.. autoclass:: manim.GrowFromEdge

GrowFromPoint
-------------

从指定点向外长大的入场动画，配合 Flash 效果极佳。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "GrowFromPoint";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``point``
        - —，Point3DLike
      * - ``point_color``
        - None

快速上手
~~~~~~~~

.. code-block:: python

   self.play(GrowFromPoint(mob, origin))

API 文档
~~~~~~~~

.. autoclass:: manim.GrowFromPoint

Homotopy
--------

同伦动画：传入关于 (x, y, z, t) 的函数，把对象连续形变到目标姿态。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Homotopy";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``homotopy``
        - —
      * - ``mobject``
        - —，Mobject
      * - ``run_time``
        - 3，float
      * - ``apply_function_kwargs``
        - None，dict[str, Any] | None

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Homotopy(lambda x, y, z, t: (x, y + t, z), mob))

API 文档
~~~~~~~~

.. autoclass:: manim.Homotopy

Indicate
--------

轻推一下目标对象（放大再回弹）的提示动画，比 Circumscribe 更含蓄。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "Indicate";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``scale_factor``
        - 1.2，float
      * - ``color``
        - ManimColor('#FFFF00')，ParsableManimColor
      * - ``rate_func``
        - <function there_and_back at…，RateFunction

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Indicate(formula))

API 文档
~~~~~~~~

.. autoclass:: manim.Indicate

LaggedStart
-----------

让一组动画按固定间隔依次启动，start_lag_ratio 控制节奏，是排队式动效的基石。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "LaggedStart";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``lag_ratio``
        - 0.05，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(LaggedStart(*[FadeIn(m) for m in group]))

API 文档
~~~~~~~~

.. autoclass:: manim.LaggedStart

LaggedStartMap
--------------

LaggedStart 的函数式版本：对一组对象统一套用同一种动画并按序启动。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "LaggedStart";
     "LaggedStart" -> "LaggedStartMap";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``animation_class``
        - —，type[Animation]
      * - ``mobject``
        - —，Mobject
      * - ``arg_creator``
        - None
      * - ``run_time``
        - 2，float
      * - ``lag_ratio``
        - 0.05，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(LaggedStartMap(FadeIn, group, lag_ratio=0.1))

API 文档
~~~~~~~~

.. autoclass:: manim.LaggedStartMap

MaintainPositionRelativeTo
--------------------------

让 Mobject 在目标对象动画期间保持相对位置，常配合 ApplyFunction 锁定局部位移。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "MaintainPositionRelativeTo";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``tracked_mobject``
        - —，Mobject

API 文档
~~~~~~~~

.. autoclass:: manim.MaintainPositionRelativeTo

MoveAlongPath
-------------

让 Mobject 沿给定路径（曲线）运动的动画。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "MoveAlongPath";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``path``
        - —，VMobject
      * - ``suspend_mobject_updating``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   self.play(MoveAlongPath(dot, circle))

API 文档
~~~~~~~~

.. autoclass:: manim.MoveAlongPath

MoveToTarget
------------

把 Mobject 移动到其 save_state 的快照位置，与 mob.target / generate_target 配合使用。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "MoveToTarget";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject

快速上手
~~~~~~~~

.. code-block:: python

   mob.generate_target()
   mob.target.shift(RIGHT)
   self.play(MoveToTarget(mob))

API 文档
~~~~~~~~

.. autoclass:: manim.MoveToTarget

PhaseFlow
---------

对向量场（如微分方程相图）随时间演化做形变动画，动力系统可视化工具。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "PhaseFlow";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``function``
        - —
      * - ``mobject``
        - —，Mobject
      * - ``virtual_time``
        - 1，float
      * - ``suspend_mobject_updating``
        - False，bool
      * - ``rate_func``
        - <function linear at 0x00000…，RateFunction

API 文档
~~~~~~~~

.. autoclass:: manim.PhaseFlow

RemoveTextLetterByLetter
------------------------

AddTextLetterByLetter 的反向动画：Text 逐字母消失。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ShowIncreasingSubsets";
     "ShowIncreasingSubsets" -> "AddTextLetterByLetter";
     "AddTextLetterByLetter" -> "RemoveTextLetterByLetter";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``text``
        - —，Text
      * - ``suspend_mobject_updating``
        - False，bool
      * - ``int_func``
        - <ufunc 'ceil'>
      * - ``rate_func``
        - <function linear at 0x00000…，Callable[[float], float]
      * - ``time_per_char``
        - 0.1，float
      * - ``run_time``
        - None，float | None
      * - ``reverse_rate_function``
        - True
      * - ``introducer``
        - False
      * - ``remover``
        - True

API 文档
~~~~~~~~

.. autoclass:: manim.RemoveTextLetterByLetter

ReplacementTransform
--------------------

把一个 Mobject 原位变形替换为另一个，是最强的「变形」动画，两个对象会融合。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ReplacementTransform";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``target_mobject``
        - —，Mobject

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ReplacementTransform(square, circle))

API 文档
~~~~~~~~

.. autoclass:: manim.ReplacementTransform

Restore
-------

让 Mobject 回到 save_state() 保存的状态，常用于「变了再变回去」。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ApplyMethod";
     "ApplyMethod" -> "Restore";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Restore(mob))

API 文档
~~~~~~~~

.. autoclass:: manim.Restore

Rotate
------

绕指定点旋转对象的动画，angle 为正逆时针。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "Rotate";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``angle``
        - 3.141592653589793，float
      * - ``axis``
        - array([0., 0., 1.])，Vector3DLike
      * - ``about_point``
        - None，Point3DLike | None
      * - ``about_edge``
        - None，Vector3DLike | None

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Rotate(square, PI / 2))

API 文档
~~~~~~~~

.. autoclass:: manim.Rotate

Rotating
--------

持续旋转动画：不占用场景时间推进的「边转边讲」，常用于旋转对称演示。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Rotating";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``angle``
        - 6.283185307179586，float
      * - ``axis``
        - array([0., 0., 1.])，Vector3DLike
      * - ``about_point``
        - None，Point3DLike | None
      * - ``about_edge``
        - None，Vector3DLike | None
      * - ``run_time``
        - 5，float
      * - ``rate_func``
        - <function linear at 0x00000…，Callable[[float], float]

快速上手
~~~~~~~~

.. code-block:: python

   self.add(Rotating(square))

API 文档
~~~~~~~~

.. autoclass:: manim.Rotating

ScaleInPlace
------------

原地缩放的强调动画，set(width=...) 类的动画版本。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ApplyMethod";
     "ApplyMethod" -> "ScaleInPlace";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``scale_factor``
        - —，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ScaleInPlace(circle, 1.5))

API 文档
~~~~~~~~

.. autoclass:: manim.ScaleInPlace

ShowIncreasingSubsets
---------------------

让 VGroup 的子对象逐个显示，适合逐步揭示列表或矩阵元素。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ShowIncreasingSubsets";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``group``
        - —，Mobject
      * - ``suspend_mobject_updating``
        - False，bool
      * - ``int_func``
        - <ufunc 'floor'>
      * - ``reverse_rate_function``
        - False

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ShowIncreasingSubsets(group))

API 文档
~~~~~~~~

.. autoclass:: manim.ShowIncreasingSubsets

ShowPartial
-----------

按进度显示路径片段的底层动画，Create 与 Uncreate 的父类，可自定义绘制方向。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ShowPartial";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —

API 文档
~~~~~~~~

.. autoclass:: manim.ShowPartial

ShowPassingFlash
----------------

一道亮斑沿路径扫过的「电流」效果动画，time_width 控制亮斑宽度。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ShowPartial";
     "ShowPartial" -> "ShowPassingFlash";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，VMobject
      * - ``time_width``
        - 0.1，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ShowPassingFlash(line))

API 文档
~~~~~~~~

.. autoclass:: manim.ShowPassingFlash

ShowPassingFlashWithThinningStrokeWidth
---------------------------------------

ShowPassingFlash 的变体：扫过时笔画由粗变细，更像真实书写。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "ShowPassingFlashWithThinningStrokeWidth";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vmobject``
        - —，VMobject
      * - ``n_segments``
        - 10，int
      * - ``time_width``
        - 0.1，float
      * - ``remover``
        - True，bool

API 文档
~~~~~~~~

.. autoclass:: manim.ShowPassingFlashWithThinningStrokeWidth

ShowSubmobjectsOneByOne
-----------------------

把 VGroup 子对象按个显示后再按个移除的序列动画，适合对比展示。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ShowIncreasingSubsets";
     "ShowIncreasingSubsets" -> "ShowSubmobjectsOneByOne";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``group``
        - —，Iterable[Mobject]
      * - ``int_func``
        - <ufunc 'ceil'>

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ShowSubmobjectsOneByOne(group))

API 文档
~~~~~~~~

.. autoclass:: manim.ShowSubmobjectsOneByOne

ShrinkToCenter
--------------

向中心收缩消失的出场动画，FadeOut 的动感替代。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "ApplyMethod";
     "ApplyMethod" -> "ScaleInPlace";
     "ScaleInPlace" -> "ShrinkToCenter";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject

快速上手
~~~~~~~~

.. code-block:: python

   self.play(ShrinkToCenter(mob))

API 文档
~~~~~~~~

.. autoclass:: manim.ShrinkToCenter

SmoothedVectorizedHomotopy
--------------------------

Homotopy 的平滑变体：在变换中保持向量场曲线平滑，减少锯齿。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Homotopy";
     "Homotopy" -> "SmoothedVectorizedHomotopy";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``homotopy``
        - —
      * - ``mobject``
        - —，Mobject
      * - ``run_time``
        - 3，float
      * - ``apply_function_kwargs``
        - None，dict[str, Any] | None

API 文档
~~~~~~~~

.. autoclass:: manim.SmoothedVectorizedHomotopy

SpinInFromNothing
-----------------

一边旋转一边淡入的复合入场动画。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "GrowFromPoint";
     "GrowFromPoint" -> "GrowFromCenter";
     "GrowFromCenter" -> "SpinInFromNothing";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``angle``
        - 1.5707963267948966，float
      * - ``point_color``
        - None

快速上手
~~~~~~~~

.. code-block:: python

   self.play(SpinInFromNothing(mob))

API 文档
~~~~~~~~

.. autoclass:: manim.SpinInFromNothing

SpiralIn
--------

让一组子对象沿螺旋轨迹飞入的编排动画，开场集合类内容很出彩。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "SpiralIn";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``shapes``
        - —，Mobject
      * - ``scale_factor``
        - 8，float
      * - ``fade_in_fraction``
        - 0.3

快速上手
~~~~~~~~

.. code-block:: python

   self.play(SpiralIn(group))

API 文档
~~~~~~~~

.. autoclass:: manim.SpiralIn

Succession
----------

把多个动画严格串成一条时间线依次播放，前一个播完才播下一个。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "Succession";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``lag_ratio``
        - 1，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Succession(FadeIn(a), FadeOut(a)))

API 文档
~~~~~~~~

.. autoclass:: manim.Succession

Swap
----

让两个 Mobject 交换位置的动画，常带交叉路径。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "CyclicReplace";
     "CyclicReplace" -> "Swap";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``path_arc``
        - 1.5707963267948966，float

API 文档
~~~~~~~~

.. autoclass:: manim.Swap

TracedPath
----------

持续记录某点运动轨迹并实时绘出的「画笔」对象，配 MoveAlongPath 做轨迹可视化。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Mobject" -> "VMobject";
     "VMobject" -> "TracedPath";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``traced_point_func``
        - —，Callable
      * - ``stroke_width``
        - 2，float
      * - ``stroke_color``
        - ManimColor('#FFFFFF')
      * - ``dissipating_time``
        - None，float | None

快速上手
~~~~~~~~

.. code-block:: python

   trace = TracedPath(dot.get_center)
   self.add(trace)
   self.play(MoveAlongPath(dot, circle))

API 文档
~~~~~~~~

.. autoclass:: manim.TracedPath

Transform
---------

把一个 Mobject 平滑变形为另一个的标准变换动画，所有 Transform 家族的基类。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject | None
      * - ``target_mobject``
        - None，Mobject | None
      * - ``path_func``
        - None，Callable | None
      * - ``path_arc``
        - 0，float
      * - ``path_arc_axis``
        - array([0., 0., 1.])，np.ndarray
      * - ``path_arc_centers``
        - None
      * - ``replace_mobject_with_target_in_scene``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Transform(square, circle))

API 文档
~~~~~~~~

.. autoclass:: manim.Transform

TransformAnimations
-------------------

把两个动画「对齐」：让第一个动画的结尾状态匹配第二个动画的起点，实现无缝衔接。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "TransformAnimations";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``start_anim``
        - —，Animation
      * - ``end_anim``
        - —，Animation
      * - ``rate_func``
        - <function squish_rate_func.…，Callable

API 文档
~~~~~~~~

.. autoclass:: manim.TransformAnimations

TransformFromCopy
-----------------

先复制出副本再变形到位的动画，原对象保留，强调「由它推导」的逻辑。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Transform";
     "Transform" -> "TransformFromCopy";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``target_mobject``
        - —，Mobject

快速上手
~~~~~~~~

.. code-block:: python

   self.play(TransformFromCopy(a, b))

API 文档
~~~~~~~~

.. autoclass:: manim.TransformFromCopy

TransformMatchingShapes
-----------------------

按形状相似度在两个 VGroup 间自动配对子对象逐一变形，重构公式、图形的神器。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "TransformMatchingShapes";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``target_mobject``
        - —，Mobject
      * - ``transform_mismatches``
        - False，bool
      * - ``fade_transform_mismatches``
        - False，bool
      * - ``key_map``
        - None，dict | None

快速上手
~~~~~~~~

.. code-block:: python

   self.play(TransformMatchingShapes(vg1, vg2))

API 文档
~~~~~~~~

.. autoclass:: manim.TransformMatchingShapes

TransformMatchingTex
--------------------

TransformMatchingShapes 的 Tex 特化：按 LaTeX 片段配对变形，公式演算的标配。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "AnimationGroup";
     "AnimationGroup" -> "TransformMatchingTex";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``target_mobject``
        - —，Mobject
      * - ``transform_mismatches``
        - False，bool
      * - ``fade_transform_mismatches``
        - False，bool
      * - ``key_map``
        - None，dict | None

快速上手
~~~~~~~~

.. code-block:: python

   self.play(TransformMatchingTex(eq1, eq2))

API 文档
~~~~~~~~

.. autoclass:: manim.TransformMatchingTex

TypeWithCursor
--------------

打字机动画 + 闪烁光标：Text 逐字输入，末尾跟一个可自定义的光标 Mobject。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ShowIncreasingSubsets";
     "ShowIncreasingSubsets" -> "AddTextLetterByLetter";
     "AddTextLetterByLetter" -> "TypeWithCursor";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``text``
        - —，Text
      * - ``cursor``
        - —，Mobject
      * - ``buff``
        - 0.1，float
      * - ``keep_cursor_y``
        - True，bool
      * - ``leave_cursor_on``
        - True，bool
      * - ``time_per_char``
        - 0.1，float
      * - ``reverse_rate_function``
        - False
      * - ``introducer``
        - True

快速上手
~~~~~~~~

.. code-block:: python

   self.play(TypeWithCursor(text, cursor))

API 文档
~~~~~~~~

.. autoclass:: manim.TypeWithCursor

Uncreate
--------

Create 的反向动画：沿路径把图形擦除。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ShowPartial";
     "ShowPartial" -> "Create";
     "Create" -> "Uncreate";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —
      * - ``reverse_rate_function``
        - True，bool
      * - ``remover``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Uncreate(circle))

API 文档
~~~~~~~~

.. autoclass:: manim.Uncreate

UntypeWithCursor
----------------

TypeWithCursor 的反向动画：带光标逐字删除文本。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "ShowIncreasingSubsets";
     "ShowIncreasingSubsets" -> "AddTextLetterByLetter";
     "AddTextLetterByLetter" -> "TypeWithCursor";
     "TypeWithCursor" -> "UntypeWithCursor";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``text``
        - —，Text
      * - ``cursor``
        - None，VMobject | None
      * - ``time_per_char``
        - 0.1，float
      * - ``reverse_rate_function``
        - True
      * - ``introducer``
        - False
      * - ``remover``
        - True

API 文档
~~~~~~~~

.. autoclass:: manim.UntypeWithCursor

Unwrite
-------

Write 的反向动画：按书写顺序把文本或公式擦除。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "DrawBorderThenFill";
     "DrawBorderThenFill" -> "Write";
     "Write" -> "Unwrite";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vmobject``
        - —，VMobject
      * - ``rate_func``
        - <function linear at 0x00000…，Callable[[float], float]
      * - ``reverse``
        - True，bool

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Unwrite(text))

API 文档
~~~~~~~~

.. autoclass:: manim.Unwrite

UpdateFromAlphaFunc
-------------------

用 updater 按动画进度 alpha 驱动任意更新逻辑的自定义动画骨架。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "UpdateFromFunc";
     "UpdateFromFunc" -> "UpdateFromAlphaFunc";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``update_function``
        - —，Callable[[Mobject], Any]
      * - ``suspend_mobject_updating``
        - False，bool

API 文档
~~~~~~~~

.. autoclass:: manim.UpdateFromAlphaFunc

UpdateFromFunc
--------------

在动画时长内对目标持续应用更新函数的自定义动画，适合「边播边算」的场景。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "UpdateFromFunc";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``update_function``
        - —，Callable[[Mobject], Any]
      * - ``suspend_mobject_updating``
        - False，bool

API 文档
~~~~~~~~

.. autoclass:: manim.UpdateFromFunc

Wait
----

停顿动画：让时间流逝 nothing 发生（或跑背景动画），self.wait() 的动画版。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Wait";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``run_time``
        - 1，float
      * - ``stop_condition``
        - None
      * - ``frozen_frame``
        - None，bool | None
      * - ``rate_func``
        - <function linear at 0x00000…，Callable[[float], float]

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Wait(2))

API 文档
~~~~~~~~

.. autoclass:: manim.Wait

Wiggle
------

让对象来回扭动摇摆的强调动画，适合标记不确定性或活跃状态。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "Wiggle";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``mobject``
        - —，Mobject
      * - ``scale_value``
        - 1.1，float
      * - ``rotation_angle``
        - 0.06283185307179587，float
      * - ``n_wiggles``
        - 6，int
      * - ``scale_about_point``
        - None，Point3DLike | None
      * - ``rotate_about_point``
        - None，Point3DLike | None
      * - ``run_time``
        - 2，float

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Wiggle(mob))

API 文档
~~~~~~~~

.. autoclass:: manim.Wiggle

Write
-----

按文字/笔画顺序「书写」文本的动画，Tex、Text 演算推导的标志性入场方式。

继承关系
~~~~~~~~

.. graphviz::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", fontname="Helvetica,sans-serif", fontsize=11, penwidth=1, width=0.05, height=0.05, margin="0.08,0.05", fillcolor="#ffffff", color="#c9ced8", fontcolor="#1f2733"];
     edge  [color="#8b93a1", arrowsize=0.6, penwidth=1];
     "Animation" -> "DrawBorderThenFill";
     "DrawBorderThenFill" -> "Write";
   }

参数
~~~~

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vmobject``
        - —
      * - ``rate_func``
        - <function linear at 0x00000…，Callable[[float], float]
      * - ``reverse``
        - False，bool

快速上手
~~~~~~~~

.. code-block:: python

   self.play(Write(text))

API 文档
~~~~~~~~

.. autoclass:: manim.Write
