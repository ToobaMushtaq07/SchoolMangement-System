import os

def view_file(filename, title):
    print("\n" + "=" * 40)
    print(title)
    print("=" * 40)

    if not os.path.exists(filename):
        print("No records found.")
        return

    with open(filename, "r") as file:
        data = file.readlines()

    if len(data) == 0:
        print("No records found.")
    else:
        for line in data:
            print(line.strip())


def view_complete_system():
    view_file("students.txt", "STUDENT RECORDS")
    view_file("teachers.txt", "TEACHER RECORDS")
    view_file("classrooms.txt", "CLASSROOM RECORDS")
    view_file("timetable.txt", "TIMETABLE RECORDS")