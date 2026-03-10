$$
Z_1 = e^{i\frac{\pi}{4}}
$$
$$
Z_2 = -1 - i
$$

a)  
![[Pasted image 20260224203354.png]]

---------------------

b)  
Bruker Euler-formelen $e^{i\theta} = \cos\theta + i\sin\theta$.

$Z_1$ på standardform:
$$
Z_1 = e^{i\frac{\pi}{4}}
      = \cos\frac{\pi}{4} + i\sin\frac{\pi}{4},
      \qquad
      \cos\frac{\pi}{4} = \sin\frac{\pi}{4} = \frac{\sqrt{2}}{2}
$$
$$
Z_1 = \frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}
$$

$Z_2$ på eksponentialform:  
$Z_2 = -1 - i$ har

- modulus $r = \sqrt{(-1)^2 + (-1)^2} = \sqrt{2}$  
- argument $\theta$: punktet $(-1,-1)$ ligger i tredje kvadrant, og vinkelen er $\theta = -\frac{3\pi}{4}$

Dermed
$$
Z_2 = \sqrt{2}\,e^{i\left(-\frac{3\pi}{4}\right)}
$$

------------------

c) $Z_1 + Z_2$:

Vi har
$$
Z_1 = \frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2},
\qquad
Z_2 = -1 - i.
$$

Da er
$$
Z_1 + Z_2
= \left(\frac{\sqrt{2}}{2} - 1\right)
  + i\left(\frac{\sqrt{2}}{2} - 1\right).
$$

Altså
$$
Z_1 + Z_2 = \left(\frac{\sqrt{2}}{2} - 1\right)(1 + i).
$$

-----------------------------

$\dfrac{Z_1}{Z_2}$:

Vi har fra før at
$$
Z_1 = e^{i\frac{\pi}{4}}, \qquad
Z_2 = \sqrt{2}\,e^{i\frac{5\pi}{4}}.
$$

Vi dividerer komplekse tall på eksponentialform slik:
$$
\frac{r_1 e^{i\alpha}}{r_2 e^{i\beta}}
= \frac{r_1}{r_2} e^{i(\alpha - \beta)}.
$$

Vi bruker dette på $\dfrac{Z_1}{Z_2}$:
$$
\frac{Z_1}{Z_2}
= \frac{e^{i\frac{\pi}{4}}}{\sqrt{2}\,e^{i\frac{5\pi}{4}}}
= \frac{1}{\sqrt{2}} e^{i\left(\frac{\pi}{4} - \frac{5\pi}{4}\right)}
= \frac{1}{\sqrt{2}} e^{-i\pi}.
$$

Siden $e^{i\pi} = -1$ (og dermed også $e^{-i\pi} = -1$), får vi
$$
\frac{Z_1}{Z_2}
= \frac{1}{\sqrt{2}}(-1)
= -\frac{1}{\sqrt{2}}.
$$

--------------------

$-\overline{Z_1}$:

Vi vet at
$$
Z_1 = e^{i\frac{\pi}{4}} = \frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}.
$$

Den komplekse konjugerte $\overline{Z_1}$ får vi ved å beholde den reelle delen og skifte fortegn på den imaginære delen:
$$
\overline{Z_1} = \frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}.
$$

Dermed
$$
-\overline{Z_1}
= -\left(\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}\right)
= -\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}.
$$

--------------------

For å finne $Z_1 + Z_2$ ved hjelp av figuren fra deloppgave a) kunne jeg ha brukt parallellogrammetoden. Det gjøres ved å konstruere et parallellogram med vektorene som nabosider, og ta diagonalen fra origo. Endepunktet til diagonalen er da $Z_1 + Z_2$. Den geometriske summen er altså vektorsummen av pilene for punktene.

Den komplekse konjugerte $\overline{Z_1}$ er speilbildet av $Z_1$ i den reelle aksen. Vi starter i punktet for $Z_1$, og speiler punktet over den horisontale (reelle) aksen ved å gå loddrett ned/opp. Det nye punktet, med samme reelle del og motsatt imaginær del, er $\overline{Z_1}$. Ligger $Z_1$ i første kvadrant, ligger $\overline{Z_1}$ i fjerde kvadrant, like langt fra origo, men under den reelle aksen.

-----------

d)

$$
Z^6 = 1 + i.
$$

Vi skriver høyresiden på eksponentialform. For $1 + i$:

- Modulus: $|1 + i| = \sqrt{1^2 + 1^2} = \sqrt{2}$
- Argument: $\arg(1 + i) = \frac{\pi}{4}$

Dermed
$$
1 + i = \sqrt{2}\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right)
      = \sqrt{2}e^{i\frac{\pi}{4}}.
$$

Ligningen blir
$$
Z^6 = \sqrt{2}\,e^{i\frac{\pi}{4}}.
$$

Vi bruker formelen for $n$-te røtter: De 6‑te røttene til et komplekst tall $re^{i\theta}$ er
$$
Z_k = r^{1/6} e^{i\frac{\theta + 2\pi k}{6}}, \qquad k = 0,1,2,3,4,5.
$$

Her er $r = \sqrt{2}$ og $\theta = \frac{\pi}{4}$, så
$$
r^{1/6} = (\sqrt{2})^{1/6} = 2^{1/12}.
$$

Altså
$$
Z_k
= 2^{1/12} e^{i\left(\frac{\frac{\pi}{4} + 2\pi k}{6}\right)}
= 2^{1/12} e^{i\left(\frac{\pi}{24} + \frac{\pi k}{3}\right)},
\qquad k = 0,1,2,3,4,5.
$$
Vi beregner de 6 røttene: 
$$
k=0:Z_0=2^{\frac{1}{12}}e^{i\frac{\pi}{24}}
$$
$$
k=1:Z_1=2^{\frac{1}{12}}e^{i(\frac{\pi}{24}+\frac{\pi}{3})}=\sqrt[12]{2}e^{i\frac{9\pi}{24}}
$$
$$
k=2:Z_2=2^{\frac{1}{12}}e^{i(\frac{\pi}{24}+\frac{2\pi}{3})}=\sqrt[12]{2}e^{i\frac{17\pi}{24}}
$$
$$
k=3:Z_3=2^{\frac{1}{12}}e^{i(\frac{\pi}{24}+\pi)}=\sqrt[12]{2}e^{i\frac{25\pi}{24}}
$$
$$
k=4:Z_4=2^{\frac{1}{12}}e^{i(\frac{\pi}{24}+\frac{4\pi}{3})}=\sqrt[12]{2}e^{i\frac{33\pi}{24}}
$$
$$
k=5:Z_5=2^{\frac{1}{12}}e^{i(\frac{\pi}{24}+\frac{5\pi}{3})}=\sqrt[12]{2}e^{i\frac{41\pi}{24}}
$$





























