for i in range(100):
    number = 100-i
    divisibleBy5 = number%5==0
    divisibleBy3 = number%3==0
    if divisibleBy3 and divisibleBy5:
        print("Testing")
    elif divisibleBy3:
        print("Software")
    elif divisibleBy5:
        print("Agile")
    else:
        print(number)