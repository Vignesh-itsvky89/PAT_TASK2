#Program to calculate  number of Vowels in the given string
string = "GUVI Geeks Network Private Limited"
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
vowels1 = {"a", "A"}
vowels2 = {"e", "E"}
vowels3 = {"i", "I"}
vowels4 = {"o", "O"}
vowels5 = {"u", "U"}
for letter in string:
    if letter in vowels1:
        count1 =  count1 + 1 
for letter in string:
    if letter in vowels2:
        count2 =  count2 + 1 
for letter in string:
    if letter in vowels3:
        count3 =  count3 + 1 
for letter in string:
    if letter in vowels4:
        count4 =  count4 + 1 
for letter in string:
    if letter in vowels5:
        count5 =  count5 + 1 
print("Count of the vowels a is:", count1)
print("Count of the vowels e is:", count2)
print("Count of the vowels i is:", count3)
print("Count of the vowels o is:", count4)
print("Count of the vowels u is:", count5)
print(len(string))
