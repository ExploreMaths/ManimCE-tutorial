
多面体
======


多面体（Polyhedron）是 3D 几何的一个子家族：与 ``Surface`` 的参数化网格不同，多面体由 **顶点坐标 + 面索引** 显式定义，因此棱角分明、可以精确控制每个面。

Polyhedron
----------

.. autoclass:: manim.Polyhedron
   :noindex:


多面体的通用基类：传入顶点列表和面列表即可构造任意凸多面体。


.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "Polyhedron" [label="Polyhedron", URL="/chapters/ch06/polyhedra.html#polyhedron"];
     "VGroup" [label="VGroup", URL="/chapters/ch02/groups.html#vgroup"];
     "VMobject" [label="VMobject", URL="/chapters/ch02/vmobject.html#vmobject"];
     "Mobject" [label="Mobject", URL="/chapters/ch02/mobject-core.html#mobject"];
     "Polyhedron" -> "VGroup";
     "VGroup" -> "VMobject";
     "VMobject" -> "Mobject";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``vertex_coords``
        - `Point3DLike_Array <https://docs.manim.community/en/v0.21.0/reference/manim.typing.html#manim.typing.Point3DLike_Array>`__
        - —
        - 顶点三维坐标数组
      * - ``faces_list``
        - list[list[int]]
        - —
        - 每个面是顶点索引的列表
      * - ``faces_config``
        - dict
        - {}
        - 传入每个面片的样式（fill_color、stroke_color 等）
      * - ``graph_config``
        - dict
        - {}
        - 顶点/边图的样式配置


构造后可以通过 ``polyhedron.graph`` 访问顶点与边的 ``VGroup`` 。一个手写四面体的例子：

.. code-block:: python

   tetra = Polyhedron(
       vertex_coords=[
           [1, 1, 1], [1, -1, -1],
           [-1, 1, -1], [-1, -1, 1],
       ],
       faces_list=[
           [0, 1, 2], [0, 1, 3],
           [0, 2, 3], [1, 2, 3],
       ],
   )


实际使用中你很少需要手写坐标——四个正多面体子类直接用 ``edge_length`` 构造。

Tetrahedron
-----------

.. autoclass:: manim.Tetrahedron
   :noindex:


正四面体（4 个面）。

.. code-block:: python

   Tetrahedron(edge_length: float = 1, **kwargs)


Octahedron
----------

.. autoclass:: manim.Octahedron
   :noindex:


正八面体（8 个面）。

.. code-block:: python

   Octahedron(edge_length: float = 1, **kwargs)


Icosahedron
-----------

.. autoclass:: manim.Icosahedron
   :noindex:


正二十面体（20 个面）。

.. code-block:: python

   Icosahedron(edge_length: float = 1, **kwargs)


Dodecahedron
------------

.. autoclass:: manim.Dodecahedron
   :noindex:


正十二面体（12 个面）。

.. code-block:: python

   Dodecahedron(edge_length: float = 1, **kwargs)


.. demo:: examples/ch06/polyhedra_showcase.py PolyhedraShowcase

   四种正多面体排成一排并缓慢环绕。它们都只收一个 ``edge_length`` 参数，其余样式经 ``faces_config`` / ``graph_config`` 传入父类 ``Polyhedron`` 。


四种正多面体的对比：

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - 类
        - 面数
        - 顶点数
        - 构造参数
      * - `Tetrahedron </api/three_d.html#tetrahedron>`__
        - 4
        - 4
        - ``edge_length``
      * - `Octahedron </api/three_d.html#octahedron>`__
        - 8
        - 6
        - ``edge_length``
      * - `Icosahedron </api/three_d.html#icosahedron>`__
        - 20
        - 12
        - ``edge_length``
      * - `Dodecahedron </api/three_d.html#dodecahedron>`__
        - 12
        - 20
        - ``edge_length``


