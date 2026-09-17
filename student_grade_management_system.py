students = {}

def add_student():
    name = input("Enter the Student Name: ")
    grade = input("Enter the Student Grade: ")
    students[name] = grade
    print("Student Successfully Added")

def update_grade():
    name = input("Enter Student Name: ")
    if name in students:
        grade = input("Enter New Grade: 3")
        students[name] = grade
        print("Grade successfully Updated")
    else :
        print("Student Not Found")

def view_students():
    if not students:
        print("There is No Student")
    else:
        for name,grade in students.items():
            print(f"Name: {name} | Grade: {grade}") 

def find_student():
    name = input("Enter Student Name: ")
    if name in students:
        print(f"{name}'s Grade: {students[name]}")
    else:
        print("Student Not Found")

def delete_student():
    name = input("Enter Student Name: ")
    if name in students:
        del students[name]
        print("Student Successfully Deleted")
    else:
        print("Student Not Found")




while True:
    print("enter the Choise\n 1. Add Student\n 2. Update Grade\n 3. View Students\n 4. Find Student\n 5. Delete Student")
    choise = input("Enter the Choise: ")
    if choise == "1":
        add_student()
    elif choise == "2":
        update_grade()
    elif choise == "3":
        view_students()
    elif choise == "4":
        find_student()
    elif choise == "5":
        delete_student()
    else:
        print("Choise Not found")