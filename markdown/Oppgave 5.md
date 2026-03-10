a)

Lar variablene være antall poser solgt av hver blanding i perioden:
- $x_1$: antall poser *Floral Fusion*
- $x_2$: antall poser *Burgundy Bonanza*
- $x_3$: antall poser *Morgensol*
- $x_4$: antall poser *Ahh Svart!*

Vi gjør om fra kilo til gram:
$$
4{,}2\,\text{kg} = 4200\,\text{g},\quad
3{,}8\,\text{kg} = 3800\,\text{g},\quad
4{,}4\,\text{kg} = 4400\,\text{g},\quad
3{,}6\,\text{kg} = 3600\,\text{g}.
$$

For hver bønnetype får vi:
- Arabica:
  $$
  50x_1 + 25x_2 + 75x_3 + 100x_4 = 4200
  $$
- Robusta:
  $$
  75x_1 + 100x_2 + 50x_3 + 25x_4 = 3800
  $$
- Liberica:
  $$
  75x_1 + 75x_2 + 75x_3 + 50x_4 = 4400
  $$
- Excelsa:
  $$
  50x_1 + 50x_2 + 50x_3 + 75x_4 = 3600
  $$

Dette er ligningssystemet $A x = b$.

---------

b)

Koeffisientmatrisen $A$ er
$$
A =
\begin{bmatrix}
50 & 25 & 75 & 100 \\
75 & 100 & 50 & 25 \\
75 & 75 & 75 & 50 \\
50 & 50 & 50 & 75
\end{bmatrix}.
$$

Vi setter denne inn i Python:
```python
import numpy as np

A = np.array([
    [50, 25, 75, 100],
    [75, 100, 50, 25],
    [75, 75, 75, 50],
    [50, 50, 50, 75]
], dtype=float)

detA = np.linalg.det(A)
print("det(A) =", detA)

```

Output: 
```TEXT
det(A) = 0.0
```

Determinanten ble beregnet til å være lik null.  
Det betyr at $A$ er singulær: radene/kolonnene er lineært avhengige, og systemet kan ikke ha en entydig løsning; det er enten ingen eller uendelig mange løsninger.

c) 

Vi bruker NumPy til å undersøke rang til $A$ og den utvidede matrisen $[A\mid b]$: 
```Python
import numpy as np

A = np.array([
    [50, 25, 75, 100],
    [75, 100, 50, 25],
    [75, 75, 75, 50],
    [50, 50, 50, 75]
], dtype=float)

b = np.array([4200, 3800, 4400, 3600], dtype=float)

rank_A  = np.linalg.matrix_rank(A)
rank_Ab = np.linalg.matrix_rank(np.c_[A, b])

print("rank(A)  =", rank_A)
print("rank([A|b]) =", rank_Ab)
```

Output: 
```TERMINAL
rank(A)  = 3
rank([A|b]) = 3
```

Siden $\operatorname{rank}(A) = \operatorname{rank}([A\mid b]) = 3$, men $A$ har $4$ ukjente ($x_1,x_2,x_3,x_4$), har systemet **uendelig mange løsninger** (minst én fri variabel). Det betyr at det finnes flere ulike kombinasjoner av antall poser av de fire blandingene som alle gir de samme totale mengdene *Arabica*, *Robusta*, *Liberica* og *Excelsa* – systemet bestemmer ikke en unik salgsfordeling. 