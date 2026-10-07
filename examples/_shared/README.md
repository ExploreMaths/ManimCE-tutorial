# Shared example code

Put shared base scenes, constants and helper functions here. Files under `examples/_shared/` are **not** rendered by `scripts/render_examples.py` and are not part of the incremental-render cache; import them from concrete example files by module path (e.g. `from examples._shared.base import MyBaseScene`).

The `examples/_shared/assets/` folder holds shared binary assets (SVG, images) that demo scenes reference by repo-relative path, e.g. `SVGMobject("examples/_shared/assets/sample.svg")` (CI runs manim from the repo root).
