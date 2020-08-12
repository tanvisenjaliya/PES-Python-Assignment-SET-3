import math
def Addition(a,b):
  'This adds the two nos'
  sum=a+b
  print "sum is",sum
def Subtraction(a,b):
  'This finds the difference of two nos'
  sub=a-b
  print "Subtraction is",sub
def Multiply(a,b):
  'This multiplies two nos'
  mul=a*b
  print "multiplication is",mul
def Division(a,b):
  'This divides the nos'
  div=a/b
  print "Division is",div
def Sqrt(num):
  'This finds the square root of a number'
  print "SQrt is ",math.sqrt(num)
Addition(3,5)
Subtraction(9,3)
Multiply(3,5)
Division(4,2)
Sqrt(9)
Sqrt(num=81)

def subStr(str,delcharctr):
  'This creates sub string from given string with the delimiter character :'
  subStr= str.split(delcharctr,6)
  print "Original String is",str
  return subStr
str="Pack:My:Box:With:Good:Food"
delcharctr=':'
subStr= subStr(str,delcharctr)
print "Substring from string is",subStr
