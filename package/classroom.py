import os
class Classroom:

    FILE_NAME = "data/classrooms.txt"

    def _init_(self, room_number, class_name, capacity):
        self.room_number = room_number
        self.class_name = class_name
        self.capacity = capacity

    # Add Classroom
    def add_classroom(self):
        try:
            with open(Classroom.FILE_NAME, "a") as file:
                file.write(f"{self.room_number},{self.class_name},{self.capacity}\n")

            print("Classroom added successfully!")

        except Exception as e:
            print("Error:", e)

    # View Classrooms
    def view_classrooms():

        try:

            if not os.path.exists(Classroom.FILE_NAME):
                print("No classroom record found.")
                return

            with open(Classroom.FILE_NAME, "r") as file:
                records = file.readlines()

            if len(records) == 0:
                print("No classroom record found.")
                return

            print("\n========== Classroom Records ==========")

            for line in records:

                room_number, class_name, capacity = line.strip().split(",")

                print(f"Room Number : {room_number}")
                print(f"Class Name  : {class_name}")
                print(f"Capacity    : {capacity}")
                print("-------------------------------------")

        except FileNotFoundError:
            print("Classroom file not found.")

        except Exception as e:
            print("Error:", e)

    # Search Classroom

    def search_classroom():

        try:

            search_room = input("Enter Room Number: ")

            if not os.path.exists(Classroom.FILE_NAME):
                print("Classroom file not found.")
                return

            found = False

            with open(Classroom.FILE_NAME, "r") as file:

                for line in file:

                    room_number, class_name, capacity = line.strip().split(",")

                    if room_number == search_room:

                        print("\nClassroom Found")
                        print("---------------------------")
                        print("Room Number :", room_number)
                        print("Class Name  :", class_name)
                        print("Capacity    :", capacity)

                        found = True
                        break

            if not found:
                print("Classroom not found.")

        except Exception as e:
            print("Error:", e)

    # Delete Classroom
    def delete_classroom():

        try:

            delete_room = input("Enter Room Number to delete: ")

            if not os.path.exists(Classroom.FILE_NAME):
                print("Classroom file not found.")
                return

            with open(Classroom.FILE_NAME, "r") as file:
                records = file.readlines()

            found = False

            with open(Classroom.FILE_NAME, "w") as file:

                for line in records:

                    room_number = line.strip().split(",")[0]

                    if room_number != delete_room:
                        file.write(line)
                    else:
                        found = True

            if found:
                print("Classroom deleted successfully!")

            else:
                print("Classroom not found.")

        except Exception as e:
            print("Error:", e)