import sys; args = sys.argv[1:]
idx = int(args[0])-30

myRegexLst = [
  r"/^0$|^10[01]$/",
  r"/^[01]*$/",
  r"/0$/",
  r"/\b\w*[aeiou]\w*[aeiou]\w*\b/im",
  r"/^[1][01]*[0]$|^[0]$/",
  r"/^[01]*110[01]*$/",
  r"/^.{2,4}$/s",
  r"/^\d{3}\s*-?[ ]*\d{2}\s*-?\s*\d{4}$/",
  r"/^.*?d\w*/im",
  r"/^[0][01]*[0]$|^[1][01]*[1]$|^0$|^1$|^$/"]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Anish Susarla, 2, 2023

'''
Challenges that needed to be solved:

1: Determine whether a string is either 0, 100, or 101.
2: Determine whether a given string is a binary string (ie. composed only of  0 and 1 characters).
3: Given a binary integer string, what regular expression determines whether it is even?
4: What is a regular expression to determine (ie. match) those words in a text that have at least two vowels?
5: Given a string, determine whether it is a non-negative, even binary integer string.
6: Determine whether a given string is a binary string containing 110 as a substring.
7: Match on all strings of length at least two, but at most four.
8: Validate a social security number entered into a field (ie. recognize ddd-dd-dddd where the d represents digits and where the dash indicates an arbitrary number of spaces with at most one dash).  For example, 542786363,   542  786363, and 542 – 78-6263 are all considered valid.
9: Determine a regular expression to help you find the first word of each line of text with a  d  in it: Match through the end of the first word with a d on each line that has a d.
10: Determine whether a string is a binary string that has the same number of 01 substrings as 10 substrings.
'''