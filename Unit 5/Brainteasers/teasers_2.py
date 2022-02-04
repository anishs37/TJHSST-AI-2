import sys; args = sys.argv[1:]
idx = int(args[0])-40

myRegexLst = [
  r"/^[xo.]{64}$/i",
  r"/^[xo]*[.]{1}[xo]*$/i",
  r"/^\.|^.*\.$|^x+o*\..*$|^.*\.o*x+$/i",
  r"/^[^ ]([^ ]{2})*$/",
  r"/^0([01]{2})*$|^1[01]([01]{2})*$/",
  r"/^[^aeiou]*([aeiou][aeiou])[^aeiou]*$/i",
  r"/^[01]*[^1][^1][^0][01]*$/s",
  r"/^[bc]+a?[bc]+$|^[bc]*a?[bc]+$|^[bc]+a?[bc]*$|^a$/",
  r"/^.*?d\w*/im",
  r"/^[012]*[02]$/"]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Anish Susarla, 2, 2023