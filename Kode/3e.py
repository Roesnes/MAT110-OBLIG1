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