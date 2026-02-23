'''
MULTIVARIABLE CALCULUS
-   Multivariable functions: have more than one variable (e.g. f(x,y) = 5x^2y,
    f(x,y,z) = 4xy^2 - 3yz^3 + 2x^2y^3z)
-   Partial derivatives: derivatives of functions of multiple input variables;
    to find out, calculate the derivative of the function with respect to
    each variable
'''

import sympy as sp
import matplotlib.pyplot as plt

x,y,z,f = sp.symbols('x y z f ',real=True)

class PartialDerivatives:
    def __init__(self):
        pass
    
    def diff_wrt_var(f,var): # var can be x, y, or z
        return sp.diff(f,var)
    
PD = PartialDerivatives()

f1 = 5*x**2*y + 4*x*y
print("Given f(x,y) =", f1)
df1_dx = PD.diff_wrt_var(f1,x)
print("df/dx =", df1_dx)
df1_dy = PD.diff_wrt_var(f1,y)
print("df/dy =", df1_dy)