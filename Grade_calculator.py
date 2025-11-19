
#Name: Stephen Hernandez
#Date: 11/18/25
#Assignmnet: extra credit


import json

grades = {}

def add_students():
    name = input("Enter student name: ")
    score = input("Enter score: ")

    try:
        score = int(score)
    except (ValueError, IndexError):
        print("Invalid score")


    grades[name] = score
    print("Student added.")


def list_students():
    if not grades:
        print("No students added.")
        return

    for i, (name, score) in enumerate(grades.items()):
        print(f"{i}. {name} - {score}")
    print()

def calculate_average():
    if not grades:
        print("No grades to calculate.")
        return

    avg = sum(grades.values()) / len(grades)
    print("Average score: {0:.2f}".format(avg))

def highest_lowest_grade():
    if not grades:
        print("No grades to available.")
        return

    highest = max(grades.items(), key=lambda x: x[1])[0]
    lowest = min(grades.items(), key=lambda x: x[1])[0]

    print(f"{highest} - {lowest}")
    print()

def save_to_json ():
        with open("grades.json", "w") as json_file:
            json.dump(grades, json_file)
        print("Grades saved.")

def load_from_json():
    global grades
    try:
        with open("grades.json", "r") as json_file:
            grades = json.load(json_file)
        print("Grades loaded.")
    except FileNotFoundError:
        print("No grades loaded.")




def student_grade():
    if not grades:
        print("No grades added.")
        return

    name = input("Enter student name: ")

    if name in grades:
        print(grades[name])
    else:
        print("Student not found.")


def grade_menu():
    while True:
        print("1. Add students")
        print("2. List students")
        print("3. Grade student")
        print("4. Highest lowest grade")
        print("5.Save grades to JSON")
        print("6.Load grades from JSON")
        print("7.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_students()
        elif choice == "2":
            list_students()
        elif choice == "3":
            student_grade()
        elif choice == "4":
            highest_lowest_grade()
        elif choice == "5":
            save_to_json()
        elif choice == "6":
            load_from_json()
        elif choice == "7":
            exit()
            print("GoodBye!")


            break
        else:
            print("Invalid choice.")



grade_menu()
