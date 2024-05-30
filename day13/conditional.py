# #strings are immutable
# #for string it will always make a new string

a = " name  Harry singh from india"
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.strip("!"))
# print(a.replace("Harry" , "raj"))
# print(a.split(" "))#will convert in the form of string 
# blogheadding = "introduction to jS"
# print(blogheadding.capitalize())#first char get capital

print(len(a))
print(a.center(29))#this method will align to the center as per tha parameter given by the user

str = "collegename is vitvellore !!!"
print(str.count('e'))#count()
print(str.endswith("!!!"))#will check if string is end with the given value or not
print(str.endswith("to" , 4 ,10))#given range mein bhi check kr skte hain
print(str.find("is"))#will return the index where "is" present ,  if not present then will return -1
print(str.index("is"))#wil use whenn we want that it should return some erroe instead of -1
print(str.isalnum())#will return true if char are 0-9 , a-z , A-Z
#isalpha will return true only if all char are a-z ,A-Z
print(str.isalpha())
#islower will check if all the char are in lower form or not 
print(str.islower())
#isprintable will return if all char,words are printable and like if it will contain \n then it will give false
print(str.isprintable())
#isspace to check the space in the string 
print(str.isspace())
#istitle will return true if first char of sen is capital
print(str.istitle())
#isupper check for all the uppercase lettern in the given string
print(str.isupper())
#startswith()
print(str.startswith("python"))
#swapcase(): upper to lower and lower to upper it will change
print(str.swapcase())
#title(): will convert all the first letter to the capital letter









