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