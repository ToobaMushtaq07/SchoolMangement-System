import os


class Timetable:

    FILE_NAME = "data/timetable.txt"

    def __init__(self, day, subject, teacher_name, time):
        self.day = day
        self.subject = subject
        self.teacher_name = teacher_name
        self.time = time

    # Add Timetable
    def add_timetable(self):
        try:
            with open(Timetable.FILE_NAME, "a") as file:
                file.write(f"{self.day},{self.subject},{self.teacher_name},{self.time}\n")

            print("Timetable added successfully!")

        except Exception as e:
            print("Error:", e)

    # View Timetable
    def view_timetable(self):

        try:

            if not os.path.exists(Timetable.FILE_NAME):
                print("No timetable record found.")
                return

            with open(Timetable.FILE_NAME, "r") as file:
                records = file.readlines()

            valid_records = []

            for line in records:
                stripped = line.strip()
                if not stripped:
                    continue  # Skip empty lines
                parts = stripped.split(",")
                if len(parts) == 4:
                    valid_records.append(parts)

            if len(valid_records) == 0:
                print("No timetable record found.")
                return

            print("\n========== Timetable Records ==========")

            for day, subject, teacher_name, time in valid_records:
                print(f"Day     : {day}")
                print(f"Subject : {subject}")
                print(f"Teacher : {teacher_name}")
                print(f"Time    : {time}")
                print("-----------------------------------")

        except FileNotFoundError:
            print("Timetable file not found.")

        except Exception as e:
            print("Error:", e)

    # Search Timetable
    def search_timetable(self):

        try:

            search_day = input("Enter Day: ").strip()

            if not os.path.exists(Timetable.FILE_NAME):
                print("Timetable file not found.")
                return

            found = False

            with open(Timetable.FILE_NAME, "r") as file:

                for line in file:
                    stripped = line.strip()
                    if not stripped:
                        continue  # Skip empty lines
                    parts = stripped.split(",")
                    if len(parts) != 4:
                        continue  # Skip corrupted lines
                    day, subject, teacher_name, time = parts

                    if day.lower() == search_day.lower():

                        print("\nTimetable Found")
                        print("----------------------------")
                        print("Day     :", day)
                        print("Subject :", subject)
                        print("Teacher :", teacher_name)
                        print("Time    :", time)

                        found = True
                        break

            if not found:
                print("Timetable not found.")

        except Exception as e:
            print("Error:", e)

    # Delete Timetable
    def delete_timetable(self):

        try:

            delete_day = input("Enter Day to delete: ").strip()

            if not os.path.exists(Timetable.FILE_NAME):
                print("Timetable file not found.")
                return

            with open(Timetable.FILE_NAME, "r") as file:
                records = file.readlines()

            found = False

            with open(Timetable.FILE_NAME, "w") as file:

                for line in records:
                    stripped = line.strip()
                    if not stripped:
                        continue  # Skip empty lines instead of writing them back
                    parts = stripped.split(",")
                    if len(parts) < 1:
                        continue
                    day = parts[0]

                    if day.lower() != delete_day.lower():
                        file.write(line)
                    else:
                        found = True

            if found:
                print("Timetable deleted successfully!")

            else:
                print("Timetable not found.")

        except Exception as e:
            print("Error:", e)