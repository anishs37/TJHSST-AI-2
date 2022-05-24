import sys
import ast
import math
import numpy as np
import random

def step(num):
    if(num > 0):
        return 1
    
    else:
        return 0

def sigmoid(num):
    return 1/(1 + math.e**(-1 * num))

def p_net(A, x, list_w, list_b):
    new_a = np.vectorize(A)
    last_a = x

    for ct, w_lay in enumerate(list_w):
        if(ct != 0):
            b_lay = list_b[ct]
            last_a = new_a(last_a@w_lay + b_lay)
    
    return last_a

chal_to_comp = 0

if(len(sys.argv[1:]) == 1):
    chal_to_comp = 1
elif(len(sys.argv[1:]) == 2):
    chal_to_comp = 2
else:
    chal_to_comp = 3

# Challenge #1

#XOR HAPPENS HERE
if(chal_to_comp == 1):
    tup = ast.literal_eval(sys.argv[1])
    w0 = np.array([[None]])
    w1 = np.array([[-2, 2], [2, -2]])
    b1 = np.array([[-1, -1]])
    w2 = np.array([[2], [2]])
    b2 = np.array([[0]])

    list_ws = [w0, w1, w2]
    list_bs = [w0, b1, b2]

    x = np.array([[tup[0], tup[1]]])
    val_ret = p_net(step, x, list_ws, list_bs)
    print(val_ret[0][0])

# Challenge #2

if(chal_to_comp == 2):
    w0 = np.array([[None]])
    w1 = np.array([[1, 1, -1, -1], [1, -1, 1, -1]])
    w2 = np.array([[1], [1], [1], [1]])
    b0 = np.array([[None]])
    b1 = np.array([[1, 1, 1, 1]])
    b2 = np.array([[-3]])

    list_ws = [w0, w1, w2]
    list_bs = [w0, b1, b2]

    x = np.array([[float(sys.argv[1]), float(sys.argv[2])]])     ## point coordinates
    val_ret = p_net(step, x, list_ws, list_bs)

    if(val_ret[0][0] < 0.5):
        print("outside")
    else:
        print("inside")

"""
w13 - 1
w14 - 1
w15 - -1
w16 - -1
w23 - 1
w24 - -1
w25 - 1
w26 - -1
w37 - 1
w47 - 1
w57 - 1
w67 - 1
b3 - 1
b4 - 1
b5 - 1
b6 - 1
b7 - -3
"""

# Challenge #3

# w0 = np.array([[None]])
# w1 = np.array([[1, 1, -1, -1], [1, -1, 1, -1]])
# w2 = np.array([[1], [1], [1], [1]])
# b2 = np.array([[-3]])

# list_ws3 = [w0, w1, w2]
# pt_b1_low, pt_b2_low, lowestMiss_b1, lowestMiss_all = 0, 0, 500, 500

# for b1_pt in np.arange(-5, 5, 0.1):
#     b1 = np.array([[b1_pt, b1_pt, b1_pt, b1_pt]])
#     list_bs3 = [w0, b1, b2]
#     numMiss = 0
#     for pt_gen in range(500):
#         pt_1, pt_2 = random.uniform(-1, 1), random.uniform(-1, 1)
#         x_np = np.array([[pt_1, pt_2]])
#         y_val = 0
#         if(pt_1**2 + pt_2**2 < 1):
#             y_val = 1
#         val_ret = p_net(sigmoid, x_np, list_ws3, list_bs3)
#         if(y_val == 1):
#             if(val_ret[0][0] < 0.5):
#                 numMiss += 1
#         else:
#             if(val_ret[0][0] > 0.5):
#                 numMiss += 1
#     if(numMiss < lowestMiss_b1):
#         pt_b1_low = b1_pt
#         lowestMiss_b1 = numMiss

# print(str(lowestMiss_b1 / 500))
# b1 = np.array([[pt_b1_low, pt_b1_low, pt_b1_low, pt_b1_low]])
# for b2_pt in np.arange(-5, 5, 0.1):
#     b2_upd = np.array([[b2_pt]])
#     list_bs3 = [w0, b1, b2_upd]
#     numMiss = 0
#     for pt_gen in range(500):
#         pt_1, pt_2 = random.uniform(-1, 1), random.uniform(-1, 1)
#         x_np = np.array([[pt_1, pt_2]])
#         y_val = 0
#         if(pt_1**2 + pt_2**2 < 1):
#             y_val = 1
#         val_ret = p_net(sigmoid, x_np, list_ws3, list_bs3)
#         if(y_val == 1):
#             if(val_ret[0][0] < 0.5):
#                 numMiss += 1
#         else:
#             if(val_ret[0][0] > 0.5):
#                 numMiss += 1
#     if(numMiss < lowestMiss_all):
#         pt_b2_low = b2_pt
#         lowestMiss_all = numMiss

# print(str(lowestMiss_all / 500))

# pt_b1_low2, pt_b2_low2, lowestMiss_b12, lowestMiss_all2 = 0, 0, 500, 500
# b2_upd2 = np.array([[pt_b2_low]])

# for b1_pt in np.arange(pt_b1_low - 0.05, pt_b1_low + 0.06, 0.01):
#     b1 = np.array([[b1_pt, b1_pt, b1_pt, b1_pt]])
#     list_bs3 = [w0, b1, b2_upd2]
#     numMiss = 0
#     for pt_gen in range(500):
#         pt_1, pt_2 = random.uniform(-1, 1), random.uniform(-1, 1)
#         x_np = np.array([[pt_1, pt_2]])
#         y_val = 0
#         if(pt_1**2 + pt_2**2 < 1):
#             y_val = 1
#         val_ret = p_net(sigmoid, x_np, list_ws3, list_bs3)
#         if(y_val == 1):
#             if(val_ret[0][0] < 0.5):
#                 numMiss += 1
#         else:
#             if(val_ret[0][0] > 0.5):
#                 numMiss += 1
#     if(numMiss < lowestMiss_b12):
#         pt_b1_low2 = b1_pt
#         lowestMiss_b12 = numMiss

# b1 = np.array([[pt_b1_low2, pt_b1_low2, pt_b1_low2, pt_b1_low2]])
# list_bsfinal = [w0, b1, b2]

if(chal_to_comp == 3):
    numFinalMiss = 0
    w0 = np.array([[None]])
    w1 = np.array([[1, 1, -1, -1], [1, -1, 1, -1]])
    w2 = np.array([[1], [1], [1], [1]])
    b1 = np.array([[1.35, 1.35, 1.35, 1.35]])
    b2 = np.array([[-3]])

    list_ws3 = [w0, w1, w2]
    list_bs3 = [w0, b1, b2]
    for i in range(500):
        pt_1, pt_2 = random.uniform(-1, 1), random.uniform(-1, 1)
        y_val = 0
        if(pt_1**2 + pt_2**2 < 1):
            y_val = 1
        np_arr = np.array([[pt_1, pt_2]])
        val_ret = p_net(sigmoid, np_arr, list_ws3, list_bs3)
        if(y_val == 1):
            if(val_ret[0][0] < 0.5):
                print(np_arr)
                numFinalMiss += 1
        else:
            if(val_ret[0][0] > 0.5):
                print(np_arr)
                numFinalMiss += 1

    print(str((1 - (numFinalMiss / 500)) * 100) + " percent classified correctly")