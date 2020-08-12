#calc.py
import math

def add(a,b):
  'This adds 2 numbers'
  print "Sum of ",a," and ",b," is",a+b
    
def diff(a,b):
  'This finds the difference between 2 nos'
  print "Difference of ", a," and ",b," is",a-b
    
def multiply(a,b):
  'This multiplies 2 nos'
  print "Multiplication of ",a," and ",b," is",a*b

   
def sqroot(a):
    print "Square root of the number ",a," is ", math.sqrt(a)

def div(a,b):
  'This divides 2 nos'
  print "Division of ",a," and ", b," is",a/b
    
def floor_div(a,b):
    print "Floor division of", a," and ",b," is", a//b
    
def fib(nterms):
  "This generates a fibonacci series"
  a=0
  b=1
  if nterms<=0:
    print("please enter positive number")
  elif nterms==1:
    print("Fibonacci series : \n",a)
  elif nterms==2:
    print("Fibonacci series : \n")
    print a
    print b
  else:
    print("Fibonacci series : \n")
    print a
    print b
    while(nterms>2):
      numnext=a+b
      print numnext
      a=b
      b=numnext
      nterms=nterms-1
#n=int(raw_input("Enter the no of terms for fibonacci series"))
#fib(n)

def isprime(num):
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print num,"is not a prime number"
                break
            else:
                print num,"is a prime number"
                break
    else:
        print num,"is not a prime number"
    
#number=int(raw_input())        
#isprime(number)
