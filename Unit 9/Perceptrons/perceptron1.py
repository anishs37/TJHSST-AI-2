import sys
import ast

def truth_table(bits, n):
    num_digits = 2**bits
    to_conv = ["0"] * num_digits
    curr_val = 2**(num_digits-1)

    for ct, val in enumerate(to_conv):
        if(curr_val <= n):
            to_conv[ct] = "1"
            n -= curr_val

        curr_val /= 2

    lines = []

    for i in range(num_digits):
        line = [i//2**j%2 for j in reversed(range(bits))]  # inspiration: https://stackoverflow.com/questions/6336424/python-build-a-dynamic-growing-truth-table
        lines.append(line)
    
    lines.reverse()
    final_to_rt = []

    for ct, l in enumerate(lines):
        tup_l = tuple(l)
        overall_tup = (tup_l, int(to_conv[ct]))
        final_to_rt.append(overall_tup)
    
    return final_to_rt

def pretty_print_tt(table):
    for val in table:
        str_to_pt = ""
        for v in val[0]:
            str_to_pt += str(v) + " "
        
        str_to_pt += "| " + str(val[1])
        print(str_to_pt)

def step(num):
    if(num > 0):
        return 1
    
    else:
        return 0

def perceptron(A, w, b, x):
    dp = 0
    for i in range(len(w)):
        dp += w[i] * x[i]
    
    inner_val = dp + b
    return A(inner_val)

def check(n, w, b):
    table = truth_table(len(w), n)
    tot = len(table)
    num_right = 0

    for s in table:
        val = perceptron(step, w, b, s[0])
        if(val == s[1]):
            num_right += 1
    
    return num_right / tot

n = int(sys.argv[1])
w = ast.literal_eval(sys.argv[2])
b = float(sys.argv[3])
print(check(n, w, b))