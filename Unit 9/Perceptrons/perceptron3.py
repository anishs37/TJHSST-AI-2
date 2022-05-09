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

# XOR HAPPENS HERE
def xor(initWeights, w13, w23, w14, w24, w35, w45, b3, b4, b5):
    layer1 = perceptron(step, initWeights, b3, (w13, w23))
    layer2 = perceptron(step, initWeights, b4, (w14, w24))
    layer3 = perceptron(step, (layer1, layer2), b5, (w35, w45))
    return layer3

w = ast.literal_eval(sys.argv[1])
print(xor(w, -2, 2, 2, -2, 2, 2, -1, -1, 0))

"""
w13 = -2
w23 = 2
b3 = -1
w14 = 2
w24 = -2
b4 = -1
w35 = 2
w45 = 2
b5 = 0
"""