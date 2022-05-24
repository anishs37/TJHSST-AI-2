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
    for val in train_set:
        x, y = val[0], val[1]
        val_ret = p_net(sigmoid, x, list_w, list_b)
        round_ret = round_val(val_ret)
        if(np.array_equal(round_ret, y) == False):
            numMiss += 1
    
    print(str((numMiss/numTotal)*100) + "% misclassified in the training set")

def check_test(list_w, list_b):
    numMiss, numTotal = 0, len(test_set)
    for val in test_set:
        x, y = val[0], val[1]
        val_ret = p_net(sigmoid, x, list_w, list_b)
        round_ret = round_val(val_ret)
        if(np.array_equal(round_ret, y) == False):
            numMiss += 1
    
    print(str((numMiss/numTotal)*100) + "% misclassified in the testing set")

with open('/Users/anish/Documents/TJHSST-AI-2/Unit 9/Back Propagation/mnist_checkpoints/checkpoint_24.pkl', 'rb') as f:
    list_wb = pickle.load(f)
    list_ws = list_wb[0]
    list_bs = list_wb[1]
    check_train(list_ws, list_bs)
    check_test(list_ws, list_bs)