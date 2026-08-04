from package.person import Person
import os


class Teacher(Person):

    FILE_NAME = "data/teacher.txt"

    def __init__(self, person_id, name, subject, qualification):
        super().__init__(person_id, name)
        self.subject = subject
        self.qualification = qualification

    # Add Teacher
    def add_teacher(self):
        try:
            with open(Teacher.FILE_NAME, "a") as file:
                file.write(f"{self.person_id},{self.name},{self.subject},{self.qualification}\n")
            print("Teacher added successfully!")

        except Exception as e:
            print("Error:", e)

    # View Teachers
    def view_teachers():
        try:
            if not os.path.exists(Teacher.FILE_NAME):
                print("No teacher record found.")
                return

            with open(Teacher.FILE_NAME, "r") as file:
                records = file.readlines()

            if len(records) == 0:
                print("No teacher record found.")
                return

            print("\n========== Teacher Records ==========")

            for line in records:
                person_id, name, subject, qualification = line.strip().split(",")

                print(f"Teacher ID    : {person_id}")
                print(f"Name          : {name}")
                print(f"Subject       : {subject}")
                print(f"Qualification : {qualification}")
                print("--------------------------------------")

        except FileNotFoundError:
            print("Teacher file not found.")

        except Exception as e:
            print("Error:", e)

    # Search Teacher
    def search_teacher():

        try:
            search_id = input("Enter Teacher ID: ")

            if not os.path.exists(Teacher.FILE_NAME):
                print("Teacher file not found.")
                return

            found = False

            with open(Teacher.FILE_NAME, "r") as file:

                for line in file:

                    person_id, name, subject, qualification = line.strip().split(",")

                    if person_id == search_id:

                        print("\nTeacher Found")
                        print("-------------------------")
                        print("Teacher ID    :", person_id)
                        print("Name          :", name)
                        print("Subject       :", subject)
                        print("Qualification :", qualification)

                        found = True
                        break

            if not found:
                print("Teacher not found.")

        except Exception as e:
            print("Error:", e)

    # Delete Teacher
    def delete_teacher():

        try:
            delete_id = input("Enter Teacher ID to delete: ")

            if not os.path.exists(Teacher.FILE_NAME):
                print("Teacher file not found.")
                return

            with open(Teacher.FILE_NAME, "r") as file:
                records = file.readlines()

            found = False

            with open(Teacher.FILE_NAME, "w") as file:

                for line in records:

                    person_id = line.strip().split(",")[0]

                    if person_id != delete_id:
                        file.write(line)
                    else:
                        found = True

            if found:
                print("Teacher deleted successfully!")

            else:
                print("Teacher not found.")

        except Exception as e:
            print("Error:", e)