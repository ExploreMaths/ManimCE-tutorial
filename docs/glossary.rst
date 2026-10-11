======
术语表
======

.. container:: table-scroll

   .. list-table::
      :header-rows: 1

      * - ``Mobject``
        - 数学对象
        - Manim 中一切可见（与部分不可见）对象的基类，构成场景内容的树形结构。
      * - ``VMobject``
        - 向量数学对象
        - 基于贝塞尔曲线的矢量图形对象基类，Text、Circle 等绝大多数图形都是它的子类。
      * - ``Scene``
        - 场景
        - 动画的舞台。继承 Scene 并实现 construct() 即可定义一个可渲染的场景。
      * - ``Updater``
        - 更新器
        - 挂在 Mobject 上的函数，每帧被调用以更新对象状态，常用于数值联动与持续动画。
      * - ``Rate Function``
        - 速率函数
        - 把动画进度 α∈[0,1] 映射为插值系数的函数，控制动画加速减速等节奏。
      * - ``Submobject``
        - 子对象
        - 属于某个 Mobject 的子节点，随父对象一起变换、淡入淡出。
      * - ``Bezier Curve``
        - 贝塞尔曲线
        - VMobject 的底层表示：若干锚点与控制点定义的三次贝塞尔曲线段序列。
      * - ``Camera``
        - 摄像机
        - 负责把 Mobject 绘制为像素帧的对象，决定分辨率、帧率与视角。
      * - ``Frame``
        - 帧
        - 动画的最小时间单位；一个 run_time 为 2 秒、30fps 的动画共 60 帧。
      * - ``Renderer``
        - 渲染器
        - 执行帧生成与视频编码的后端，v0.21.0 提供 Cairo（默认）与 OpenGL 两种。
      * - ``Cairo``
        - Cairo
        - 默认的软件光栅化渲染器，输出确定性高，适合精确构图与测试。
      * - ``OpenGL``
        - OpenGL
        - 基于 GPU 的实验性渲染器（--renderer=opengl），速度快但不保证逐帧一致。
      * - ``Pango``
        - Pango
        - Text/MarkupText 背后的文字排版库，负责把字符串转成可渲染的矢量字形。
      * - ``LaTeX``
        - LaTeX
        - 专业排版系统；Tex/MathTex 通过调用 LaTeX 生成 SVG 再导入场景。
      * - ``Typst``
        - Typst
        - 新一代排版系统；v0.21.0 新增 MathTypst，可作为 LaTeX 之外的公式方案。
      * - ``ValueTracker``
        - 数值跟踪器
        - 一个不可见的 Mobject，用来在动画中平滑地插值数值，配合 Updater 使用。
      * - ``lag_ratio``
        - 错峰比例
        - AnimationGroup/play 中多个动画依次错开的比例，0 表示完全同时。
      * - ``run_time``
        - 时长
        - 动画播放的秒数，可在 play() 或动画构造时指定。
      * - ``partial movie file``
        - 分片视频
        - 渲染时按 play 调用切分的中间 mp4 片段，最终由 ffmpeg 拼接。
      * - ``media directory``
        - 输出目录
        - manim 的输出根目录（--media_dir），内含 videos/ 与 images/ 子目录。
      * - ``config``
        - 配置
        - manim 的多层配置体系：CLI 参数 > 命令行 config 文件 > 用户配置 > 默认配置。
      * - ``CLI``
        - 命令行接口
        - manim 命令本身，负责渲染、插件、初始化项目等全部入口操作。
      * - ``plugin``
        - 插件
        - 通过 entry point 注册到 manim 的第三方扩展，安装后自动加载。
      * - ``entry point``
        - 入口点
        - Python 打包机制中声明的注册点；manim 插件借此被发现与加载。
      * - ``ManimColor``
        - Manim 颜色
        - v0.18 起统一的颜色类型，替代旧的颜色常量字符串，支持运算与插值。
      * - ``SVG``
        - 可缩放矢量图
        - 矢量图格式；Tex/MathTex/Text 的底层载体，也可直接用 SVGMobject 导入。
      * - ``PNG``
        - 位图格式
        - 位图格式；ImageMobject 导入的图像格式，也可通过 --format png 输出帧。
      * - ``FFMPEG``
        - 视频编码器
        - manim 依赖的开源视频编码工具，负责把分片拼接并编码为 mp4。
      * - ``tex template``
        - TeX 模板
        - Tex/MathTex 使用的 LaTeX 文档模板，可通过 TexTemplate 定制宏包与导言区。
      * - ``section``
        - 章节
        - 本教程内容的一级组织单元，对应 content/chapters/<part>/<section>.md 一个文件。
      * - ``construct``
        - 构造方法
        - Scene 子类必须实现的方法，渲染器调用它来搭建并播放整个场景。
      * - ``play``
        - 播放动画
        - Scene 的方法，把一个或多个 Animation 加入当前时间点并播放。
      * - ``wait``
        - 等待
        - Scene 的方法，让画面静止指定秒数，等效于播放一个空动画。
      * - ``z-index``
        - 层级
        - Mobject 的 z_index 属性，控制同深度下对象的叠放顺序，越大越靠上。
      * - ``stroke``
        - 描边
        - 矢量图形的轮廓线；可设置颜色、宽度（stroke_width）与透明度。
      * - ``fill``
        - 填充
        - 矢量图形内部的着色；set_fill 控制颜色与不透明度。
      * - ``gradient``
        - 渐变
        - 让 fill 或 stroke 在多色之间线性过渡，VMobject 支持逐子路径设置。
      * - ``anchor``
        - 锚点
        - 贝塞尔曲线上的点：锚点（anchor）落在曲线上，控制点（handle）决定切线方向。
      * - ``frame rate``
        - 帧率
        - 每秒帧数（fps），由质量标志（-ql/-qm/-qh）决定，影响动画流畅度与文件大小。
      * - ``分辨率``
        - 分辨率
        - 输出视频的像素尺寸，随质量标志变化，也可通过 config 自定义。
      * - ``quality``
        - 画质
        - CLI 质量标志（-ql/-qm/-qh/-qk 等）的统称，同时决定分辨率与帧率。
      * - ``增量渲染``
        - 增量渲染
        - 本教程示例视频的缓存机制：示例文件内容哈希未变时直接复用已有视频。
      * - ``manifest``
        - 清单文件
        - media/manifest.json，记录每个示例的哈希、视频路径与渲染状态。
      * - ``hash``
        - 哈希
        - 示例文件内容（含 manim 版本盐）的 SHA-256，作为增量渲染的缓存键。
      * - ``VGroup``
        - 向量组
        - VMobject 的容器，把多个 VMobject 组合成一个整体统一操作。
      * - ``ThreeDScene``
        - 三维场景
        - 支持 3D 相机运动的场景类，可设置 phi/theta/gamma 观察角度。
      * - ``phi/theta/gamma``
        - 摄像机视角
        - ThreeDCamera 的三个角度参数：phi 极角、theta 方位角、gamma 画面旋转。
