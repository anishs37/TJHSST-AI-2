import sys
from colorama import init, Back, Fore
import re

init()
 
reg = sys.argv[1]
s = "While inside they wined and dined, safe from the howling wind.\nAnd she whined, it seemed, for the 100th time, into the ear of her friend,\nWhy indeed should I wind the clocks up, if they all run down in the end?"

flags = []
counter = 0
indTwo = len(reg)
testCounter = 0

for ind, char in enumerate(reg):
    if(counter == 2):
        flags.append(char)

        if(ind != len(reg) and testCounter == 0):
            testCounter += 1
            indTwo = ind

    if(char == '/'):
        counter += 1

reg = reg[0:indTwo]

for flag in flags:
    reg = "(?" + flag + ")" + reg

reg = reg.replace("/", "")
exp  = re.compile(reg)

prevInd = 0
prevColor = 0

for result in exp.finditer(s):
    if(int(result.start()) - prevInd == 0 and prevInd != 0):
        if(prevColor == 0):
            print(s[prevInd:int(result.start())] + Back.LIGHTCYAN_EX + str(result[0]) + Back.RESET, end = '')
            prevColor = 1
        
        else:
            print(s[prevInd:int(result.start())] + Back.LIGHTYELLOW_EX + str(result[0]) + Back.RESET, end = '')
            prevColor = 0

    else:
        print(s[prevInd:int(result.start())] + Back.LIGHTYELLOW_EX + str(result[0]) + Back.RESET, end = '')
        prevColor = 0

    prevInd = int(result.end())

print(s[prevInd:])