.. admonition:: 提示
   :class: tip

   正多面体里没有“正方体”——立方体（6 个正方形面）在 Manim 中属于 3D 几何家族，直接用上一节的 ``Cube`` 。


ConvexHull3D
------------

.. autoclass:: manim.ConvexHull3D
   :noindex:


凸包多面体：给一组 3D 点，自动计算凸包并生成对应的多面体。

.. code-block:: python

   ConvexHull3D(*points: Point3D, tolerance: float = 1e-5, **kwargs)


.. manimchain::

   digraph G {
     graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, size="", nodesep="0.15", ranksep="0.3"];
     node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];
     edge  [penwidth=1];
     "ConvexHull3D" [label="ConvexHull3D", URL="/chapters/ch06/polyhedra.html#convexhull3d"];
     "Polyhedron" [label="Polyhedron", URL="/chapters/ch06/polyhedra.html#polyhedron"];
     "VGroup" [label="VGroup", URL="/chapters/ch02/groups.html#vgroup"];
     "ConvexHull3D" -> "Polyhedron";
     "Polyhedron" -> "VGroup";
   }


.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - name
        - type
        - default
        - desc
      * - ``*points``
        - `Point3D <https://docs.manim.community/en/v0.21.0/reference/manim.typing.html#manim.typing.Point3D>`__
        - —
        - 任意多个三维点（至少 4 个不共面点）
      * - ``tolerance``
        - float
        - 1e-5
        - 数值容差，决定多少个点被视为共面


.. demo:: examples/ch06/convex_hull_3d.py ConvexHullDemo

   12 个随机点先用 ``Dot3D`` 标出， ``ConvexHull3D(*points)`` 自动求出包住所有点的最小凸多面体。示例用 ``np.random.default_rng(0)`` 固定随机种子，保证每次渲染结果一致。


常见错误与建议
--------------


.. admonition:: 常见错误
   :class: warning

   ``ConvexHull3D`` 要求点不全部共面；只给 3 个或更少的点、或所有点共面时会构造失败或得到退化结果。另外它求的是 **凸** 包——凹陷形状（如杯子）的轮廓会被凸包“填平”。


.. admonition:: 常见错误
   :class: warning

   ``faces_list`` 中的是顶点 **索引** （从 0 起），不是坐标；索引越界或面没有按一致方向（逆时针/顺时针）给出时，面的法线与着色可能不符合预期。


.. admonition:: 提示
   :class: tip

   想高亮某个面，可在 ``faces_config`` 中传样式，或构造后直接操作多面体子对象； ``polyhedron.graph`` 里的点、边也都可以单独着色。


.. admonition:: 版本说明
   :class: notice-version

   本节签名基于 ``manim 0.21.0`` 本机 ``inspect`` 核实（ ``ConvexHull3D(*points, tolerance=1e-5)`` ）。


自测
----


.. dropdown:: ✏️ 练习

   手头的点云可能包含噪声离群点，直接用 ``ConvexHull3D(*points)`` 会怎样？有什么简单的替代思路？

   .. dropdown:: ✅ 参考答案

      凸包对离群点非常敏感：一个远离主体的点会把整个多面体拉扯变形。简单思路是先做去噪/筛选（例如去掉远离中心的点、限制 z 分数，或用 ``tolerance`` 调大容差合并近似共面的点），再求凸包。


.. dropdown:: ✏️ 练习

   想画一个“房子”形状（立方体 + 四棱锥屋顶）作为一个整体移动，有哪些做法？

   .. dropdown:: ✅ 参考答案

      两种思路：一是把 ``Cube`` 与 ``Polyhedron`` （手写屋顶顶点/面）放进同一个 ``VGroup`` ，统一变换；二是直接用 ``Polyhedron`` 手写完整顶点与面列表一次成型。前者更简单，后者在需要单一样式/单个整体多面体时更合适。


下一步
------


3D 内容到此为止。接下来回到摄像机本身：下一节讲 ``MovingCameraScene``——在 2D 世界里平移、缩放摄像机的标准做法。
