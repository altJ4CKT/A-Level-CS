def program():  
    def days_converter(days):   
        total_seconds = days * 24 * 60 * 60
        hours = total_seconds / 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        return hours, minutes, seconds

    days_input = float(input("How many days would you like to convert ?\n"))
    hours, minutes, seconds = days_converter(days_input)
    print(f"{hours} hours, {minutes} minutes and {seconds:.3f} seconds")
    exit_input = str(input("Type yes if you want to exit the program:\n"))
    if exit_input == "yes":
        exit()    
    elif exit_input != "yes":
        program()
program()