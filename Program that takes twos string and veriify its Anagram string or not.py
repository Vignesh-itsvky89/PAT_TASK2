string1 = input("Enter the  1st String to verify it, whether is Anagram string or not: ")
string2 = input("Enter the  2nd String to verify it, whether is Anagram string or not: ")


#string1 = "listen"
#string2 = "silent"

x= sorted(string1)
y = sorted(string2)
if x == y:
    print("The given string is Anagram")
else:
    print("The given string is not Anagram")