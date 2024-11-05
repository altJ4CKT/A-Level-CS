usr_input = input("Is it raining? (yes/no): ")
usr_input = usr_input.lower()
print(usr_input)
if usr_input == "yes":
    usr_input2 = input("Is it windy? (yes/no): ")
    usr_input2 = usr_input2.lower()
    print(usr_input2)
    if usr_input2 == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
