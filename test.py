import sympy as sym
import numpy as np
import scipy.integrate as integrate



f = lambda x:x**3 - 1

F= abs(integrate.quad(f, -1, 0)[0]) + integrate.quad(f, 0, 1)[0]
print(F)
print(f)
print(f)