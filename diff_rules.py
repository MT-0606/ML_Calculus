import sympy as sp
import matplotlib.pyplot as plt

x,f,g = sp.symbols('x f g',real=True)

class DifferentiationRules:
    def __init__(self):
        pass

    def power_rule(self, n): # f(x)=x^n => f'(x)=n*x^(n-1)
        return n*x**(n-1)
    
    def constant_rule(self, c): # f(x)=c => f'(x)=0
        return 0
    
    def constant_multiple_rule(self, c, f): # f(x)=c*g(x) => f'(x)=c*g'(x)
        return c*sp.diff(f,x)
    
    def sum_rule(self, f, g): # f(x)=g(x)+h(x) => f'(x)=g'(x)+h'(x)
        return sp.diff(f,x) + sp.diff(g,x)
    
    def difference_rule(self, f, g): # f(x)=g(x)-h(x) => f'(x)=g'(x)-h'(x)
        return sp.diff(f,x) - sp.diff(g,x)
    
    def product_rule(self, f, g): # f(x)=g(x)*h(x) => f'(x)=g'(x)*h(x)+g(x)*h'(x)
        return sp.diff(f,x)*g + f*sp.diff(g,x)
    
    def quotient_rule(self, f, g): # f(x)=g(x)/h(x) => f'(x)=(g'(x)*h(x)-g(x)*h'(x))/(h(x))**2
        return (sp.diff(f,x)*g - f*sp.diff(g,x))/(g**2)
    
dF = DifferentiationRules()

'''
EXAMPLE #1: Find the derivative of f(x) = 5.
'''
f1 = 5
df1 = dF.constant_rule(f1)
print(f"If f(x)={f1}, f'(x)={df1}.")

p_f1 = sp.plot(f1, (x,0,5), show=False)
p_df1 = sp.plot(df1, (x,0,5), show=False)
p_f1.extend(p_df1) # combine the two plots into one
p_f1.title = "f(x) and f'(x) for f(x)=5"
p_f1.legend = True
p_f1[0].line_color='r' # f(x) in red
p_f1[1].line_color='b' # f'(x) in blue
p_f1[0].label='f(x)'
p_f1[1].label="f'(x)"
p_f1.show()

'''
EXAMPLE #2: Find the derivative of f(x) = x^4.
'''
f2 = x**4
df2 = dF.power_rule(f2)
print(f"If f(x)={f2}, f'(x)={df2}.")

'''
EXAMPLE #2: Find the derivative of f(x) = x^7.
'''
f3 = x**7
df3 = dF.power_rule(f3)
print(f"If f(x)={f3}, f'(x)={df3}.")