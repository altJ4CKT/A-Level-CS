students = {

}


def num_of_students():
    num_students = int(input("Enter number of students: "))
    if num_students <= 0:
        print("That's not possible. Try again.")
        num_of_students()

    for i in range(num_students):
        name = input("Enter name: ")
        student_id = input("Enter id: ")
        students[student_id] = {"name":name}
        print(f"Student ID: {student_id}, Name: {name}")

    menu()


def add_details():
    student_id = input("Enter id: ")
    date_of_birth = input("Enter date of birth: ")
    email = input("Enter email: ")
    students[student_id] = {"name": students[student_id]["name"], "email": email, "date_of_birth": date_of_birth}
    print(f"Student ID: {student_id}, Name: {students[student_id]['name']}, Email: {students[student_id]['email']}, "
          f"date of birth: {students[student_id]['date_of_birth']}")

    menu()


def view_student_data():
    student_id = input("Enter id: ")
    print(f"Student ID: {student_id}, Name: {students[student_id]['name']}, Email: {students[student_id]['email']}, date of birth: {students[student_id]['date_of_birth']} ")


def menu():
    menu_input = input("1) Add students\n2) Add student details\n3) View student data\n4)Exit\n")
    if menu_input == "1":
        num_of_students()
    elif menu_input == "2":
        add_details()
    elif menu_input == "3":
        view_student_data()


num_of_students()