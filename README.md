# ManimCE Tutorial

> A complete interactive tutorial site for ManimCE v0.21.0 — every class and function, rendered video demos, an interactive inheritance graph, and reading progress tracking. Built with Sphinx + MyST + Furo, GitHub Actions incremental rendering, deployed on Cloudflare Pages.

Manim Community Edition v0.21.0 的完整中文交互式教程站：

- **7 大板块、62 节、259 个 API 条目**：入门、基础图形、文本与公式、坐标系与数据可视化、动画进阶、3D 与摄像机、高级主题。
- **每个类/函数五要素讲解**：签名、参数表（`:::params`）、继承链、易错点提示、与相近 API 的对比，全部配**预渲染动画演示**。
- **交互继承图**：可视化 Manim 核心类层级，可点击跳转。
- **阅读进度记忆**：本地记录每节阅读状态，支持全文搜索与亮/暗主题（Furo 原生）。

## 仓库结构

```
.
├── content/                  # 内容源
│   ├── site.config.json      #   板块/章节结构 + 每节 covers 清单（唯一事实来源）
│   ├── chapters/<part>/<section>.md   # 章节 Markdown（指令方言）
│   ├── glossary.json         #   术语表
│   ├── inheritance.json      #   继承图数据
├── docs/                     # Sphinx 站点
│   ├── conf.py               #   Sphinx 配置（Furo 主题、MyST、扩展）
│   ├── _ext/manim_tutorial.py  # 仅剩两个自定义指令：demo（构建时注入示例源码）、
│   │                           #   manimsig（inspect 生成签名行）；其余全走原生 MyST/Sphinx
│   ├── _static/              #   custom.css / custom.js（进度记忆等交互）
│   ├── requirements.txt      #   站点构建依赖（与渲染依赖分离，避免缓存失效）
│   └── chapters/ …           #   MyST 源（scripts/build_docs.py 生成，勿手改）
├── examples/                 # 示例场景源码（一文件一场景）
│   └── _shared/              #   共享辅助代码（渲染时跳过）
├── scripts/
│   ├── build_docs.py         #   章节 Markdown → docs/ MyST + 首页/API 索引/术语表/重定向
│   ├── render_examples.py    #   增量渲染 examples/ → media/*.mp4
│   └── merge_media.py        #   media/ → 构建输出/media/（部署前合并）
├── .github/workflows/build.yml  # CI：增量渲染 + Sphinx 构建 + 部署 Cloudflare Pages
├── media/                    # 渲染产物（gitignore，由 CI 生成/缓存在 media 分支）
└── requirements.txt          # 渲染依赖（manim 0.21.0 锁版本，缓存哈希依赖它）
```

## 本地开发

**环境要求**

- Python 3.10+（CI 使用 3.12）
- 站点构建依赖：`pip install -r docs/requirements.txt`（Sphinx、Furo、MyST、sphinx-design）
- **graphviz `dot`**：继承关系图与章节内继承链由原生 `{graphviz}` 指令在构建时渲染（Windows 装到 `C:\Program Files\Graphviz`，确认 `dot -V` 可用即可；CI 已用 apt 安装）
- 可选：安装 `manim==0.21.0`（`pip install -r requirements.txt`，渲染缓存哈希依赖该版本号）与 LaTeX——仅本地渲染示例视频、或让 `{manimsig}` 生成真实签名行时需要

**构建与预览**（Windows 用 `py -3`，macOS/Linux 用 `python3`）

```bash
# 1. 生成 MyST 源（章节 + 首页 + API 索引 + 术语表 + 重定向；缺 covers 时退出码 1）
py -3 scripts/build_docs.py

# 2. 构建静态站点（输出 docs/_build/html/）
py -3 -m sphinx -b html docs docs/_build/html

# 3. 本地预览（视频需先把 media/ 合并进输出目录）
py -3 scripts/merge_media.py --media-dir media --dist docs/_build/html
py -3 -m http.server 8000 --directory docs/_build/html
```

章节页面 URL 形如 `/chapters/ch04/number-line.html`。旧版 `/ch/<part>/<section>` 路径由 `_redirects` 301 重定向到新路径。

> 本地不渲染视频也能跑：`{demo}` 块在 `media/` 下找不到对应 mp4 时输出“🎬 视频渲染中……”占位。

## 内容编写指南

### 新增/修改章节

章节文件为 `content/chapters/<part>/<section>.md`，结构由 `content/site.config.json` 登记（part 列表 → sections，每项含 `id` / `title` / `covers`）。文件开头可写 YAML front-matter `title:` 覆盖标题。

Markdown 之上支持以下指令方言（容器以 `:::` 独占一行闭合）：

| 指令 | 用法 |
| --- | --- |
| `:::demo <examples路径> <Scene名>` | 嵌入示例源码 + 预渲染视频；正文为图注。路径须真实存在，如 `:::demo examples/ch02/circle_intro.py CircleIntro` |
| `:::params` | 参数表，表头固定为 `\| name \| type \| default \| desc \|` 的管道表 |
| `:::compare` | 对比表，任意多列管道表 |
| `:::notice <level>` | 提示块，level 取 `version` / `deprecated` / `warning` / `tip`，首行为标题 |
| `:::inheritance` | 继承链，正文用 `A → B → C` 分隔 |
| `:::exercise` + `:::answer` | 练习题，answer 为嵌套容器，两层 `:::` 依次闭合 |

