from package.person import Person
from package.db import get_connection


class Teacher(Person):

    def __init__(self, person_id, name, subject, qualification):
        super().__init__(person_id, name)
        self.subject = subject
        self.qualification = qualification

    # Add Teacher
    def add_teacher(self):
        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO teacher (person_id, name, subject, qualification) VALUES (%s, %s, %s, %s)",
                (self.person_id, self.name, self.subject, self.qualification)
            )
            conn.commit()
            print("Teacher added successfully!")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # View Teachers
    def view_teachers(self):
        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM teacher")
            records = cursor.fetchall()

            if not records:
                print("No teacher record found.")
                return

            print("\n========== Teacher Records ==========")

            for row in records:
                print(f"Teacher ID    : {row[0]}")
                print(f"Name          : {row[1]}")
                print(f"Subject       : {row[2]}")
                print(f"Qualification : {row[3]}")
                print("--------------------------------------")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # Search Teacher
    def search_teacher(self):
        search_id = input("Enter Teacher ID: ")

        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT * FROM teacher WHERE person_id = %s",
                (search_id,)
            )
            row = cursor.fetchone()

            if row:
                print("\nTeacher Found")
                print("-------------------------")
                print("Teacher ID    :", row[0])
                print("Name          :", row[1])
                print("Subject       :", row[2])
                print("Qualification :", row[3])
            else:
                print("Teacher not found.")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()

    # Delete Teacher
    def delete_teacher(self):
        delete_id = input("Enter Teacher ID to delete: ")

        conn = get_connection()
        if conn is None:
            return

        cursor = conn.cursor()

        try:
            cursor.execute(
                "DELETE FROM teacher WHERE person_id = %s",
                (delete_id,)
            )
            conn.commit()

            if cursor.rowcount > 0:
                print("Teacher deleted successfully!")
            else:
                print("Teacher not found.")

        except Exception as e:
            print("Error:", e)

        finally:
            cursor.close()
            conn.close()