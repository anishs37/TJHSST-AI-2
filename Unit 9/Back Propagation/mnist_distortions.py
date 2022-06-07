import csv
import sys
import numpy as np
import math
import random
import pickle
from PIL import Image
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
                    # print(a_vals[ct-1].shape)
                    # print(b_lay.shape)
                    # print(w_lay.shape)
                    dot.append((a_vals[ct - 1])@w_lay + b_lay)
                    a_vals.append(act(dot[ct]))
            
            n = len(dot) - 1
            delta = [None] * n
            delta.append(actDeriv(dot[n])*(yVal - a_vals[n]))
            for lay in range(n - 1, 0, -1):
                # print("deltas[lay + 1] shape: " + str((delta[lay + 1]).shape))
                # print("w[lay+1].transpose() shape " + str((list_w[lay+1].transpose()).shape))
                delta[lay] = actDeriv(dot[lay])*(delta[lay + 1]@list_w[lay + 1].transpose())
            for ct, delVal in enumerate(delta):
                if(ct != 0):
                    list_b[ct] = list_b[ct] + L*delVal
                    list_w[ct] = list_w[ct] + L*((a_vals[ct - 1]).transpose())@delVal

        file_name = 'checkpoint_' + str(ep) + ".pkl"
        whole_path = '/Users/anish/Documents/TJHSST-AI-2/Unit 9/Back Propagation/mnist_checkpoints4/' + file_name
        with open(whole_path, 'wb') as f:
            pickle.dump([list_w, list_b], f)

    return list_w, list_b

def error_funct(out, y):
    return (1/2) * (np.linalg.norm(y - out)) ** 2

def create_random(l):
    w_list, b_list = [None], [None]
    for i in range(1, len(l)):
        weight = 2*np.random.rand(l[i-1], l[i])-1
        bias = 2*np.random.rand(1, l[i])-1
        w_list.append(weight)
        b_list.append(bias)
    return w_list, b_list

train_path = '/Users/anish/Documents/TJHSST-AI-2/Unit 9/Back Propagation/mnist_train.csv'
test_path = '/Users/anish/Documents/TJHSST-AI-2/Unit 9/Back Propagation/mnist_test.csv'
train_set, test_set = [], []

def rotate(img, angle):
    rot_ang = np.radians(angle)
    c_ang, s_ang = np.cos(rot_ang), np.sin(rot_ang)
    rotation_mat = np.array([[c_ang, -s_ang], [s_ang, c_ang]])
    res_img = img.reshape((392,2))
    mult_arr = res_img@rotation_mat
    return mult_arr

def roll_array(img, dir):
    #up, right, down, left
    if(dir == 0):
        img_roll = np.roll(img, 1, axis=0)
    elif(dir == 1):
        img_roll = np.roll(img, 1, axis=1)
    elif(dir == 2):
        img_roll = np.roll(img, -1, axis=0)
    else:
        img_roll = np.roll(img, -1, axis=1)
    return img_roll

final_train_set = []
with open(train_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        x_vals = []
        y_val = [0] * 10
        for i in range(1, 785):
            x_vals.append((int(row[i]))/255)

        y_val[int(row[0])] = 1
        x_np = np.array([x_vals])
        x_np.reshape((28,28))
        y_np = np.array([y_val])
        train_set.append((x_np, y_np))

for val in range(60000):
    rand_num = random.uniform(0,1)
    x_val = train_set[val][0]
    x_val_res = x_val.reshape((28,28))
    y_val = train_set[val][1]
    if(rand_num < 0.33):
        if(rand_num < 0.167):
            rot_arr = rotate(x_val_res, 15)
        else:
            rot_arr = rotate(x_val_res, -15)
        rot_arr.reshape((784,1))
        for ct, elem in enumerate(rot_arr):
            rot_arr[ct] = elem * 255
        rot_arr.resize((1,784))
        for ct, elem in enumerate(rot_arr):
            rot_arr[ct] = elem / 255
        final_train_set.append((rot_arr, y_val))
    else:
        if(rand_num < 0.5):
            roll_arr = roll_array(x_val_res, 0)
        elif(rand_num < 0.67):
            roll_arr = roll_array(x_val_res, 1)
        elif(rand_num < 0.83):
            roll_arr = roll_array(x_val_res, 2)
        else:
            roll_arr = roll_array(x_val_res, 3)
        roll_arr.resize((1,784))
        final_train_set.append((roll_arr, y_val))

file_name = "distorted_train_set_1.pkl"
whole_path = '/Users/anish/Documents/TJHSST-AI-2/Unit 9/Back Propagation/' + file_name
with open(whole_path, 'wb') as f:
    pickle.dump(final_train_set, f)

with open(test_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        x_vals = []
        y_val = [0] * 10
        for i in range(1, 785):
            x_vals.append((int(row[i]))/255)
            
        y_val[int(row[0])] = 1
        x_np = np.array([x_vals])
        y_np = np.array([y_val])
        test_set.append((x_np, y_np))

list_ws, list_bs = create_random((784, 300, 100, 10))
w_back, b_back = backprop(25, sigmoid, sig_deriv, final_train_set, list_ws, list_bs)