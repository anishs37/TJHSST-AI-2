import sys; args = sys.argv[1:]
idx = int(args[0])-60

myRegexLst = [
  r"/^(?!\d*010)[01]*$/i",
  r"/^(?!\d*101)(?!\d*010)[01]*$/i",
  r"/^(0[01]*0|1[01]*1|0|1)$/",
  r"/\b(?=\w*(\w))(?!\w*\1\w)\w*\b/i",
  r"/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/im",
  r"/\b(?!\w*cat)\w{6}\b/i",
  r"/\b(?!\w*(\w)\w*\1)\w*[^!. ]/i",
  r"/^(?!\d*10011)[01]*$/",
  r"/(?!^00$)^(0|1(01?0)*1)+$/im",
  r"/^(?!\d*1[01]1)[01]*$/"]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Anish Susarla, 2, 2023