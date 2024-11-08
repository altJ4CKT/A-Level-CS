Number = False

def Challenge8():
    global Number
    usr_input = int(input("Enter a number between 10 and 20 (inclusive): "))
    if usr_input >= 10 and usr_input <= 20:
        print("Correct")
        Number = True
    else:
        print("Incorrect")
        Number = False

while Number == False:
    Challenge8()