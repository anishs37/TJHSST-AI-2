import sys
import math
import numpy as np

eq_check = sys.argv[1]

def a(x, y):
    f1 = (4*x**2)-(3*x*y)+(2*y**2)+(24*x)-(20*y)
    return f1

def b(x, y):
    f2 = ((1-y)**2) + ((x-(y**2))**2)
    return f2

def one_d_minimize(f, left, right, tolerance):
    if((right-left) < tolerance):
        return (left + right) / 2

    to_add = (right - left) / 3
    pt_1 = left + to_add
    pt_2 = pt_1 + to_add
    
    a = pt_1
    ev_pt1 = eval(f)
    a = pt_2
    ev_pt2 = eval(f)

    if(ev_pt1 > ev_pt2):
        val = one_d_minimize(f, pt_1, right, tolerance)
        if val is not None:
            return val
    
    else:
        val = one_d_minimize(f, left, pt_2, tolerance)
        if val is not None:
            return val

def sin(num):
    return math.sin(num)

eq = 'sin(a) + sin(3*a) + sin(4*a)'
print(one_d_minimize(eq, -1, 0, 0.00000001))