#stringop.py
def sortNumbers(num):
  for i in range(len(num)-1):
    for j in range(len(num)-1):
      if num[j] > num[j+1]:
        temp = num[j]
        num[j] = num[j+1]
        num[j+1] = temp
  print "Sorted numbers:", num
    
def binarySearch(list1, item):
    list1.sort()
    first = 0
    last = len(list1)-1
    found = False
    
    while first<=last and not found:
        midpoint = (first+last)/2
        if list1[midpoint] == item:
            found = True
            return " Element : ",item ,"Found = ",found
        else:
            if item < list1[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return " Element : ",item ,"Found = ",found

def reverselist(list2):
    list2.reverse()
    return "\nReversed list :", list2
