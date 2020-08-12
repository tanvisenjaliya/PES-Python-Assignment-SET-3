strlist=list()
print "The last line as first line and first line as last line (Reverse the lines of the file)"
for lines in reversed(open("firstFile.txt").readlines()):
    print lines.rstrip()
    strlist.append(lines.rstrip())
print ".................................."    
print "Characters of file from last character of file till the first character of the file.(Reverse entire contents of  file )"   
for string in strlist:
    print string[::-1]
    
