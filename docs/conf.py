"""Sphinx configuration for the ManimCE Chinese tutorial site."""

from __future__ import annotations

import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent
ROOT = DOCS.parent
sys.path.insert(0, str(DOCS / "_ext"))

project = "ManimCE 中文教程"
author = "ExploreMaths"
version = release = "0.21.0"
language = "zh_CN"

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "manim_tutorial",
]

source_suffix = {".md": "markdown"}
root_doc = "index"
exclude_patterns = ["_build", "_extra", "Thumbs.db"]

# --- MyST -----------------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "attrs_inline",
    "attrs_block",
]
myst_heading_anchors = 4

# --- Theme ----------------------------------------------------------------
html_theme = "furo"
html_title = "ManimCE 中文教程"
html_static_path = ["_static"]
html_extra_path = ["_extra"]
html_css_files = ["custom.css"]
html_js_files = ["custom.js"]
html_search_language = "zh"
html_theme_options = {
    "navigation_with_keys": True,
    "top_of_page_buttons": ["view"],
    "source_repository": "https://github.com/ExploreMaths/ManimCE-tutorial",
    "source_branch": "main",
    "source_directory": "docs/",
}

# --- copybutton ------------------------------------------------------------
copybutton_prompt_text = r">>> |\.\.\. |\$ "

# --- manim_tutorial extension ----------------------------------------------
manim_examples_dir = str(ROOT / "examples")
manim_media_dir = str(ROOT / "media")
manim_media_url = "/media/"
