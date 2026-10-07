---
title: CLI 深度
---

# CLI 深度

ch01 掌握了 `manim render` 的常用选项，本节把 `--help` 里其余选项按类别补齐，并讲清配置子命令 `manim cfg` 与 v0.21.0 的弃用标志。所有选项的描述均以本机 `manim render --help` 输出为准。

## 命令结构总览

```text
manim [--version] [--show-splash / --hide-splash] COMMAND
```

子命令一览：

:::compare
| 子命令 | 作用 |
| ------ | ---- |
| `render`（默认） | 渲染场景；`manim file.py Scene` 等价于 `manim render file.py Scene` |
| `cfg` | 管理配置文件（见下文） |
| `checkhealth` | 检查安装健康度（Python 版本、ffmpeg、LaTeX 等依赖） |
| `init` | 创建项目脚手架或向现有文件插入场景模板 |
| `plugins` | 列出已安装的插件（见“插件机制”一节） |
:::

## 渲染控制类

:::compare
| 选项 | 作用 |
| ---- | ---- |
| `-q, --quality [l\|m\|h\|p\|k]` | 画质五档 |
| `-r, --resolution "W,H"` | 自定义分辨率（覆盖画质档） |
| `--fps, --frame_rate FLOAT` | 自定义帧率 |
| `-n, --from_animation_number TEXT` | 只渲染第 N 到 M 个动画（0 起），M 省略则渲染到结尾 |
| `-a, --write_all` | 渲染文件中的全部场景 |
| `--renderer [cairo\|opengl]` | 选择渲染器 |
| `-t, --transparent` | 输出带 alpha 通道的透明背景 |
| `--seed INTEGER` | 固定随机种子 |
| `--dry_run` | 只执行逻辑，不产出图片/视频，也不开窗口 |
:::

## 输出类

:::compare
| 选项 | 作用 |
| ---- | ---- |
| `--format [png\|gif\|mp4\|webm\|mov]` | 输出格式，默认 mp4 |
| `-o, --output_file TEXT` | 自定义输出文件名 |
| `-s, --save_last_frame` | 只保存最后一帧 PNG |
| `-0, --zero_pad INTEGER` | PNG 文件名补零位数（0–9） |
| `--media_dir PATH` | 输出根目录 |
| `--log_dir PATH` / `--log_to_file` | 日志目录 / 把终端日志写入文件 |
| `--write_to_movie` | OpenGL 渲染时写出视频文件（OpenGL 默认只预览） |
:::

## 缓存类

:::compare
| 选项 | 作用 |
| ---- | ---- |
| `--disable_caching` | 本次渲染不使用部分视频缓存（缓存文件仍会生成） |
| `--flush_cache` | 渲染前删除已缓存的部分视频文件 |
| `--max-inflight-encoders N` | 并行编码的动画数上限（默认 1，详见“性能与缓存”） |
| `--encoder-queue-size N` | 每个编码器积压的帧缓冲上限（默认 8，仅并行编码时生效） |
:::

## 日志与交互类

:::compare
| 选项 | 作用 |
| ---- | ---- |
| `-v, --verbosity [debug\|info\|warning\|error\|critical]` | 日志详细程度；同时影响 ffmpeg 日志级别 |
| `--progress_bar [display\|leave\|none]` | 进度条：显示 / 渲染完保留 / 关闭。CI 或管道输出时设 `none` |
| `-p, --preview` | 渲染后预览（OpenGL 弹实时窗口，Cairo 打开播放器） |
| `--show_in_file_browser` | 渲染后在文件管理器中定位输出文件 |
| `--preview_command TEXT` | 自定义预览命令（如 vlc） |
| `--notify_outdated_version / --silent` | 版本过期提醒开关 |
| `--jupyter` | 以 Jupyter magic 方式调用（配合 `%%manim`） |
| `--no_latex_cleanup` | 保留 TeX 产生的 .aux/.dvi/.log 中间文件 |
:::

OpenGL 专属（一般用户用不到）：`--enable_wireframe`、`--force_window`、`--use_projection_fill_strokes`、`--use_projection_stroke_shaders`、`--enable_gui`、`--gui_location`、`--fullscreen`。

## 全局选项

出现在所有子命令之前：`--version`、`--show-splash / --hide-splash`。注意 `--config_file`、`-c` 属于 render 的全局选项组（`-c` 指定配置文件，见“配置系统深度”）。

## v0.21.0 的弃用标志

源码中的弃用警告（`manim/cli/render/commands.py`）确认了三个：

:::notice deprecated
废弃提醒
`-g, --save_pngs` 与 `-i, --save_as_gif` 已标记弃用：请改用 `--format png` 与 `--format gif`。旧标志暂时仍可用，运行时会打印警告并自动映射到对应的 `--format` 值，未来版本可能移除。
:::

:::notice deprecated
废弃提醒
`-f`（`show_in_file_browser` 的短形式）已标记弃用：使用时日志会提示 “The short form of show_in_file_browser is deprecated”。目前功能仍正常，建议改用长选项 `--show_in_file_browser`，为 `-f` 未来改作 `--format` 短选项让路。
:::

## manim cfg 子命令

`manim cfg` 有三个子命令（注意没有 `level` 子命令，`level` 是 `write` 的选项）：

:::compare
| 子命令 | 作用 | 常用选项 |
| ------ | ---- | -------- |
| `cfg show` | 打印当前生效的全部配置值 | — |
| `cfg write` | 交互式生成配置文件 | `-l, --level [user\|cwd]`（用户级或当前目录级）、`-o, --open`（写完后打开） |
| `cfg export` | 把当前配置导出为文件 | `-d, --directory TEXT`（输出目录） |
:::

典型用法：

```bash
manim cfg show                       # 查看生效配置
manim cfg write --level cwd          # 在当前目录生成 manim.cfg 模板
manim cfg export -d ./backups        # 导出当前配置
```

## 常见错误与建议

:::notice warning
常见错误
`-n` 的编号是**动画序号**（每个 `play()` 一个号）而不是时间，且从 0 开始；`upto_animation_number` 配置文件键同理。想按时间截取请用视频剪辑工具。
:::

:::notice tip
提示
记不住选项时记住两个入口：`manim --help` 看子命令全景，`manim render --help` 看全部渲染选项；`manim cfg show` 看“当前这次运行实际生效的值”。三者都是从本机安装版本输出的，永远比网络资料新。
:::

## 自测

:::exercise
想把一个场景的输出格式改成 gif，同时文件名定为 `demo`，命令怎么写？旧的 `-i -o demo` 写法有什么问题？
:::answer
新写法：

```bash
manim -qm --format gif -o demo scene.py MyScene
```

`-i` 在 v0.21.0 已弃用（虽仍可用并打印警告），`-o demo` 本身没问题但注意 gif 模式下输出文件名按 `zero_pad` 与帧序列规则组织。推荐统一用 `--format` 控制输出类型。
:::
:::

:::exercise
`manim cfg write` 想生成项目级配置模板，加什么选项？`cfg export` 与它有什么区别？
:::answer
加 `--level cwd`（或 `-l cwd`）在当前目录生成 `manim.cfg` 模板；`--level user` 则写到用户级位置。`cfg export` 不是生成模板，而是把**当前生效的**配置导出到 `-d` 指定目录——适合备份或迁移配置。
:::
:::

## 下一步

命令行是驱动 Manim 的第一种方式。下一节看第二种方式：在 Python 脚本里直接调用 `Scene.render()`，把 Manim 当库用。
