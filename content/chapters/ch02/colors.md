---
title: 颜色系统
---

# 颜色系统

Manim 的颜色核心是 `ManimColor`：几乎所有 `color` 参数（类型标注 `ParsableManimColor`）都能接受十六进制字符串、`ManimColor`、`HSV`/`RGBA` 实例或 RGB 元组，并统一转换到内部表示。

## ManimColor

`ManimColor` 是不可变的颜色值对象，封装 RGB(A) 四个通道。

```python
ManimColor("#58C4DD")              # 十六进制
ManimColor((0.345, 0.769, 0.867))  # RGB 元组（0~1 浮点）
ManimColor(RED)                    # 从既有颜色构造
```

常用工厂与实例方法：

:::compare
| 方法 | 签名 | 作用 |
| ---- | ---- | ---- |
| `from_hex` | `(hex_str, alpha=1.0)` | 从 #RRGGBB 字符串构造 |
| `from_hsv` | `(hsv, alpha=1.0)` | 从 HSV 三元组（0~1）构造 |
| `from_rgb` / `from_rgba` | `(tuple, alpha)` | 从浮点元组构造 |
| `interpolate` | `(other, alpha)` | 与另一颜色按比例插值 |
| `lighter` / `darker` | `(blend=0.2)` | 向白/黑混合，提亮或压暗 |
| `opacity` | `(opacity)` | 返回带新不透明度的副本 |
| `contrasting` | `(threshold=0.5, light, dark)` | 按亮度返回黑或白（保证可读性） |
| `invert` | `()` | RGB 通道取反 |
| `to_hex` / `to_rgb` / `to_rgba` | `()` | 导出为字符串或 ndarray |
| `to_int_rgb` / `to_int_rgba` | `()` | 导出 0~255 整数 |
| `into` | `(ManimColor)` | 把自身混入另一个颜色（原地语义） |
:::

```python
base = ManimColor.from_hex("#58C4DD")
base.lighter(0.5)                       # 更浅的青
base.darker(0.5)                        # 更深的青
base.interpolate(PURE_RED, 0.6)         # 偏向红的混合色
ManimColor("#123456").contrasting()     # #FFFFFF（深底配白字）
```

常见坑：`ManimColor` 的方法都返回**新对象**，需要 `color = color.darker(0.3)` 接收；`ParsableManimColor` 注解表示“以上任意形式”。

:::demo examples/ch02/colors_demo.py ColorsDemo
`ManimColor` 的提亮、压暗、插值与半透明变体并排展示；下方是 `color_gradient` 生成的 12 级渐变，以及 `RandomColorGenerator(seed=7)` 生成的可复现随机色。
:::

## HSV

`HSV` 是 `ManimColor` 的子类，用 HSV 三元组（色相、饱和度、明度，均为 0~1 浮点）构造颜色，适合程序化生色。

```python
HSV((0.0, 1.0, 1.0))    # 纯红
HSV((0.33, 0.8, 0.9))   # 偏绿的色调
```

:::inheritance
HSV → ManimColor
:::

## RGBA

`RGBA` 与 `ManimColor` 平行的颜色表示，直接携带 alpha 通道，构造参数同 `ManimColor`（value + alpha）。

```python
RGBA((1.0, 0.0, 0.0, 0.5))   # 半透明红
```

常见坑：`RGBA` 不是 `ManimColor` 的子类（两者各自实现同一套接口）；在 `color=` 参数里 Manim 会自动解析，混用时以 `ParsableManimColor` 兼容为准。

## RandomColorGenerator

`RandomColorGenerator` 按需从调色板中随机取色，支持种子复现。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `seed` | int \| None | None | 随机种子；设置后取色序列可复现 |
| `sample_colors` | list[ManimColor] \| None | None | 抽样池；None 时使用全部内置 Manim 颜色 |
:::

```python
rcg = RandomColorGenerator(seed=42)      # 两次运行取色序列一致
rcg.next()                               # 取下一个随机颜色
rcg2 = RandomColorGenerator(sample_colors=[RED, GREEN, BLUE])
```

:::notice tip
提示
需要“每次渲染都不一样”的随机效果时，不传 seed 并用 CLI 的 `--seed` 或 `Scene(random_seed=...)` 控制整体可复现性。
:::

## 内置调色板

Manim 内置了一套品牌调色板。每个彩色系有 5 个亮度阶梯（`_A` 最浅、`_E` 最深），主色名（如 `BLUE`）取中间档：

:::compare
| 色系 | 常量 | 说明 |
| ---- | ---- | ---- |
| 蓝 | `BLUE_A` … `BLUE_E`、`BLUE` | 品牌主色系 |
| 青 | `TEAL_A` … `TEAL_E`、`TEAL` | |
| 绿 | `GREEN_A` … `GREEN_E`、`GREEN` | |
| 黄 | `YELLOW_A` … `YELLOW_E`、`YELLOW` | |
| 金 | `GOLD_A` … `GOLD_E`、`GOLD` | |
| 红 | `RED_A` … `RED_E`、`RED` | |
| 栗 | `MAROON_A` … `MAROON_E`、`MAROON` | |
| 紫 | `PURPLE_A` … `PURPLE_E`、`PURPLE` | |
:::

