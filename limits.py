'''
WHY ARE LIMITS IMPORTANT?
-   Derivatives and integrals are defined in terms of limits.
-   They help us determine the value of a function (limit of f at P = value of f at P) even at points where
    it is not defined.
'''

'''
THE DEFINITION OF A LIMIT
-   Let f be a function.
-   The notation lim(x->P f(x)) = L means f can be made arbitrarily close to a limit L by making x sufficiently
    close to, but not equal to, P.
'''


'''
EXAMPLE #1: Find lim(x->3) f(x) where f(x) = x+2.
'''
import sympy as sp
import matplotlib.pyplot as plt

# STEP 1: Define a function.
x = sp.symbols('x')
y = x+2

# STEP 2: Determine whether the function is defined at the point of interest.
P = 3
print(f"f({P}) = {y.subs(x,P)}") # f(3) is defined and equals 5

# STEP 3: Take all values of x that are close to P and see what happens to f(x).
x_values = [2.9, 2.99, 2.999, 2.9999, 3.0001, 3.001, 3.01, 3.1]
y_values = []
for inputs in x_values:
    outputs = y.subs(x,inputs)
    y_values.append(outputs)
y_values = [round(value,4) for value in y_values]
print(f"Values of f(x) as x approaches {P}: {y_values}")

# STEP 4: Graph the function and visually inspect the behaviour of f(x) as x approaches P.
limit_values = zip(x_values, y_values)
plt.plot(x_values, y_values, 'r') # 'r' means red
plt.axvline(x=P, color='b') # vertical line at x = P
plt.axhline(y=y.subs(x,P), color='g') # horizontal line at y = f(P)
for inputs,outputs in limit_values:
    plt.axvline(x=inputs, color='b', linestyle='--')  # vertical lines at each x value
    plt.axhline(y=outputs, color='g', linestyle='--') # horizontal lines at each y value
plt.title(f"Graph of f(x) = {y} as x approaches {P}")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
