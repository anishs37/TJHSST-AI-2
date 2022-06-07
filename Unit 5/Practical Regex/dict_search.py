import sys
import re

dictionary = sys.argv[1]

with open(dictionary) as f:
    dict_list = [line.strip() for line in f]

reg1 = r"^(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w*$"
exp1 = re.compile(reg1, re.I)
min_len_1 = 999999999
word_list_1 = []
word_list_1_final = []

reg2 = r"^([^aeiou]*[aeiou]){5}[^aeiou]*$"
exp2 = re.compile(reg2, re.I)
max_len_2 = 0
word_list_2 = []
word_list_2_final = []

reg3 = r"^(\w)(?!\w*(\w*\1\w))(?=\w*\1)\w*$"
exp3 = re.compile(reg3, re.I)
max_len_3 = 0
word_list_3 = []
word_list_3_final = []

reg4 = r"^(\w)(\w)(\w)\w*\3\2\1$|^(\w)(\w)\w?\5\4$|^(\w)\w\6$"
exp4 = re.compile(reg4, re.I)
word_list_4 = []

reg5 = r"^[^bt]*(bt|tb)[^bt]*$"
exp5 = re.compile(reg5, re.I)
word_list_5 = []

reg6 = r"^\w*(\w)\1\w*$"
exp6 = re.compile(reg6, re.I)
max_continuous = 0
word_list_6 = []
word_list_6_final = []

reg7 = r"^\w*(\w)\w*\1\w*$"
exp7 = re.compile(reg7, re.I)
max_charlen = 0
word_list_7 = []
word_list_7_final = []

reg8 = r"^\w*(\w\w)\w*\1\w*$"
exp8 = re.compile(reg8, re.I)
max_repeats = 0
word_list_8 = []
word_list_8_final = []

reg9 = r"^\w*[bcdfghjklmnpqrstvwxyz]\w*$"
exp9 = re.compile(reg9, re.I)
max_conslen = 0
word_list_9 = []
word_list_9_final = []

reg10 = r"^(?!\w*(\w)(\w*\1){2})\w*$"
exp10 = re.compile(reg10, re.I)
max_len_10 = 0
word_list_10 = []
word_list_10_final = []

def num_contin(word):
    curr_contin = 1
    max_contin = 1
    last_char = word[0]

    for ch in range(1, len(word)):
        char_check = word[ch]

        if(char_check == last_char):
            curr_contin += 1
        
        else:
            if(curr_contin > max_contin):
                max_contin = curr_contin
            
            curr_contin = 1

        last_char = char_check

    if(curr_contin > max_contin):
        max_contin = curr_contin

    return max_contin

def num_maxchar(word):
    char_freq = {}
    for i in word:
        if i in char_freq:
            char_freq[i] += 1
        else:
            char_freq[i] = 1
    
    max_freq = 0

    for ch in char_freq:
        ch_get = char_freq[ch]
        if(ch_get > max_freq):
            max_freq = ch_get

    return max_freq

def num_maxchar_cons(word):
    num_cons = 0

    for i in word:
        new_char = i.lower()

        if(new_char != 'a' and new_char != 'e' and new_char != 'i' and new_char != 'o' and new_char != 'u'):
            num_cons += 1

    return num_cons

def num_repeats(word):
    freq_table = {}
    max_return = 0

    for i in range(0, (len(word) - 1), 1):
        ch_1 = word[i]
        ch_2 = word[i + 1]
        str_comb = ch_1 + ch_2

        if(str_comb not in freq_table):
            freq_table[str_comb] = 1
        
        else:
            prev_val = freq_table.get(str_comb)
            freq_table[str_comb] = prev_val + 1
    
    for val in freq_table:
        to_get = freq_table[val]
        
        if(to_get > max_return):
            max_return = to_get
 
    return max_return

for word in dict_list:
    for result in exp1.finditer(word):
        word_list_1.append(word)
        if(len(word) < min_len_1):
            min_len_1 = len(word)

    for result in exp2.finditer(word):
        word_list_2.append(word)
        if(len(word) > max_len_2):
            max_len_2 = len(word)

    for result in exp3.finditer(word):
        word_list_3.append(word)
        if(len(word) > max_len_3):
            max_len_3 = len(word)

    for result in exp4.finditer(word):
        word_list_4.append(word)

    for result in exp5.finditer(word):
        word_list_5.append(word)
    
    for result in exp6.finditer(word):
        word_list_6.append(word)
        contin_len = num_contin(word)

        if(contin_len > max_continuous):
            max_continuous = contin_len
    
    for result in exp7.finditer(word):
        word_list_7.append(word)
        max_char = num_maxchar(word)

        if(max_char > max_charlen):
            max_charlen = max_char
    
    for result in exp8.finditer(word):
        word_list_8.append(word)
        num_rpts = num_repeats(word)

        if(num_rpts > max_repeats):
            max_repeats = num_rpts

    for result in exp9.finditer(word):
        word_list_9.append(word)
        max_cons = num_maxchar_cons(word)

        if(max_cons > max_conslen):
            max_conslen = max_cons

    for result in exp10.finditer(word):
        word_list_10.append(word)
        if(len(word) > max_len_10):
            max_len_10 = len(word)

