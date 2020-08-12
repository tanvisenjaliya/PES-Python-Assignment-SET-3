def BiggestRequiredArg(a,b,c,d):
  'this checks for biggest of 4 nos'
  if a>b and a>c and a>d:
    print a," is the biggest"
  elif b>a and b>c and b>d:
    print b," is the biggest"
  elif c>a and c>b and c>d:
    print c," is the biggest"
  else:
    print d," is the biggest"
  return
BiggestRequiredArg(2,3,4,1)
