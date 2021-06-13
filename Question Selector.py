import math

def part_one():
    A =(ID[0] - ID[1])
    for x in range(5):
        A=math.sqrt(A)
    return int(A)

def part_two(flag):
    if flag == 0:
        B = (ID[2] - ID[1])
        for x in range(3):
            B = math.sqrt(B) + 4
    else:
        B = (ID[2] - ID[0])
        for x in range(3):
            B = math.sqrt(B) + 5
    return int(B)

def part_three(flag):
    if flag == 0:
        C = (ID[0] - ID[3])
        for x in range(3):
            C = math.sqrt(C) + 10
    else:
        C = (ID[2] - ID[3])
        for x in range(3):
            C = math.sqrt(C) + 11
    return int(C)

def part_four():
    D = (ID[0] + ID[1] + ID[2] - ID[3]) / (ID[0] - ID[1] + ID[2] - ID[3])-0.95
    return int(D*D)

def f(x):
    if x == "1":
        print(part_one())
    elif x == "2":
        flag = 0
        for i in range(2):
            print(part_two(flag))
            flag = 1
    elif x == "3":
        flag = 0
        for i in range(2):
            print(part_three(flag))
            flag = 1
    elif x == "4":
        print(part_four())


ID=[320734304,320467335,323274787,208209817]
x = input("Enter the number of the part you want to know the questions you need to do: \n1 for Part A, 2 for Part B , 3 for Part C , 4 for Part D?\nChoice: ")
f(x)