fo=open("firstFile.txt","r")
print "Reading 10 character and display current position : "
position=0
while(True):
    a=fo.read(10)
    if not a:
        break
    else:
        print a
        position+=10
        print "position=",position

fo=open("firstFile.txt","r")
position=0
a=fo.read(100)
print "....................."
print "First 100 character of file :\n",a
print "....................."
print "Content from fifth line onwords : "
fo=open("firstFile.txt","r")
for i in range(5):
    fo.readline()
for line in fo:	
	print "line=",line
fo.close()
