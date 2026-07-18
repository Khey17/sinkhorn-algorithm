# Sinkhorn Algorithm Notes

Foundational notes and demos on entropic optimal transport / Sinkhorn, from a Computational Optimal Transport reading seminar (Summer 2026).

**Site:** [khey17.github.io/sinkhorn-algorithm](https://khey17.github.io/sinkhorn-algorithm/)

This is a working-notes site (not an expert guide). Main reference: Peyré & Cuturi ([arXiv:1803.00567](https://arxiv.org/abs/1803.00567)).

## Outline

| Path | What |
|------|------|
| `docs/` | MkDocs site (home, notes chapters, notebook) |
| `notebooks/sinkhorn_OT_demo.ipynb` | Runnable Sinkhorn demo |
| `notes/` | Handwritten PDFs |
| `assets/` | ε slider + sketches |

## Local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # site preview
jupyter notebook notebooks/sinkhorn_OT_demo.ipynb
```
