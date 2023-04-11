# Program to check a String is palindrome or not

str = input("Enter a string : ")
print(str)
str1 = str[::-1]
print(str1)

if str ==str1:
    print(str, "is a palindrome word")
else:
    print(str, "is not a palindrome word")