# 00. Recap — Monge & Kantorovich

*Transcribed from my handwritten notes (`notes/Optimal_Transport.pdf`). Foundational only.*

## Monge problem

Find a map $T: X \to Y$ that moves mass $\mu$ to a target $\nu$ as cheaply as possible.

- $\mu,\nu$ — probability measures  
- $X$ — source space · $Y$ — target space

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

- $c$ — cost function  
- $\gamma$ — transport plan (discrete OT: a matrix $P$)

Valid plans:

$$
\Pi(\mu,\nu)=\bigl\{\gamma\in\mathcal{P}(X\times Y):\;(\pi_x)_{\#}\gamma=\mu,\;(\pi_y)_{\#}\gamma=\nu\bigr\}.
$$

## Monge vs Kantorovich (tiny example)

Sources $m_1=10$, $m_2=15$ and targets $m_A=5$, $m_B=20$ (total mass $25$). One valid plan:

$$
\gamma=\begin{bmatrix}5&5\\0&15\end{bmatrix}.
$$

Mass *can* split (source 1 sends $5$ to A and $5$ to B) — Kantorovich flexibility that Monge does not allow.

## Duality (pickup / dropoff fees)

Idea from the notes: $\min(\mathrm{KP})=\max(\mathrm{DP})$.

$$
\max\Bigl(\int\phi\,d\mu+\int\psi\,d\nu\Bigr)=\min\int c\,d\gamma,
$$

restricted by $\phi+\psi\le c$.

In words: the cost of two 1D arrays $(\phi,\psi)$ combined cannot exceed the cost of the actual route (2D matrix).

Computationally $\phi,\psi$ are arrays of prices (dual potentials) on source and target bins.

## When a Monge map exists

If $c(x,y)=h(x-y)$ with $h$ strictly convex (e.g. $|x-y|^2$), and $\phi+\psi=c$ at optimum, differentiating in $x$ gives

$$
\nabla\phi(x)=\nabla h(x-y)\quad\Rightarrow\quad y=x-(\nabla h)^{-1}(\nabla\phi(x))=:T(x).
$$

Under those conditions the optimal plan is induced by a deterministic map $T$.

!!! tip "Discrete language"
    Chapter 3 of the computational book, rewritten discretely: measures → vectors, plan $\gamma$ → matrix $P$.

## Discrete OT as a linear program

Cheapest way to shift histogram $a$ to histogram $b$:

$$
L_C(a,b)=\min_{P\in U(a,b)}\sum_{ij}C_{ij}P_{ij}=\min_{P\in U(a,b)}\langle C,P\rangle.
$$

$U(a,b)$ = non-negative matrices with **rows summing to $a$**, **columns summing to $b$**.

A linear objective over linear constraints ⇒ a linear program. Flatten $P\to p$ and write margins as $Ap=\begin{bmatrix}a\\b\end{bmatrix}$.

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
