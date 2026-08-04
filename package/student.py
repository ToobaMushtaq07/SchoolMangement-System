from package.person import Person
import os

class Student(Person):

    FILE_NAME = "student.txt"

    def __init__(self, person_id, name, age, department):
        super().__init__(person_id, name)
        self.age = age
        self.department = department

    # Add Student
    def add_student(self):
        try:
            with open(Student.FILE_NAME, "a") as file:
                file.write(f"{self.person_id},{self.name},{self.age},{self.department}\n")
            print("Student added successfully!")

        except Exception as e:
            print("Error:", e)

    # View Students
    def view_students(self):
        try:
            if not os.path.exists(Student.FILE_NAME):
                print("No student record found.")
                return

            with open(Student.FILE_NAME, "r") as file:
                records = file.readlines()

            if len(records) == 0:
                print("No student record found.")
                return

            print("\n========== Student Records ==========")

            for line in records:
                person_id, name, age, department = line.strip().split(",")

                print(f"Student ID : {person_id}")
                print(f"Name       : {name}")
                print(f"Age        : {age}")
                print(f"Department : {department}")
                print("-------------------------------------")

        except FileNotFoundError:
            print("Student file not found.")

        except Exception as e:
            print("Error:", e)

    # Search Student
    def search_student(self):

        try:
            search_id = input("Enter Student ID: ")

            if not os.path.exists(Student.FILE_NAME):
                print("Student file not found.")
                return

            found = False

            with open(Student.FILE_NAME, "r") as file:

                for line in file:

                    person_id, name, age, department = line.strip().split(",")

                    if person_id == search_id:

                        print("\nStudent Found")
                        print("----------------------")
                        print("Student ID :", person_id)
                        print("Name       :", name)
                        print("Age        :", age)
                        print("Department :", department)

                        found = True
                        break

            if not found:
                print("Student not found.")

        except Exception as e:
            print("Error:", e)

    # Delete Student
    def delete_student(self):

        try:
            delete_id = input("Enter Student ID to delete: ")

            if not os.path.exists(Student.FILE_NAME):
                print("Student file not found.")
                return

            with open(Student.FILE_NAME, "r") as file:
                records = file.readlines()

            found = False

            with open(Student.FILE_NAME, "w") as file:

                for line in records:

                    person_id = line.strip().split(",")[0]

                    if person_id != delete_id:
                        file.write(line)
                    else:
                        found = True

            if found:
                print("Student deleted successfully!")

            else:
                print("Student not found.")

        except Exception as e:
            print("Error:", e)