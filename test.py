import numpy as np
from sympy import Matrix

a = np.array([[-1,2,-1],[2,-2,-2],[-3,2,1]])
m = Matrix(a)

T, J = m.jordan_form()

print(f"Jordan form of matrix a: {J}")
print(f"Matrix T: {T}")
print(f"Matrix T^-1: {T.inv()}")


