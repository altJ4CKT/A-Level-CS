print("1) Square\n2) Triangle\n")
usr_input = int(input("Enter a number: "))

if usr_input == 1:
    usr_input = int(input("Enter the length of a side: "))
    area = usr_input ** 2   
    print(f"The area of the square is {area}")
elif usr_input == 2:
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area}")
else:
    print("Invalid input")