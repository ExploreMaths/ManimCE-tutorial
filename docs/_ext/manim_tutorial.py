"""Custom directives for the ManimCE tutorial Sphinx site.

Everything that has a native Sphinx equivalent lives in plain MyST
(see scripts/build_docs.py); only two build-time behaviors need custom
directives:

- {demo} <example.py> <Scene>: video player + <details> with the example
  source injected at build time from examples/ (no native equivalent).
- {manimsig} <Name>: auto-generated signature line for a public manim API
  (inspected from the installed manim package) plus a link to the official
  v0.21.0 docs via intersphinx. Emits nothing for names not exported by
  manim (methods, CLI flags, IPython magics, ...).
"""

from __future__ import annotations

import html
import inspect
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx import addnodes
from sphinx.util import logging

logger = logging.getLogger(__name__)

_MANIM_NS: dict | None = None


def _manim():
    """Import manim once per build (lazy so table-only builds stay fast)."""
    global _MANIM_NS
    if _MANIM_NS is None:
        try:
            import manim
        except Exception as err:  # noqa: BLE001 - manim optional at build time
            logger.warning(f"manimsig: manim not importable ({err}); skipping all")
            _MANIM_NS = {}
        else:
            _MANIM_NS = vars(manim)
    return _MANIM_NS


def _fmt_default(value: object) -> str:
    text = repr(value)
    return text if len(text) <= 24 else text[:21] + "…"


def _signature_text(name: str, obj: object) -> str | None:
    try:
        sig = inspect.signature(obj)
    except (TypeError, ValueError):
        return None
    parts: list[str] = []
    for p in sig.parameters.values():
        if p.kind is p.VAR_POSITIONAL:
            parts.append("*" + p.name)
        elif p.kind is p.VAR_KEYWORD:
            parts.append("**" + p.name)
        elif p.default is not p.empty:
            parts.append(f"{p.name}={_fmt_default(p.default)}")
        else:
            parts.append(p.name)
    return f"{name}({', '.join(parts)})"


class DemoDirective(Directive):
    """```{demo} examples/ch04/number_line.py NumberLineDemo

    optional caption (markdown, parsed inline)
    ```
    """
    required_arguments = 2
    optional_arguments = 0
    has_content = True

    def run(self):
        env = self.state.document.settings.env
        example_arg = self.arguments[0].replace("\\", "/")
        scene = self.arguments[1]
        if example_arg.startswith("examples/"):
            example_arg = example_arg[len("examples/"):]
        if example_arg.endswith(".py"):
            example_arg = example_arg[:-3]
        example, _, basename = example_arg.rpartition("/")

        src_path = Path(env.config.manim_examples_dir) / f"{example_arg}.py"
        if not src_path.is_file():
            return [self.state.document.reporter.error(
                f"{{demo}}: missing example examples/{example_arg}.py", line=self.lineno)]
        code = src_path.read_text(encoding="utf-8")

        video_rel = f"{example}/{basename}__{scene}.mp4"
        video_exists = (Path(env.config.manim_media_dir) / video_rel).is_file()
        media_url = env.config.manim_media_url.rstrip("/")

        container = nodes.container(classes=["demo-block"])
        # caption
        if any(line.strip() for line in self.content):
            cap = nodes.container(classes=["demo-caption"])
            self.state.nested_parse(self.content, self.content_offset, cap)
            container.append(cap)
        # video or placeholder
        if video_exists:
            video_html = (
                '<div class="demo-video-area">'
                f'<video controls preload="metadata" playsinline '
                f'src="{media_url}/{html.escape(video_rel)}"></video>'
                "</div>"
            )
        else:
            video_html = (
                '<div class="demo-video-area demo-video-missing" '
                f'data-src="{media_url}/{html.escape(video_rel)}">'
                "<span>🎬 视频渲染中……</span></div>"
            )
        container.append(nodes.raw("", video_html, format="html"))
        # source in <details>
        container.append(nodes.raw(
            "", '<details class="demo-source"><summary>查看源码 '
               f'<code class="docutils literal">{html.escape(basename)}.py</code>'
               "</summary>",
            format="html"))
        container.append(nodes.literal_block(code, code, language="python"))
        container.append(nodes.raw("", "</details>", format="html"))
        return [container]


class ManimSigDirective(Directive):
    """```{manimsig} NumberLine

    Auto signature line for a public manim API + link to the official docs.
    Silently skipped when manim is not importable or the name is not a
    top-level manim export (methods, CLI flags, IPython magics, ...).
    """
    required_arguments = 1
    optional_arguments = 0
    has_content = False

    def run(self):
        name = self.arguments[0]
        obj = _manim().get(name)
        if obj is None:
            return []
        sig_text = _signature_text(name, obj)
        if sig_text is None:
            return []
        kind = "class" if inspect.isclass(obj) else "function"
        fullname = f"{obj.__module__}.{obj.__qualname__}"
        para = nodes.paragraph(classes=["manim-sig"])
        para.append(nodes.literal(sig_text, sig_text))
        xref = addnodes.pending_xref(
            "",
            nodes.inline("", "官方文档 ↗"),
            refdomain="py",
            reftype=kind,
            reftarget=fullname,
        )
        xref["classes"] = ["manim-sig-link"]
        para.append(nodes.Text(" "))
        para.append(xref)
        return [para]


def setup(app):
    app.add_config_value("manim_examples_dir", "examples", "env")
    app.add_config_value("manim_media_dir", "media", "env")
    app.add_config_value("manim_media_url", "/media/", "env")
    app.add_directive("demo", DemoDirective)
    app.add_directive("manimsig", ManimSigDirective)
    return {"version": "1.0", "parallel_read_safe": False}
