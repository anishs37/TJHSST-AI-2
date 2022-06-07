import sys; args = sys.argv[1:]
idx = int(args[0])-40

myRegexLst = [
  r"/^[xo.]{64}$/i",
  r"/^[xo]*\.[xo]*$/i",
  r"/^\.|^(.*\.|x+o*\..*|.*\.o*x+)$/i",
  r"/^[^ ]([^ ]{2})*$/",
  r"/^(0|1[01])([01]{2})*$/",
  r"/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
  r"/^((0|10)*|(01)*)1*$/",
  r"/^([bc]*a[bc]*|a?[bc]+)$/",
  r"/^\b[bc]*(a[bc]*a|b|c)+$/",
  r"/^(2|1[02]*1)(1[02]*1|0|2)*$/"]
  
if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Anish Susarla, 2, 2023

'''
Challenges that needed to be solved:

1: Write a regular expression that will match on an Othello board represented as a string.
2: Given a string of length 8, determine whether it could represent an Othello edge with exactly one hole.
3: Given an Othello edge as a string, determine whether there is a hole such that if X plays to the hole (assuming it could), it will be connected to one of the corners through X tokens.  Specifically, this means that one of the ends must be a hole, or starting from an end there is a sequence of at least one x followed immediately by a sequence (possibly empty) of o, immediately followed by a hole.
4: Match on all strings of odd length.
5: Match on all odd length binary strings starting with 0, and on even length binary strings starting with 1.
6: Match all words having two adjacent vowels that differ.
7: Match on all binary strings which DON’T contain the substring 110.
8: Match on all non-empty strings over the alphabet {a, b, c} that contain at most one a.
9: Match on all non-empty strings over the alphabet {a, b, c} that contain an even number of a's.
10: Match on all positive, even, base 3 integer strings.
'''