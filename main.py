from package.student import Student
from package.teacher import Teacher
from package.classroom import Classroom
from package.timetable import Timetable
from package.view import View


while True:

    print("\n========== SCHOOL MANAGEMENT SYSTEM ==========")
    print("1. Student")
    print("2. Teacher")
    print("3. Classroom")
    print("4. Timetable")
    print("5. View All Records")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ---------------- STUDENT MENU ---------------- #

    if choice == "1":

        while True:

            print("\n========== STUDENT MENU ==========")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Back")

            student_choice = input("Enter your choice: ")

            if student_choice == "1":

                person_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                age = input("Enter Age: ")
                department = input("Enter Department: ")

                student = Student(person_id, name, age, department)
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
                print("Invalid Choice!")

# ---------------- TEACHER MENU ---------------- #

    elif choice == "2":

        while True:

            print("\n========== TEACHER MENU ==========")
            print("1. Add Teacher")
            print("2. View Teachers")
            print("3. Search Teacher")
            print("4. Delete Teacher")
            print("5. Back")

            teacher_choice = input("Enter your choice: ")

            if teacher_choice == "1":

                person_id = input("Enter Teacher ID: ")
                name = input("Enter Teacher Name: ")
                subject = input("Enter Subject: ")
                qualification = input("Enter Qualification: ")

                teacher = Teacher(person_id, name, subject, qualification)
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
                print("Invalid Choice!")

    # ---------------- CLASSROOM MENU ---------------- #

    elif choice == "3":

        while True:

            print("\n========== CLASSROOM MENU ==========")
            print("1. Add Classroom")
            print("2. View Classrooms")
            print("3. Search Classroom")
            print("4. Delete Classroom")
            print("5. Back")

            classroom_choice = input("Enter your choice: ")

            if classroom_choice == "1":

                room_number = input("Enter Room Number: ")
                class_name = input("Enter Class Name: ")
                capacity = input("Enter Capacity: ")

                classroom = Classroom(room_number, class_name, capacity)
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
                print("Invalid Choice!")   

# ---------------- TIMETABLE MENU ---------------- #

    elif choice == "4":

        while True:

            print("\n========== TIMETABLE MENU ==========")
            print("1. Add Timetable")
            print("2. View Timetable")
            print("3. Search Timetable")
            print("4. Delete Timetable")
            print("5. Back")

            timetable_choice = input("Enter your choice: ")

            if timetable_choice == "1":

                day = input("Enter Day: ")
                subject = input("Enter Subject: ")
                teacher_name = input("Enter Teacher Name: ")
                time = input("Enter Time: ")

                timetable = Timetable(day, subject, teacher_name, time)
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
                print("Invalid Choice!")

    # ---------------- VIEW ALL ---------------- #

    elif choice == "5":

        View.view_all()

    # ---------------- EXIT ---------------- #

    elif choice == "6":

        print("\nThank you for using School Management System.")
        break

    else:
        print("Invalid Choice! Please try again.")                 

                            
