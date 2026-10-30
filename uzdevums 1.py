positive = 0
negative = 0
zero = 0

for i in range(10):
    num = int(input("Ievadi skaitli: "))

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

    print("Pozitīvie skaitļi:", positive)
    print("Negatīvie skaitļi:", negative)
    print("Nulles:", zero)