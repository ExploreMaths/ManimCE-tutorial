---
title: 位图与 SVG
---

# 位图与 SVG

本节介绍两种“外部资源”图形：像素图片（`ImageMobject` 家族）与矢量图（`SVGMobject` 家族）。

## AbstractImageMobject

`AbstractImageMobject` 是所有图片 mobject 的抽象基类，位于 `manim.mobject.types.image_mobject` 模块（**没有**导出到 `manim` 顶级命名空间，需要显式导入）。它负责像素数据的读取、缩放与分辨率换算，日常使用直接用其子类 `ImageMobject`。

```python
from manim.mobject.types.image_mobject import AbstractImageMobject
```

:::inheritance
ImageMobject → AbstractImageMobject → Mobject
:::

## ImageMobject

`ImageMobject` 在场景中显示一张位图，图片来源可以是**文件路径**，也可以直接是**内存中的 numpy 数组**。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `filename_or_array` | StrPath \| NDArray | — | 图片文件路径，或 HxW(xC) 的 numpy 数组 |
| `scale_to_resolution` | int | 1080 | 构造时把图片高度缩放到该像素数对应的 Manim 高度 |
| `invert` | bool | False | 是否做黑白反转 |
| `image_mode` | str | RGBA | 像素格式，如 RGBA、RGB、L |
:::

```python
ImageMobject("photo.png")              # 从文件加载
ImageMobject(np.zeros((64, 64, 4), dtype=np.uint8))  # 从内存数组构造
```

:::demo examples/ch02/image_array_demo.py ImageArrayDemo
`ImageMobject` 直接用 numpy 数组构造 64×64 棋盘格，无需任何外部图片文件；`scale_to_resolution` 保证像素图在不同分辨率下尺寸一致，之后用 `scale` / `.animate` 控制大小。
:::

常见坑：

- 数组构造时 dtype 必须是 `np.uint8`，通道顺序为 RGBA；数组必须是三维（高 × 宽 × 通道）。
- `ImageMobject` 是像素图，`set_stroke` / `set_fill` 对它无效；想“框住”图片请叠一个 `SurroundingRectangle`。

## SVGMobject

`SVGMobject` 把 SVG 文件解析为矢量 mobject：路径、填充、描边都会尽量保留，之后可以像普通 VMobject 一样着色、变换。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `file_name` | str \| PathLike \| None | None | SVG 文件路径（相对渲染时的当前工作目录） |
| `should_center` | bool | True | 是否把图形居中到原点 |
| `height` | float \| None | 2 | 构造后缩放到该高度；None 保持原尺寸 |
| `width` | float \| None | None | 缩放到该宽度；与 height 同时给时按最后逻辑生效 |
| `color` | ParsableManimColor \| None | None | 整体描边色覆盖 |
| `opacity` | float \| None | None | 整体不透明度覆盖 |
| `fill_color` / `fill_opacity` | — \| None | None | 填充覆盖 |
| `stroke_color` / `stroke_opacity` / `stroke_width` | — \| None | None | 描边覆盖 |
| `svg_default` | dict \| None | None | 解析 SVG 时的默认样式（如 `{"fill_color": ...}`） |
| `path_string_config` | dict \| None | None | 路径字符串解析配置 |
| `use_svg_cache` | bool | True | 是否缓存解析结果（按文件内容哈希） |
:::

```python
star = SVGMobject("examples/_shared/assets/sample.svg", height=3)
star.set_fill(YELLOW, opacity=1)
```

:::demo examples/ch02/svg_mobject_demo.py SvgMobjectDemo
从 `examples/_shared/assets/sample.svg` 加载 SVG，先按文件原样 `DrawBorderThenFill` 入场，再整体替换为黄色填充、红色描边的版本并缩小。CI 从仓库根目录运行 manim，因此这里使用仓库相对路径。
:::

:::notice warning
常见错误
`SVGMobject` 的 `file_name` 是**相对当前工作目录**的路径，不是相对场景文件的路径。本地运行和 CI 的工作目录可能不同，跨环境复现请使用仓库根目录相对的完整路径（如 `examples/_shared/assets/sample.svg`）。
:::

:::notice tip
提示
SVG 文件内容有改动而画面没变？`use_svg_cache=True` 时解析结果按文件内容哈希缓存，正常会自动失效；如果仍看到旧图形，传 `use_svg_cache=False` 排查，或清理媒体缓存目录。
:::

## VMobjectFromSVGPath

`VMobjectFromSVGPath` 从单个 SVG 路径对象（`svgelements.Path`）构造 mobject，是 `SVGMobject` 解析每一段路径时使用的内部类，也被 `Brace` 用来把大括号 SVG 路径变成矢量图形。

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `path_obj` | se.Path | — | svgelements 路径对象 |
| `long_lines` | bool | False | 是否把长直线段细分为多段 |
| `should_subdivide_sharp_curves` | bool | False | 是否细分急转弯曲线 |
| `should_remove_null_curves` | bool | False | 是否移除零长度曲线 |
:::

日常几乎不需要手动构造；理解它有助于排查 SVG 解析问题（例如急角显示异常时开启 `should_subdivide_sharp_curves`）。

:::inheritance
VMobjectFromSVGPath → VMobject
:::

## 常见错误与建议

:::notice tip
提示
位图与矢量的选择：需要照片、截图、渐变时选 `ImageMobject`；需要无损缩放、按路径着色时选 `SVGMobject`。两者都支持 `FadeIn`、`.animate` 等所有通用动画。
:::

## 自测

:::exercise
场景要展示一张临时生成的热力图（代码里用 numpy 算出来的 2D 数组），又不想写临时图片文件，怎么做？
:::answer
把 2D 数据归一化后映射成 RGBA 的 `np.uint8` 数组，直接传给 `ImageMobject`：

```python
data = np.random.rand(64, 64)
rgba = np.zeros((64, 64, 4), dtype=np.uint8)
rgba[..., 0] = (data * 255).astype(np.uint8)   # 红通道表示数值
rgba[..., 3] = 255                             # 不透明
self.add(ImageMobject(rgba))
```
:::
:::

## 下一步

最后一节介绍颜色系统：`ManimColor`、调色板常量与颜色工具函数。