### 新增示例

示例位于 `examples/<part>/*.py`，约定：**一文件一场景**（渲染器取第一个基类名以 `Scene` 结尾的顶层类）；单场景时长 ≤ 5s（时长约定，非脚本强制）；**文件路径创建后不可改名/移动**——增量渲染以「相对路径（去扩展名）」作为缓存键，改名即视为全新示例并重渲。共享代码放 `examples/_shared/`（不参与渲染）。产出的视频名为 `<路径>__<Scene名>.mp4`。

### covers 机制

`site.config.json` 中每节的 `covers` 列表与该节 Markdown 里的 `## 标题`（剥掉行内首个 `` `代码` `` 后）**一一对应**：匹配上的二级标题以其 API 名（小写）作为锚点进入 API 索引；标题 slug 与 cover 不一致时 `build_docs.py` 会自动补显式锚点 `(Cover)=`。运行 `py -3 scripts/build_docs.py` 可校验，缺失会在构建时输出 `MISSING covers` 并以退出码 1 失败。

## 渲染：首次全量与日常增量

推送 `main` 后由 GitHub Actions 自动完成（见下节）。本地手动渲染：

```bash
# 渲染单个示例（最快迭代路径）
py -3 scripts/render_examples.py --media-dir media --only ch02/circle_intro

# 全量/增量渲染（多进程并行，默认 min(4, CPU 核数)）
py -3 scripts/render_examples.py --media-dir media --workers 4

# 只检查缓存状态，不渲染
py -3 scripts/render_examples.py --media-dir media --dry-run
```

产物落在本地 `media/` 下，重新执行 `build_docs.py` + `sphinx-build` 后预览即可看到视频。

**增量原理**（`media/manifest.json`）：每个示例以相对路径为键，缓存值 = `sha256(源文件字节 + "\nmanim==0.21.0" 盐)`。当且仅当哈希一致、`status == "ok"` 且记录的视频文件存在时直接复用；任一条件不满足即入队重渲（子进程调用 `manim render -qm --format mp4`）。单个示例失败**不阻塞**整体（退出码仍为 0），失败列表写入 `media/render-summary.json` 由 CI 汇总展示。源文件被删除时其缓存条目自动清理。

## CI 与部署

`.github/workflows/build.yml`（触发：`push` 到 `main` 或手动 `workflow_dispatch`，并发串行）：

1. 检出 `main`，并检出 `media` 分支到 `media/` 作为渲染缓存（不存在则首次全量渲染）；
2. 安装系统依赖（ffmpeg、pango、cairo、完整 TeX Live、graphviz）与 `requirements.txt`；
3. `render_examples.py` 增量渲染，渲染摘要（复用/新渲/失败清单）写入 Job Summary；
4. 将 `media/` 提交回推 `media` 分支（推送被拒时自动 rebase 重试一次）——**视频不进入 main，缓存与历史留在 media 分支**；
5. 安装 `docs/requirements.txt`，`build_docs.py` 生成 MyST 源（缺 covers 即失败），`sphinx-build` 构建静态站到 `docs/_build/html/`；
6. `merge_media.py` 把 `media/*.mp4` 合并进 `docs/_build/html/media/`；
7. `cloudflare/wrangler-action@v4` 部署 `docs/_build/html/` 到 Cloudflare Pages（项目名 `manimce-tutorial`）。

部署所需 `CF_API_TOKEN` / `CF_ACCOUNT_ID` 两个 secrets 已配置好，**推送 `main` 即自动部署**到 <https://manimce-tutorial.pages.dev>。

**可选：自定义域名**——Cloudflare 控制台 → Pages 项目 → **Custom domains** → 添加域名，再按提示在 DNS 中添加一条 CNAME 记录指向 `manimce-tutorial.pages.dev` 即可（免费套餐支持）。

## 迁移预案：media 分支 → Cloudflare R2

Cloudflare Pages 站点总重超过 1GB 时的迁移路径（只需替换产物上传/同步环节，前端与渲染管线不变）：

1. **建 bucket**：Cloudflare 控制台创建 R2 bucket（如 `manimce-tutorial-media`），开启公开访问（Public access）或经 CDN/Worker 反向代理暴露；
2. **迁移存量**：用 `rclone` 或 `aws s3 sync` 把 `media` 分支内容（注意排除 `manifest.json` / `render-summary.json`）同步到 bucket；
3. **改工作流**：把「Commit and push media branch」步骤替换为 `aws s3 sync media/ s3://<bucket>/`（增量上传，manifest 依旧照写 bucket 或保留在 artifacts 中供缓存读取）；
4. **改视频 URL 前缀**：修改 `docs/conf.py` 中的 `manim_media_url`（如 `https://media.example.com/`），`{demo}` 指令逻辑不变。

## 许可与致谢

- 许可证：MIT
- 感谢 [Manim Community](https://www.manim.community/) 开发出如此优秀的动画引擎。
