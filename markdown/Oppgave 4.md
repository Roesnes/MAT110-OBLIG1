$$
\vec{u} =
\begin{bmatrix}
\dfrac{1}{\sqrt{2}} \\[4pt]
\dfrac{1}{2} \\[4pt]
\dfrac{1}{2}
\end{bmatrix},
\qquad
\vec{v} =
\begin{bmatrix}
-\dfrac{1}{\sqrt{2}} \\[4pt]
\dfrac{1}{2} \\[4pt]
\dfrac{1}{2}
\end{bmatrix},
\qquad
\vec{w} =
\begin{bmatrix}
-\dfrac{1}{\sqrt{2}} \\[4pt]
0 \\[4pt]
\dfrac{1}{\sqrt{2}}
\end{bmatrix}
$$

a)  

Lengden til en vektor $\vec{a} = (a_1,a_2,a_3)$ er
$$
\|\vec{a}\| = \sqrt{a_1^2 + a_2^2 + a_3^2}.
$$

---

Lengden til $\vec{u}$:
$$
\vec{u} =
\begin{bmatrix}
\dfrac{1}{\sqrt{2}} \\[4pt]
\dfrac{1}{2} \\[4pt]
\dfrac{1}{2}
\end{bmatrix}
$$
$$
\|\vec{u}\|^{2}
= \left(\dfrac{1}{\sqrt{2}}\right)^{2}
  + \left(\dfrac{1}{2}\right)^{2}
  + \left(\dfrac{1}{2}\right)^{2}
= \dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{4}
= 1
$$
$$
\Rightarrow \|\vec{u}\| = 1.
$$

---

Lengden til $\vec{v}$:
$$
\vec{v} =
\begin{bmatrix}
-\dfrac{1}{\sqrt{2}} \\[4pt]
\dfrac{1}{2} \\[4pt]
\dfrac{1}{2}
\end{bmatrix}
$$
$$
\|\vec{v}\|^{2}
= \left(-\dfrac{1}{\sqrt{2}}\right)^{2}
  + \left(\dfrac{1}{2}\right)^{2}
  + \left(\dfrac{1}{2}\right)^{2}
= \dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{4}
= 1
$$
$$
\Rightarrow \|\vec{v}\| = 1.
$$

---

Lengden til $\vec{w}$:
$$
\vec{w} =
\begin{bmatrix}
-\dfrac{1}{\sqrt{2}} \\[4pt]
0 \\[4pt]
\dfrac{1}{\sqrt{2}}
\end{bmatrix}
$$
$$
\|\vec{w}\|^{2}
= \left(-\dfrac{1}{\sqrt{2}}\right)^{2}
  + 0^{2}
  + \left(\dfrac{1}{\sqrt{2}}\right)^{2}
= \dfrac{1}{2} + 0 + \dfrac{1}{2}
= 1
$$
$$
\Rightarrow \|\vec{w}\| = 1.
$$

---

b)  

Vi bruker skalarprodukt-formelen
$$
\cos\theta = \dfrac{\vec{a}\cdot\vec{b}}{\|\vec{a}\|\,\|\vec{b}\|}.
$$
Alle tre vektorene har lengde $1$, så for enhetsvektorer er $\cos\theta = \vec{a}\cdot\vec{b}$.

$$
\vec{u} =
\begin{bmatrix}
\dfrac{1}{\sqrt{2}} \\[4pt]
\dfrac{1}{2} \\[4pt]
\dfrac{1}{2}
\end{bmatrix},
\qquad
\vec{v} =
\begin{bmatrix}
-\dfrac{1}{\sqrt{2}} \\[4pt]
\dfrac{1}{2} \\[4pt]
\dfrac{1}{2}
\end{bmatrix},
\qquad
\vec{w} =
\begin{bmatrix}
-\dfrac{1}{\sqrt{2}} \\[4pt]
0 \\[4pt]
\dfrac{1}{\sqrt{2}}
\end{bmatrix}
$$

**Vinkelen mellom $\vec{u}$ og \(\vec{v}\)**

Skalarprodukt:
$$
\vec{u}\cdot\vec{v}
= \dfrac{1}{\sqrt{2}}\!\left(-\dfrac{1}{\sqrt{2}}\right)
  + \dfrac{1}{2}\cdot\dfrac{1}{2}
  + \dfrac{1}{2}\cdot\dfrac{1}{2}
= -\dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{4}
= 0.
$$

Siden $\|\vec{u}\| = \|\vec{v}\| = 1$, får vi
$$
\cos\theta_{uv} = 0 \;\Rightarrow\; \theta_{uv} = \dfrac{\pi}{2}\;(90^\circ).
$$

---

**Vinkelen mellom $\vec{u}$ og \(\vec{w}\)**

$$
\vec{u}\cdot\vec{w}
= \dfrac{1}{\sqrt{2}}\!\left(-\dfrac{1}{\sqrt{2}}\right)
  + \dfrac{1}{2}\cdot 0
  + \dfrac{1}{2}\cdot\dfrac{1}{\sqrt{2}}
