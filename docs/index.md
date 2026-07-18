# Sinkhorn Algorithm Notes

Foundational notes and runnable demos on **entropic optimal transport** and the **Sinkhorn algorithm**, from a Computational Optimal Transport reading seminar (Summer 2026).

This is a working notebook + field notes site — not a textbook. I’m learning this material and writing down what clicked.

!!! note "What this is"
    Companion notes to Peyré & Cuturi, *Computational Optimal Transport* ([arXiv:1803.00567](https://arxiv.org/abs/1803.00567)), focused on the entropy / Sinkhorn chapter. Code uses [POT](https://pythonot.github.io/).

## Materials / outline

| Section | What it covers |
|---|---|
| [00. Recap — Monge & Kantorovich](00_recap_ot.md) | Map vs coupling, duality, discrete LP view |
| [01. Entropy & Sinkhorn](01_entropy_sinkhorn.md) | Why blur the plan, $-\varepsilon H$, Sinkhorn updates |
| [02. Sinkhorn notebook](02_sinkhorn_demo.ipynb) | From-scratch Sinkhorn, vs POT, demos, takeaways |
| [Interactive ε slider](epsilon_slider.md) | Watch the plan go blurry ↔ sharp |

## About these notes

### Who is this for?

**You:** comfortable with basic linear algebra / probability, curious about OT, and okay reading a Jupyter notebook.

**This site:** walks through the foundations — Monge → Kantorovich → entropic OT → Sinkhorn — with small examples and plots.

### How to use it

1. Skim **00** and **01** for the story in the notes.  
2. Run (or read) the **02** notebook — same story, executable.  
3. Play with the **ε slider** to feel the blur trade-off.

### Source

All materials are on GitHub: [Khey17/sinkhorn-algorithm](https://github.com/Khey17/sinkhorn-algorithm).
