import os

from package.student import Student
from package.teacher import Teacher
from package.classroom import Classroom
from package.timetable import Timetable
from package.view import View


# VALIDATION FUNCTIONS
def get_unique_integer_id(file_name, id_label):
    """
    Gets a positive integer ID and checks whether it already
    exists in the specified file.

    IDs such as 1, 01 and 001 are considered the same.
    """

    while True:
        entered_id = input(f"Enter {id_label}: ").strip()

        # Check that the entered ID is an integer
        try:
            new_id = int(entered_id)
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        # Do not allow zero or negative IDs
        if new_id <= 0:
            print("Invalid input! ID must be greater than 0.")
            continue

        duplicate_found = False

        # Check for a duplicate ID
        if os.path.exists(file_name):

            try:
                with open(file_name, "r") as file:

                    for line in file:

                        if not line.strip():
                            continue

                        existing_id = line.strip().split(",", 1)[0]

                        try:
                            existing_id = int(existing_id)
                        except ValueError:
                            # Ignore old records containing invalid IDs
                            continue

                        if existing_id == new_id:
                            duplicate_found = True
                            break

            except OSError as error:
                print("Error while reading the file:", error)
                continue

        if duplicate_found:
            print(
                f"{id_label} {new_id} already exists! "
                "Please enter another ID."
            )
            continue

        # Convert it back to a string for writing to the text file
        return str(new_id)


def get_positive_integer(prompt, field_name):
    """Gets a positive integer for age, capacity, etc."""

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

                person_id = get_unique_integer_id(
                    Student.FILE_NAME,
                    "Student ID"
                )

                name = input("Enter Student Name: ").strip()

                age = get_positive_integer(
                    "Enter Age: ",
                    "Age"
                )

                department = input("Enter Department: ").strip()

                student = Student(
                    person_id,
                    name,
                    age,
                    department
                )

                student.add_student()

            elif student_choice == "2":

                student = Student("", "", "", "")
                student.view_students()

            elif student_choice == "3":

                student = Student("", "", "", "")
                student.search_student()

            elif student_choice == "4":

                student = Student("", "", "", "")
                student.delete_student()

            elif student_choice == "5":
                break

            else:
                print("Invalid choice! Please enter a number from 1 to 5.")

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

                person_id = get_unique_integer_id(
                    Teacher.FILE_NAME,
                    "Teacher ID"
                )

                name = input("Enter Teacher Name: ").strip()
                subject = input("Enter Subject: ").strip()
                qualification = input("Enter Qualification: ").strip()

                teacher = Teacher(
                    person_id,
                    name,
                    subject,
                    qualification
                )

                teacher.add_teacher()

            elif teacher_choice == "2":

                teacher = Teacher("", "", "", "")
                teacher.view_teachers()

            elif teacher_choice == "3":

                teacher = Teacher("", "", "", "")
                teacher.search_teacher()

            elif teacher_choice == "4":

                teacher = Teacher("", "", "", "")
                teacher.delete_teacher()

            elif teacher_choice == "5":
                break

            else:
                print("Invalid choice! Please enter a number from 1 to 5.")

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

                room_number = get_unique_integer_id(
                    Classroom.FILE_NAME,
                    "Room Number"
                )

                class_name = input("Enter Class Name: ").strip()

                capacity = get_positive_integer(
                    "Enter Capacity: ",
                    "Capacity"
                )

                classroom = Classroom(
                    room_number,
                    class_name,
                    capacity
                )

                classroom.add_classroom()

            elif classroom_choice == "2":

                classroom = Classroom("", "", "")
                classroom.view_classrooms()

            elif classroom_choice == "3":

                classroom = Classroom("", "", "")
                classroom.search_classroom()

            elif classroom_choice == "4":

                classroom = Classroom("", "", "")
                classroom.delete_classroom()

            elif classroom_choice == "5":
                break

            else:
                print("Invalid choice! Please enter a number from 1 to 5.")

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

                timetable = Timetable(
                    day,
                    subject,
                    teacher_name,
                    time
                )

                timetable.add_timetable()

            elif timetable_choice == "2":

                timetable = Timetable("", "", "", "")
                timetable.view_timetable()

            elif timetable_choice == "3":

                timetable = Timetable("", "", "", "")
                timetable.search_timetable()

            elif timetable_choice == "4":

                timetable = Timetable("", "", "", "")
                timetable.delete_timetable()

            elif timetable_choice == "5":
                break

            else:
                print("Invalid choice! Please enter a number from 1 to 5.")

# VIEW ALL

    elif choice == "5":

        View().view_all()

# EXIT 

    elif choice == "6":

        print("\nThank you for using School Management System.")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")