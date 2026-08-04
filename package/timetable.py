from package.db import get_connection


class Timetable:

    def __init__(self, day, subject, teacher_name, time):
        self.day = day
        self.subject = subject
        self.teacher_name = teacher_name
        self.time = time

    # Add Timetable
    def add_timetable(self):
        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO timetable (day, subject, teacher_name, time) VALUES (%s, %s, %s, %s)",
                (self.day, self.subject, self.teacher_name, self.time)
            )
            conn.commit()
            print("Timetable added successfully!")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # View Timetable
    def view_timetable(self):
        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM timetable")
            records = cursor.fetchall()

            if not records:
                print("No timetable record found.")
                return

            print("\n========== Timetable Records ==========")

            for row in records:
                print(f"Day     : {row[1]}")
                print(f"Subject : {row[2]}")
                print(f"Teacher : {row[3]}")
                print(f"Time    : {row[4]}")
                print("-----------------------------------")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # Search Timetable
    def search_timetable(self):
        search_day = input("Enter Day: ")

        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM timetable WHERE LOWER(day) = LOWER(%s)",
                (search_day,)
            )
            rows = cursor.fetchall()

            if not rows:
                print("Timetable not found.")
                return

            print("\nTimetable Found")
            print("----------------------------")

            for row in rows:
                print("Day     :", row[1])
                print("Subject :", row[2])
                print("Teacher :", row[3])
                print("Time    :", row[4])
                print("----------------------------")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # Delete Timetable
    def delete_timetable(self):
        delete_day = input("Enter Day to delete: ")

        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "DELETE FROM timetable WHERE LOWER(day) = LOWER(%s)",
                (delete_day,)
            )
            conn.commit()

            if cursor.rowcount > 0:
                print("Timetable deleted successfully!")
            else:
                print("Timetable not found.")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()