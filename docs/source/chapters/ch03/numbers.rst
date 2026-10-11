
数字与变量
==========


``DecimalNumber`` 、 ``Integer`` 、 ``Variable`` 把“数值”封装成 Mobject：数值变化时对象自动重排字符，配合 ``ValueTracker`` 就能做出滚动的计数器、实时更新的坐标等效果。

.. admonition:: 版本说明
   :class: notice-version

   本节示例的默认数字外观由 ``MathTex`` 排版，依赖 LaTeX，示例由 CI 渲染。 ``ValueTracker`` 本身只是数值容器，其机制在「动画进阶」板块的数值动画一节详细讲解，本节只用到 ``tracker.get_value()`` 与 ``tracker.animate.set_value(...)`` 。


DecimalNumber
-------------

.. autoclass:: manim.DecimalNumber
   :noindex:


``DecimalNumber`` 渲染一个浮点数， **值改变时自动增删字符并保持对齐** ，是计数器动画的核心。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "DecimalNumber" [label="DecimalNumber", URL="/api/text.html#decimalnumber"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "DecimalNumber" -> "VMobject";
     "VMobject" -> "Mobject";
   }



.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``number``
        - float
        - 0
        - 初始数值
      * - ``num_decimal_places``
        - int
        - 2
        - 小数位数
      * - ``mob_class``
        - type[`SingleStringMathTex </api/text.html#singlestringmathtex>`__]
        - `MathTex </chapters/ch03/tex-and-mathtex.html#mathtex>`__
        - 单个数字/字符的排版类
      * - ``include_sign``
        - bool
        - False
        - 始终显示正负号
      * - ``group_with_commas``
        - bool
        - True
        - 整数部分加千分位逗号
      * - ``show_ellipsis``
        - bool
        - False
        - 末尾显示省略号（暗示截断）
      * - ``unit``
        - str | None
        - None
        - 追加的单位（如 ``"m/s"`` ），与数字同字号
      * - ``include_background_rectangle``
        - bool
        - False
        - 给整个数字加背景矩形
      * - ``edge_to_fix``
        - :class:`manim.typing.Vector3DLike`
        - `LEFT <https://docs.manim.community/en/v0.21.0/reference/manim.constants.html#manim.constants.LEFT>`__
        - 数值增长时固定不动的边缘


核心用法： ``set_value(x)`` 更新数值（ instantly ），配合 ``ValueTracker`` + updater 或 ``.animate.set_value`` 实现平滑滚动：

.. demo:: examples/ch03/decimal_number_demo.py DecimalNumberDemo

   ``ValueTracker`` 从 0 动画到 1，updater 每帧把 ``PI * tracker`` 写入 ``DecimalNumber``——省略号来自 ``show_ellipsis=True`` 。本示例由 CI 渲染。


.. admonition:: 提示
   :class: tip

   ``edge_to_fix=LEFT`` 是默认值：数字向右增长时左侧对齐，适合左对齐的计数器。做居中计分板时传入 ``ORIGIN`` 保持整体居中。


Integer
-------

.. autoclass:: manim.Integer
   :noindex:


``Integer`` 是 ``DecimalNumber`` 的子类，固定 ``num_decimal_places=0`` 的整数版本，参数其余相同。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Integer" [label="Integer", URL="/api/text.html#integer"];
     "DecimalNumber" [label="DecimalNumber", URL="/api/text.html#decimalnumber"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Integer" -> "DecimalNumber";
     "DecimalNumber" -> "VMobject";
   }


.. code-block:: python

   Integer(number: float = 0, num_decimal_places: int = 0, **kwargs)


典型场景：帧计数、得分、粒子数。配合 ``ValueTracker`` 的写法和 ``DecimalNumber`` 完全一致。

Variable
--------

.. autoclass:: manim.Variable
   :noindex:


``Variable`` 把“标签 + 数值”组合显示，自带一个 ``tracker`` （ ``ValueTracker`` 实例），常用于展示“变量名 = 当前值”。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Variable" [label="Variable", URL="/api/text.html#variable"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "Variable" -> "VMobject";
     "VMobject" -> "Mobject";
   }



.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``var``
        - float
        - —
        - 初始值
      * - ``label``
        - str | `Tex </chapters/ch03/tex-and-mathtex.html#tex>`__ | `MathTex </chapters/ch03/tex-and-mathtex.html#mathtex>`__ | `Text </chapters/ch03/text-and-paragraph.html#text>`__ | `SingleStringMathTex </api/text.html#singlestringmathtex>`__
        - —
        - 变量名，字符串按 ``var_type`` 同引擎排版，也可直接传文本对象
      * - ``var_type``
        - type
        - `DecimalNumber </api/text.html#decimalnumber>`__
        - 数值部分用的类（ `DecimalNumber </api/text.html#decimalnumber>`__ 或 `Integer </api/text.html#integer>`__ ）
      * - ``num_decimal_places``
        - int
        - 2
        - 小数位数（透传给数值类）


成员： ``v.tracker`` 是内部 ``ValueTracker`` ； ``v.label`` 是变量名部分； ``v.value`` 显示数值。改值用 ``v.set_value(x)`` 或直接动 ``v.tracker`` ：

.. demo:: examples/ch03/variable_demo.py VariableDemo

   ``x`` 与 ``x^2`` 两个 ``Variable`` 并排， ``x^2`` 注册 updater 依赖 ``x.tracker``——动画只驱动 ``x`` ，另一个自动跟随。本示例由 CI 渲染。


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 
        - `DecimalNumber </api/text.html#decimalnumber>`__
        - `Integer </api/text.html#integer>`__
        - `Variable </api/text.html#variable>`__
      * - 小数
        - 支持
        - 不支持
        - 由 ``var_type`` 决定
      * - 自带标签
        - 无
        - 无
        - 有（ ``label`` ）
      * - 自带 tracker
        - 无
        - 无
        - 有（ ``.tracker`` ）
      * - 适用
        - 测量值、进度
        - 计数、得分
        - 展示“变量 = 值”


.. admonition:: 常见错误
   :class: warning

   ``DecimalNumber`` 的子对象是按 **当前位数** 重建的： ``set_value`` 前后位数若变化， ``num[3]`` 这类硬编码索引会指到别的字符。要对特定位做动画，先确认位数固定，或改用 ``unit`` 、 ``include_sign`` 等参数稳定结构。


自测
----


.. dropdown:: ✏️ 练习

   做一个从 0 滚到 100 的居中整数计数器，写出关键代码。

   .. dropdown:: ✅ 参考答案


      .. code-block:: python

         tracker = ValueTracker(0)
         counter = Integer(0, edge_to_fix=ORIGIN)
         counter.add_updater(lambda m: m.set_value(tracker.get_value()))
         self.add(counter)
         self.play(tracker.animate.set_value(100), run_time=3)

      ``edge_to_fix=ORIGIN`` 让增长中的数字保持整体居中。


.. dropdown:: ✏️ 练习

   ``Variable(0, "x")`` 中 ``label`` 传字符串与传 ``Text("x")`` 有何区别？

   .. dropdown:: ✅ 参考答案

      传字符串时，标签按 ``var_type`` 的排版引擎（默认 ``DecimalNumber`` → ``MathTex`` ，数学斜体）渲染；传 ``Text("x")`` 则用 Pango 渲染成普通文本字体。外观不同，且前者需要 LaTeX。想与非数学风格的场景统一，显式传 ``Text`` 对象。


下一步
------


有了文本和数字，还需要组织内容的结构——下一节看 ``BulletedList`` 与 ``Title`` 。
