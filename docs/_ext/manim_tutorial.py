"""Custom directives for the ManimCE tutorial Sphinx site.

- {demo} <example.py> <Scene>: video player + <details> with the example
  source injected at build time from examples/.
- {params}: GFM pipe table (name/type/default/desc) as a styled docutils table.
- {compare}: GFM pipe table with a header row.
- {inheritance}: `A → B → C` chain rendered as styled breadcrumbs.
- {inheritance-graph}: full interactive Graphviz graph (data embedded as JSON,
  rendered client-side with viz.js by _static/custom.js).
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util import logging

logger = logging.getLogger(__name__)


def split_row(s: str) -> list[str]:
    """Split a pipe-table row on *unescaped* pipes (cells may contain '\\|')."""
    s = s.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]


def parse_pipe_table(lines: list[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in lines:
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            rows.append(split_row(s))
        elif rows:
            break
    if len(rows) >= 2 and all(re.fullmatch(r":?-{2,}:?", c or "---") for c in rows[1]):
        rows.pop(1)
    return rows


def unescape_cell(text: str) -> str:
    return text.replace("\\|", "|").strip()


class _CellMixin:
    state: Directive.state  # type: ignore[name-defined]

    def _entry(self, text: str) -> nodes.entry:
        entry = nodes.entry()
        inline_nodes, msgs = self.state.inline_text(unescape_cell(text), self.lineno)
        entry.extend(inline_nodes + msgs)
        return entry

    def _table(self, header: list[str], rows: list[list[str]], classes: list[str]) -> nodes.table:
        ncols = len(header)
        t = nodes.table(classes=classes)
        tgroup = nodes.tgroup(cols=ncols)
        t.append(tgroup)
        for _ in range(ncols):
            tgroup.append(nodes.colspec(colwidth=1))
        thead = nodes.thead()
        tgroup.append(thead)
        hrow = nodes.row()
        for cell in header:
            hrow.append(self._entry(cell))
        thead.append(hrow)
        tbody = nodes.tbody()
        tgroup.append(tbody)
        for r in rows:
            row = nodes.row()
            for cell in r:
                row.append(self._entry(cell))
            tbody.append(row)
        return t


class ParamsDirective(_CellMixin, Directive):
    has_content = True

    def run(self):
        rows = parse_pipe_table(self.content)
        if not rows:
            return [self.state.document.reporter.error(
                "{params}: no pipe table in directive content", line=self.lineno)]
        header = [c.lower() for c in rows[0]]
        if header != ["name", "type", "default", "desc"]:
            return [self.state.document.reporter.error(
                "{params}: header must be | name | type | default | desc |",
                line=self.lineno)]
        table = self._table(rows[0], rows[1:], ["params-table"])
        wrapper = nodes.container(classes=["table-scroll"])
        wrapper.append(table)
        return [wrapper]


class CompareDirective(_CellMixin, Directive):
    has_content = True

    def run(self):
        rows = parse_pipe_table(self.content)
        if not rows:
            return [self.state.document.reporter.error(
                "{compare}: no pipe table in directive content", line=self.lineno)]
        table = self._table(rows[0], rows[1:], ["compare-table"])
        wrapper = nodes.container(classes=["table-scroll"])
        wrapper.append(table)
        return [wrapper]


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


class InheritanceDirective(Directive):
    """```{inheritance}
    NumberLine → Line → TipableVMobject → VMobject
    ```
    """
    has_content = True

    def run(self):
        chain: list[str] = []
        for line in self.content:
            for piece in re.split(r"→|->", line):
                piece = piece.strip()
                if piece:
                    chain.append(piece)
        if not chain:
            return [self.state.document.reporter.error(
                "{inheritance}: empty chain", line=self.lineno)]
        parts: list[str] = []
        for idx, name in enumerate(chain):
            if idx:
                parts.append('<span class="ic-arrow">→</span>')
            parts.append(f'<span class="ic-node">{html.escape(name)}</span>')
        raw = f'<div class="inheritance-chain">{"".join(parts)}</div>'
        return [nodes.raw("", raw, format="html")]


class InheritanceGraphDirective(Directive):
    """Full interactive inheritance graph; nodes JSON passed via :nodes: option."""
    required_arguments = 0
    optional_arguments = 0
    has_content = False
    option_spec = {"nodes": directives.unchanged_required}

    def run(self):
        data = self.options["nodes"].strip()
        # validate JSON early so build fails loudly on a broken data file
        nodes_json = json.dumps(json.loads(data), ensure_ascii=False)
        raw = (
            '<div class="inheritance-graph" id="inheritance-graph">'
            '<div class="graph-toolbar">'
            '<input type="search" class="graph-filter" aria-label="筛选类名" placeholder="筛选类名">'
            '<button type="button" class="graph-btn" data-act="expand">展开全部</button>'
            '<button type="button" class="graph-btn" data-act="collapse">折叠全部</button>'
            "</div>"
            '<div class="graph-container"><p class="state-box">继承关系图加载中……</p></div>'
            f'<script type="application/json" class="inheritance-data">{nodes_json}</script>'
            "</div>"
        )
        return [nodes.raw("", raw, format="html")]


def setup(app):
    app.add_config_value("manim_examples_dir", "examples", "env")
    app.add_config_value("manim_media_dir", "media", "env")
    app.add_config_value("manim_media_url", "/media/", "env")
    app.add_directive("demo", DemoDirective)
    app.add_directive("params", ParamsDirective)
    app.add_directive("compare", CompareDirective)
    app.add_directive("inheritance", InheritanceDirective)
    app.add_directive("inheritance-graph", InheritanceGraphDirective)
    return {"version": "1.0", "parallel_read_safe": True}
