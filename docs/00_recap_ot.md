# 00. Recap: Monge & Kantorovich

*Transcribed from my handwritten notes (`notes/Optimal_Transport.pdf`). Foundational only.*

## Monge problem

Find a map $T: X \to Y$ that moves mass $\mu$ to a target $\nu$ as cheaply as possible. Here $\mu$ and $\nu$ are probability measures on the source space $X$ and target space $Y$.

$$
\min_T\left\{\int_X c\!\left(x,T(x)\right)\,d\mu(x):\; T_{\#}\mu=\nu\right\}
$$

Push-forward (conserving mass):

$$
(T_{\#}\mu)(A) := \mu\!\left(T^{-1}(A)\right)=\nu(A).
$$

Monge cannot *split* mass: each source point goes to one target.

## Kantorovich problem

Relax to a coupling $\gamma$ (a joint plan) on $X\times Y$:

$$
\min_{\gamma\in\Pi(\mu,\nu)}\int_{X\times Y} c\,d\gamma.
$$

Here $c$ is the cost function and $\gamma$ is the transport plan — in the discrete setting, a matrix $P$.

Valid plans:

$$
\Pi(\mu,\nu)=\bigl\{\gamma\in\mathcal{P}(X\times Y):\;(\pi_x)_{\#}\gamma=\mu,\;(\pi_y)_{\#}\gamma=\nu\bigr\}.
$$

## Monge vs Kantorovich (tiny example)

Sources $m_1=10$, $m_2=15$ and targets $m_A=5$, $m_B=20$ (total mass $25$). One valid plan is

$$
\gamma=\begin{bmatrix}5&5\\0&15\end{bmatrix}.
$$

![Monge vs Kantorovich tiny example: sources m1=10, m2=15 to targets mA=5, mB=20 with plan matrix [[5,5],[0,15]]](assets/monge_vs_kantorovich.svg){ width="100%" }

Mass *can* split — source 1 sends $5$ to A and $5$ to B. That flexibility is Kantorovich; Monge does not allow it.

## Duality (think of it as pickup / dropoff fees for a courier)

Idea from the notes: $\min(\mathrm{KP})=\max(\mathrm{DP})$.

$$
\max\Bigl(\int\phi\,d\mu+\int\psi\,d\nu\Bigr)=\min\int c\,d\gamma,
$$

restricted by $\phi+\psi\le c$.

In words: the cost of two 1D arrays $(\phi,\psi)$ combined cannot exceed the cost of the actual route (2D matrix). Computationally, $\phi$ and $\psi$ are arrays of prices (dual potentials) on source and target bins.

## When a Monge map exists

If $c(x,y)=h(x-y)$ with $h$ strictly convex (e.g. $|x-y|^2$), and $\phi+\psi=c$ at optimum, differentiating in $x$ gives

$$
\nabla\phi(x)=\nabla h(x-y)\quad\Rightarrow\quad y=x-(\nabla h)^{-1}(\nabla\phi(x))=:T(x).
$$

Under those conditions the optimal plan is induced by a deterministic map $T$.

!!! tip "Discrete language"
    In the discrete view from Santambrogio, [*Optimal Transport for Applied Mathematicians*](https://math.univ-lyon1.fr/~santambrogio/OTAM-cvgmt.pdf) (OTAM) — especially the discrete numerical discussion — finitely supported measures become mass vectors, and the coupling $\gamma$ becomes a matrix of shipments between atoms. Same story as continuous OT, just written so we can compute.

## Discrete OT as a linear program

Cheapest way to shift histogram $a$ to histogram $b$:

$$
L_C(a,b)=\min_{P\in U(a,b)}\sum_{ij}C_{ij}P_{ij}=\min_{P\in U(a,b)}\langle C,P\rangle.
$$

$U(a,b)$ is the set of non-negative matrices with **rows summing to $a$** and **columns summing to $b$**.

A linear objective over linear constraints is a linear program. Flatten $P\to p$ and write the margins as $Ap=\begin{bmatrix}a\\b\end{bmatrix}$.

### Dual / $c$-transform

Constraint on every route $(i,j)$: $f_i+g_j\le C_{ij}$.

Given source prices $f$, the tightest feasible target prices are

$$
(f^c)_j=\min_i(C_{ij}-f_i),
$$

so

$$
L_C(a,b)=\max_f\langle f,a\rangle+\langle f^c,b\rangle.
$$

**Complementary slackness.** At optimum, mass only flows where $f_i+g_j=C_{ij}$.

Next: [01. Entropy & Sinkhorn](01_entropy_sinkhorn.md) — blur the plan and solve it with Sinkhorn.
