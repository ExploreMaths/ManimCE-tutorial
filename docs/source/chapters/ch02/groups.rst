
组合容器
========


单个图形之外的下一个问题是 **组织** ：把多个 mobject 当成一个整体移动、缩放、着色。Manim 提供三个容器： ``Group`` 、 ``VGroup`` 与按键取值的 ``VDict`` 。

Group
-----

.. autoclass:: manim.Group
   :noindex:


``Group`` 是最朴素的组合容器：把任意多个 ``Mobject`` 收进一个 ``submobjects`` 列表，整体参与布局与变换。它不校验成员类型，因此可以混合装入位图、3D 对象等任何 mobject。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Group" [label="Group", URL="/chapters/ch02/groups.html#group"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Group" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   Group(*mobjects, **kwargs)


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``*mobjects``
        - `Mobject </chapters/ch02/mobject-core.html#mobject>`__
        - —
        - 任意数量的成员，可空
      * - ``kwargs``
        - —
        - —
        - 转发给 `Mobject </chapters/ch02/mobject-core.html#mobject>`__ 构造


.. admonition:: 常见错误
   :class: warning

   同一个 mobject 重复 ``add`` 进同一个组会被 **静默忽略** （官方文档明确说明）。如果需要两个一样的图形，先 ``copy()`` 再添加。


VGroup
------

.. autoclass:: manim.VGroup
   :noindex:


``VGroup`` 是矢量图形的专用组合容器：成员 **必须是 ``VMobject``** ，因此它继承了 ``VMobject`` 的全部样式方法，可以对整组统一 ``set_fill`` 、整体渐变，并支持 ``arrange`` 自动排版。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "VGroup" [label="VGroup", URL="/chapters/ch02/groups.html#vgroup"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "VGroup" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. code-block:: python

   VGroup(*vmobjects, **kwargs)


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``*vmobjects``
        - `VMobject </chapters/ch02/vmobject.html#vmobject>`__ | Iterable[`VMobject </chapters/ch02/vmobject.html#vmobject>`__]
        - —
        - 成员；也可先建空组再 ``add``
      * - ``kwargs``
        - —
        - —
        - 转发给 `VMobject </chapters/ch02/vmobject.html#vmobject>`__ 构造


与 ``Group`` 的对比如下：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 维度
        - `Group </chapters/ch02/groups.html#group>`__
        - `VGroup </chapters/ch02/groups.html#vgroup>`__
      * - 继承
        - `Mobject </chapters/ch02/mobject-core.html#mobject>`__
        - `VMobject </chapters/ch02/vmobject.html#vmobject>`__
      * - 成员类型
        - 任意 `Mobject </chapters/ch02/mobject-core.html#mobject>`__
        - 仅 `VMobject </chapters/ch02/vmobject.html#vmobject>`__，否则 ``TypeError``
      * - 样式方法
        - 无填充/描边概念
        - ``set_fill`` / ``set_stroke`` / ``set_opacity`` 等对整组生效
      * - 整体渐变
        - 不支持
        - ``set_color_by_gradient`` 按子对象依次着色
      * - 典型场景
        - 混合类型（位图 + 矢量 + 3D）
        - 同类的矢量图形批量排版


.. demo:: examples/ch02/groups_demo.py GroupsDemo

   ``arrange(RIGHT, buff=0.4)`` 一键横排；对整组 ``scale + rotate`` 时三个图形保持相对位置不变；下排演示用下标 ``squares[1]`` 取单个成员单独上色。


.. admonition:: 常见错误
   :class: warning

   ``VGroup(Square(), ImageMobject("a.png"))`` 会抛 ``TypeError``——``VGroup.add`` 会校验成员是 ``VMobject`` 。混入非矢量对象时请改用 ``Group`` 。


.. admonition:: 提示
   :class: tip

   ``arrange(direction=RIGHT, buff=0.25, center=True)`` 是 ``Mobject`` 上的方法，任何容器都能用：它按方向排开所有子对象并保持组中心不变。 ``VGroup(*[Square() for _ in range(4)])`` 批量构造列表成员是最常见的写法。


VDict
-----

.. autoclass:: manim.VDict
   :noindex:


``VDict`` 是“字典版 VGroup”：每个成员关联一个可哈希的键，可以像 Python 字典一样 ``d["key"]`` 取值、 ``d["key"] = mob`` 赋值。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "VDict" [label="VDict", URL="/api/types.html#vdict"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "VDict" -> "VMobject";
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
      * - ``mapping_or_iterable``
        - Mapping | Iterable[tuple]
        - {}
        - 初始键值对，如 ``{"sq": Square()}``
      * - ``show_keys``
        - bool
        - False
        - 是否在成员左侧显示键文本（调试用）


字典式操作一览：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 操作
        - 效果
      * - ``d["sq"]``
        - 取出键对应的 mobject（ ``__ getitem__`` ）
      * - ``d["tri"] = Triangle()``
        - 新增或替换键值对（ ``__ setitem__`` ）
      * - ``d.add({"c": Circle()})``
        - 批量添加，参数同构造的映射
      * - ``d.remove("sq")``
        - 按键移除
      * - ``d.keys()`` / ``d.values()`` / ``d.items()``
        - 字典三件套


.. demo:: examples/ch02/vdict_demo.py VDictDemo

   ``VDict`` 按键索引： ``d["sq"]`` 单独给方块填色， ``d["tri"] = ...`` 动态新增一个三角形成员。


.. admonition:: 常见错误
   :class: warning

   ``show_keys=True`` 会用 ``Tex`` 渲染键名， **需要本机安装 LaTeX** ；没有 LaTeX 环境时请保持默认 ``False`` 。另外 ``VDict`` 的值必须是 ``VMobject`` ，与 ``VGroup`` 一样会做类型校验。


自测
----


.. dropdown:: ✏️ 练习

   ``Group`` 和 ``VGroup`` 各应该在什么情况下使用？

   .. dropdown:: ✅ 参考答案

      成员全部是矢量图形、需要对整组上色/渐变时用 ``VGroup`` ；成员类型混杂（如 ``ImageMobject`` 、3D 对象）或只是纯逻辑分组时用 ``Group``——``Group`` 不校验类型， ``VGroup`` 遇到非 VMobject 会抛 ``TypeError`` 。


.. dropdown:: ✏️ 练习

   为什么 ``VGroup(sq, sq)`` 里只有一个方块？怎样得到两个？

   .. dropdown:: ✅ 参考答案

      ``add`` 会忽略重复添加的同一对象（ ``Group``/``VGroup`` 都是如此，避免子对象树出现环）。需要两份时先拷贝： ``VGroup(sq, sq.copy())`` 。


下一步
------


容器就位后，下一节进入实战：圆、矩形、多边形等 **基本形状** 的参数与画法。
