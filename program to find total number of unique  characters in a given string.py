#string =  "GUVI Geeks Network Private Limited"
string = input("Enter your String to return unique characters in it: ")
New_String = ""
count = 0
for i in string:
    if i not in New_String:
        New_String=New_String+i
print("Number of unique characters in a string:", len(New_String))
