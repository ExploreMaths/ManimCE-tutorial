
NumberLine
==========


数轴是坐标系家族的地基： ``Axes`` 、 ``NumberPlane`` 乃至对数刻度都建立在它之上。本节先讲清楚 ``NumberLine`` 本身，以及它的特例 ``UnitInterval`` 。

NumberLine
----------

.. autoclass:: manim.NumberLine
   :noindex:


``NumberLine`` 表示一条 **带刻度、可带数字与箭头** 的数轴，是 ``Line`` 的子类——它本质上就是一条线段，再加上刻度（ticks）、数字标签和可选的末端箭头。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "NumberLine" [label="NumberLine", URL="/chapters/ch04/number-line.html#numberline"];
     "Line" [label="Line", URL="/chapters/ch02/lines-and-arrows.html#line"];
     "TipableVMobject" [label="TipableVMobject", URL="/chapters/ch02/lines-and-arrows.html#tipablevmobject"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "NumberLine" -> "Line";
     "Line" -> "TipableVMobject";
     "TipableVMobject" -> "VMobject";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``x_range``
        - Sequence[float] | None
        - None
        - ``(起点, 终点, 步长)`` ；None 时取 ``(-7, 7, 1)``
      * - ``length``
        - float | None
        - None
        - 数轴总长度（场景单位），与 ``unit_size`` 二选一
      * - ``unit_size``
        - float
        - 1
        - 单位长度：1 个坐标单位对应多少场景单位
      * - ``include_ticks``
        - bool
        - True
        - 是否绘制刻度线
      * - ``tick_size``
        - float
        - 0.1
        - 刻度线长度
      * - ``numbers_with_elongated_ticks``
        - Iterable[float] | None
        - None
        - 需要加长刻度的坐标值
      * - ``include_tip``
        - bool
        - False
        - 末端是否加箭头
      * - ``include_numbers``
        - bool
        - False
        - 是否自动添加数字标签（标签走 LaTeX）
      * - ``label_direction``
        - :class:`manim.typing.Point3DLike`
        - `DOWN <https://docs.manim.community/en/v0.21.0/reference/manim.constants.html#manim.constants.DOWN>`__
        - 数字标签相对数轴的方向
      * - ``label_constructor``
        - type[:class:`manim.typing.ManimTextLabel`]
        - `MathTex </chapters/ch03/tex-and-mathtex.html#mathtex>`__
        - 标签构造函数；可换 `Text </chapters/ch03/text-and-paragraph.html#text>`__/`MathTypst </api/text.html#mathtypst>`__ 摆脱 LaTeX
      * - ``scaling``
        - `_ScaleBase </chapters/ch04/scales.html#_scalebase>`__
        - `LinearBase </chapters/ch04/scales.html#linearbase>`__ ()
        - 缩放基，见下一节（`LogBase </chapters/ch04/scales.html#logbase>`__ 等）
      * - ``line_to_number_buff``
        - float
        - 0.25
        - 数字与数轴的间距
      * - ``numbers_to_exclude``
        - Iterable[float] | None
        - None
        - 排除不显示的数字
      * - ``numbers_to_include``
        - Iterable[float] | None
        - None
        - 只显示这些数字


最常用的三个操作： **坐标互转** （ ``number_to_point`` / ``point_to_number`` ，别名 ``n2p`` / ``p2n`` ）、 **加数字** （ ``add_numbers`` ）、 **加自定义标签** （ ``add_labels`` ）。

.. demo:: examples/ch04/number_line.py NumberLineDemo

   ``add_labels`` 传入 ``{坐标值: Mobject}`` 字典； ``number_to_point`` 与 ``point_to_number`` 互为逆运算，是把几何位置和抽象坐标联系起来的桥梁。


常用方法速览：

- ``line.add_numbers(x_values=None, ...)`` —— 自动按 ``x_range`` 的步长补数字（默认走 ``MathTex`` ，需要 LaTeX）
- ``line.add_labels({1: Tex("a"), 2: Text("b")}, ...)`` —— 自定义标签，值可以是任意带 ``font_size`` 属性的 Mobject
- ``line.get_number_mobject(x)`` / ``get_number_mobjects(...)`` —— 取回数字标签 Mobject
- ``line @ x`` —— ``number_to_point`` 的运算符写法

.. admonition:: 常见错误
   :class: warning

   v0.21.0 中 ``add_labels`` 加的标签存放在 ``line.labels`` 属性里，但 ``line.get_labels()`` **不会返回它们**——它内部直接转调 ``get_number_mobjects()`` （取刻度数字）。想取出 ``add_labels`` 的标签请用 ``line.labels`` ，且只有在调用过 ``add_numbers`` 之后 ``get_labels()`` 才可用（否则会抛 ``AttributeError`` ）。


.. admonition:: 提示
   :class: tip

   不想依赖 LaTeX 时，把 ``label_constructor=Text`` 传给构造或 ``add_numbers``/``add_labels`` ，标签就会用 Pango 渲染，例如 ``NumberLine(x_range=[0, 10], include_numbers=True, label_constructor=Text)`` 。


UnitInterval
------------

.. autoclass:: manim.UnitInterval
   :noindex:


``UnitInterval`` 是一条 **固定覆盖 0 到 1、每单位长 10** 的特化数轴：等价于 ``NumberLine(x_range=(0, 1), unit_size=10)`` 。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "UnitInterval" [label="UnitInterval", URL="/api/graphing.html#unitinterval"];
     "NumberLine" [label="NumberLine", URL="/chapters/ch04/number-line.html#numberline"];
     "Line" [label="Line", URL="/chapters/ch02/lines-and-arrows.html#line"];
     "UnitInterval" -> "NumberLine";
     "NumberLine" -> "Line";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``unit_size``
        - float
        - 10
        - 单位长度（1 对应 10 个场景单位，即整条轴长 10）
      * - ``numbers_with_elongated_ticks``
        - list[float] | None
        - [0, 1]
        - 加长刻度的坐标
      * - ``decimal_number_config``
        - dict | None
        - None
        - 数字标签（`DecimalNumber </api/text.html#decimalnumber>`__）的配置


.. admonition:: 版本说明
   :class: warning

   ``UnitInterval`` **没有出现在官方文档中** （未公开的便捷类），但它在 ``manim`` 顶层命名空间可直接导入，行为稳定。需要 0–1 区间且长度恰为 10 的数轴时用它最省事；要其他区间请直接用 ``NumberLine`` 。


.. admonition:: 常见错误
   :class: warning

   ``UnitInterval`` 和其他 ``NumberLine`` 一样 **以自身中心对齐原点** ： ``number_to_point(0)`` 位于场景 ``x = -5`` ，而不是原点。若需要“0 在原点”的 0–1 数轴，请自行 ``shift(RIGHT * 5)`` 或用 ``x_range`` 构造。


.. demo:: examples/ch04/unit_interval.py UnitIntervalDemo

   默认 0 和 1 处有长刻度；注意整条轴以中心为原点对称展开。


自测
----


.. dropdown:: ✏️ 练习

   ``NumberLine(x_range=[-2, 8, 0.5], length=10)`` 上， ``number_to_point(3)`` 大约在场景什么位置？

   .. dropdown:: ✅ 参考答案

      数轴总长 10，覆盖 10 个单位，因此 ``unit_size = 1`` 。值 3 位于 ``(-2 → 8)`` 区间的 5/10 处，即数轴中点；而数轴整体居中于原点，所以该点约为原点（x = 0）。一般结论： ``point = unit_size * (number - x_min - (x_max - x_min)/2)`` 。


.. dropdown:: ✏️ 练习

   想让数轴上 0 到 10 的范围内只显示 2、4、6 三个数字，怎么做？

   .. dropdown:: ✅ 参考答案

      构造时传 ``include_numbers=True`` 并配合 ``numbers_to_include=[2, 4, 6]`` （也可用 ``numbers_to_exclude`` 反向排除）。
