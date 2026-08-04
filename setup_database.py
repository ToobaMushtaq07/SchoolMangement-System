from package.db import get_connection
from werkzeug.security import generate_password_hash


def create_tables():
    conn = get_connection()

    if conn is None:
        print("Database connection failed.")
        return

    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student (
                person_id INT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL,
                department VARCHAR(100) NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS teacher (
                person_id INT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                subject VARCHAR(100) NOT NULL,
                qualification VARCHAR(100) NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS classroom (
                room_number INT PRIMARY KEY,
                class_name VARCHAR(100) NOT NULL,
                capacity INT NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS timetable (
                id SERIAL PRIMARY KEY,
                day VARCHAR(50) NOT NULL,
                subject VARCHAR(100) NOT NULL,
                teacher_name VARCHAR(100) NOT NULL,
                time VARCHAR(50) NOT NULL
            );
        """)

        admin_password = generate_password_hash("admin123")

        cursor.execute("""
            INSERT INTO users (username, password_hash)
            VALUES (%s, %s)
            ON CONFLICT (username) DO NOTHING;
        """, ("admin", admin_password))

        conn.commit()
        print("Tables created successfully!")
        print("Default login: admin / admin123")

    except Exception as e:
        conn.rollback()
        print("Error creating tables:", e)

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    create_tables()