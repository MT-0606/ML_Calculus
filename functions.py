'''
GLOSSARY
-   SINGLE-VARIABLE CALCULUS: Based on functions that accept a single input and return a single output
-   FUNCTION: A relation from a set of inputs (x1, x2, ..., xn) to a set of possible outputs
    (y1, y2, ..., yn)) in which each input is related to exactly one output (x1->y1, x2->y2, ..., xn->yn)
-   NON-LINEAR FUNCTION: A function that does not have a constant gradient (e.g. f(x) = x^2); instead,
    it can be represented with curves, parabolas, etc.
'''

def f(x): # a linear function of the form 'f(x) = mx + c'
    m = 2 # gradient (shows how steep the line is)
    c = 1 # y-intercept (shows where the line is relative to the origin)
    return m*x + c

# STEP 1: Choose input values for x.
x = [0,1]

# STEP 2: Plug in inputs and calculate outputs.
y = []
for inputs in x:
    outputs = f(inputs)
    y.append(outputs)
    
# STEP 3: Plot the points (x, f(x)).
import matplotlib.pyplot as plt
plt.plot(x, y, 'r') # 'r' means red
plt.show()