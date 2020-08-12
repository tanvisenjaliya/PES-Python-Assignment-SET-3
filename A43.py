def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False



lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
	ele = int(input()) 

	lst.append(ele) # adding the element 
	
print(lst) 
n=input("enter element to search")
if search(lst, n): 
	print("Found") 
else: 
	print("Not Found") 
