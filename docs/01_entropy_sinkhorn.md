# 01. Entropy & Sinkhorn

*Transcribed from my handwritten notes (`notes/Entropy_in_Optimal_Transport.pdf` + the Sinkhorn pages in `Optimal_Transport.pdf`).*

## Exact OT

$$
L_C(a,b)=\min_{P\in U(a,b)}\langle C,P\rangle=\min_{P\in U(a,b)}\sum_{ij}C_{ij}P_{ij}.
$$

Find the cheapest way to ship supply $a$ (source $\sim\mu$) to demand $b$ (target $\sim\nu$), given cost table $C$ and plan $P$. The feasible set $U(a,b)$ is all non-negative matrices that move mass legally (row sums $a$, column sums $b$).

## Exact OT is sharp — and combinatorial

A fundamental fact of linear programming: the cheapest plan is sharp and sparse — the optimum of a linear objective over a polytope sits at a **corner**.

Exact OT is accurate but slow (combinatorial search). The idea in the notes: *blur* $P$ so the solution is smooth instead of a hard corner.

## Entropy = a spread score

$$
H(P)=-\sum_{ij}P_{ij}(\log P_{ij}-1).
$$

$H$ is a scalar measuring blurriness. Low $H$ means a sharp plan (few routes); high $H$ means the mass is spread across many routes.

![Low entropy sharp diagonal plan vs high entropy spread plan](assets/entropy_low_vs_high_H.svg){ width="100%" }

Same margins can still admit different plans. With $a=[0.4,0.6]$ and $b=[0.2,0.8]$, the sharper plan $P_1$ has a zero entry; the blurrier $P_2$ uses every route and scores a higher $H$.

![Two feasible plans with same margins and different entropy](assets/entropy_two_plans_example.svg){ width="100%" }

## Entropic OT: add $-\varepsilon H$

$$
L_C^{\varepsilon}(a,b)=\min_{P\in U(a,b)}\langle C,P\rangle-\varepsilon H(P).
$$

Here $\varepsilon$ is the knob that controls blur. At $\varepsilon=0$ the optimum is pinned to a corner. Adding $-\varepsilon H$ turns the flat feasible set into a **smooth bowl**; the interior point slides inward as $\varepsilon$ grows.

![Feasible-set triangle: exact OT at a corner, entropic OT in the interior](assets/entropy_feasible_triangle.svg){ width="72%" }

Why unique? $H$ is concave ($\partial^2 H/\partial P_{ij}^2=-1/P_{ij}<0$), so $-\varepsilon H$ is strictly convex and there is exactly one best plan $P^{\varepsilon}$.

## The trade-off

$$
\langle C,P^{\varepsilon}\rangle\;\ge\;\langle C,P^{\star}\rangle=L_C(a,b).
$$

The blurred plan costs at least as much as the sharp one. What you buy is smoothness and uniqueness.

| Exact OT ($\varepsilon\to 0$) | Entropic OT ($\varepsilon>0$) |
|---|---|
| Sharp / sparse | Blurry / spread |
| ~$O(n^3)$ LP | Sinkhorn iterations |
| Hard for NNs (non-diff) | Smooth, unique, usable as a loss |

![Sharp exact plan vs blurry entropic plan with source and target marginals](assets/entropy_sharp_vs_blurry.svg){ width="100%" }

## Sinkhorn's algorithm

Lagrangian with duals $f$ (rows / $P\mathbf{1}=a$) and $g$ (cols / $P^\top\mathbf{1}=b$). Stationarity gives

$$
P_{ij}=e^{(f_i+g_j-C_{ij})/\varepsilon}.
$$

With $K=e^{-C/\varepsilon}$, $u=e^{f/\varepsilon}$, $v=e^{g/\varepsilon}$:

$$
P=\operatorname{diag}(u)\,K\,\operatorname{diag}(v),\qquad
u\odot(Kv)=a,\quad v\odot(K^\top u)=b.
$$

![Sinkhorn factorization P = diag(u) K diag(v)](assets/sinkhorn_factorization.svg){ width="100%" }

```text
K = exp(-C / ε)
v = ones
repeat:
    u ← a / (K v)      # fix rows
    v ← b / (Kᵀ u)     # fix cols
return P = diag(u) K diag(v)
```

**Why it works.** $K>0$ entrywise, so a $(u,v)$ pair exists that fixes both margins (**Sinkhorn's theorem**). The updates alternate — fix row, fix col, repeat — and stop as they converge.

Mass on route $i\to j$: $P_{ij}=u_i K_{ij} v_j$.

Next: run the same story in code — [02. Sinkhorn notebook](02_sinkhorn_demo.ipynb).
