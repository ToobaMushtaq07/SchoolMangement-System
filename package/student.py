from package.person import Person
from package.db import get_connection


class Student(Person):

    def __init__(self, person_id, name, age, department):
        super().__init__(person_id, name)
        self.age = age
        self.department = department

    # Add Student
    def add_student(self):
        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO student (person_id, name, age, department) VALUES (%s, %s, %s, %s)",
                (self.person_id, self.name, self.age, self.department)
            )
            conn.commit()
            print("Student added successfully!")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # View Students
    def view_students(self):
        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM student")
            records = cursor.fetchall()

            if not records:
                print("No student record found.")
                return

            print("\n========== Student Records ==========")

            for row in records:
                print(f"Student ID : {row[0]}")
                print(f"Name       : {row[1]}")
                print(f"Age        : {row[2]}")
                print(f"Department : {row[3]}")
                print("-------------------------------------")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # Search Student
    def search_student(self):
        search_id = input("Enter Student ID: ")

        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM student WHERE person_id = %s",
                (search_id,)
            )
            row = cursor.fetchone()

            if row:
                print("\nStudent Found")
                print("----------------------")
                print("Student ID :", row[0])
                print("Name       :", row[1])
                print("Age        :", row[2])
                print("Department :", row[3])
            else:
                print("Student not found.")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # Delete Student
    def delete_student(self):
        delete_id = input("Enter Student ID to delete: ")

        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "DELETE FROM student WHERE person_id = %s",
                (delete_id,)
            )
            conn.commit()

            if cursor.rowcount > 0:
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()