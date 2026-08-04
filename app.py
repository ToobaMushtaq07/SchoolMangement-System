import os
from functools import wraps

from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import check_password_hash
from psycopg2.extras import RealDictCursor

from dotenv import load_dotenv
from package.db import get_connection

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_secret_key")


# ================= AUTH DECORATOR =================

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            flash("Please login first.", "warning")
            return redirect("/")
        return func(*args, **kwargs)
    return wrapper


# ================= DATABASE HELPERS =================

def fetch_all(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cursor.execute(query, params or ())
        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def fetch_one(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cursor.execute(query, params or ())
        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()


def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query, params or ())
        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cursor.close()
        conn.close()


# ================= LOGIN =================

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()

        user = fetch_one(
            "SELECT * FROM users WHERE username = %s",
            (username,)
        )

        if user and check_password_hash(user["password_hash"], password):
            session["user"] = username
            flash("Login successful!", "success")
            return redirect("/dashboard")

        flash("Invalid username or password.", "danger")
        return redirect("/")

    return render_template("login.html")


# ================= LOGOUT =================

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully.", "success")
    return redirect("/")


# ================= DASHBOARD =================

@app.route("/dashboard")
@login_required
def dashboard():
    student_count = fetch_one("SELECT COUNT(*) AS total FROM student")["total"]
    teacher_count = fetch_one("SELECT COUNT(*) AS total FROM teacher")["total"]
    classroom_count = fetch_one("SELECT COUNT(*) AS total FROM classroom")["total"]
    timetable_count = fetch_one("SELECT COUNT(*) AS total FROM timetable")["total"]

    return render_template(
        "dashboard.html",
        student_count=student_count,
        teacher_count=teacher_count,
        classroom_count=classroom_count,
        timetable_count=timetable_count
    )


# ================= STUDENT CRUD =================

@app.route("/students")
@login_required
def students():
    data = fetch_all("SELECT * FROM student ORDER BY person_id")
    return render_template("students.html", students=data, edit_student=None)


@app.route("/students/add", methods=["POST"])
@login_required
def add_student():
    try:
        person_id = int(request.form["person_id"])
        name = request.form["name"].strip()
        age = int(request.form["age"])
        department = request.form["department"].strip()

        execute_query("""
            INSERT INTO student (person_id, name, age, department)
            VALUES (%s, %s, %s, %s)
        """, (person_id, name, age, department))

        flash("Student added successfully!", "success")

    except Exception as e:
        flash(f"Error adding student: {e}", "danger")

    return redirect("/students")


@app.route("/students/edit/<int:person_id>")
@login_required
def edit_student(person_id):
    edit_data = fetch_one(
        "SELECT * FROM student WHERE person_id = %s",
        (person_id,)
    )
    data = fetch_all("SELECT * FROM student ORDER BY person_id")
    return render_template("students.html", students=data, edit_student=edit_data)


@app.route("/students/update/<int:person_id>", methods=["POST"])
@login_required
def update_student(person_id):
    try:
        name = request.form["name"].strip()
        age = int(request.form["age"])
        department = request.form["department"].strip()

        execute_query("""
            UPDATE student
            SET name = %s, age = %s, department = %s
            WHERE person_id = %s
        """, (name, age, department, person_id))

        flash("Student updated successfully!", "success")

    except Exception as e:
        flash(f"Error updating student: {e}", "danger")

    return redirect("/students")


@app.route("/students/delete/<int:person_id>", methods=["POST"])
@login_required
def delete_student(person_id):
    try:
        execute_query(
            "DELETE FROM student WHERE person_id = %s",
            (person_id,)
        )
        flash("Student deleted successfully!", "success")

    except Exception as e:
        flash(f"Error deleting student: {e}", "danger")

    return redirect("/students")


# ================= TEACHER CRUD =================

@app.route("/teachers")
@login_required
def teachers():
    data = fetch_all("SELECT * FROM teacher ORDER BY person_id")
    return render_template("teachers.html", teachers=data, edit_teacher=None)


@app.route("/teachers/add", methods=["POST"])
@login_required
def add_teacher():
    try:
        person_id = int(request.form["person_id"])
        name = request.form["name"].strip()
        subject = request.form["subject"].strip()
        qualification = request.form["qualification"].strip()

        execute_query("""
            INSERT INTO teacher (person_id, name, subject, qualification)
            VALUES (%s, %s, %s, %s)
        """, (person_id, name, subject, qualification))

        flash("Teacher added successfully!", "success")

    except Exception as e:
        flash(f"Error adding teacher: {e}", "danger")

    return redirect("/teachers")


@app.route("/teachers/edit/<int:person_id>")
@login_required
def edit_teacher(person_id):
    edit_data = fetch_one(
        "SELECT * FROM teacher WHERE person_id = %s",
        (person_id,)
    )
    data = fetch_all("SELECT * FROM teacher ORDER BY person_id")
    return render_template("teachers.html", teachers=data, edit_teacher=edit_data)


@app.route("/teachers/update/<int:person_id>", methods=["POST"])
@login_required
def update_teacher(person_id):
    try:
        name = request.form["name"].strip()
        subject = request.form["subject"].strip()
        qualification = request.form["qualification"].strip()

        execute_query("""
            UPDATE teacher
            SET name = %s, subject = %s, qualification = %s
            WHERE person_id = %s
        """, (name, subject, qualification, person_id))

        flash("Teacher updated successfully!", "success")

    except Exception as e:
        flash(f"Error updating teacher: {e}", "danger")

    return redirect("/teachers")


@app.route("/teachers/delete/<int:person_id>", methods=["POST"])
@login_required
def delete_teacher(person_id):
    try:
        execute_query(
            "DELETE FROM teacher WHERE person_id = %s",
            (person_id,)
        )
        flash("Teacher deleted successfully!", "success")

    except Exception as e:
        flash(f"Error deleting teacher: {e}", "danger")

    return redirect("/teachers")


# ================= CLASSROOM CRUD =================

@app.route("/classrooms")
@login_required
def classrooms():
    data = fetch_all("SELECT * FROM classroom ORDER BY room_number")
    return render_template("classrooms.html", classrooms=data, edit_classroom=None)


@app.route("/classrooms/add", methods=["POST"])
@login_required
def add_classroom():
    try:
        room_number = int(request.form["room_number"])
        class_name = request.form["class_name"].strip()
        capacity = int(request.form["capacity"])

        execute_query("""
            INSERT INTO classroom (room_number, class_name, capacity)
            VALUES (%s, %s, %s)
        """, (room_number, class_name, capacity))

        flash("Classroom added successfully!", "success")

    except Exception as e:
        flash(f"Error adding classroom: {e}", "danger")

    return redirect("/classrooms")


@app.route("/classrooms/edit/<int:room_number>")
@login_required
def edit_classroom(room_number):
    edit_data = fetch_one(
        "SELECT * FROM classroom WHERE room_number = %s",
        (room_number,)
    )
    data = fetch_all("SELECT * FROM classroom ORDER BY room_number")
    return render_template("classrooms.html", classrooms=data, edit_classroom=edit_data)


@app.route("/classrooms/update/<int:room_number>", methods=["POST"])
@login_required
def update_classroom(room_number):
    try:
        class_name = request.form["class_name"].strip()
        capacity = int(request.form["capacity"])

        execute_query("""
            UPDATE classroom
            SET class_name = %s, capacity = %s
            WHERE room_number = %s
        """, (class_name, capacity, room_number))

        flash("Classroom updated successfully!", "success")

    except Exception as e:
        flash(f"Error updating classroom: {e}", "danger")

    return redirect("/classrooms")


@app.route("/classrooms/delete/<int:room_number>", methods=["POST"])
@login_required
def delete_classroom(room_number):
    try:
        execute_query(
            "DELETE FROM classroom WHERE room_number = %s",
            (room_number,)
        )
        flash("Classroom deleted successfully!", "success")

    except Exception as e:
        flash(f"Error deleting classroom: {e}", "danger")

    return redirect("/classrooms")


# ================= TIMETABLE CRUD =================

@app.route("/timetable")
@login_required
def timetable():
    data = fetch_all("SELECT * FROM timetable ORDER BY id")
    return render_template("timetable.html", timetable=data, edit_timetable=None)


@app.route("/timetable/add", methods=["POST"])
@login_required
def add_timetable():
    try:
        day = request.form["day"].strip()
        subject = request.form["subject"].strip()
        teacher_name = request.form["teacher_name"].strip()
        time = request.form["time"].strip()

        execute_query("""
            INSERT INTO timetable (day, subject, teacher_name, time)
            VALUES (%s, %s, %s, %s)
        """, (day, subject, teacher_name, time))

        flash("Timetable added successfully!", "success")

    except Exception as e:
        flash(f"Error adding timetable: {e}", "danger")

    return redirect("/timetable")


@app.route("/timetable/edit/<int:id>")
@login_required
def edit_timetable(id):
    edit_data = fetch_one(
        "SELECT * FROM timetable WHERE id = %s",
        (id,)
    )
    data = fetch_all("SELECT * FROM timetable ORDER BY id")
    return render_template("timetable.html", timetable=data, edit_timetable=edit_data)


@app.route("/timetable/update/<int:id>", methods=["POST"])
@login_required
def update_timetable(id):
    try:
        day = request.form["day"].strip()
        subject = request.form["subject"].strip()
        teacher_name = request.form["teacher_name"].strip()
        time = request.form["time"].strip()

        execute_query("""
            UPDATE timetable
            SET day = %s, subject = %s, teacher_name = %s, time = %s
            WHERE id = %s
        """, (day, subject, teacher_name, time, id))

        flash("Timetable updated successfully!", "success")

    except Exception as e:
        flash(f"Error updating timetable: {e}", "danger")

    return redirect("/timetable")


@app.route("/timetable/delete/<int:id>", methods=["POST"])
@login_required
def delete_timetable(id):
    try:
        execute_query(
            "DELETE FROM timetable WHERE id = %s",
            (id,)
        )
        flash("Timetable deleted successfully!", "success")

    except Exception as e:
        flash(f"Error deleting timetable: {e}", "danger")

    return redirect("/timetable")


# ================= VIEW ALL RECORDS =================

@app.route("/records")
@login_required
def records():
    students_data = fetch_all("SELECT * FROM student ORDER BY person_id")
    teachers_data = fetch_all("SELECT * FROM teacher ORDER BY person_id")
    classrooms_data = fetch_all("SELECT * FROM classroom ORDER BY room_number")
    timetable_data = fetch_all("SELECT * FROM timetable ORDER BY id")

    return render_template(
        "records.html",
        students=students_data,
        teachers=teachers_data,
        classrooms=classrooms_data,
        timetable=timetable_data
    )


# ================= RUN APP =================

if __name__ == "__main__":
    app.run(debug=True)