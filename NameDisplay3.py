usr_input = input("Enter your name: ")
n = int(input("How many times do you want to display your name? "))
for i in range(n):
    for j in range(len(usr_input)):
        print(usr_input[j])