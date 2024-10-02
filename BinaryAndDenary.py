def binarytodecimal():

    binary = input("Enter an 8 bit binary number: ")
    if len(binary) != 8:
        print("Sorry but you entered a number that is more or less than 8 bits")
        return
    elif len(binary) == 8:
        deca = int(binary[0]) * 128
        decb = int(binary[1]) * 64
        decc = int(binary[2]) * 32
        decd = int(binary[3]) * 16
        dece = int(binary[4]) * 8
        decf = int(binary[5]) * 4
        decg = int(binary[6]) * 2
        dech = int(binary[7]) * 1

        dec_value = deca + decb + decc + decd + dece + decf + decg + dech
        print(dec_value)
        menu()

def decimaltobinary():

    decimal = int(input("Enter a decimal number that is more than 0 and less than or equal to 255: "))
    if decimal < 0 or decimal >= 256:
        print("Sorry, you have entered a number that is either too small or large for this program. Try again.")
        return
    else:
        original_decimal = decimal
        binary_str = ""

        for value in [128, 64, 32, 16, 8, 4, 2, 1]:
            if decimal >= value:
                binary_str += "1"
                decimal -= value
            elif decimal < value:
                binary_str += "0"
        print(f"The binary value of {original_decimal} is: {binary_str}")
    

def menu():
    user_input = str(input("Choose 1, 2 or 3:\n1) convert binary to decimal\n2) convert decimal to binary\n3) exit program\n"))
    if user_input == "1":
        binarytodecimal()
    elif user_input == "2":
        decimaltobinary()
    elif user_input == "3":
        exit()
    else:
        print("You have not selected 1, 2 or 3. Choose again:")
        menu()

menu()