$$
x_1 + 2k x_3 + k x_4 = 2
$$
$$
x_1 + x_2 + (2k-1)x_3 = 1
$$
$$
-2x_1 - 4k x_3 + k x_4 = 5
$$

a)  
Skriver opp totalmatrisen.

Ligningssystemet
$$
\left\{
\begin{aligned}
x_{1} + 0x_{2} + 2k x_{3} + k x_{4} &= 2 \\
x_{1} + x_{2} + (2k - 1)x_{3} + 0x_{4} &= 1 \\
-2x_{1} + 0x_{2} - 4k x_{3} + k x_{4} &= 5
\end{aligned}
\right.
$$
gir denne totalmatrisen:
$$
\left[
\begin{array}{rrrr|r}
 1 & 0 & 2k   & k & 2 \\
 1 & 1 & 2k-1 & 0 & 1 \\
-2 & 0 & -4k  & k & 5
\end{array}
\right]
$$

Rekkereduksjon til trappeform.

Bruker rad $1$ som pivot i første kolonne:
$$
R_2 \leftarrow R_2 - R_1
$$
$$
R_2 : (1,1,2k-1,0,1) - (1,0,2k,k,2) = (0,1,-1,-k,-1)
$$
$$
R_3 \leftarrow R_3 + 2R_1
$$
$$
R_3 : (-2,0,-4k,k,5) + 2(1,0,2k,k,2) = (0,0,0,3k,9)
$$

Trappeform:
$$
\left[
\begin{array}{rrrr|r}
1 & 0 & 2k &  k  &  2 \\
0 & 1 & -1 & -k  & -1 \\
0 & 0 &  0 & 3k &  9
\end{array}
\right]
$$

--------------

b)  
Vi bruker trappeformen fra deloppgave a):
$$
\left[
\begin{array}{rrrr|r}
1 & 0 & 2k &  k  &  2 \\
0 & 1 & -1 & -k  & -1 \\
0 & 0 &  0 & 3k &  9
\end{array}
\right]
$$

Den siste raden tilsvarer ligningen
$$
0x_1 + 0x_2 + 0x_3 + 3k x_4 = 9 \;\Rightarrow\; 3k x_4 = 9.
$$

Hvis $k \neq 0$: Da er $3k \neq 0$, så
$$
x_4 = \frac{9}{3k} = \frac{3}{k}
$$
er entydig bestemt. De to øverste radene gir da entydige $x_1,x_2$ uttrykt ved $x_3$ (som blir fri variabel), altså minst én fri variabel og dermed uendelig mange løsninger.

Hvis $k = 0$: Da blir siste rad
$$
0 = 9,
$$
som er en motsigelse. Systemet er da inkonsistent og har ingen løsning.

Vi har dermed

1. Nøyaktig én løsning: ingen verdier av $k$.  
   (For unik løsning måtte alle variabler være pivoter, uten fri variabel, men vi har $4$ variabler og maks $3$ pivoter.)
2. Nøyaktig to løsninger: aldri mulig for et lineært system – enten $0,1$ eller uendelig mange.
3. Ingen løsning: $k = 0$.
4. Uendelig mange løsninger: alle $k \neq 0$.

-------------

c)  
Vi bruker trappeformen fra deloppgave a):
$$
\left[
\begin{array}{rrrr|r}
1 & 0 & 2k &  k  &  2 \\
0 & 1 & -1 & -k  & -1 \\
0 & 0 &  0 & 3k &  9
\end{array}
\right]
$$

Vi setter inn $k = 6$:
$$
\left[
\begin{array}{rrrr|r}
1 & 0 & 12 &  6 &  2 \\
0 & 1 & -1 & -6 & -1 \\
0 & 0 &  0 & 18 &  9
\end{array}
\right]
$$

som tilsvarer systemet
$$
\left\{
\begin{aligned}
x_{1} + 12x_{3} + 6x_{4} &= 2 \\
x_{2} - x_{3} - 6x_{4} &= -1 \\
18x_{4} &= 9
\end{aligned}
\right.
$$

Fra tredje ligning:
$$
x_4 = \frac{9}{18} = \frac{1}{2}.
$$

La $x_3 = t$ være fri variabel (ingen pivot i kolonne $3$). Da får vi
$$
x_2 = -1 + x_3 + 6x_4
    = -1 + t + 6 \cdot \frac{1}{2}
    = -1 + t + 3
    = t + 2
$$
$$
x_1 = 2 - 12x_3 - 6x_4
    = 2 - 12t - 6 \cdot \frac{1}{2}
    = 2 - 12t - 3
    = -1 - 12t.
$$

Løsningen når $k = 6$ er dermed
$$
(x_1,x_2,x_3,x_4) = (-1 - 12t,\; 2 + t,\; t,\; \tfrac{1}{2}),
\qquad t \in \mathbf{R}.
$$

















































































	


































 












