def program(): 
    num1 = int(input("Enter a number: 1, 2, 3")) 

    if num1 == 1: 
        print("Thank you") 
    elif num1 == 2: 
        print("Well done") 
    elif num1 == 3: 
        print("Correct") 
    else: 
        print("Error: you have selected a number that is not 1, 2 or 3") 
        program() 
program() 