import os
FILE_NAME = "students.txt"

# Add Student
def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll_no},{name},{age},{department}\n")

    print("Student added successfully!")


# View Students
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No student record found.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if len(data) == 0:
        print("No student record found.")
    else:
        print("\n------ Student Records ------")
        for line in data:
            print(line.strip())


# Search Student
def search_student():
    roll = input("Enter Roll No to search: ")

    if not os.path.exists(FILE_NAME):
        print("No record found.")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.startswith(roll + ","):
                print("\nStudent Found:")
                print(line.strip())
                found = True
                break

    if not found:
        print("Student not found.")


# Delete Student
def delete_student():
    roll = input("Enter Roll No to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No record found.")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    found = False

    with open(FILE_NAME, "w") as file:
        for line in lines:
            if not line.startswith(roll + ","):
                file.write(line)
            else:
                found = True

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found.")