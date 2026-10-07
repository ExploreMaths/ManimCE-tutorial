---
title: 配置系统深度
---

# 配置系统深度

ch01 用过 `-qm`、`--media_dir` 等 CLI 选项。这些选项背后是一个统一的配置系统：`manim._config.config`（一个 `ManimConfig` 实例）。本节讲清它的优先级链、配置文件格式与常用字段。

## 优先级链

一次渲染的最终配置由五层来源合并而成，**高优先级覆盖低优先级**：

:::compare
| 优先级 | 来源 | 说明 |
| ------ | ---- | ---- |
| 最高 | CLI 命令行选项 | 如 `-qm`、`--format gif`，只影响本次运行 |
| 高 | `-c/--config_file` 指定的文件 | 只影响本次运行；**替代**目录级 `manim.cfg` |
| 中 | 目录级 `manim.cfg` | 当前工作目录下的 `manim.cfg`，只对目录内场景生效 |
| 低 | 用户级 `manim.cfg` | 对该用户所有项目生效 |
| 最低 | 库自带 `default.cfg` | Manim 安装目录内的默认值，保证每个选项都有值 |
:::

三个 `manim.cfg` 的搜索位置（由 `manim._config.config_file_paths()` 定义）：

- **库级**：安装目录内的 `manim/_config/default.cfg`（只读基准，无需关心路径）
- **用户级**：Windows 为 `%APPDATA%\Manim\manim.cfg`（即 `C:\Users\<用户名>\AppData\Roaming\Manim\manim.cfg`）；macOS / Linux 为 `~/.config/manim/manim.cfg`
- **目录级**：运行 `manim` 命令时**当前工作目录**下的 `manim.cfg`

:::notice tip
提示
注意用户级路径随操作系统变化。老教程常见的 `~/.manim.cfg` 写法在 Windows 上不生效——Windows 的正确位置是 `%APPDATA%\Manim\manim.cfg`。不确定时，用 `manim cfg show` 查看实际生效的值。
:::

## manim.cfg 文件格式

配置文件是 INI 格式，最常用的两个小节是 `[CLI]`（渲染行为）和 `[custom_folders]`（自定义输出目录结构）。一个项目级 `manim.cfg` 示例：

```ini
[CLI]
; 默认中画质，日常调试不用每次敲 -qm
pixel_width = 1280
pixel_height = 720
frame_rate = 30
; 输出格式与目录
format = mp4
media_dir = ./media
; 关掉进度条，便于在 CI 日志里阅读输出
progress_bar = none
; 随机种子固定，保证多人协作结果一致
seed = 42
; 声明本项目依赖的插件（缺失时报警）
plugins = manim_mobject_svg

[custom_folders]
; 配合 CLI --custom_folders 使用，定义输出目录结构
media_dir = videos
video_dir = {media_dir}
```

`{media_dir}`、`{module_name}`、`{quality}`、`{scene_name}` 是占位符，会在运行时被替换为实际值。大部分选项的键名与 CLI 长选项一致（如 `frame_rate`、`disable_caching`），但也有例外：画质档位（`-q`）没有对应的配置键，要用 `pixel_width/pixel_height/frame_rate` 三件套表达。

## ManimConfig 常用字段

