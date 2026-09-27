# Student Management System - Fatima Zahra
students = []

def add_student():
    name = input("Name: ")
    grade = input("Grade: ")
    students.append(name + " - " + grade)
    print("Added!")

def show():
    for s in students:
        print(s)

while True:
    print("1.Add 2.Show 3.Exit")
    x = input("Choose: ")
    if x == "1": add_student()
    elif x == "2": show()
    else: break