= -\dfrac{1}{2} + 0 + \dfrac{1}{2\sqrt{2}}.
$$
Det gir
$$
\vec{u}\cdot\vec{w}
= -\dfrac{1}{2} + \dfrac{1}{2\sqrt{2}}.
$$
Med $\|\vec{u}\| = \|\vec{w}\| = 1$:
$$
\cos\theta_{uw} = -\dfrac{1}{2} + \dfrac{1}{2\sqrt{2}}.
$$
Altså
$$
\theta_{uw} = \arccos\!\left(-\dfrac{1}{2} + \dfrac{1}{2\sqrt{2}}\right).
$$

---

c)  

$$
\vec{u} =
\begin{bmatrix}
\dfrac{1}{\sqrt{2}} \\[4pt]
\dfrac{1}{2} \\[4pt]
\dfrac{1}{2}
\end{bmatrix},
\qquad
\vec{v} =
\begin{bmatrix}
-\dfrac{1}{\sqrt{2}} \\[4pt]
\dfrac{1}{2} \\[4pt]
\dfrac{1}{2}
\end{bmatrix}
$$

En vektor som står vinkelrett på både $\vec{u}$ og $\vec{v}$ finner vi ved kryssproduktet $\vec{u}\times\vec{v}$. Kryssprodukt-komponentene er gitt ved
$$
\vec{u} \times \vec{v} =
\begin{bmatrix}
u_{2}v_{3} - u_{3}v_{2} \\
u_{3}v_{1} - u_{1}v_{3} \\
u_{1}v_{2} - u_{2}v_{1}
\end{bmatrix}.
$$

Vi setter inn:

- Første komponent
$$
u_{2}v_{3} - u_{3}v_{2}
= \dfrac{1}{2}\cdot\dfrac{1}{2}
  - \dfrac{1}{2}\cdot\dfrac{1}{2}
= \dfrac{1}{4} - \dfrac{1}{4}
= 0
$$

- Andre komponent
$$
u_{3}v_{1} - u_{1}v_{3}
= \dfrac{1}{2}\!\left(-\dfrac{1}{\sqrt{2}}\right)
  - \dfrac{1}{\sqrt{2}}\cdot\dfrac{1}{2}
= -\dfrac{1}{2\sqrt{2}} - \dfrac{1}{2\sqrt{2}}
= -\dfrac{1}{\sqrt{2}}
$$

- Tredje komponent
$$
u_{1}v_{2} - u_{2}v_{1}
= \dfrac{1}{\sqrt{2}}\cdot\dfrac{1}{2}
  - \dfrac{1}{2}\!\left(-\dfrac{1}{\sqrt{2}}\right)
= \dfrac{1}{2\sqrt{2}} + \dfrac{1}{2\sqrt{2}}
= \dfrac{1}{\sqrt{2}}
$$

Dermed
$$
\vec{u} \times \vec{v} =
\begin{bmatrix}
0 \\[4pt]
-\dfrac{1}{\sqrt{2}} \\[4pt]
\dfrac{1}{\sqrt{2}}
\end{bmatrix}.
$$

---

d)  

Vektoren $\vec{a}\times\vec{b}$ står alltid vinkelrett på både $\vec{a}$ og $\vec{b}$ (forutsatt at de ikke er parallelle, eller én av dem er null). Dermed er vinkelen mellom $\vec{a}$ og $\vec{a}\times\vec{b}$ alltid $\dfrac{\pi}{2}$ (90°):
$$
\angle(\vec{a},\vec{a}\times\vec{b}) = \dfrac{\pi}{2}.
$$

---------

e)  

$$
\|\vec{a}\| = 2
$$
$$
\vec{a}\cdot[5\vec{a}+\vec{b}+(\vec{a}\times\vec{b})]
$$

Skalarproduktet er distributivt, og $\vec{a} \perp \vec{b}$ og $\vec{a} \perp (\vec{a} \times \vec{b})$:
$$
\vec{a}\cdot \bigl(5\vec{a} + \vec{b} + (\vec{a} \times \vec{b})\bigr)
= \vec{a}\cdot (5\vec{a}) + \vec{a}\cdot\vec{b} + \vec{a}\cdot(\vec{a}\times\vec{b}).
$$

- $\vec{a}\cdot(5\vec{a}) = 5\,\vec{a}\cdot\vec{a} = 5\|\vec{a}\|^{2} = 5\cdot 2^{2} = 20$.
- $\vec{a}\cdot\vec{b} = 0$ siden de står vinkelrett.
- $\vec{a}\cdot(\vec{a}\times\vec{b}) = 0$ siden kryssproduktet er ortogonalt på $\vec{a}$.

Dermed er
$$
\vec{a}\cdot\bigl[5\vec{a} + \vec{b} + (\vec{a} \times \vec{b})\bigr] = 20.
$$
