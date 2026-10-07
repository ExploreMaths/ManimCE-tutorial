---
title: 渲染流程与输出结构
---

# 渲染流程与输出结构

了解一次 `manim` 命令背后发生了什么，能帮你在缓存、画质和输出目录问题上少踩很多坑。整体流程是：

1. **逐帧渲染**：`play()` 的每个动画被逐帧光栅化为 PNG 帧。
2. **部分视频（partial movie）**：每个 `play()` / `wait()` 调用的帧先由 ffmpeg 单独编码成一个小视频文件，称为部分视频，并以内容哈希命名缓存。
3. **合并输出**：场景结束时，所有部分视频按顺序拼接为最终的 `<场景名>.mp4`；已缓存的部分视频会直接复用，不重渲染。

正因为按“每次 play 调用”切片，Manim 才能支持增量渲染（`--from_animation_number`）和跨次运行的缓存复用。

## SceneFileWriter

`SceneFileWriter`（位于 `manim.scene.scene_file_writer`）负责上面流程中所有与文件和 ffmpeg 打交道的工作：写入部分视频、合并最终视频、保存最后一帧图片、导出字幕等。

它是对外可见、但面向内部的组件——日常开发你不会直接实例化它，而是通过场景间接使用：

```python
class InspectWriter(Scene):
    def construct(self):
        # 场景持有的文件写入器就是 SceneFileWriter
        writer = self.renderer.file_writer
        print(type(writer).__name__)  # SceneFileWriter
        self.play(Create(Circle()))
```

`Scene` 本身只负责组织动画逻辑，帧如何变成 `.mp4` 完全由 `SceneFileWriter` 与渲染器协作完成。

## 输出目录结构

默认所有产物都写在 `./media/` 下，布局如下：

```text
media/
├── videos/
│   └── <文件 stem>/            # 如 square_to_circle
│       └── 720p30/             # <高>p<帧率>，随画质而变
│           ├── SquareToCircle.mp4
│           └── partial_movie_files/
│               └── SquareToCircle/
│                   ├── <哈希>.mp4
│                   └── partial_movie_file_list.txt
├── images/
│   └── <文件 stem>/<场景名>.png   # -s 保存的最后一帧
├── Tex/                        # LaTeX 中间产物（tex_dir）
├── texts/                      # Text 的中间产物
└── logs/
```

`-o NAME` 可改变输出文件名；`--media_dir PATH` 可把整个 `media` 目录挪到别处。

## QUALITIES

画质档位定义在 `manim.constants.QUALITIES` 字典中，CLI 的 `-q` 标志即对应其中的键：

:::compare
| 档位 | 分辨率 | 帧率 | CLI 缩写 | 适用场景 |
| ---- | ------ | ---- | ---- | ---- |
| fourk | 3840×2160 | 60 | `-qk` | 4K 发布 |
| production | 2560×1440 | 60 | `-qp` | 高质量发布 |
| high | 1920×1080 | 60 | `-qh` | 默认正式档 |
| medium | 1280×720 | 30 | `-qm` | 日常调试（本教程示例档） |
| low | 854×480 | 15 | `-ql` | 快速预览 |
| example | 854×480 | 30 | 无 | 文档与测试示例 |
:::

`high_quality` 是 CLI 不指定 `-q` 时的默认档；`example_quality` 没有专用缩写，主要用于文档与测试。`-r "W,H"` 与 `--fps N` 可以覆盖任意档位的分辨率和帧率。

## 帧尺寸常量

Manim 的坐标系以“帧高”为基准：**默认 `frame_height = 8.0`**，即画面高度对应 8 个坐标单位；宽度按 16:9 推出 **`frame_width ≈ 14.222`**。原点 `(0, 0)` 在画面正中心。

注意这两个值来自 `manim._config`（通过 `from manim import config` 访问 `config.frame_height`），**不要**从 `manim.constants` 导入——`FRAME_HEIGHT` / `FRAME_WIDTH` 并不在那里。`manim.constants` 中常用的是布局缓冲常量：

| 常量 | 值 | 含义 |
| ---- | ---- | ---- |
| `DEFAULT_MOBJECT_TO_MOBJECT_BUFFER` | 0.25 | `next_to` 等布局的默认物体间距 |
| `SMALL_BUFF` | 0.1 | 小间距 |
| `MED_SMALL_BUFF` | 0.25 | 中间距 |
| `MED_LARGE_BUFF` | 0.5 | 较大间距 |
| `LARGE_BUFF` | 1.0 | 大间距 |
| `DEFAULT_DOT_RADIUS` | 0.08 | `Dot` 的默认半径 |

## 只出图：-s

加 `-s` / `--save_last_frame` 只渲染最后一帧并保存为 PNG，适合快速检查构图：

```bash
manim -sqh scene.py MyScene
# 输出 media/images/scene/MyScene.png
```

图片输出在 `media/images/<文件 stem>/` 下，与视频目录相互独立。

## 部分视频与 --from_animation_number

每个 `play()` 调用的部分视频文件名包含该次调用的内容哈希。改代码后，只有内容变化的那次 `play()` 需要重渲染，其余直接复用缓存。

`-n` / `--from_animation_number` 利用这一机制实现增量渲染：

```bash
manim -qm -n 3 scene.py MyScene      # 从第 3 个动画（0 起编号）开始渲染
manim -qm -n 3,6 scene.py MyScene    # 只渲染第 3 到第 6 个
```

被跳过的动画仍会执行对应的 Python 逻辑（以保证场景状态正确），只是不参与输出。相关辅助标志：`--disable_caching`（本次不用缓存）、`--flush_cache`（清空整个部分视频缓存）、`--dry_run`（只跑逻辑不产出任何文件）。

## 常见错误与建议

:::notice warning
常见错误
缓存哈希包含分辨率、帧率等配置。用 `-ql` 调好的场景换 `-qh` 输出时**整段都会重渲染**，反之亦然——这是正常现象，不是缓存坏了。
:::

:::notice warning
常见错误
`media/` 目录可能多达数百 MB，且内容可随时重新生成，请勿提交到 git。官方 `.gitignore` 已包含它；迁移旧项目时请检查。
:::

:::notice tip
提示
产物太多想一次性清空？直接删除 `media/` 目录是安全的，最坏后果是下次渲染慢一点。
:::

## 下一步

命令行与输出结构都清楚了，下一节把 CLI 常用选项一次讲全，并介绍如何把长视频切成带名字的章节（Section）。
