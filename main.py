import os
import psycopg2

from package.student import Student
from package.teacher import Teacher
from package.classroom import Classroom
from package.timetable import Timetable
from package.view import View
from package.db import get_connection


def get_unique_integer_id(table_name, id_column, id_label):
    while True:
        entered_id = input(f"Enter {id_label}: ").strip()

        try:
            new_id = int(entered_id)
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        if new_id <= 0:
            print("ID must be greater than 0.")
            continue

        conn = get_connection()
        if conn is None:
            continue

        cursor = conn.cursor()

        try:
            cursor.execute(
                f"SELECT * FROM {table_name} WHERE {id_column} = %s",
                (new_id,)
            )
            result = cursor.fetchone()

            if result:
                print(f"{id_label} {new_id} already exists!")
                continue

            return new_id

        except Exception as e:
            print("Error:", e)
            continue

        finally:
            cursor.close()
            conn.close()


def get_positive_integer(prompt, field_name):
    while True:
        entered_value = input(prompt).strip()

        try:
            value = int(entered_value)
        except ValueError:
            print(f"Invalid input! Please enter an integer for {field_name}.")
            continue

        if value <= 0:
            print(f"{field_name} must be greater than 0.")
            continue

        return str(value)


# MAIN PROGRAM
while True:

    print("\n========== SCHOOL MANAGEMENT SYSTEM ==========")
    print("1. Student")
    print("2. Teacher")
    print("3. Classroom")
    print("4. Timetable")
    print("5. View All Records")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    # STUDENT MENU
    if choice == "1":

        while True:

            print("\n========== STUDENT MENU ==========")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Back")

            student_choice = input("Enter your choice: ").strip()

            if student_choice == "1":

                person_id = get_unique_integer_id("student", "person_id", "Student ID")
                name = input("Enter Student Name: ").strip()
                age = get_positive_integer("Enter Age: ", "Age")
                department = input("Enter Department: ").strip()

                student = Student(person_id, name, age, department)
                student.add_student()

            elif student_choice == "2":
                Student("", "", "", "").view_students()

            elif student_choice == "3":
                Student("", "", "", "").search_student()

            elif student_choice == "4":
                Student("", "", "", "").delete_student()

            elif student_choice == "5":
                break

            else:
                print("Invalid choice!")

    # TEACHER MENU
    elif choice == "2":

        while True:

            print("\n========== TEACHER MENU ==========")
            print("1. Add Teacher")
            print("2. View Teachers")
            print("3. Search Teacher")
            print("4. Delete Teacher")
            print("5. Back")

            teacher_choice = input("Enter your choice: ").strip()

            if teacher_choice == "1":

                person_id = get_unique_integer_id("teacher", "person_id", "Teacher ID")
                name = input("Enter Teacher Name: ").strip()
                subject = input("Enter Subject: ").strip()
                qualification = input("Enter Qualification: ").strip()

                teacher = Teacher(person_id, name, subject, qualification)
                teacher.add_teacher()

            elif teacher_choice == "2":
                Teacher("", "", "", "").view_teachers()

            elif teacher_choice == "3":
                Teacher("", "", "", "").search_teacher()

            elif teacher_choice == "4":
                Teacher("", "", "", "").delete_teacher()

            elif teacher_choice == "5":
                break

            else:
                print("Invalid choice!")

    # CLASSROOM MENU
    elif choice == "3":

        while True:

            print("\n========== CLASSROOM MENU ==========")
            print("1. Add Classroom")
            print("2. View Classrooms")
            print("3. Search Classroom")
            print("4. Delete Classroom")
            print("5. Back")

            classroom_choice = input("Enter your choice: ").strip()

            if classroom_choice == "1":

                room_number = get_unique_integer_id("classroom", "room_number", "Room Number")
                class_name = input("Enter Class Name: ").strip()
                capacity = get_positive_integer("Enter Capacity: ", "Capacity")

                classroom = Classroom(room_number, class_name, capacity)
                classroom.add_classroom()

            elif classroom_choice == "2":
                Classroom("", "", "").view_classrooms()

            elif classroom_choice == "3":
                Classroom("", "", "").search_classroom()

            elif classroom_choice == "4":
                Classroom("", "", "").delete_classroom()

            elif classroom_choice == "5":
                break

            else:
                print("Invalid choice!")

    # TIMETABLE MENU
    elif choice == "4":

        while True:

            print("\n========== TIMETABLE MENU ==========")
            print("1. Add Timetable")
            print("2. View Timetable")
            print("3. Search Timetable")
            print("4. Delete Timetable")
            print("5. Back")

            timetable_choice = input("Enter your choice: ").strip()

            if timetable_choice == "1":

                day = input("Enter Day: ").strip()
                subject = input("Enter Subject: ").strip()
                teacher_name = input("Enter Teacher Name: ").strip()
                time = input("Enter Time: ").strip()

                timetable = Timetable(day, subject, teacher_name, time)
                timetable.add_timetable()

            elif timetable_choice == "2":
                Timetable("", "", "", "").view_timetable()

            elif timetable_choice == "3":
                Timetable("", "", "", "").search_timetable()

            elif timetable_choice == "4":
                Timetable("", "", "", "").delete_timetable()

            elif timetable_choice == "5":
                break

            else:
                print("Invalid choice!")

    # VIEW ALL
    elif choice == "5":
        View().view_all()

    # EXIT
    elif choice == "6":
        print("\nThank you for using School Management System.")
        break

    else:
        print("Invalid choice!")