def program():
    def decimal_to_binary(denary):
        binary = ''
        while denary > 0:
            binary = str(denary % 2) + binary
            denary = denary // 2
        return binary

    def binary_to_decimal(binary_str):
        if not isinstance(binary_str, str):
            raise ValueError("Input must be a string representing a binary number.")
    
        if not all(digit in '01' for digit in binary_str):
            raise ValueError("Input string must only contain binary digits (0 and 1).")
    
        decimal_value = 0
        for index, digit in enumerate(binary_str[::-1]):
            decimal_value += int(digit) * (2 ** index)
        return decimal_value

    while True:
        user_input = input("Choose 1, 2 or 3:\n1) Convert decimal to binary\n2)convert binary to decimal\n3) exit\n")
        
        if user_input == "1":
            number = int(input("Choose an integer to convert to binary: "))
            binary_number = decimal_to_binary(number)
            print(f"The binary representation of {number} is {binary_number}")
        elif user_input == "2":
            number = input("Choose a binary number to conver to a decimal: ")
            decimal_number = binary_to_decimal(number)
            print(f"The decimal representation of {number} is {decimal_number}")
        elif user_input == "3":
            exit()
program()


