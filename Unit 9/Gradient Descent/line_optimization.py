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
    ev_pt1 = f(a)
    a = pt_2
    ev_pt2 = f(a)

    if(ev_pt1 > ev_pt2):
        val = one_d_minimize(f, pt_1, right, tolerance)
        if val is not None:
            return val
    
    else:
        val = one_d_minimize(f, left, pt_2, tolerance)
        if val is not None:
            return val

#[C, x, y]
#[C, x, y, xy, x^2, y^2, x^3, y^3]
part_a_x = [24, 8, -3]
part_a_y = [-20, -3, 4]
part_b_x = [0, 2, 0, 0, 0, -2, 0, 0]
part_b_y = [-2, 0, 2, -4, 0, 0, 0, 4]

curr_x, curr_y = 0, 0
grad_error = 9999999
print("Starting Location: (%s, %s)" %(curr_x, curr_y))

def make_funct(x1, x, y1, y, f):
    def funct(l):
        return f(x - (l*x1), y - (l*y1))
    return funct

while(grad_error >= 0.000000001):
    if(eq_check == "A"):
        term_x, term_y = part_a_x[0] + part_a_x[1]*curr_x + part_a_x[2]*curr_y, part_a_y[0] + part_a_y[1]*curr_x + part_a_y[2]*curr_y
        f = a
    
    else:
        term_x = part_b_x[0] + part_b_x[1]*curr_x + part_b_x[2]*curr_y + part_b_x[3]*curr_x*curr_y + part_b_x[4]*(curr_x**2) + part_b_x[5]*(curr_y**2) + part_b_x[6]*(curr_x**3) + part_b_x[7]*(curr_y**3)
        term_y = part_b_y[0] + part_b_y[1]*curr_x + part_b_y[2]*curr_y + part_b_y[3]*curr_x*curr_y + part_b_y[4]*(curr_x**2) + part_b_y[5]*(curr_y**2) + part_b_y[6]*(curr_x**3) + part_b_y[7]*(curr_y**3)
        f = b

    np_grad_vec = np.array([term_x, term_y])
    mag = np.linalg.norm(np_grad_vec)
    to_min = make_funct(np_grad_vec[0], curr_x, np_grad_vec[1], curr_y, f)
    l = one_d_minimize(to_min, 0, 5, 0.00000001)
    curr_x -= (l * term_x)
    curr_y -= (l * term_y)
    print("Current Location: (%s, %s)" %(curr_x, curr_y) + "\t\t" + "Current Gradient Vector: " + str(np_grad_vec))
    grad_error = mag