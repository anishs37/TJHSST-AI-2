import matplotlib.pyplot as plt
import numpy as np

max_epochs = 100
l = 1

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

def check2(table, n, w, b):
    tot = len(table)
    num_right = 0

    for s in table:
        val = perceptron(step, w, b, s[0])
        if(val == s[1]):
            num_right += 1
    
    return num_right / tot

def train(n, t_table):
    epoch_ct = 1
    w, b = [0] * n, 0
    w = tuple(w)

    while(epoch_ct <= 100):
        num_equal = 0
        for v in t_table:
            x = v[0]
            x_exp = v[1]
            f_star = perceptron(step, w, b, x)
            mult_val = (x_exp - f_star) * l
            x_upd = []
            w_upd = []

            for val in x:
                x_upd.append(val * mult_val)

            for i in range(len(w)):
                w_upd.append(w[i] + x_upd[i])

            w_old = w
            b_old = b
            w = w_upd
            b += mult_val

            if(w == w_old and b == b_old):
                num_equal += 1
            
            else:
                num_equal = 0

        if(num_equal >= len(t_table)):
            return w, b
        
        epoch_ct += 1
    
    return w, b

def test(n):
    num_poss, num_corr = 2 ** (2 ** n), 0
    
    for i in range(num_poss):
        tt = truth_table(n, i)
        w, b = train(n, tt)
        prob = check2(tt, i, w, b)

        if(prob == 1):
            num_corr += 1

    print(str(num_poss) + " possible functions; " + str(num_corr) + " can be correctly modeled.")

# plt.xticks(np.arange(-2, 2, 0.1))
# plt.yticks(np.arange(-2, 2, 0.1))

for i in range(16):
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    tt = truth_table(2, i)
    w, b = train(2, tt)
    x_green, y_green, x_red, y_red = [], [], [], []

    for x in np.arange(-2, 2.01, 0.1):
        for y in np.arange(-2, 2.01, 0.1):
            ret_val = perceptron(step, w, b, (x,y))
            if(ret_val == 0):
                plt.plot([x], [y], marker="o", markersize=1, markeredgecolor="red", markerfacecolor="red")
            
            else:
                plt.plot([x], [y], marker="o", markersize=1, markeredgecolor="green", markerfacecolor="green")

    for v in tt:
        if(v[1] == 0):
            plt.plot([v[0][0]], [v[0][1]], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red")
        
        else:
            plt.plot([v[0][0]], [v[0][1]], marker="o", markersize=5, markeredgecolor="green", markerfacecolor="green")

    plt.show()