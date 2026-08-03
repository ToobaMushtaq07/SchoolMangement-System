import os

FILE_NAME = "teachers.txt"


# Add Teacher
def add_teacher():
    teacher_id = input("Enter Teacher ID: ")
    name = input("Enter Teacher Name: ")
    subject = input("Enter Subject: ")
    qualification = input("Enter Qualification: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{teacher_id},{name},{subject},{qualification}\n")

    print("Teacher added successfully!")


# View Teachers
def view_teachers():
    if not os.path.exists(FILE_NAME):
        print("No teacher records found.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if len(data) == 0:
        print("No teacher records found.")
    else:
        print("\n===== Teacher Records =====")
        for line in data:
            print(line.strip())


# Delete Teacher
def delete_teacher():
    teacher_id = input("Enter Teacher ID to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No teacher records found.")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    found = False

    with open(FILE_NAME, "w") as file:
        for line in lines:
            if not line.startswith(teacher_id + ","):
                file.write(line)
            else:
                found = True

    if found:
        print("Teacher deleted successfully!")
    else:
        print("Teacher not found.")