string = input("Enter the  String to verify it, whether is Palindrome or not (Full upper case or Lower case letters): ")
# Eg: string = "MALAYALAM"
if string == (string[::-1]):
    print ("Given string is palidrome:", string)
else:
    print ("Given string is not palidrome:", string)