reg6b = r"^\w*(\w)\1{"+str(max_continuous - 1)+r"}\w*$"
exp6b = re.compile(reg6b, re.I)

reg7b = r"^\w*(\w)(\w*\1){"+str(max_charlen - 1)+r"}\w*$"
exp7b = re.compile(reg7b, re.I)

reg8b = r"^\w*(\w\w)(\w*\1){"+str(max_repeats - 1)+r"}\w*$"
exp8b = re.compile(reg8b, re.I)

reg9b = r"^(\w*[bcdfghjklmnpqrstvwxyz]){"+str(max_conslen)+r"}\w*$"
exp9b = re.compile(reg9b, re.I)

for word in word_list_1:
    if(len(word) == min_len_1):
        word_list_1_final.append(word)

for word in word_list_2:
    if(len(word) == max_len_2):
        word_list_2_final.append(word)

for word in word_list_3:
    if(len(word) == max_len_3):
        word_list_3_final.append(word)

for word in word_list_6:
    for result in exp6b.finditer(word):
        word_list_6_final.append(word)

for word in word_list_7:
    for result in exp7b.finditer(word):
        word_list_7_final.append(word)

for word in word_list_8:
    for result in exp8b.finditer(word):
        word_list_8_final.append(word)

for word in word_list_9:
    for result in exp9b.finditer(word):
        word_list_9_final.append(word)

for word in word_list_10:
    if(len(word) == max_len_10):
        word_list_10_final.append(word)

print('#1 re.compile("' + reg1 + '", re.I)')
print(str(len(word_list_1_final)) + " total matches")
for i in range(min(5, len(word_list_1_final))):
    print(word_list_1_final[i].lower())
print()

print('#2 re.compile("' + reg2 + '", re.I)')
print(str(len(word_list_2_final)) + " total matches")
for i in range(min(5, len(word_list_2_final))):
    print(word_list_2_final[i].lower())
print()

print('#3 re.compile("' + reg3 + '", re.I)')
print(str(len(word_list_3_final)) + " total matches")
for i in range(min(5, len(word_list_3_final))):
    print(word_list_3_final[i].lower())
print()

print('#4 re.compile("' + reg4 + '", re.I)')
print(str(len(word_list_4)) + " total matches")
for i in range(min(5, len(word_list_4))):
    print(word_list_4[i].lower())
print()

print('#5 re.compile("' + reg5 + '", re.I)')
print(str(len(word_list_5)) + " total matches")
for i in range(min(5, len(word_list_5))):
    print(word_list_5[i].lower())
print()

print('#6 re.compile("' + reg6b + '", re.I)')
print(str(len(word_list_6_final)) + " total matches")
for i in range(min(5, len(word_list_6_final))):
    print(word_list_6_final[i].lower())
print()

print('#7 re.compile("' + reg7b + '", re.I)')
print(str(len(word_list_7_final)) + " total matches")
for i in range(min(5, len(word_list_7_final))):
    print(word_list_7_final[i].lower())
print()

print('#8 re.compile("' + reg8b + '", re.I)')
print(str(len(word_list_8_final)) + " total matches")
for i in range(min(5, len(word_list_8_final))):
    print(word_list_8_final[i].lower())
print()

print('#9 re.compile("' + reg9b + '", re.I)')
print(str(len(word_list_9_final)) + " total matches")
for i in range(min(5, len(word_list_9_final))):
    print(word_list_9_final[i].lower())
print()

print('#10 re.compile("' + reg10 + '", re.I)')
print(str(len(word_list_10_final)) + " total matches")
for i in range(min(5, len(word_list_10_final))):
    print(word_list_10_final[i].lower())
print()

'''
Challenges that needed to be solved:

1: Match all words of minimum length that contain each vowel at least once.
2: Match all words of maximum length that contain precisely 5 vowels.
3: Match all words of maximum length where the first letter reappears as the last letter but does not appear
anywhere else in the word.
4: Match all words where the first three letters, reversed, are the last three letters (overlapping allowed).
5: Match all words where there is exactly one “b”, exactly one “t”, and they are adjacent to each other.
6: Match all words with the longest contiguous block of a single letter.
7: Match all words with the greatest number of a repeated letter
8: Match all words with the greatest number of adjacent pairs of identical letters.
9: Match all words with the greatest number of consonants.
10: Match all words of maximum length where no letter is repeated more than once.
'''