import os
FILE_NAME = "timetable.txt"

# Add Timetable
def add_timetable():
    class_name = input("Enter Class Name: ")
    day = input("Enter Day: ")
    subject = input("Enter Subject: ")
    teacher = input("Enter Teacher Name: ")
    time = input("Enter Time: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{class_name},{day},{subject},{teacher},{time}\n")

    print("Timetable added successfully!")


# View Timetable
def view_timetable():
    if not os.path.exists(FILE_NAME):
        print("No timetable records found.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if len(data) == 0:
        print("No timetable records found.")
    else:
        print("\n===== Timetable Records =====")
        for line in data:
            print(line.strip())


# Delete Timetable
def delete_timetable():
    class_name = input("Enter Class Name to delete timetable: ")

    if not os.path.exists(FILE_NAME):
        print("No timetable records found.")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    found = False

    with open(FILE_NAME, "w") as file:
        for line in lines:
            if not line.startswith(class_name + ","):
                file.write(line)
            else:
                found = True

    if found:
        print("Timetable deleted successfully!")
    else:
        print("Timetable not found.")