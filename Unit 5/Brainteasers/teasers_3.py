import sys; args = sys.argv[1:]
idx = int(args[0])-50

myRegexLst = [
  r"/\w*(\w)\w*\1\w*/i",
  r"/\w*(\w)\w*\1\w*\1\w*\1\w*/i",
  r"/^(0[01]*0|1[01]*1|0|1)$/",
  r"/\b(?=\w*cat)\w{6}\b/i",
  r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/im",
  r"/\b(?!\w*cat)\w{6}\b/i",
  r"/\b(?!\w*(\w)\w*\1)\w*[^!. ]/i",
  r"/^(?!\d*10011)[01]*$/",
  r"/\w*([aeiou])(?!\1)[aeiou]\w*/im",
  r"/^(?!\d*1[01]1)[01]*$/"]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Anish Susarla, 2, 2023

'''
Challenges that needed to be solved:

1: Match all words where some letter appears twice in the same word.
2: Match all words where some letter appears four times in the same word.
3: Match all non-empty binary strings with the same number of 01 substrings as 10 substrings.
4: Match all six letter words containing the substring cat.
5: Match all 5 to 9 letter words containing both the substrings bri and ing.
6: Match all six letter words not containing the substring cat.
7: Match all words with no repeated characters.
8: Match all binary strings not containing the forbidden substring 10011.
9: Match all words having two different adjacent vowels.
10: Match all binary strings containing neither 101 nor 111 as substrings.
'''