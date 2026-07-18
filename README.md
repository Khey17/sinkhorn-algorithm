# Sinkhorn Algorithm — Entropic Optimal Transport

Demonstration and notes on the **Sinkhorn algorithm** for entropic optimal transport, from the Computational Optimal Transport reading seminar (Summer 2026).

**Live notebook:** [khey17.github.io/sinkhorn-algorithm](https://khey17.github.io/sinkhorn-algorithm/)

## What’s here

| Path | Description |
|------|-------------|
| [`notebooks/sinkhorn_OT_demo.ipynb`](notebooks/sinkhorn_OT_demo.ipynb) | Main demo: Sinkhorn from scratch, vs POT, ε-sweep, oscillation, 2D transport |
| [`notes/`](notes/) | Handwritten notes (Exact OT → Entropy → Sinkhorn) |
| [`assets/`](assets/) | Interactive ε slider (HTML) and Monge vs Kantorovich sketch |

## Main reference

Gabriel Peyré & Marco Cuturi, *Computational Optimal Transport* ([arXiv:1803.00567](https://arxiv.org/abs/1803.00567)).

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/sinkhorn_OT_demo.ipynb
```

## Publish

Pushing to `main` runs GitHub Actions: execute the notebook → HTML → deploy to GitHub Pages.
