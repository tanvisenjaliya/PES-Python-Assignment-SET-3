def PoundToKg(pound):
  try:
    assert (pound>=0),"Negative weight not allowed"
    return pound*0.453592
  except AssertionError, exp:
    return exp
print "43 Pound : ",PoundToKg(43)
print "-13 Pound : ",PoundToKg(-13)


def PoundToKg(pound):
  try:
    assert (pound>=100), "Weight should be more than or equal to 100"
    return pound*0.453592
  except AssertionError, exp:
    return exp

print "56 Pound : ",PoundToKg(56)," kg."
print "101 Pound : ",PoundToKg(101)," kg."




