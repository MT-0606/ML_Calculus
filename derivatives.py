import sympy as sp
import matplotlib.pyplot as plt

x,y = sp.symbols('x y',real=True)

def fprime(f,x,h=1e-6): # produces the slope of the tangent line to the curve of f at a given point x
    return (f(x+h) - f(x))/h

'''
EXAMPLE #1: Find the derivative of f(x) = x^2 + 1 at x = 2.
'''

# STEP 1: Define the function.
y = x**2 + 1

# STEP 2: Plug in the function and the point of interest into the formula for the derivative.
P = 2
dy = fprime(y.subs(x,P),x)
print(f"The derivative of f(x) at x={P} is {dy}.")