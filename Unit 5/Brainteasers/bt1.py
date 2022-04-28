import sys; args = sys.argv[1:]
import re
idx = int(args[0])-30
ipt = args[1]

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

re_to_comp = re.compile(myRegexList[])
# Anish Susarla, 2, 2023