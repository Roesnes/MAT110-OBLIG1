$$
A =
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & -1 \\
2 & 3 & 3
\end{bmatrix},
\qquad
B =
\begin{bmatrix}
1 & 1 \\
1 & -1 \\
-1 & 2
\end{bmatrix}
$$

a)  
$A$ har dimensjoner $3\times 3$.  
$B$ har dimensjoner $3\times 2$.

------------------

$A + B$:

Addisjon av matriser krever samme dimensjoner, noe som ikke stemmer med de gitte matrisene. Det er ikke mulig å beregne $A + B$.

-----------------

$3A - B^T$:

$3A$ har dimensjon $3\times 3$.  
$B^T$ er $2\times 3$, siden transponering bytter rader og kolonner. Da er $3A$ og $B^T$ ulike dimensjoner, og det er ikke mulig å beregne $3A - B^T$.

--------------

$AB$:

$A$ er $3\times 3$, $B$ er $3\times 2$.  
Indre dimensjon $3 = 3$, så produktet $AB$ er definert og får dimensjon $3\times 2$.

Vi beregner:
$$
AB =
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & -1 \\
2 & 3 & 3
\end{bmatrix}
\begin{bmatrix}
1 & 1 \\
1 & -1 \\
-1 & 2
\end{bmatrix}
=
\begin{bmatrix}
1\cdot1 + 1\cdot1 + 1\cdot(-1) &
1\cdot1 + 1\cdot(-1) + 1\cdot2 \\[4pt]
1\cdot1 + 2\cdot1 + (-1)\cdot(-1) &
1\cdot1 + 2\cdot(-1) + (-1)\cdot2 \\[4pt]
2\cdot1 + 3\cdot1 + 3\cdot(-1) &
2\cdot1 + 3\cdot(-1) + 3\cdot2
\end{bmatrix}
=
\begin{bmatrix}
1 & 2 \\
4 & -3 \\
2 & 5
\end{bmatrix}
$$

-------------

$BA$:

$B$ er $3\times 2$, $A$ er $3\times 3$.  
Her er antall kolonner i $B$ lik $2$, antall rader i $A$ lik $3$, så $2\neq 3$.  
Det er ikke mulig å beregne $BA$.

-------------

$B^T A$:

$B^T$ er $2\times 3$, $A$ er $3\times 3$.  
Indre dimensjon $3 = 3$, så produktet er definert og får dimensjon $2\times 3$.
$$
B^{T} =
\begin{bmatrix}
1 & 1 & -1 \\
1 & -1 & 2
\end{bmatrix}
$$
$$
B^{T}A =
\begin{bmatrix}
1 & 1 & -1 \\
1 & -1 & 2
\end{bmatrix}
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & -1 \\
2 & 3 & 3
\end{bmatrix}
$$
Rad $1=(1,1,-1):$
- Kolonne $1=(1,1,2):$  
$$
1\cdot1+1\cdot1+(-1)\cdot2=1+1-2=0
$$
- Kolonne $2=(1,2,3):$
$$
1\cdot1+1\cdot2+(-1)\cdot3=1+2-3=0
$$
- Kolonne $3=(1,-1,3):$
$$
1\cdot1+1(-1)+(-1)3=1-1-3=-3
$$
Rad $2=(1,-1,2):$
- Kolonne $1=(1,1,2):$
$$
1\cdot1+(-1)1+2\cdot2=1-1+4=4
$$
- Kolonne $2=(1,2,3)$
$$
1\cdot1+(-1)2+2\cdot3=1-2+6=5
$$
- Kolonne $3=(1,-1,3):$
$$
1\cdot1+(-1)(-1)+2\cdot3=1+1+6=8
$$
Vi får da
$$
B^TA=
\begin{bmatrix}
0 & 0 & -3 \\
4 & 5 & 8
\end{bmatrix}
$$

-------------

b)  

Standardformelen sier at for en matrise
$$
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
$$
er
$$
\det A = a(ei - fh) - b(di - fg) + c(dh - eg).
$$

Her har vi
$$
a=1,\quad b=1,\quad c=1
$$
$$
d=1,\quad e=2,\quad f=-1
$$
$$
g=2,\quad h=3,\quad i=3
$$

Vi beregner leddene
$$
1:\; ei - fh = 2\cdot 3 - (-1)\cdot 3 = 6 + 3 = 9
$$
$$
2:\; di - fg = 1\cdot 3 - (-1)\cdot 2 = 3 + 2 = 5
$$
$$
3:\; dh - eg = 1\cdot 3 - 2\cdot 2 = 3 - 4 = -1
$$

Vi setter det inn i formelen:
$$
\det A = 1\cdot 9 - 1\cdot 5 + 1\cdot (-1) = 9 - 5 - 1 = 3
$$

Vi har da
$$
\det A = 3.
$$

-------------

c)  

Vi finner $A^{-1}$ ved å sette opp $[A\mid I]$ og rekkeredusere til $[I\mid A^{-1}]$:
$$
A =
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & -1 \\
2 & 3 & 3
\end{bmatrix},
\qquad
[A \mid I] =
\left[
\begin{array}{ccc|ccc}
1 & 1 & 1 & 1 & 0 & 0 \\
1 & 2 & -1 & 0 & 1 & 0 \\
2 & 3 & 3 & 0 & 0 & 1
\end{array}
\right]
$$

Rekkereduksjon:

1. $R_2 \leftarrow R_2 - R_1,\; R_3 \leftarrow R_3 - 2R_1$:
$$
\left[
\begin{array}{ccc|ccc}
1 & 1 & 1 &  1 & 0 & 0 \\
0 & 1 & -2 & -1 & 1 & 0 \\
0 & 1 & 1 & -2 & 0 & 1
\end{array}
\right]
$$

