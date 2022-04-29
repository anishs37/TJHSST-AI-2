import sys
import numpy as np

eq_check = sys.argv[1]

L = 0.1

#[C, x, y]
#[C, x, y, xy, x^2, y^2, x^3, y^3]
part_a_x = [24, 8, -3]
part_a_y = [-20, -3, 4]
part_b_x = [0, 2, 0, 0, 0, -2, 0, 0]
part_b_y = [-2, 0, 2, -4, 0, 0, 0, 4]

curr_x, curr_y = 0, 0
grad_error = 9999999
print("Starting Location: (%s, %s)" %(curr_x, curr_y))

while(grad_error >= 0.000000001):
    if(eq_check == "A"):
        term_x, term_y = part_a_x[0] + part_a_x[1]*curr_x + part_a_x[2]*curr_y, part_a_y[0] + part_a_y[1]*curr_x + part_a_y[2]*curr_y
    
    else:
        term_x = part_b_x[0] + part_b_x[1]*curr_x + part_b_x[2]*curr_y + part_b_x[3]*curr_x*curr_y + part_b_x[4]*(curr_x**2) + part_b_x[5]*(curr_y**2) + part_b_x[6]*(curr_x**3) + part_b_x[7]*(curr_y**3)
        term_y = part_b_y[0] + part_b_y[1]*curr_x + part_b_y[2]*curr_y + part_b_y[3]*curr_x*curr_y + part_b_y[4]*(curr_x**2) + part_b_y[5]*(curr_y**2) + part_b_y[6]*(curr_x**3) + part_b_y[7]*(curr_y**3)

    np_grad_vec = np.array([term_x, term_y])
    mag = np.linalg.norm(np_grad_vec)
    curr_x -= (L * term_x)
    curr_y -= (L * term_y)
    print("Current Location: (%s, %s)" %(curr_x, curr_y) + "\t\t" + "Current Gradient Vector: " + str(np_grad_vec))
    grad_error = mag