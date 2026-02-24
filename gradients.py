from abc import ABC,abstractmethod # for inheritance
import sympy as sp
from math import sqrt # to obtain the maximum directional derivative

x,y,z,f = sp.symbols('x y z f',real=True)

class Gradients(ABC):
    def __init__(self):
        super().__init__()
        
    def diff_wrt_var(self,f,var): # var can be x, y, or z
        return sp.diff(f,var)

    @abstractmethod
    def evaluate(self,df,P_x,P_y): # (P_x,P_y) is our point of interest
        pass

class RegressionGradient(Gradients):
    def nabla(self,f,x,y,P_x,P_y): # the gradient of a two-variable function
        # nabla_x = sp.diff(f,x)
        df_dx = self.diff_wrt_var(f,x)
        df_dy = self.diff_wrt_var(f,y)
        nabla_x = self.evaluate(df_dx,P_x,P_y)
        nabla_y = self.evaluate(df_dy,P_x,P_y)
        return f"({nabla_x},{nabla_y})"

    def DD(self,nabla_x,nabla_y): # i.e. maximum directional derivative
        return sqrt(nabla_x**2+nabla_y**2)

    def evaluate(self,df,P_x,P_y): # (P_x,P_y) is our point of interest
        return df.subs({x:P_x, y:P_y})

g = RegressionGradient()

f = x**2 + 4*x*y + 2*y**2
P_x,P_y = 2,1
nabla_f = g.nabla(f,x,y,P_x,P_y)
print(f"If f(x,y) = {f}, the gradient at ({P_x},{P_y}) is {nabla_f}.")