2. $R_3 \leftarrow R_3 - R_2$:
$$
\left[
\begin{array}{ccc|ccc}
1 & 1 & 1 & 1 & 0 & 0 \\
0 & 1 & -2 & -1 & 1 & 0 \\
0 & 0 & 3 & -1 & -1 & 1
\end{array}
\right]
$$

3. Pivot i $R_3$: $R_3 \leftarrow \tfrac{1}{3}R_3$:
$$
\left[
\begin{array}{ccc|ccc}
1 & 1 & 1 & 1 & 0 & 0 \\
0 & 1 & -2 & -1 & 1 & 0 \\
0 & 0 & 1 & -\tfrac{1}{3} & -\tfrac{1}{3} & \tfrac{1}{3}
\end{array}
\right]
$$

4. Nulle ut over pivot i kolonne 3: $R_1 \leftarrow R_1 - R_3,\; R_2 \leftarrow R_2 + 2R_3$:
$$
R_{1} : [1, 1, 0 \mid \tfrac{4}{3}, \tfrac{1}{3}, -\tfrac{1}{3}],\qquad
R_{2} : [0, 1, 0 \mid -\tfrac{5}{3}, \tfrac{1}{3}, \tfrac{2}{3}]
$$
altså
$$
\left[
\begin{array}{ccc|ccc}
1 & 1 & 0 & \tfrac{4}{3} & \tfrac{1}{3} & -\tfrac{1}{3} \\
0 & 1 & 0 & -\tfrac{5}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\
0 & 0 & 1 & -\tfrac{1}{3} & -\tfrac{1}{3} & \tfrac{1}{3}
\end{array}
\right]
$$

5. Nulle ut over pivot i kolonne 2: $R_1 \leftarrow R_1 - R_2$:
$$
R_1 : [1,0,0 \mid 3,0,-1]
$$

Da får vi
$$
\left[
\begin{array}{ccc|ccc}
1 & 0 & 0 & 3 & 0 & -1 \\
0 & 1 & 0 & -\tfrac{5}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\
0 & 0 & 1 & -\tfrac{1}{3} & -\tfrac{1}{3} & \tfrac{1}{3}
\end{array}
\right]
$$

Venstresiden er nå identitetsmatrisen, og høyresiden er $A^{-1}$:
$$
A^{-1} =
\begin{bmatrix}
3 & 0 & -1 \\
-\tfrac{5}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\
-\tfrac{1}{3} & -\tfrac{1}{3} & \tfrac{1}{3}
\end{bmatrix}.
$$

----------

Systemet
$$
x_1 + x_2 + x_3 = 1
$$
$$
x_1 + 2x_2 - x_3 = 4
$$
$$
2x_1 + 3x_2 + 3x_3 = 2
$$

d)  

Vi skriver systemet som $A\mathbf{x} = \mathbf{b}$ og bruker $\mathbf{x} = A^{-1}\mathbf{b}$.
$$
A =
\begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & -1 \\
2 & 3 & 3
\end{bmatrix},
\qquad
\mathbf{x} =
\begin{bmatrix}
x_{1} \\
x_{2} \\
x_{3}
\end{bmatrix},
\qquad
\mathbf{b} =
\begin{bmatrix}
1 \\
4 \\
2
\end{bmatrix}
$$

Fra deloppgave c) har vi
$$
A^{-1} =
\begin{bmatrix}
3 & 0 & -1 \\
-\tfrac{5}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\
-\tfrac{1}{3} & -\tfrac{1}{3} & \tfrac{1}{3}
\end{bmatrix}
$$

Vi regner ut $\mathbf{x} = A^{-1}\mathbf{b}$:
$$
\mathbf{x} =
\begin{bmatrix}
3 & 0 & -1 \\
-\tfrac{5}{3} & \tfrac{1}{3} & \tfrac{2}{3} \\
-\tfrac{1}{3} & -\tfrac{1}{3} & \tfrac{1}{3}
\end{bmatrix}
\begin{bmatrix}
1 \\
4 \\
2
\end{bmatrix}
$$

Første komponent:
$$
x_1 = 3\cdot 1 + 0\cdot 4 + (-1)\cdot 2 = 3 - 2 = 1
$$

Andre komponent:
$$
x_{2}
= -\tfrac{5}{3}\cdot 1
+ \tfrac{1}{3}\cdot 4
+ \tfrac{2}{3}\cdot 2
= -\tfrac{5}{3}
+ \tfrac{4}{3}
+ \tfrac{4}{3}
= \tfrac{3}{3}
= 1
$$

Tredje komponent:
$$
x_{3}
= -\tfrac{1}{3}\cdot 1
- \tfrac{1}{3}\cdot 4
+ \tfrac{1}{3}\cdot 2
= -\tfrac{1}{3}
- \tfrac{4}{3}
+ \tfrac{2}{3}
= -\tfrac{3}{3}
= -1
$$

Dermed blir løsningen:
$$
(x_1,x_2,x_3) = (1,1,-1).
$$

---------

e)  

```python
import numpy as np

# Definer matrise A og vektor b
A = np.array([
    [1, 1,  1],
    [1, 2, -1],
    [2, 3,  3]
], dtype=float)

b = np.array([1, 4, 2], dtype=float)

# Sjekk determinanten for å se at A er inverterbar
detA = np.linalg.det(A)
print("det(A) =", detA)

if abs(detA) > 1e-9:
    # Løs systemet Ax = b
    x = np.linalg.solve(A, b)
    print("Løsningen x:")
    print(x)
else:
    print("Systemet har ingen unik løsning (determinant ≈ 0)")
```

Output: 
```TEXT
det(A) = 3.0000000000000004
Løsningen x:
[ 1.  1. -1.]
```
