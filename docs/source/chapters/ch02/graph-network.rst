图与网络
========


``Graph`` / ``DiGraph`` 把 networkx 的图论能力与 Manim 的动画系统结合起来：顶点、边都是普通 mobject，可以用任意动画逐个创建、移动、重连，非常适合讲解数据结构、状态机与网络拓扑。

Graph
-----

.. autoclass:: manim.Graph
   :noindex:


``Graph`` 构造三个要素：顶点序列、边序列（顶点对的列表）和布局。布局可以是名字（``"circular"`` / ``"spring"`` / ``"kamada_kawai"`` / ``"planar"`` 等，由 networkx 计算）、坐标字典或自定义函数；``vertex_config`` / ``edge_config`` 控制样式，``labels=True`` 自动给顶点加标签。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Graph" [label="Graph", URL="/chapters/ch02/graph-network.html#graph"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "Graph" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``vertices``
        - Sequence[Hashable]
        - —
        - 顶点集合（任意可哈希值）
        - ``edges``
        - Sequence[tuple]
        - —
        - 顶点对列表
        - ``layout``
        - str | dict | callable
        - ``spring``
        - 布局名 / 坐标字典 / 布局函数
        - ``labels``
        - bool | dict
        - False
        - 顶点标签；True 时自动编号
        - ``vertex_config`` / ``edge_config``
        - dict | None
        - None
        - 顶点 / 边样式
        - ``partitions`` + ``root_vertex``
        - —
        - None
        - 分层布局的分区与根

.. demo:: examples/ch02/graph_network.py GraphDemo

   ``Graph``（左）与 ``DiGraph``（右）使用同一组顶点和边；``labels=True`` 显示顶点编号。

DiGraph
-------

.. autoclass:: manim.DiGraph
   :noindex:


``DiGraph`` 是有向图：构造参数与 ``Graph`` 完全一致，区别在于每条边会自动加上箭头（可用 ``edge_config`` 里的 ``tip_config`` 调整箭头样式）。表示状态转移、依赖关系、流程图时用它。

.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "DiGraph" [label="DiGraph", URL="/chapters/ch02/graph-network.html#digraph"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "object" [label="object"];
     "DiGraph" -> "VMobject";
     "VMobject" -> "Mobject";
     "Mobject" -> "object";
   }


.. admonition:: 提示
   :class: tip

   图建好之后的动态修改（加顶点、换布局、改样式）直接对 ``Graph`` 对象调用相应方法后用 ``self.play`` 播放即可，官方文档的 MovingDiGraph 示例演示了移动顶点的标准写法。
