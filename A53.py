fo = open("firstFile.txt", "r+")
print "1.Name of the file: ", fo.name
print "2.Flush: \n"
fo.flush()
fid = fo.fileno()
print "3.File Descriptor: ", fid
ret = fo.isatty()
print "4.Return value : ", ret
print "5."
for index in range(5):
   line = fo.next()
   print "Line No %d - %s" % (index, line)
fo.close()
fo=open("firstFile.txt","r")
line = fo.read(100)
print "6.Read first 100 character: " ,line
fo.close()
fo = open("firstFile.txt", "r+")

line = fo.readline()
print "7.Read Line: %s" % (line)

fo.close()

fo = open("firstFile.txt", "r")# Again set the pointer to the beginning
fo.seek(0, 0)
line = fo.readline()
print "8.Using seek()Read Line: %s" % (line)
fo.close()

fo = open("firstFile.txt", "w")

# Get the current position of the file.
pos = fo.tell()
print "9.Current Position: %d" % (pos)
# Close opend file
fo.close()
print "10.Opening file in write mode"
fo = open("firstFile.txt", "w")

str = "This is 7th line"
# Write a line at the end of the file.
#fo.seek(0, 1)
line = fo.write( str )
# Now read complete file from beginning.
fo.close()
print "After writing\n11.Opening File in Read Mode\n"
fo = open("firstFile.txt", "r")
print "12.Reading file after adding string"
fo.seek(0,0)
lines=fo.read()
print lines
print "13.File Closing"
fo.close()




