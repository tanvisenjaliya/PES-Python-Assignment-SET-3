def fib(nterms):
 
  a=0
  b=1
  if nterms<=0:
    print("please enter positive number")
  elif nterms==1:
    print("Fibonacci series:",a)
  elif nterms==2:
    print a
    print b
  else:
    print a
    print b
    while(nterms>2):
      numnext=a+b
      print numnext
      a=b
      b=numnext
      nterms=nterms-1
# Now you can call fib function
n=int(input("Enter the no of terms"))
fib(n)
