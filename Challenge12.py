first_name = input("Enter your first name: ")
if len(first_name) < 5:
    last_name = input("Enter your last name: ")
    full_name = first_name.upper() + "" + last_name.upper()
    print(full_name)
else:
    print(first_name.lower())