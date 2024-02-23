# This program is to create a pyramid of numbers from 1 to 20 using For loop

for i in range(1,20):
    for j in range (20 - i):
        print(" ", end= " ")
    for j in range(1, i  ):
        print(j, end=" ")
    for i in range(i, 0, -1):
        print(i, end= " ")

    print ("\n") 