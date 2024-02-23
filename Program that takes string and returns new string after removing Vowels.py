# string =  "GUVI Geeks Network Private Limited" 
string = input("Enter your Sring for which Vowels to be removed: ")
New_String = ""
vowels = {"a","e","i","o","u", "A", "E", "I", "O", "U"}
for i in range(len(string)):
    if string[i] not in vowels:
       New_String=New_String+string[i]
print("The new string after removing Vowels is: ", New_String)
       

