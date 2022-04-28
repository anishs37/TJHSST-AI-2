import sys
import csv
import math

file_name = "/Users/anish/Documents/TJHSST-AI-2/Unit 8/Decision Trees/play_tennis.csv"

all_data = []
list_fts = []
lab_val = ""
poss_vals = []

with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_ct = 0

    for row in csv_reader:
        if(line_ct == 0):
            for s in row:
                list_fts.append(s)
            
            lab_val = list_fts[len(list_fts) - 1]

        if(line_ct >= 1):
            tuple_app = tuple()
            for i in range(len(list_fts)):
                new_tup = (row[i],)
                tuple_app = tuple_app + new_tup

            all_data.append(tuple_app)
        
        line_ct += 1

for d in all_data:
    if(len(poss_vals) != 2):
        if(d[len(d) - 1] not in poss_vals):
            poss_vals.append(d[len(d) - 1])

num_t, num_f = 0, 0

for r in all_data:
    if(r[len(r) - 1] == poss_vals[0]):
        num_t += 1
    
    else:
        num_f += 1

tot = num_t + num_f

start_entropy = ((num_t/tot)*math.log2(num_t/tot) + (num_f/tot)*math.log2(num_f/tot)) * -1
print("Starting Entropy " + str(start_entropy))
curr_entropy = start_entropy
fts_used = []

def rec_funct(data):
    ft_info_gain = ""
    max_info_gain = 0
    dist_vals = set()

    for val in data:
        dist_vals.add(val[len(val) - 1])

    dist_vals = list(dist_vals)
    tot_vals = len(data)

    list_fts = []

    for ft in data[0]:
        list_fts.append(ft)
    
    dict_dist = dict()

    for ct, ft in enumerate(list_fts):
        if(ct != len(list_fts) - 1):
            list_ft = []

            for val in data:
                list_ft.append(val[ct])

            myset = set(list_ft)
            mylist = list(myset)
            vals_for_ft = dict.fromkeys(list(range(0, len(mylist))))

            for i in range(len(vals_for_ft)):
                vals_for_ft[i] = []

            for val in data:
                ind_check = mylist.index(val[ct])
                vals_for_ft[ind_check].append(val[len(val) - 1])

            tot_ent_calc = 0

            for i in range(len(vals_for_ft)):
                num_each = [0, 0]
                list_ret = vals_for_ft[i]

                for elem in list_ret:
                    if(elem == dist_vals[0]):
                        num_each[0] = num_each[0] + 1
                    
                    else:
                        num_each[1] = num_each[1] + 1
                
                num_one, num_two = num_each[0], num_each[1]
                ft_ent_calc = 0

                if(num_one != 0 and num_two != 0):
                    ft_ent_calc = ((num_one/(num_one + num_two))*math.log2(num_one/(num_one + num_two)) + (num_two/(num_one + num_two))*math.log2(num_two/(num_one + num_two))) * -1
                    ft_ent_calc *= (num_one + num_two) / tot_vals
                
                tot_ent_calc += ft_ent_calc

            ft_inf_gain = curr_entropy - tot_ent_calc

            if(ft_inf_gain > max_info_gain):
                max_info_gain = ft_inf_gain
                ft_info_gain = ft

    print(ft_info_gain + "? (information gain: " + str(max_info_gain) + ")")
    ind = list_fts.index(ft_info_gain)
    dist_ft_vals = set()

    for r in data:
        dist_ft_vals.add(r[ind])

    dist_ft_vals = list(dist_ft_vals)

    # for ft in dist_ft_vals:
    #     split_data = [x for x in data if x[ind] == ft]
    #     split_data.append(data[0])
    #     rec_funct(split_data)

all_data_copy = all_data.copy()
print(all_data_copy)
rec_funct(all_data_copy)