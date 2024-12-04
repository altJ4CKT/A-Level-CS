def leapYr(yr):
    if yr % 4 == 0:
        if yr % 100 != 0:
            print(f"{yr} is a leap year")
    else:
        return False

usr_input = int(input("Print next 20 leap years (1) or check if a year is a leap year (2): "))
if usr_input == 1:
    for i in range (2024, 2105):
        leapYr(i)
elif usr_input == 2:
    yr = int(input("Enter a year: "))
    leapYr(yr)

