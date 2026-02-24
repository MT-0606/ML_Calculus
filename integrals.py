'''
WHAT IS INTEGRATION?
- Simply put, the inverse of differentiation.
- Hence, an integral is also known as an antiderivative.
- The area of a curve.
'''

from abc import ABC,abstractmethod # for inheritance
import sympy as sp
x,f,g = sp.symbols('x f g',real=True)

class Integrals(ABC):
    def __init__(self,a,b): # a is the upper limit and b the lower limit
        self.a = a
        self.b = b
        
class Properties(Integrals):
    def __init__(self,a,b): # a is the upper limit and b the lower limit
        super().__init__(a,b)
    
    def constant_rule(self,c):
        return c*(self.b-self.a) # i.e. constant times interval length
    def constant_function_rule(self,c,f):
        return c*sp.integrate(f,self.a,self.b)
    def sum_or_diff_rules(self,f,g,op):
        if op=='+':
            return sp.integrate(f,self.a,self.b) + sp.integrate(g,self.a,self.b)
        elif op=='-':
            return sp.integrate(f,self.a,self.b) - sp.integrate(g,self.a,self.b)

'''
BASIC PROPERTIES IN ACTION
'''
# EXAMPLE 1: The integral of 4 + 3x^2 over the interval [0,1].
f,g = 4,3*x**2
lower_limit,upper_limit = 0,1
P = Properties(lower_limit,upper_limit)
f_plus_g = P.sum_or_diff_rules(f,g,'+')
print(f"If f(x) = {f}, the integral over [{lower_limit}, {upper_limit}] is {f_plus_g}.")