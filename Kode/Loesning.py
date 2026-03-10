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
