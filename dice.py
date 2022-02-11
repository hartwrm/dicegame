import random

print("Roll the dice? y/n")
x = input()
while x == "y":
    numbers = random.randint(1,6)
    print(numbers)

    if numbers == 1:
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------")
    if numbers == 2:
        print("-----------")
        print("|         |")
        print("|  0   0  |")
        print("|         |")
        print("-----------")
    if numbers == 3:
        print("-----------")
        print("| 0       |")
        print("|    0    |")
        print("|       0 |")
        print("-----------")
    if numbers == 4:
        print("-----------")
        print("|  0    0 |")
        print("|         |")
        print("|  0    0 |")
        print("-----------")
    if numbers == 5:
        print("-----------")
        print("|  0    0 |")
        print("|    0   |")
        print("|  0    0 |")
        print("-----------")
    if numbers == 6:
        print("-----------")
        print("|  0    0 |")
        print("|  0    0 |")
        print("|  0    0 |")
        print("-----------")
    # print("roll again? y/n")
    x = input("roll again? y/n\n")

else: print("goodbye")
