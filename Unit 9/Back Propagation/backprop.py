import sys
import ast
import numpy as np
import math
import random

inp = sys.argv[1]

# Challenge #1
L = 0.1

def sigmoid(num):
    return 1/(1 + math.e**(-1 * num))

def sig_deriv(num):
    return (math.e**(-1 * num)) / ((1 + math.e**(-1 * num))**2)

def p_net(A, x, list_w, list_b):
    new_a = np.vectorize(A)
    last_a = x

    for ct, w_lay in enumerate(list_w):
        if(ct != 0):
            b_lay = list_b[ct]
            last_a = new_a(last_a@w_lay + b_lay)
    
    return last_a

def test_pts(ep, trainSet, list_w, list_b):
    numMiss = 0
    for val in trainSet:
        x, y = val[0], val[1]
        val_ret = p_net(sigmoid, x, list_w, list_b)
        val_mag = np.linalg.norm(val_ret)
        ret_round = 1
        if(val_mag <= 0.5):
            ret_round = 0

        if(ret_round != int(y[0])):
            numMiss += 1

    print("Epoch " + str(ep) + ": " + str(numMiss) + " misclassified out of 10000 points")

def backprop(numEpochs, A, Aderiv, trainSet, list_w, list_b):
    act, actDeriv = np.vectorize(A), np.vectorize(Aderiv)

    for ep in range(numEpochs):
        for val in trainSet:
            dot = [None]
            xVal, yVal = val[0], val[1]
            a_vals = [xVal]

            for ct, w_lay in enumerate(list_w):
                if(ct != 0):
                    b_lay = list_b[ct]
                    dot.append((a_vals[ct - 1])@w_lay + b_lay)
                    a_vals.append(act(dot[ct]))
            
            n = len(dot) - 1
            delta = [None] * n
            delta.append(actDeriv(dot[n])*(yVal - a_vals[n]))
            for lay in range(n - 1, 0, -1):
                delta[lay] = actDeriv(dot[lay])*(delta[lay + 1]@list_w[lay + 1].transpose())
            for ct, delVal in enumerate(delta):
                if(ct != 0):
                    list_b[ct] = list_b[ct] + L*delVal
                    list_w[ct] = list_w[ct] + L*((a_vals[ct - 1]).transpose())@delVal
        
        if(inp == 'C'):
            test_pts(ep, trainSet, list_w, list_b)
    
    return list_w, list_b

def error_funct(out, y):
    return (1/2) * (np.linalg.norm(y - out)) ** 2

w0 = np.array([[None]])
w1 = np.array([[1, -0.5], [1, 0.5]])
b1 = np.array([[1, -1]])
w2 = np.array([[1, 2], [-1, -2]])
b2 = np.array([[-0.5, 0.5]])

list_ws = [w0, w1, w2]
list_bs = [w0, b1, b2]

x = np.array([[2, 3]])
y = np.array([[.8, 1]])
# print(list_ws)
# print(list_bs)
# val_out = p_net(sigmoid, x, list_ws, list_bs)
# print(error_funct(val_out, y))

# w_back, b_back = backprop(1, sigmoid, sig_deriv, [(x, y)], list_ws, list_bs)
# print(w_back)
# print()
# print(b_back)
# val_out2 = p_net(sigmoid, x, w_back, b_back)
# print(error_funct(val_out2, y))


# Challenge #2

def create_random(l):
    w_list, b_list = [None], [None]
    for i in range(1, len(l)):
        weight = 2*np.random.rand(l[i-1], l[i])-1
        bias = 2*np.random.rand(1, l[i])-1
        w_list.append(weight)
        b_list.append(bias)
    return w_list, b_list

def check_all(one, two, three, four):
    numCorr = 0

    if(one[0][0] < 0.5 and one[0][1] < 0.5): numCorr += 1
    if(two[0][0] < 0.5 and two[0][1] >= 0.5): numCorr += 1
    if(three[0][0] < 0.5 and three[0][1] >= 0.5): numCorr += 1
    if(four[0][0] >= 0.5 and four[0][1] < 0.5): numCorr += 1

    return numCorr

x1 = np.array([[0, 0]])
x2 = np.array([[0, 1]])
x3 = np.array([[1, 0]])
x4 = np.array([[1, 1]])
y1 = np.array([[0, 0]])
y2 = np.array([[0, 1]])
y3 = np.array([[0, 1]])
y4 = np.array([[1, 0]])

list_ws2, list_bs2 = create_random((2, 6, 4, 1))
# print(list_bs2)

if(inp == 'S'):
    w_back2, b_back2 = backprop(40000, sigmoid, sig_deriv, [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], list_ws2, list_bs2)
    p1 = p_net(sigmoid, x1, w_back2, b_back2)
    p2 = p_net(sigmoid, x2, w_back2, b_back2)
    p3 = p_net(sigmoid, x3, w_back2, b_back2)
    p4 = p_net(sigmoid, x4, w_back2, b_back2)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    numCorr = check_all(p1, p2, p3, p4)
    print(numCorr / 4)


# Challenge #3

points, total_list = [], []

for i in range(10000):
    rand1, rand2 = random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5)
    np_arr = np.array([[rand1, rand2]])
    points.append(np_arr)
    y_val = 0
    to_app = np.array([[0]])

    if((rand1**2 + rand2**2) < 1):
        y_val = 1
        to_app = np.array([[1]])
    
    total_list.append((np_arr, to_app))

list_ws3, list_bs3 = create_random((2, 4, 1))
print(list_ws3)

if(inp == 'C'):
    w_back3, b_back3 = backprop(100, sigmoid, sig_deriv, total_list, list_ws3, list_bs3)