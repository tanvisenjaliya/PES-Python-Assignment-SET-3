import math
import sys
import time
#Exception
try:
    num=a/2
except Exception:
    print"Exception"

#Standard error
try:
    f0=open("file1.txt","r")
except StandardError:
    print "Standard error:No file exists"

#Arithmetic error
try:
    div=2/0
except ArithmeticError:
    print "Arithmetic error exception"

#StopIteration
try:
    fo=open('temp.txt',"r")
    for i in range(1,10):
        print fo.next()
except StopIteration:
    print "Stop Iteration Exception"
fo.close()

#Systemexit
try:
    sys.exit()
except SystemExit:
    print "system exit exception"

