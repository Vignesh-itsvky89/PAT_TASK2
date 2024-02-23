# string1 =  "GUVIGeeksNetworkPrivateLimited"
string1 = input("Enter the  String to find most frequent characters in it: ")

new_String = {}
for string in string1: 
    if string not in new_String: 
        new_String[string] = 1
    else:
        new_String[string]= new_String[string]+1

print(new_String)
print("Most frequent string is :", max(new_String, key=new_String.get))


most_frequent = max(set(string1), key = string1.count)
print('The most frequent character is, ', most_frequent)