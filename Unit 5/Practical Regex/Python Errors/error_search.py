import sys
import re

file_to_search = sys.argv[1]

with open(file_to_search) as f:
    lines = [line.strip() for line in f]

reg1 = r"\d.*=."
exp1 = re.compile(reg1)

reg2 = r"^#?(?!def|if|elif|while|print)\w*\("
exp2 = re.compile(reg2)

reg4 = r"^#?(if|while|else|elif|def)[^:]*$"
exp4 = re.compile(reg4)

reg5 = r"^#?(if|while|elif|return)[^=]*=[^=]*$"
exp5 = re.compile(reg5)

print("Variable names that begin with digits")
count1 = 1

for ln in lines:
    for result in exp1.finditer(ln):
        print(count1)
    
    count1 += 1

print()
count1 = 1
print("Function calls to undefined functions")

for ln in lines:
    for result in exp2.finditer(ln):
        funct_name = ""
        index_of_2 = ln.index('(')

        if('=' in ln):
            index_of = ln.index('=')
            funct_name = ln[index_of + 1:index_of_2]
            funct_name = funct_name.strip()

        else:
            if(ln[0] == '#'):
                funct_name = ln[1:index_of_2]
            
            else:
                funct_name = ln[0:index_of_2]
        
        reg2b = r"^def[ ]*"+funct_name+r"[ ]*\("
        exp2b = re.compile(reg2b)
        count2 = 1
        check_2 = 0

        while(count2 < count1):
            ln_to_check = lines[count2 - 1]
            for result in exp2b.finditer(ln_to_check):
                check_2 += 1

            count2 += 1

        if(check_2 == 0):
            print(count1)

    count1 += 1

print()
print("Function calls to defined functions with wrong number of arguments")
count1 = 1

for ln in lines:
    for result in exp2.finditer(ln):
        funct_name = ""
        args_check = ""
        index_of_2 = ln.index('(')

        if('=' in ln):
            index_of = ln.index('=')
            funct_name = ln[index_of + 1:index_of_2]
            args_check = ln[index_of + 1:]
            funct_name = funct_name.strip()
            args_check = args_check.strip()

        else:
            if(ln[0] == '#'):
                funct_name = ln[1:index_of_2]
            
            else:
                funct_name = ln[0:index_of_2]

            args_check = ln
        
        reg2b = r"^def[ ]*"+funct_name+r"[ ]*\("
        exp2b = re.compile(reg2b)
        count2 = 1
        check_2 = 0
        line_def = 0

        while(count2 < count1):
            ln_to_check = lines[count2 - 1]
            for result in exp2b.finditer(ln_to_check):
                check_2 += 1
                line_def = count2 - 1

            count2 += 1

        if(check_2 != 0):
            funct_def_ln = lines[line_def]
            num_commas = funct_def_ln.count(',')
            num_commas_2 = args_check.count(',')

            if(num_commas != num_commas_2):
                print(count1)
        
    count1 += 1

print()
count1 = 1
print("Missing colons")

for ln in lines:
    for result in exp4.finditer(ln):
        print(count1)
    
    count1 += 1

print()
count1 = 1
print("= used instead of ==")

for ln in lines:
    for result in exp5.finditer(ln):
        print(count1)
    
    count1 += 1