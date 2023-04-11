# program to remove given character from String.


str = input("Enter a string :  ")
print("string is ", str)
rstr = input("Enter char to remove from string:  ")
print("Remove char from string is ", rstr)

str1 = str.replace(rstr,"")
print(str1)