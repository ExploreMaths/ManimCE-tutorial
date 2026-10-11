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

Also registers an autodoc-process-docstring hook: manim class docstrings
contain ``.. manim::`` example blocks (rendered by manim's own Sphinx
extension upstream, which we do not ship). They are demoted to static
``code-block`` listings so the example code survives autodoc intact.
"""

from __future__ import annotations

import html
import inspect
import re
from pathlib import Path

import jinja2
from docutils import nodes
from docutils.parsers.rst import Directive
from manim.utils.docbuild.manim_directive import ManimDirective
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


class DemoDirective(ManimDirective):
    r"""```{demo} examples/ch04/number_line.py NumberLineDemo

    optional caption (markdown, parsed inline)
    ```

    A subclass of manim's own ``.. manim::`` directive
    (:class:`manim.utils.docbuild.manim_directive.ManimDirective`) that keeps
    its jinja-template + ``insert_input`` rendering mechanism but replaces the
    build-time rendering with a lookup of CI-pre-rendered videos under
    ``manim_media_dir`` (falling back to a placeholder when the video is not
    rendered yet). The directive arguments are ``<example> <Scene>`` instead
    of the scene class name, and the source comes from ``manim_examples_dir``
    instead of the directive content. Options are inherited from the base
    directive (``:ref_classes:`` and friends are accepted for parity; they are
    not rendered because no build-time rendering happens).
    """

    required_arguments = 2
    optional_arguments = 0
    has_content = True
    option_spec = ManimDirective.option_spec

    def run(self) -> list[nodes.Element]:
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

        caption = [line for line in self.content if line.strip()]
        source_block = "\n".join("      " + line for line in code.split("\n"))
        rendered_template = jinja2.Template(DEMO_TEMPLATE).render(
            caption=caption,
            basename=html.escape(basename),
            video_exists=video_exists,
            media_url=html.escape(media_url),
            video_rel=html.escape(video_rel),
            source_block=source_block,
        )
        self.state_machine.insert_input(
            rendered_template.split("\n"),
            source=self.state.document.attributes["source"],
        )
        return []


DEMO_TEMPLATE = r"""
.. container:: demo-block

{% if caption %}
   .. container:: demo-caption

{% for line in caption %}
      {{ line }}
{% endfor %}
{% endif %}
   .. raw:: html

      <div class="demo-video-area{% if not video_exists %} demo-video-missing{% endif %}"{% if not video_exists %} data-src="{{ media_url }}/{{ video_rel }}"{% endif %}>
{% if video_exists %}
      <video controls preload="metadata" playsinline src="{{ media_url }}/{{ video_rel }}"></video>
{% else %}
      <span>🎬 视频渲染中……</span>
{% endif %}
      </div>

   .. raw:: html

      <details class="demo-source"><summary>查看源码 <code class="docutils literal">{{ basename }}.py</code></summary>

   .. code-block:: python

{{ source_block }}

   .. raw:: html

      </details>
"""


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
    app.connect("autodoc-process-docstring", _sanitize_manim_docstrings)
    return {"version": "1.0", "parallel_read_safe": False}


_MANIM_EXAMPLE_RE = re.compile(r"^(?P<indent>\s*)\.\. manim\s*::.*$")
_MANIM_OPTION_RE = re.compile(r"^\s*:[a-zA-Z0-9_-]+:.*$")


def _sanitize_manim_docstrings(app, what, name, obj, options, lines):
    """Demote ``.. manim::`` example blocks to static python code-blocks.

    Upstream manim renders these as videos with its own Sphinx extension;
    here we keep the example source as a plain listing and drop the
    directive options (:quality:, :save_last_frame:, :ref_classes:, ...).
    Cross-manual ``:doc:`` references point at manim's own documentation
    tree and do not exist here; they are downgraded to inline literals.
    """
    for idx, line in enumerate(lines):
        lines[idx] = re.sub(r":doc:`([^`]*)`", r"``\1``", line)
    i = 0
    while i < len(lines):
        m = _MANIM_EXAMPLE_RE.match(lines[i])
        if not m:
            i += 1
            continue
        lines[i] = f"{m.group('indent')}.. code-block:: python"
        i += 1
        while i < len(lines) and _MANIM_OPTION_RE.match(lines[i]):
            del lines[i]
