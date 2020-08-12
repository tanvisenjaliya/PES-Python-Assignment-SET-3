def PalindromeCheckDefaultParam(myStr):
  myStr=myStr.lower()
  myStr1=myStr[::-1]
  if myStr==myStr1:
    print "The given string",myStr,"is palindrome"
  else:
    print "The given string",myStr,"is not palindrome"
  return
myStr=raw_input("Enter the string")
PalindromeCheckDefaultParam(myStr)

