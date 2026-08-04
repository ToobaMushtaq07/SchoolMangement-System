import os
from package.db import get_connection


class Classroom:

    def __init__(self, room_number, class_name, capacity):
        self.room_number = room_number
        self.class_name = class_name
        self.capacity = capacity

    # Add Classroom
    def add_classroom(self):
        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO classroom (room_number, class_name, capacity) VALUES (%s, %s, %s)",
                (self.room_number, self.class_name, self.capacity)
            )
            conn.commit()
            print("Classroom added successfully!")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # View Classrooms
    def view_classrooms(self):
        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM classroom")
            records = cursor.fetchall()

            if not records:
                print("No classroom record found.")
                return

            print("\n========== Classroom Records ==========")

            for row in records:
                print(f"Room Number : {row[0]}")
                print(f"Class Name  : {row[1]}")
                print(f"Capacity    : {row[2]}")
                print("-------------------------------------")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # Search Classroom
    def search_classroom(self):
        search_room = input("Enter Room Number: ")

        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM classroom WHERE room_number = %s",
                (search_room,)
            )
            row = cursor.fetchone()

            if row:
                print("\nClassroom Found")
                print("---------------------------")
                print("Room Number :", row[0])
                print("Class Name  :", row[1])
                print("Capacity    :", row[2])
            else:
                print("Classroom not found.")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # Delete Classroom
    def delete_classroom(self):
        delete_room = input("Enter Room Number to delete: ")

        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "DELETE FROM classroom WHERE room_number = %s",
                (delete_room,)
            )
            conn.commit()

            if cursor.rowcount > 0:
                print("Classroom deleted successfully!")
            else:
                print("Classroom not found.")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()