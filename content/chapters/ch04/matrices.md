---
title: 矩阵
---

# 矩阵

`manim.mobject.matrix` 模块把“二维数组”排版成带方括号的数学矩阵：`Matrix` 是基类，四个特化子类决定**元素**如何渲染（公式 / 整数 / 小数 / 任意 Mobject），另有 `get_det_text` 与 `matrix_to_*` 两个工具函数。

:::notice warning
版本说明
v0.21.0 中 `Matrix` 的**括号始终由 `MathTex` 生成**（`_add_brackets` 内部硬编码），且 `Integer` / `DecimalNumber` 的数字字符默认也由 `MathTex` 排版——因此本节所有示例都依赖 LaTeX，由 CI 渲染。即使元素全部换成 `Text`，括号仍会触发 LaTeX 编译。
:::

## Matrix

`Matrix` 把嵌套列表排版成矩阵：元素按网格排列，两侧加上可伸缩的方括号。

:::inheritance
Matrix → VMobject → Mobject
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `matrix` | Iterable[Iterable[Any] \| Vector2DLike] | — | 二维数据（必需） |
| `v_buff` | float | 0.8 | 行间距 |
| `h_buff` | float | 1.3 | 列间距 |
| `bracket_h_buff` | float | 0.25 | 括号与内容的水平间距 |
| `bracket_v_buff` | float | 0.25 | 括号纵向外延量 |
| `add_background_rectangles_to_entries` | bool | False | 给每个元素加背景矩形 |
| `include_background_rectangle` | bool | False | 给整个矩阵加背景矩形 |
| `element_to_mobject` | type[VMobject] \| Callable | MathTex | 元素构造函数（子类改写的核心） |
| `element_to_mobject_config` | dict | {} | 传给元素构造函数的参数 |
| `element_alignment_corner` | Vector3DLike | UR `(1,-1,0)` | 元素对齐角（默认右上） |
| `left_bracket` / `right_bracket` | str | "[" / "]" | 括号样式（`(`, `\|`, `\langle` 等 LaTeX 定界符） |
| `stretch_brackets` | bool | True | 括号是否拉伸到矩阵全高 |
| `bracket_config` | dict | {} | 传给括号 `MathTex` 的样式 |
:::

访问与着色：

- `matrix.get_rows()` / `get_columns()` —— 返回每行 / 每列的 `VGroup`，可直接 `.animate.set_color(...)`
- `matrix.get_entries()` —— 返回**全部**元素的扁平 `VGroup`（注意：与 `Table.get_entries(pos)` 不同，不接受坐标参数）；按行优先展开，第 i 行第 j 列的扁平下标是 `i * 列数 + j`
- `matrix.get_brackets()` —— 返回左右括号 `VGroup`
- `matrix.set_row_colors(*colors)` / `set_column_colors(*colors)` —— 整行 / 整列批量着色

:::demo examples/ch04/integer_matrix.py IntegerMatrixDemo
`get_rows()` / `get_columns()` / `get_entries()` 返回的 VGroup 可以直接做动画；这是矩阵讲解中“高亮某行某列”的标准手法。
:::

本示例依赖 LaTeX，由 CI 渲染。

## IntegerMatrix

`IntegerMatrix` 是 `Matrix` 的子类，只改一件事：元素构造函数换成 `Integer`（逐位排版、整数专用）。

:::inheritance
IntegerMatrix → Matrix → VMobject
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `matrix` | Iterable[Iterable[Any]] | — | 二维数据（必需） |
| `element_to_mobject` | … | Integer | 元素构造函数，一般保持默认 |
:::

`Integer` 的数字外观由 `MathTex` 逐字符排版（见 ch03「数字与变量」），需要 LaTeX；想把数字换成 Pango 渲染，可显式传 `element_to_mobject_config` 无法做到（`mob_class` 是 `Integer` 的构造参数而非 config）——更简单的做法是直接用 `Matrix(..., element_to_mobject=Text)` 自己排版。注意：**括号仍然走 `MathTex`**，整个 `Matrix` 家族在 v0.21.0 都无法完全脱离 LaTeX。

## DecimalMatrix

`DecimalMatrix` 把元素渲染为 `DecimalNumber`（支持小数位控制），默认保留 **1 位**小数。

:::inheritance
DecimalMatrix → Matrix → VMobject
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `matrix` | Iterable[Iterable[Any]] | — | 二维数据（必需） |
| `element_to_mobject_config` | dict | {'num_decimal_places': 1} | 透传给 `DecimalNumber`，常用 `num_decimal_places` |
:::

:::demo examples/ch04/matrix_det.py MatrixDetDemo
`element_to_mobject_config={"num_decimal_places": 1}` 统一小数位；`get_det_text` 生成与矩阵等高的 `det(A) = 值` 标注（`MathTex`）。
:::

