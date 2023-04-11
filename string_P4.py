# program to check given character is vowel or consonant.

vowel = {"a","e","i","o","u"}
char = input("Enter a character : ")

for i in char:
    if i != vowel:
        print(char, "is consonant")
    else:
        print(char, "is vowel")