灰色系有美式/英式**双拼写**，逐对相等（`GRAY == GREY`）：

:::compare
| 常量 | 说明 |
| ---- | ---- |
| `GRAY_A` … `GRAY_E` / `GREY_A` … `GREY_E` | 五级灰 |
| `GRAY` / `GREY`、`DARK_GRAY` / `DARK_GREY` | 中灰、深灰 |
| `DARKER_GRAY` / `DARKER_GREY` | 更深的灰 |
| `LIGHT_GRAY` / `LIGHT_GREY`、`LIGHTER_GRAY` / `LIGHTER_GREY` | 浅灰 |
| `GRAY_BROWN`、`DARK_BROWN`、`LIGHT_BROWN` | 棕色系 |
| `BLACK`、`WHITE`、`PINK`、`LIGHT_PINK`、`ORANGE` | 独立色 |
| `PURE_RED`、`PURE_GREEN`、`PURE_BLUE`、`PURE_CYAN`、`PURE_MAGENTA`、`PURE_YELLOW` | 通道纯值（绘图/示波风格） |
| `LOGO_WHITE`、`LOGO_BLACK`、`LOGO_BLUE`、`LOGO_GREEN`、`LOGO_RED` | 官方 Logo 用色 |
:::

## 颜色工具函数

`manim.utils.color` 还提供一组模块级工具函数：

:::compare
| 函数 | 签名 | 作用 |
| ---- | ---- | ---- |
| `average_color` | `(*colors)` | 多颜色（加权）平均 |
| `color_gradient` | `(reference_colors, length_of_output)` | 生成参考色之间的渐变列表 |
| `interpolate_color` | `(color1, color2, alpha)` | 两色插值（`ManimColor.interpolate` 的函数版） |
| `invert_color` | `(color)` | 颜色取反 |
| `random_color` | `()` | 返回一个随机内置颜色 |
| `hex_to_rgb` | `(hex_string)` | `#RRGGBB` → RGB 数组 |
| `rgb_to_hex` | `(rgb_array)` | RGB 数组 → `#RRGGBB` |
| `color_to_rgb` / `color_to_rgba` | `(color)` | 任意可解析颜色 → 数组 |
| `rgb_to_color` / `rgba_to_color` | `(array)` | 数组 → `ManimColor` |
:::

```python
color_gradient([BLUE_E, GREEN, YELLOW], 12)   # 12 级渐变
average_color(RED, BLUE)                      # 两色平均
```

:::notice tip
提示
老教程中的 `BLUE` 等颜色在旧版是字符串、可以 `+` 拼接取平均；v0.21.0 它们是 `ManimColor` 对象，颜色混合请用 `average_color` 或 `interpolate_color`。
:::

## 更多颜色常量模块

除内置调色板外，`manim.utils.color` 下还有六个大型命名色表模块，每个模块直接以属性形式提供颜色常量：

:::compare
| 模块 | 来源 |
| ---- | ---- |
| `manim.utils.color.XKCD` | XKCD 颜色调查（924 色，如 `XKCD.ACIDGREEN`） |
| `manim.utils.color.SVGNAMES` | SVG 命名色（如 `SVGNAMES.LIGHTSKYBLUE`） |
| `manim.utils.color.DVIPSNAMES` | LaTeX dvips 色（如 `DVIPSNAMES.NAVYBLUE`） |
| `manim.utils.color.X11` | X11 颜色（如 `X11.LIGHTSKYBLUE`） |
| `manim.utils.color.AS2700` | 澳大利亚标准 AS2700（如 `AS2700.N53_BLUE_GREY`） |
| `manim.utils.color.BS381` | 英国标准 BS381（如 `BS381.AIRCRAFT_BLUE`） |
:::

## 常见错误与建议

:::notice warning
常见错误
向 `color=` 传十六进制字符串时别忘了 `#`：`ManimColor("58C4DD")` 会解析失败；正确写法 `ManimColor("#58C4DD")`。
:::

## 自测

:::exercise
如何生成一个从 `RED` 到 `BLUE`、共 7 个颜色的列表，并把第 3 个颜色设为一条线的颜色？
:::answer
用 `color_gradient` 一次生成，按下标取值：

```python
palette = color_gradient([RED, BLUE], 7)
line = Line(LEFT, RIGHT, color=palette[2])
```
:::
:::

:::exercise
深色的标题文字 `ManimColor("#0A1444")` 想配一个自动可读的强调色（深色配白、浅色配黑），怎么做？
:::answer
用 `contrasting()`，它按颜色亮度自动返回黑或白：

```python
title_color = ManimColor("#0A1444")
accent = title_color.contrasting()   # 深色 -> WHITE；也可传 threshold 调阈值
```
:::
:::

## 下一步

到这里基础图形板块接近尾声：你已经掌握了线、圆弧、布尔组合、标注与颜色。下一板块进入文本与公式。
