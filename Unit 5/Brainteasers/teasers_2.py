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