# 01. Entropy & Sinkhorn

*Transcribed from my handwritten notes (`notes/Entropy_in_Optimal_Transport.pdf` + the Sinkhorn pages in `Optimal_Transport.pdf`).*

## Exact OT

$$
L_C(a,b)=\min_{P\in U(a,b)}\langle C,P\rangle=\min_{P\in U(a,b)}\sum_{ij}C_{ij}P_{ij}.
$$

Find the cheapest way to ship supply $a$ (source $\sim\mu$) to demand $b$ (target $\sim\nu$), given cost table $C$ and plan $P$.

$U(a,b)$ = feasible set of non-negative matrices (every legal way to move mass).

## Exact OT is sharp — and combinatorial

Fundamental fact of LP: the cheapest plan is sharp & sparse — optimum of a linear objective over a polytope sits at a **corner**.

**The problem:** Exact OT is accurate but slow (combinatorial search). Idea: *blur* $P$ so the solution is smooth instead of a hard corner.

## Entropy = a spread score

$$
H(P)=-\sum_{ij}P_{ij}(\log P_{ij}-1).
$$

$H$ is a scalar measuring blurriness.

- Low $H$ ≈ sharp (few routes)  
- High $H$ ≈ spread

## Entropic OT: add $-\varepsilon H$

$$
L_C^{\varepsilon}(a,b)=\min_{P\in U(a,b)}\langle C,P\rangle-\varepsilon H(P).
$$

- $\varepsilon$ — knob that controls blur  

At $\varepsilon=0$ the optimum is pinned to a corner. $-\varepsilon H$ turns the flat triangle into a **smooth bowl**; the interior point slides inward as $\varepsilon\uparrow$.

Why unique? $H$ is concave ($\partial^2 H/\partial P_{ij}^2=-1/P_{ij}<0$) ⇒ $-\varepsilon H$ strictly convex ⇒ exactly one best plan $P^{\varepsilon}$.

## The trade-off

$$
\langle C,P^{\varepsilon}\rangle\;\ge\;\langle C,P^{\star}\rangle=L_C(a,b).
$$

| Exact OT ($\varepsilon\to 0$) | Entropic OT ($\varepsilon>0$) |
|---|---|
| Sharp / sparse | Blurry / spread |
| ~$O(n^3)$ LP | Sinkhorn iterations |
| Hard for NNs (non-diff) | Smooth, unique, usable as a loss |

## Sinkhorn's algorithm

Lagrangian with duals $f$ (rows / $P\mathbf{1}=a$) and $g$ (cols / $P^\top\mathbf{1}=b$). Stationarity ⇒

$$
P_{ij}=e^{(f_i+g_j-C_{ij})/\varepsilon}.
$$

With $K=e^{-C/\varepsilon}$, $u=e^{f/\varepsilon}$, $v=e^{g/\varepsilon}$:

$$
P=\operatorname{diag}(u)\,K\,\operatorname{diag}(v),\qquad
u\odot(Kv)=a,\quad v\odot(K^\top u)=b.
$$

```text
K = exp(-C / ε)
v = ones
repeat:
    u ← a / (K v)      # fix rows
    v ← b / (Kᵀ u)     # fix cols
return P = diag(u) K diag(v)
```

**Why it works.** $K>0$ entrywise ⇒ a $(u,v)$ pair exists that fixes both margins (**Sinkhorn's theorem**). Updates alternate and **stop as they converge (like oscillation)**.

Mass on route $i\to j$: $P_{ij}=u_i K_{ij} v_j$.

Next: run the same story in code — [02. Sinkhorn notebook](02_sinkhorn_demo.ipynb).
