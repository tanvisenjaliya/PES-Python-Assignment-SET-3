fo = open("firstFile.txt","r")
print "Read String is : ",fo.read()
fo.close()

fo=open("firstFile2.txt","w")
fo.writelines("so we have come to the end now\ni dont think this is\nyes very true\n still to go\n this is final now")
fo.close()


fo=open("firstFile2.txt","a")
fo.writelines("finally\nso we have come to the end now\n again and again\nsorry to keep you waiting\nFINAL ONE!!!!")
fo.close()

