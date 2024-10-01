def askforbill():
    total_bill = float(input("What is the total bill ?\n"))
    total_people = int(input("How many people are there ?\n"))

    price_person = total_bill / total_people
    print(f"The price per person ${price_person:.2f}")
askforbill()