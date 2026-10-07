# ManimCE Tutorial

> A complete interactive tutorial site for ManimCE v0.21.0 — every class and function, rendered video demos, an interactive inheritance graph, and reading progress tracking. Built with Vue 3, GitHub Actions incremental rendering, deployed on Cloudflare Pages.

Manim Community Edition v0.21.0 的完整中文交互式教程站：

- **7 大板块、62 节、259 个 API 条目**：入门、基础图形、文本与公式、坐标系与数据可视化、动画进阶、3D 与摄像机、高级主题。
- **每个类/函数五要素讲解**：签名、参数表（`:::params`）、继承链、易错点提示、与相近 API 的对比，全部配**预渲染动画演示**。
- **交互继承图**：可视化 Manim 核心类层级，可点击跳转。
- **阅读进度记忆**：本地记录每节阅读状态，支持搜索（API 索引 + 全文检索）与暗色模式。

## 仓库结构

```
.
├── content/                  # 内容源
│   ├── site.config.json      #   板块/章节结构 + 每节 covers 清单（唯一事实来源）
│   ├── chapters/<part>/<section>.md   # 章节 Markdown（指令方言）
│   ├── glossary.json         #   术语表
│   ├── inheritance.json      #   继承图数据
├── examples/                 # 示例场景源码（一文件一场景）
│   └── _shared/              #   共享辅助代码（渲染时跳过）
├── scripts/
│   ├── build_content.py      #   Markdown → src/data/*.json
│   ├── render_examples.py    #   增量渲染 examples/ → media/*.mp4
│   └── merge_media.py        #   media/ → dist/media/（部署前合并）
├── src/                      # Vue 3 前端（views/components/composables/data）
├── .github/workflows/build.yml  # CI：增量渲染 + 部署 Cloudflare Pages
├── media/                    # 渲染产物（gitignore，由 CI 生成/缓存）
└── dist/                     # 构建产物（gitignore）
```

## 本地开发

**环境要求**

- Node.js 18+（CI 使用 20）
- Python 3.10+，安装 `manim==0.21.0`（`pip install -r requirements.txt`，渲染缓存哈希依赖该版本号）
- 可选：LaTeX（TeX Live）或 Typst——仅渲染含 `Tex` / `MathTex` 的示例时需要

**安装与启动**（Windows 用 `py -3`，macOS/Linux 用 `python3`）

```bash
# 1. 安装前端依赖
npm ci

# 2. 安装 Python 依赖
pip install -r requirements.txt

# 3. 生成内容数据（Markdown → src/data/*.json）
py -3 scripts/build_content.py

# 4. 启动开发服务器
npm run dev
```

其他常用命令：

```bash
npm run build        # 生产构建（输出 dist/）
npm run preview      # 本地预览构建产物
npm run typecheck    # vue-tsc 类型检查

# 校验 covers 完整性（缺失时退出码 1，CI 中作为非阻塞告警）
py -3 scripts/build_content.py --strict
```

> 本地开发不渲染视频也能跑：`:::demo` 块在 `media/` 下找不到对应 mp4 时照常输出代码块，仅没有视频。

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

`site.config.json` 中每节的 `covers` 列表与该节 Markdown 里的 `## 标题`（剥掉行内首个 `` `代码` `` 后）**一一对应**：匹配上的二级标题以其 API 名作为锚点进入搜索索引和 API 目录（首字母大写记为 class，否则为 function）。运行 `py -3 scripts/build_content.py --strict` 可校验，缺失会在构建时输出 `MISSING covers`。

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

产物落在本地 `media/` 下，重新执行 `build_content.py` 后 `npm run dev` 即可预览视频。

**增量原理**（`media/manifest.json`）：每个示例以相对路径为键，缓存值 = `sha256(源文件字节 + "\nmanim==0.21.0" 盐)`。当且仅当哈希一致、`status == "ok"` 且记录的视频文件存在时直接复用；任一条件不满足即入队重渲（子进程调用 `manim render -qm --format mp4`）。单个示例失败**不阻塞**整体（退出码仍为 0），失败列表写入 `media/render-summary.json` 由 CI 汇总展示。源文件被删除时其缓存条目自动清理。

## CI 与部署

`.github/workflows/build.yml`（触发：`push` 到 `main` 或手动 `workflow_dispatch`，并发串行）：

1. 检出 `main`，并检出 `media` 分支到 `media/` 作为渲染缓存（不存在则首次全量渲染）；
2. 安装系统依赖（ffmpeg、pango、cairo、精简 TeX Live）与 `requirements.txt`；
3. `build_content.py --media-dir media` 生成内容，`--strict` 覆盖率检查作为非阻塞告警；
4. `render_examples.py` 增量渲染，渲染摘要（复用/新渲/失败清单）写入 Job Summary；
5. 将 `media/` 提交回推 `media` 分支（推送被拒时自动 rebase 重试一次）——**视频不进入 main，缓存与历史留在 media 分支**；
6. `npm ci && npm run build`，`merge_media.py` 把 `media/*.mp4` 合并进 `dist/media/`；
7. `cloudflare/pages-action@v1` 部署 `dist/` 到 Cloudflare Pages（项目名 `ManimCE-tutorial`）。

部署所需 `CF_API_TOKEN` / `CF_ACCOUNT_ID` 两个 secrets 已配置好，**推送 `main` 即自动部署**到 <https://manimce-tutorial.pages.dev>。

**可选：自定义域名**——Cloudflare 控制台 → Pages 项目 → **Custom domains** → 添加域名，再按提示在 DNS 中添加一条 CNAME 记录指向 `manimce-tutorial.pages.dev` 即可（免费套餐支持）。

## 迁移预案：media 分支 → Cloudflare R2

Cloudflare Pages 站点总重超过 1GB 时的迁移路径（只需替换产物上传/同步环节，前端与渲染管线不变）：

1. **建 bucket**：Cloudflare 控制台创建 R2 bucket（如 `manimce-tutorial-media`），开启公开访问（Public access）或经 CDN/Worker 反向代理暴露；
2. **迁移存量**：用 `rclone` 或 `aws s3 sync` 把 `media` 分支内容（注意排除 `manifest.json` / `render-summary.json`）同步到 bucket；
3. **改工作流**：把「Commit and push media branch」步骤替换为 `aws s3 sync media/ s3://<bucket>/`（增量上传，manifest 依旧照写 bucket 或保留在 artifacts 中供缓存读取）；
4. **改前端 URL 前缀**：把视频 URL 前缀从 `media/` 换为 R2 域名（如 `https://media.example.com/`），`:::demo` 引用逻辑不变。

## 许可与致谢

- 许可证：MIT
- 感谢 [Manim Community](https://www.manim.community/) 开发出如此优秀的动画引擎。
