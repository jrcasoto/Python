# Problem 03
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*x*x + b*x + c

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    return evalQuadratic(a1,b1,c1,x1) + evalQuadratic(a2,b2,c2,x2)

# Test case
a1 = -3.51
b1 = -3.44
c1 = 2.57
x1 = -9.77
a2 = 5.6
b2 = -4.9
c2 = -1.66
x2 = 5.92

print(evalQuadratic(a, b, c, x))
print(twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2))