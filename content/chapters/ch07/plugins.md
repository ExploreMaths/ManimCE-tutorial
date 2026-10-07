---
title: 插件机制
---

# 插件机制

插件（plugin）是把自定义 mobject、动画、工具函数打包成 Python 包、随 `pip` 分发的机制。你的场景文件只要多一行 `import`，就能使用插件提供的全部内容；本节介绍发现、安装、编写插件的方式。

## 插件的发现机制

Manim 使用 Python 标准的 **entry points** 机制发现插件：一个包只要在打包元数据里声明自己属于 `manim.plugins` 组，就会被 `manim plugins -l` 列出来。

对插件作者而言，声明方式是在 `pyproject.toml` 里加一个 entry points 表：

```toml
[project.entry-points."manim.plugins"]
mypackage = "mypackage"
```

`mypackage = "mypackage"` 的含义：entry point 的名字（左侧）是插件名，右侧是 `import` 时执行的模块路径。安装这个包（`pip install .`）之后，它就出现在插件列表里。

对用户而言，查看本机已安装的插件：

```bash
manim plugins -l
```

输出形如：

```text
Plugins:
 • manim_mobject_svg
```

`manim plugins` 子命令只有 `-l/--list` 一个选项，仅负责**列出**插件，不负责安装或卸载——安装就是普通的 `pip install`，卸载是 `pip uninstall`。

## 在场景中使用插件

插件被列出不等于其内容自动可用。**在 v0.21.0，使用插件内容需要在场景文件里显式导入**：

```python
from manim import *
from manim_mobject_svg import SVGMobject  # 插件提供的类
```

配置项 `[CLI] plugins`（逗号分隔的插件名列表）仍然存在：Manim 在导入时会核对这些插件是否已安装，缺失的会在日志中给出警告（`Missing Plugins: ...`）。它是一个“声明依赖、及早报警”的机制，不再触发自动导入。

:::notice version
版本说明
在 v0.18.0 及更早版本中，配置 `[CLI] plugins` 里列出的插件会在 `import manim` 时被**自动导入**；v0.18.1 移除了这一行为，改为显式 `import`。从旧版本迁移的脚本，需要在文件顶部补上对插件的导入语句。见“杂项”一节的废弃提醒写法与本节说明。
:::

:::notice warning
常见错误
`manim plugins -l` 能列出某插件，但场景里 `SomeClass` 报 `NameError`——列出只说明 entry point 存在，不代表名字进了命名空间。检查场景文件顶部是否真的 `import` 了插件提供的模块。
:::

## 社区插件举例

社区维护的插件覆盖了演示播放、物理模拟、机器学习可视化等方向（可用性随时间变化，安装前请以 PyPI 页面为准）：

- `manim-slides`：把场景导出为可键盘控制的演示幻灯片，带后退、跳过、触碰翻页等功能，是最流行的 Manim 生态插件之一
- `manim-physics`：引力场、电磁场、刚体等物理模拟可视化组件
- `manim-ml`：神经网络、Transformer 等机器学习结构的可视化
- `manim_mobject_svg`：把任意 `VMobject` 导出为 SVG 文件（本机已安装，可用 `manim plugins -l` 看到）

这些插件的用法一致：安装后在场景文件顶部显式导入。

## 编写自己的插件

最小可行插件只有三步：

1. 写一个普通 Python 包（`pyproject.toml` + 你的模块），内容就是你想复用的 mobject / 动画 / 工具函数。
2. 在 `pyproject.toml` 中添加上文的 `[project.entry-points."manim.plugins"]` 声明。
3. `pip install .` 后 `manim plugins -l` 能列出它，场景文件 `import` 即可使用。

换言之，插件包本身没有任何 Manim 特有的代码结构要求——entry point 只是一枚“我是 Manim 插件”的徽章。

:::notice tip
提示
插件里的自定义 mobject、自定义 Animation 遵循本节前两节的原则：继承 `VMobject` 重写 `generate_points`，或继承 `Animation` 重写插值钩子。把调试工具（如 `manim.utils.debug` 的 `index_labels`）一并收进插件，团队的调试体验也会一致。
:::

## 常见错误与建议

:::notice warning
常见错误
不要在插件模块顶层执行重活（连接网络、渲染测试片段）。entry point 的加载发生在 `manim plugins -l` 等命令中，顶层代码会被立即执行，拖慢所有命令并可能在没有显示环境的机器上失败。
:::

## 自测

:::exercise
安装了某个插件后，场景里直接使用它提供的类却报 `NameError`，但 `manim plugins -l` 能列出它。可能是什么原因？
:::answer
v0.18.1 起插件不再自动导入，entry point 只负责“登记”。需要在场景文件顶部显式 `import` 插件提供的模块，名字才会进入命名空间。
:::
:::

:::exercise
如何把自己写的 `FancyBanner` mobject 打包成插件供他人 `pip install` 使用？
:::answer
最小做法：建一个 Python 包，把 `FancyBanner` 放进模块里；在 `pyproject.toml` 添加 `[project.entry-points."manim.plugins"]` 表（`包名 = "模块路径"`）；`pip install .` 发布或本地安装。使用者 `pip install` 后在场景文件里显式导入即可。
:::
:::

## 下一步

插件解决“代码如何分享”，接下来的三节转向“渲染如何受控”：先深入配置系统，再看性能与缓存，最后把 CLI 的全部选项一次讲透。
