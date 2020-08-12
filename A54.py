import time
i=1
try:
    while(i<5):
        time.sleep(1)
        print i
        i+=1
except KeyboardInterrupt:
    print "KeyboardInterrupt"
    
    
try:
    name = input("Enter your name:")
    print "Good Morning "+ name
except NameError:#Enter your name in Quotes else NameError msg will appear
    print "Enter your name in Quotes else NameError msg will appear.\nNameError"


a=input("Enter an int")
b=input("Enter an int")
try:
    num= a/b
except ArithmeticError:
    print "ArithmeticError"
