string1 =  "GUVI Geeks Network Private Limited"
string2 =  "GUVI  Private Limited"
# string1 = input("Enter the 1st string : ")
# string2 = input("Enter your 2nd String : ")
new_string = []
x = (string1.split())
y= (string2.split())

for i in x:
    if i in y:
       z= new_string.append(i)
print("The Longest common sub string between strings are:" , new_string)