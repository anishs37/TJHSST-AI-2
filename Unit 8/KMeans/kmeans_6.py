import math
import sys
import csv
import math
import random

k = 6
all_data = []
all_all_data = dict()

with open('star_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_ct = 0

    for row in csv_reader:
        if(line_ct >= 1):
            all_data.append((math.log(float(row[0])), math.log(float(row[1])), math.log(float(row[2])), float(row[3])))
            all_all_data[all_data[line_ct - 1]] = int(row[4])
        
        line_ct += 1

# print(all_all_data)

'''
Brown Dwarf -> Star Type = 0
Red Dwarf -> Star Type = 1
White Dwarf-> Star Type = 2
Main Sequence -> Star Type = 3
Supergiant -> Star Type = 4
Hypergiant -> Star Type = 5
'''

orig_sets = []

for i in range(k):
    len_data = len(all_data)
    rand_num = random.randint(0, len_data - 1)
    orig_sets.append(all_data[rand_num])

def find_stars_dict(orig_sets):
    stars_dict = dict()

    for i in range(k):
        stars_dict[i] = list()

    for s in all_data:
        sq_errors = []

        for o_s in orig_sets:
            sq_er = (s[0] - o_s[0]) ** 2 + (s[1] - o_s[1]) ** 2 + (s[2] - o_s[2]) ** 2 + (s[3] - o_s[3]) ** 2
            sq_errors.append(sq_er)
        
        min_loc = 0
        min_err = max(sq_errors)

        for ct, sq in enumerate(sq_errors):
            if(sq < min_err):
                min_loc = ct
                min_err = sq
        
        stars_dict[min_loc].append(s)

    return stars_dict

def print_results(stars_dict):
    # print(str(len(stars_dict[0])) + " " + str(len(stars_dict[1])) + " " + str(len(stars_dict[2])) + " " + str(len(stars_dict[3])) + " " + str(len(stars_dict[4])) + " " + str(len(stars_dict[5])))
    elem_0, elem_1, elem_2, elem_3, elem_4, elem_5 = [], [], [], [], [], []

    for elem in stars_dict[0]:
        elem_check = all_all_data[elem]
        elem_0.append(elem_check)
    
    print("Mean 0: " + str(elem_0))
    print()

    for elem in stars_dict[1]:
        elem_check = all_all_data[elem]
        elem_1.append(elem_check)
    
    print("Mean 1: " + str(elem_1))
    print()

    for elem in stars_dict[2]:
        elem_check = all_all_data[elem]
        elem_2.append(elem_check)
    
    print("Mean 2: " + str(elem_2))
    print()

    for elem in stars_dict[3]:
        elem_check = all_all_data[elem]
        elem_3.append(elem_check)
    
    print("Mean 3: " + str(elem_3))
    print()

    for elem in stars_dict[4]:
        elem_check = all_all_data[elem]
        elem_4.append(elem_check)
    
    print("Mean 4: " + str(elem_4))
    print()

    for elem in stars_dict[5]:
        elem_check = all_all_data[elem]
        elem_5.append(elem_check)
    
    print("Mean 5: " + str(elem_5))

    # sq_er = 0

    # for i in range(k):
    #     sq_er += (len(stars_dict[i]) - 40) ** 2

    # print(sq_er)
    
stars_dict = find_stars_dict(orig_sets)
# print_results(stars_dict)

for check in range(80):
    for l in stars_dict:
        list_check = stars_dict[l]
        list_means = list()

        for i in range(4):
            list_i = [x[i] for x in list_check]
            list_means.append(sum(list_i) / len(list_i))

        tuple_means = tuple(list_means)
        orig_sets[l] = tuple_means
    stars_dict = find_stars_dict(orig_sets)

print_results(stars_dict)