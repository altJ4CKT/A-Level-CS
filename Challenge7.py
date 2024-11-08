Number = False

def Challenge7(): 
    global Number  
    usr_input = int(input("Enter a number between 10 and 20: "))
    if usr_input < 10:
        print("Too low")
        Number = False
    elif usr_input > 10 and usr_input < 20:
        print("Correct")
        Number = True
    elif usr_input > 20:
        print("Too high")
        Number = False
    
while Number == False:
    Challenge7()