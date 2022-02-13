import sys
import copy

dfa_spec = sys.argv[1]
dfa_test = sys.argv[2]

spec_type = -1

try:
    spec_type = 0
    test_int = int(dfa_spec)

except:
    spec_type = 1

if(spec_type == 1):
    with open(dfa_spec) as f:
        dfa_specs = [line.strip() for line in f]
    
    valid_letters = dfa_specs[0]
    num_states = int(dfa_specs[1])
    final_states = dfa_specs[2].split(" ")
    final_states = [int(state) for state in final_states]

with open(dfa_test) as f:
    dfa_tests = [line.strip() for line in f]

dfa1 = {
    0: {
        "a": 1,
        "b": 4
    },

    1: {
        "a": 2,
        "b": 4
    },

    2: {
        "a": 4,
        "b": 3
    },

    3: {
        "a": 4,
        "b": 4
    },

    4: {
        "a": 4,
        "b": 4
    }
}

dfa2 = {
    0: {
        "0": 0,
        "1": 1,
        "2": 0
    },

    1: {
        "0": 0,
        "1": 1,
        "2": 0
    }
}

dfa3 = {
    0: {
        "a": 0,
        "b": 1,
        "c": 0
    },

    1: {
        "a": 1,
        "b": 1,
        "c": 1
    }
}

dfa4 = {
    0: {
        "0": 1,
        "1": 0
    },

    1:{
        "0": 0,
        "1": 1
    }
}

dfa5 = {
    0: {
        "0": 1,
        "1": 2
    },

    1: {
        "0": 0,
        "1": 3
    },

    2: {
        "0": 3,
        "1": 0
    },

    3: {
        "0": 2,
        "1": 1
    }
}

dfa6 = {
    0: {
        "a": 1,
        "b": 0,
        "c": 0
    },

    1: {
        "a": 1,
        "b": 2,
        "c": 0
    },

    2: {
        "a": 1,
        "b": 0,
        "c": 3
    },

    3: {
        "a": 3,
        "b": 3,
        "c": 3
    }
}

dfa7 = {
    0: {
        "0": 0,
        "1": 1
    },

    1: {
        "0": 2,
        "1": 1
    },

    2: {
        "0": 2,
        "1": 3
    },

    3: {
        "0": 2,
        "1": 4
    },

    4: {
        "0": 4,
        "1": 4
    },
}

list_valid = []
list_valid.append(("a", "b"))
list_valid.append(("0", "1"))
list_valid.append(("a", "b"))
list_valid.append(("0", "1"))
list_valid.append(("0", "1"))
list_valid.append(("a", "b", "c"))
list_valid.append(("0", "1"))

list_final = []
list_final.append(3)
list_final.append(1)
list_final.append(1)
list_final.append(0)
list_final.append(0)
list_final.append((0, 1, 2))
list_final.append(4)

list_dfa = []
list_dfa.append(dfa1)
list_dfa.append(dfa2)
list_dfa.append(dfa3)
list_dfa.append(dfa4)
list_dfa.append(dfa5)
list_dfa.append(dfa6)
list_dfa.append(dfa7)

if(spec_type == 1):
    count = 0
    curr_state = 0
    sub_dict = {}
    dfa = {}

    for line in dfa_specs:
        if(count == 4):
            curr_state = int(line)

        if(count > 4):
            if(len(line) == 1):
                copy_sub_dict = sub_dict.copy()
                dfa[curr_state] = copy_sub_dict
                curr_state = int(line)
                sub_dict.clear()
            
            elif(len(line) != 0):
                char_toState = line.split(" ")
                ch_toAdd = char_toState[0]
                toState = int(char_toState[1])
                sub_dict[ch_toAdd] = toState
                
        count += 1

    dfa[curr_state] = sub_dict

else:
    dfa = list_dfa[test_int - 1]

    if(test_int == 6):
        final_states = [x for x in list_final[test_int - 1]]
    
    else:
        final_states = [list_final[test_int - 1]]

def go_through_string(test):
    ind = 0
    next_state = 0

    while(ind < len(test)):
        char_to_check = test[ind]
        sub_dict = dfa[next_state]
        
        if(char_to_check not in sub_dict):
            return False

        next_state = sub_dict[char_to_check]
        ind += 1
    
    if(next_state in final_states):
        return True
    
    return False

first_line_print = "*"

try:
    valid_letters

except:
    valid_letters = [x for x in list_valid[test_int - 1]]

for lts in valid_letters:
    first_line_print += "\t" + lts

print(first_line_print)

for st in dfa:
    str_to_print = str(st)

    for vl in valid_letters:
        if(vl not in dfa[st]):
            str_to_print += "\t" + "_"
        
        else:
            str_to_print += "\t" + str(dfa[st][vl])
    
    print(str_to_print)

print("Final nodes: " + str(final_states))
for line in dfa_tests:
    print(str(go_through_string(line)) + " " + line)