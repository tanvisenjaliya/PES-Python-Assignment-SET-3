try:
    myfile =open("firstFile.txt","r")
    print myfile.read()
    myfile.write("Hello")
except IOError:
    print "Writing mode is not allowed"

try:
    num = int(input("Enter value:"))
except ValueError:
    print "ValueError"

'''Output Extract:
Enter value:'trttr'
ValueError'''
