import numpy as np

A = np.array([
    [50, 25, 75, 100],
    [75, 100, 50, 25],
    [75, 75, 75, 50],
    [50, 50, 50, 75]
], dtype=float)

detA = np.linalg.det(A)
print("det(A) =", detA)
