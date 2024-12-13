list = [1, 3, 13, 344, 45, 67, 567, 523, 9, 98]
def max_list(listToCheck):
    max_list = max(listToCheck)
    print(f"The maximum number in the list is {max_list}")

max_list(list)

def reverse_list(listToReverse):
    lst = listToReverse
    reversed_list = lst[::-1]  
    print(f"The reversed list is {reversed_list}")

reverse_list(list)

def in_list(listToCheck):
    lst = listToCheck
    n = int(input("Enter a number: "))
    if n in lst:
        print(f"{n} is in the list")
    else:
        print(f"{n} is not in the list")

in_list(list)

def count_element(listToCheck):
    lst = listToCheck
    n = int(input("Enter a number to count: "))
    count = lst.count(n)
    print(f"{n} appears {count} times in the list")