脚本里可以通过 `from manim import config` 访问 `ManimConfig` 实例。常用字段（默认值来自库自带 `default.cfg`）：

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `media_dir` | str | `./media` | 输出根目录 |
| `video_dir` | str | `{media_dir}/videos/{module_name}/{quality}` | 视频输出目录模板 |
| `images_dir` | str | `{media_dir}/images/{module_name}` | 图片输出目录模板 |
| `pixel_width` / `pixel_height` | int | 1920 / 1080 | 帧分辨率 |
| `frame_rate` | float | 60 | 帧率 |
| `frame_width` / `frame_height` | float | 14.222… / 8 | 逻辑坐标系尺寸（帧宽/高，只读派生） |
| `format` | str | `mp4` | 输出格式（png/gif/mp4/webm/mov） |
| `renderer` | str | `cairo` | 渲染器（cairo/opengl） |
| `background_color` | ManimColor | BLACK | 背景色 |
| `background_opacity` | float | 1 | 背景不透明度 |
| `quality` | str | `high_quality` | 画质档位名（由 -q 或分辨率决定） |
| `save_last_frame` | bool | False | 只保存最后一帧 |
| `write_to_movie` | bool | True | 是否输出视频文件 |
| `disable_caching` | bool | False | 不使用部分视频缓存 |
| `flush_cache` | bool | False | 渲染前清空部分视频缓存 |
| `max_files_cached` | int | 100 | 部分视频缓存保留的文件数上限 |
| `max_inflight_encoders` | int | 1 | 并行编码的动画数上限 |
| `partial_movie_dir` | str | `{video_dir}/partial_movie_files/{scene_name}` | 部分视频文件目录 |
| `verbosity` | str | INFO | 日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL） |
| `progress_bar` | str | display | 进度条（display/leave/none） |
| `seed` | int \| None | None | 随机种子 |
| `tex_dir` / `text_dir` | str | `{media_dir}/Tex`、`{media_dir}/texts` | LaTeX / 文本中间产物目录 |
| `assets_dir` | str | `./` | `add_sound` 等查找素材的目录 |
:::

用法示例：

```python
from manim import *

config.background_color = "#1a1a2e"   # 改背景
config.verbosity = "WARNING"          # 减少日志输出
config.media_dir = "./my_media"       # 改输出目录

class MyScene(Scene):
    def construct(self):
        ...
```

:::notice warning
常见错误
在场景文件里给 `config` 赋值会**覆盖**同一次运行的 CLI 选项与配置文件值。执行顺序是：`import manim` 时消化配置文件 → CLI 消化命令行选项 → **之后**才导入场景文件，所以场景文件顶部的 `config.xxx = ...` 是最后写入的、最终生效。想让 CLI 说了算，就不要在场景文件里设置同一字段；脚本赋值只适合作为“无 CLI 对应项时的默认值”（已实渲验证：场景里 `config.background_color = "#112233"` 会盖过 `-c` 配置文件中的 `background_color = RED`）。
:::

:::notice tip
提示
`manim cfg show` 打印当前生效的全部配置；`manim cfg write` 交互式生成用户级（`--level user`）或目录级（`--level cwd`）配置模板；`manim cfg export` 把当前配置导出到文件。三个子命令的具体用法见“CLI 深度”一节。
:::

## 常见错误与建议

:::notice warning
常见错误
目录级 `manim.cfg` 只在**当前工作目录**生效，不随场景文件位置自动切换。在别的目录运行 `manim path/to/scene.py` 时，读的是运行命令时所在目录的 `manim.cfg`，不是场景文件旁边的那个。
:::

## 自测

:::exercise
想让某个项目默认以 1280×720@30fps 渲染、且输出目录为项目内的 `./media`，最少要写哪些配置？写在哪？
:::answer
在项目根目录建 `manim.cfg`，在 `[CLI]` 小节写：

```ini
[CLI]
pixel_width = 1280
pixel_height = 720
frame_rate = 30
media_dir = ./media
```

注意 `-q` 画质档没有配置键，必须用分辨率 + 帧率三件套表达。
:::
:::

:::exercise
脚本里写了 `config.background_color = "#112233"`，又用 `manim -ql -c my.cfg scene.py MyScene` 渲染，其中 `my.cfg` 写着 `background_color = RED`。最终背景是什么颜色？
:::answer
`#112233`（脚本里的值）。CLI 的 `-c` 在场景文件导入之前消化，而场景文件里的 `config.background_color = "#112233"` 是最后写入的，直接覆盖配置文件。实测背景像素即 (17, 34, 51) = #112233。要让配置文件说了算，就不要在场景文件里赋值同一字段。
:::
:::

## 下一步

配置决定了“渲染成什么样”，下一节看“渲染得有多快”：性能优化与缓存机制。
