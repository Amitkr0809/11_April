# Program to count occurrence of a given characters in string.

str = input("enter a string : ")

"""count = 0
for i in str:
    count= count+1

print(count)"""

char = input("enter char : ")
count = 0
for i in str:
    if i == char:
        count = count+1
print(count)
