def countdown_from(n):
    for i in range(n):
        number = n - i
        divisible_by_5 = number % 5 == 0
        divisible_by_3 = number % 3 == 0
        if divisible_by_3 and divisible_by_5:
            print("Testing")
        elif divisible_by_3:
            print("Software")
        elif divisible_by_5:
            print("Agile")
        else:
            print(number)


countdown_from(100)
