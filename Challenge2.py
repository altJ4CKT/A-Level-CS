def askfornum():
    num1 = int(input("Enter an integer that is more than 100"))
    if num1 < 100:
        print("That is not an integer that is more than 100. TRY AGAIN")
        askfornum()
    else:
        print("Great")

    num2 = int(input("Enter an integer that is less than 10 and more than 0"))
    if num2 > 10 or num2 < 0:
        print("Sorry you have selected a number that is less than 0 or more than 10. TRY AGAIN")
        askfornum()
    else:
        print("Great")

    remainder = num1 % num2
    print(f"The remainder of your numbers is {remainder}")
askfornum()