import os

FILE_NAME = "classrooms.txt"


# Add Classroom
def add_classroom():
    room_no = input("Enter Classroom Number: ")
    class_name = input("Enter Class Name: ")
    capacity = input("Enter Capacity: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{room_no},{class_name},{capacity}\n")

    print("Classroom added successfully!")


# View Classrooms
def view_classrooms():
    if not os.path.exists(FILE_NAME):
        print("No classroom records found.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if len(data) == 0:
        print("No classroom records found.")
    else:
        print("\n===== Classroom Records =====")
        for line in data:
            print(line.strip())


# Delete Classroom
def delete_classroom():
    room_no = input("Enter Classroom Number to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No classroom records found.")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    found = False

    with open(FILE_NAME, "w") as file:
        for line in lines:
            if not line.startswith(room_no + ","):
                file.write(line)
            else:
                found = True

    if found:
        print("Classroom deleted successfully!")
    else:
        print("Classroom not found.")