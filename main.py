from student import *
from teacher import *
from classroom import *
from timetable import *
from view import *


while True:
    print("\n========== SCHOOL MANAGEMENT SYSTEM ==========")
    print("1. Student Menu")
    print("2. Teacher Menu")
    print("3. Classroom Menu")
    print("4. Timetable Menu")
    print("5. View Complete System")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Student Menu
    if choice == "1":
        while True:
            print("\n----- Student Menu -----")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Back")

            student_choice = input("Enter your choice: ")

            if student_choice == "1":
                add_student()
            elif student_choice == "2":
                view_students()
            elif student_choice == "3":
                search_student()
            elif student_choice == "4":
                delete_student()
            elif student_choice == "5":
                break
            else:
                print("Invalid Choice!")

    # Teacher Menu
    elif choice == "2":
        while True:
            print("\n----- Teacher Menu -----")
            print("1. Add Teacher")
            print("2. View Teachers")
            print("3. Delete Teacher")
            print("4. Back")

            teacher_choice = input("Enter your choice: ")

            if teacher_choice == "1":
                add_teacher()
            elif teacher_choice == "2":
                view_teachers()
            elif teacher_choice == "3":
                delete_teacher()
            elif teacher_choice == "4":
                break
            else:
                print("Invalid Choice!")

    # Classroom Menu
    elif choice == "3":
        while True:
            print("\n----- Classroom Menu -----")
            print("1. Add Classroom")
            print("2. View Classrooms")
            print("3. Delete Classroom")
            print("4. Back")

            classroom_choice = input("Enter your choice: ")

            if classroom_choice == "1":
                add_classroom()
            elif classroom_choice == "2":
                view_classrooms()
            elif classroom_choice == "3":
                delete_classroom()
            elif classroom_choice == "4":
                break
            else:
                print("Invalid Choice!")

    # Timetable Menu
    elif choice == "4":
        while True:
            print("\n----- Timetable Menu -----")
            print("1. Add Timetable")
            print("2. View Timetable")
            print("3. Delete Timetable")
            print("4. Back")

            timetable_choice = input("Enter your choice: ")

            if timetable_choice == "1":
                add_timetable()
            elif timetable_choice == "2":
                view_timetable()
            elif timetable_choice == "3":
                delete_timetable()
            elif timetable_choice == "4":
                break
            else:
                print("Invalid Choice!")

    # View Complete System
    elif choice == "5":
        view_complete_system()

    # Exit
    elif choice == "6":
        print("Thank you for using the School Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")