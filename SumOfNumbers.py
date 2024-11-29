#first program:


# n = int(input("Enter a number you want the sum of the previous numbers: "))
# sum = n * (n + 1) / 2  #Guassian sum formula
# print(f"The sum of the numbers from 1 to {n} is {sum}")

#second program:

# Nlist = []
# sum = 0
# n = int(input("Enter a number: "))
# for i in range(n):
#     if i % 3 == 0 or i % 5 == 0:
#         Nlist.append(i)
#         sum += i

# print(f"The sum of the numbers that are multiples of 3 and 5 are up to {n} are: {sum}"

#third program:

def calculate_sum(n):
    sum = n * (n + 1) / 2
    return sum

def calculate_product(n):
    product = n
    if n < 2:
        product = 1
        return product
    else:
        while n > 1:
            product = product * (n - 1)
            n -= 1
        return product

def menu():
    calculation = False
    while calculation == False:
        n = int(input("Enter a number: "))
        usr_input = input(f"Do you want to display the result of the sum or the product from 1 to {n} ?\n 1. Sum 2. Product: ")
        if usr_input == "1":
            print(f"The sum of 1 to your number, {n}, is equal to {calculate_sum(n)}")
        elif usr_input == "2":
            print(f"The product of 1 to your number, {n}, is equal to {calculate_product(n)}")

menu()

#fourth program:

# def multiplicationTable():
#     for i in range(1, 13):
#         for j in range(1, 13):
#             print(i * j, end="\t")
#         print()

# multiplicationTable()