本示例依赖 LaTeX，由 CI 渲染。

## MobjectMatrix

`MobjectMatrix` 把**任意 Mobject 直接当作元素**（默认恒等映射，不做任何转换），适合“图形矩阵”“状态表”这类非纯文本排版。

:::inheritance
MobjectMatrix → Matrix → VMobject
:::

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `matrix` | Iterable[Iterable[VMobject]] | — | 由 Mobject 组成的二维数据（必需） |
| `element_to_mobject` | Callable | 恒等 lambda | 元素预处理函数，可自行替换 |
:::

:::demo examples/ch04/mobject_matrix.py MobjectMatrixDemo
元素就是 `Circle`、`Square` 等现成图形；`h_buff` 调大避免图形重叠。行列访问与数字矩阵完全一致。
:::

本示例的元素虽是矢量图形，但括号仍由 `MathTex` 生成，依赖 LaTeX，由 CI 渲染。

## get_det_text

`get_det_text(matrix, determinant=None, background_rect=False, initial_scale_factor=2)` 是**模块级工具函数**（不是方法）：生成 `det(A) = <值>` 的 `MathTex` 标注，高度与给定矩阵匹配，通常与矩阵左右排布。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `matrix` | Matrix | — | 用于匹配高度的矩阵（必需） |
| `determinant` | int \| str \| None | None | 行列式的值；None 时**不计算**，只生成 `det ( A )` 框架 |
| `background_rect` | bool | False | 是否加背景矩形 |
| `initial_scale_factor` | float | 2 | `det` 字样相对矩阵的初始缩放 |
:::

:::notice tip
提示
`determinant` 传**字符串**（如 `"x^2 - 1"`）可以显示符号表达式，传数值则显示计算结果。它生成的是独立 Mobject，不会自动与矩阵组合，记得 `VGroup(det, matrix).arrange(RIGHT)` 或 `next_to`。
:::

## matrix_to_tex_string

`matrix_to_tex_string(matrix: np.ndarray) -> str` 把 numpy 数组转成 LaTeX 字符串，格式为 `\left[ \begin{array}{cc} ... \end{array} \right]`（方括号 + array 环境）；一维数组会被 `reshape((size, 1))` 成**列向量**。

适合先拿到字符串做拼接的场景：把矩阵嵌进更大的公式、替换个别元素、或接入自定义 `MathTex` / `MathTypst`。

## matrix_to_mobject

`matrix_to_mobject(matrix: np.ndarray) -> MathTex` 是前者的 Mobject 版：内部即 `MathTex(matrix_to_tex_string(matrix))`，一步到位直接上屏。

:::demo examples/ch04/matrix_tex_helpers.py MatrixTexHelpersDemo
`matrix_to_tex_string` 适合先拿到字符串做拼接（如把矩阵嵌进更大的公式），`matrix_to_mobject` 适合直接上屏；两者输出完全对应。
:::

本示例依赖 LaTeX，由 CI 渲染。

:::notice warning
常见错误
`matrix_to_tex_string` 的元素是 `astype("str")` 的裸转换：`np.array([[1.0, 2.5]])` 会得到 `"1.0"`、`"2.5"` 这样的原始字符串，而不是 LaTeX 友好的 `1`、`\frac{5}{2}`。需要精细排版时请拿到字符串后自行替换，或干脆手写 `MathTex(r"\begin{pmatrix}...\end{pmatrix}")`。
:::

## 自测

:::exercise
为什么 `IntegerMatrix([[1, 2], [3, 4]])` 在没装 LaTeX 的机器上也会失败，即使整数元素本身不需要公式排版？
:::answer
因为 `Matrix._add_brackets` 生成左右括号时**硬编码使用 `MathTex`**（括号的可伸缩定界符 `\left[ ... \right]` 只能由 LaTeX 排版）。v0.21.0 中整个 `Matrix` 家族没有任何参数能绕过这一步，所以所有矩阵类都依赖 LaTeX。
:::
:::

:::exercise
想高亮 3 行 4 列矩阵 `m` 的第 2 行第 3 列元素，两种写法分别是什么？
:::answer
按行列取：`m.get_rows()[1]` 得第二行再取下标，或 `m.get_columns()[2][1]`；按扁平下标取：`m.get_entries()[1 * 4 + 2]` 即 `get_entries()[6]`（行优先展开）。随后直接 `.animate.set_color(RED)` 即可。
:::
:::

:::exercise
`matrix_to_tex_string(np.array([1, 2, 3]))` 的输出是什么形状？这会带来什么便利或隐患？
:::answer
一维数组被 `reshape((size, 1))` 成**列向量**，输出 `\left[ \begin{array}{c}1\\2\\3\end{array} \right]`。便利：向量默认按数学惯例竖排；隐患：一维行数据会被静默转置，若你预期的是行向量需要自行 `reshape(1, -1)`。
:::
:::
