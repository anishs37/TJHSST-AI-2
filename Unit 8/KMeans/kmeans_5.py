import math
import sys
import csv
import math
import random

k = 5
all_data = []

with open('star_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_ct = 0

    for row in csv_reader:
        if(line_ct >= 1):
            all_data.append((math.log(float(row[0])), math.log(float(row[1])), math.log(float(row[2])), float(row[3])))
        
        line_ct += 1

#print(all_data)

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
    print(str(len(stars_dict[0])) + " " + str(len(stars_dict[1])) + " " + str(len(stars_dict[2])) + " " + str(len(stars_dict[3])) + " " + str(len(stars_dict[4])))
    sq_er = 0

    for i in range(k):
        sq_er += (len(stars_dict[i]) - 48) ** 2

    print(sq_er)
    
stars_dict = find_stars_dict(orig_sets)
print_results(stars_dict)

for check in range(15):
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