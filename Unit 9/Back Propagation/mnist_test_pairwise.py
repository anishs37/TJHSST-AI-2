import csv
import sys
import numpy as np
import math
import random
import pickle

train_path = '/Users/anish/Documents/TJHSST-AI-2/Unit 9/Back Propagation/mnist_train.csv'
test_path = '/Users/anish/Documents/TJHSST-AI-2/Unit 9/Back Propagation/mnist_test.csv'
train_set, test_set = [], []

with open(train_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        x_vals = []
        y_val = [0] * 10
        for i in range(1, 785):
            x_vals.append((int(row[i]))/255)
            
        y_val[int(row[0])] = 1
        x_np = np.array([x_vals])
        y_np = np.array([y_val])
        train_set.append((x_np, y_np))

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

def round_val(val):
    highestVal, highestPos = 0, 0
    for ct, v in enumerate(val[0]):
        if(v > highestVal):
            highestVal, highestPos = v, ct

    y_val = [0] * 10
    y_val[highestPos] = 1
    y_np = np.array([y_val])
    return y_np        

def check_train(list_w, list_b):
    numMiss, numTotal = 0, len(train_set)
    numThru = 0
    num_pred, num_conf = [0] * 10, [0] * 10
    counter = 0
    for val in train_set:
        x, y = val[0], val[1]
        for i in range(10):
            for j in range(10):
                if(i < j):
                    w_loc, b_loc = list_w[counter], list_b[counter]
                    val_ret = p_net(sigmoid, x, w_loc, b_loc)
                    # round_ret = round_val(val_ret)
                    check_val = 0
                    if(val_ret[0][0] < 0.5):
                        check_val = i
                    else:
                        check_val = j
                    num_pred[check_val] += 1
                    num_conf[check_val] += abs(0.5 -val_ret[0][0])
                    counter += 1
        max_val = max(num_pred)
        max_pos = num_pred.index(max_val)
        numSame, listSame, maxConf = 0, [], 0
        for ct, val in enumerate(num_pred):
            if(val == max_val):
                numSame += 1
                listSame.append(ct)
        if(numSame > 1):
            for ct, val in enumerate(num_conf):
                if(ct in listSame):
                    if(val > maxConf):
                        maxConf = val
                        max_pos = ct
        if(1 != int(y[0][max_pos])):
            numMiss += 1
        numThru += 1
        print((numMiss, numThru))
        counter = 0
        num_pred = [0] * 10
    
    print(str((numMiss/numTotal)*100) + "% misclassified in the training set")

def check_test(list_w, list_b):
    numMiss, numTotal = 0, len(test_set)
    num_pred = [0] * 10
    counter = 0
    for val in test_set:
        x, y = val[0], val[1]
        for i in range(10):
            for j in range(10):
                if(i < j):
                    w_loc, b_loc = list_w[counter], list_b[counter]
                    val_ret = p_net(sigmoid, x, w_loc, b_loc)
                    #round_ret = round_val(val_ret)
                    check_val = 0
                    if(val_ret[0][0] < 0.5):
                        check_val = i
                    else:
                        check_val = j
                    num_pred[check_val] += 1
                    counter += 1
        max_val = max(num_pred)
        max_pos = num_pred.index(max_val)
        if(1 != int(y[0][max_pos])):
            numMiss += 1
        counter = 0
        num_pred = [0] * 10
    
    print(str((numMiss/numTotal)*100) + "% misclassified in the testing set")

with open('/Users/anish/Documents/TJHSST-AI-2/Unit 9/Back Propagation/all_pairwise_wb.pkl', 'rb') as f:
    list_wb = pickle.load(f)

list_ws, list_bs = [], []
for i in list_wb:
    list_ws.append(i[0])
    list_bs.append(i[1])

check_train(list_ws, list_bs)
check_test(list_ws, list_bs)