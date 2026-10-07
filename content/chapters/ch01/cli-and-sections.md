---
title: CLI 基础与章节分段
---

# CLI 基础与章节分段

`manim` 命令的完整形式是 `manim render [OPTIONS] FILE [SCENE_NAMES]...`，其中 `render` 是默认子命令，可以省略。除 `render` 外还有四个子命令：`cfg`（管理配置文件）、`checkhealth`（检查安装健康度）、`init`（创建项目/场景模板）、`plugins`（管理插件）。

## render 常用选项

:::compare
| 选项 | 作用 |
| ---- | ---- |
| `-q, --quality [l\|m\|h\|p\|k]` | 画质档位，对应 `QUALITIES` 五档 |
| `-r, --resolution "W,H"` | 自定义分辨率（覆盖画质档位） |
| `--fps, --frame_rate N` | 自定义帧率 |
| `-p, --preview` | 渲染结束后预览 |
| `-f, --show_in_file_browser` | 渲染结束后打开输出目录 |
| `-s, --save_last_frame` | 只保存最后一帧为 PNG |
| `-a, --write_all` | 渲染文件中的全部场景 |
| `-n, --from_animation_number N[,M]` | 只渲染第 N 到第 M 个动画（0 起编号） |
| `--format [png\|gif\|mp4\|webm\|mov]` | 输出格式，默认 mp4 |
| `-o, --output_file NAME` | 自定义输出文件名 |
| `--media_dir PATH` | 自定义 media 根目录 |
| `-c, --config_file PATH` | 指定额外的配置文件 |
| `-v, --verbosity LEVEL` | 日志详细程度（DEBUG/INFO/WARNING/ERROR） |
| `--disable_caching` | 本次渲染不使用部分视频缓存 |
| `--flush_cache` | 渲染前清空部分视频缓存 |
| `--dry_run` | 只执行逻辑，不产出任何文件 |
| `--seed N` | 固定随机种子，保证随机效果可复现 |
| `--renderer [cairo\|opengl]` | 选择渲染器，默认 cairo |
| `--progress_bar` | 进度条开关（`yes/no/display`） |
| `--save_sections` | 额外导出章节视频，见下文 |
:::

:::notice deprecated
废弃提醒
`-g, --save_pngs` 与 `-i, --save_as_gif` 在 v0.21.0 已标记为 Deprecated：请改用 `--format png` 与 `--format gif`。旧标志暂时仍可用，但会在日志中给出警告，且未来版本可能移除。
:::

如果文件里有多个场景类，直接在文件名后面跟上场景名即可指定；不写则渲染第一个，`-a` 渲染全部：

```bash
manim -pqm scene.py MyScene OtherScene
```

## Section

`Section` 是场景内“章节”的数据载体，记录在 `manim.scene.section` 中。开启 `--save_sections` 后，场景会按章节切成独立的小视频，并生成一份 JSON 清单，供交互式播放器、自动剪辑等第三方应用使用。

五要素即构造函数的四个参数：

:::params
| name | type | default | desc |
| ---- | ---- | ------- | ---- |
| `type_` | str | — | 章节类型，取 `DefaultSectionType` 的值 |
| `video` | str \| None | None | 章节视频文件名（位于 sections 输出目录） |
| `name` | str | — | 章节名称，来自 `next_section(name=...)` |
| `skip_animations` | bool | — | 该章节是否跳过了动画 |
:::

通常不需要手动构造 `Section`——调用 `next_section()` 时场景会自动创建并追加到 `self.sections`。

## next_section

`Scene.next_section()` 标记一个章节的起点：从上一次 `next_section()` 调用（或场景开头）到这一次调用之间的所有动画，属于上一个章节。

```python
Scene.next_section(
    name="unnamed",
    section_type=DefaultSectionType.NORMAL,
    skip_animations=False,
)
```

典型写法是在 `construct()` 开头和每个内容分界处调用：

:::demo examples/ch01/sections_demo.py SectionsDemo
三次 `next_section()` 把场景切成 intro / shift / outro 三个章节；配合 `--save_sections` 会额外导出 3 个章节视频与一份 JSON 清单。
:::

## DefaultSectionType

`DefaultSectionType` 是定义章节类型的 StrEnum，目前只有唯一成员：

```python
class DefaultSectionType(StrEnum):
    NORMAL = "default.normal"
```

它是为第三方应用预留的扩展点：播放器或剪辑工具可以按 `type` 区分章节的语义（例如正文、跳过、循环等）。当前所有章节都是 `NORMAL`，在 `sections.json` 中体现为 `"type": "default.normal"`。

:::notice deprecated
废弃提醒
旧版教程中的 `SectionScene` **在 v0.21.0 不存在**，请直接使用 `Scene.next_section()`。从旧版本迁移时，删除 `SectionScene` 的继承并在 `construct()` 里插入 `next_section()` 调用即可。
:::

## --save_sections 与 sections.json

渲染时加上 `--save_sections`：

```bash
manim -qm --save_sections examples/ch01/sections_demo.py SectionsDemo
```

输出结构：

```text
media/videos/sections_demo/720p30/
├── SectionsDemo.mp4            # 完整视频
└── sections/
    ├── SectionsDemo.json       # 章节清单
    ├── SectionsDemo_0000_intro.mp4
    ├── SectionsDemo_0001_shift.mp4
    └── SectionsDemo_0002_outro.mp4
```

`SectionsDemo.json` 是一个数组，每个元素描述一个章节：名称、类型、视频文件、分辨率、帧数、时长、编码等元数据。文件名中的序号是章节在场景中的顺序，名称取自 `next_section(name=...)`。

## 常见错误与建议

:::notice warning
常见错误
`next_section()` 只切分视频，不影响播放顺序和动画本身；忘加 `--save_sections` 时它不会产生任何文件，日志里也没有明显提示。
:::

:::notice tip
提示
`-n` 与 `--save_sections` 可以组合：跳过的动画不进入任何章节，章节序号会相应前移。用 `-n` 调试后半段场景时，不要惊讶于 sections 目录里只有部分章节。
:::

## 自测

:::exercise
场景里有 8 个 `play()` 调用，如何只渲染第 3 到第 5 个（按 1 起数）？
:::answer
动画编号从 0 开始，第 3 到第 5 个对应编号 2 到 4：

```bash
manim -qm -n 2,4 scene.py MyScene
```
:::
:::

:::exercise
已经用 `next_section()` 把场景分好章节，为什么 `media/` 里找不到章节视频？
:::answer
`next_section()` 本身不产生文件，必须加 `--save_sections` 才会导出 `sections/` 目录（章节视频 + `<场景名>.json` 清单）。
:::
:::

:::exercise
旧脚本里的 `-i` 标志在 v0.21.0 还能用吗？推荐怎么改？
:::answer
暂时仍可用，但它已标记为 Deprecated 并会打印警告。推荐改用 `--format gif`；同理 `-g` 改用 `--format png`，其他输出格式（mp4/webm/mov）也由 `--format` 统一控制。
:::
:::

## 下一步

入门板块到此结束：你已经会安装、写场景、控制画质和输出。下一板块进入图形世界，从 `Mobject` 核心概念讲起。
