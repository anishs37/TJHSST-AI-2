import sys
import re

dictionary = sys.argv[1]

with open(dictionary) as f:
    dict_list = [line.strip() for line in f]

exp1 = re.compile(r"")

for word in dict_list:
    counter = 0

    for result in exp1.finditer(word):
        counter += 1

print("#1: re.compile(r"", re.I, )")
