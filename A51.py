import glob

def countOfTreasureFiles(list_of_files):
	pattern="Treasure"
	count=0
	for f in list_of_files:
		fo=open(f,"r")
		content=fo.read()
		fo.close()
		if pattern in content:
			count+=1
	print "Total ",count," number of files have the pattern",pattern," in ",f

countOfTreasureFiles(['firstFile.txt','firstFile2.txt','temp.txt','temp2.txt'])
def countOfTreasureInEachFile(list_of_files):
	pattern="Treasure"
	count=0
	for f in list_of_files:
		fo=open(f,"r")
		content=fo.read()
		fo.close()
		if pattern in content:
			numOfOccurences=content.count(pattern)
			print f,"has ",numOfOccurences," times of ",pattern," in it"
		else:
			print f,"has no",pattern 
		

countOfTreasureInEachFile(['firstFile.txt','firstFile2.txt','temp.txt','temp2.txt'])
