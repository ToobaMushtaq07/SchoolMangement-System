# 📚 School Management System (Python - OOP & File Handling)

A simple **School Management System** built using **Python**, implementing core programming concepts such as **Object-Oriented Programming (OOP)**, **Inheritance**, **File Handling**, **Input Validation**, and a **Menu-Driven Interface**.

This project is designed to manage school records efficiently through a modular structure using multiple Python files.

---

## ✨ Features

- ✅ Object-Oriented Programming (OOP)
- ✅ Inheritance
- ✅ File Handling
- ✅ Input Validation
- ✅ Exception Handling
- ✅ Menu-Driven Interface
- ✅ Modular Programming

---

## 📂 Project Structure

```text
SchoolMangement-System/
│
├── main.py
│
├── data/
│   ├── student.txt
│   ├── teacher.txt
│   ├── classroom.txt
│   └── timetable.txt
│
└── package/
    ├── __init__.py
    ├── person.py
    ├── student.py
    ├── teacher.py
    ├── classroom.py
    ├── timetable.py
    └── view.py
```

---

# 🏗️ Project Modules

## 🔹 Person (Base Class)

The **Person** class acts as the parent class for both **Student** and **Teacher**.

### Attributes

- Person ID
- Name

### Purpose

Avoids duplicate code by storing common attributes shared between students and teachers.

---

## 👨‍🎓 Student (Inherits Person)

The Student class inherits from the Person class.

### Stores

- Student ID
- Name
- Age
- Department

### Data File

```text
data/student.txt
```

### Operations

- ➕ Add Student
- 📄 View Students
- 🔍 Search Student
- ❌ Delete Student

---

## 👨‍🏫 Teacher (Inherits Person)

The Teacher class also inherits from the Person class.

### Stores

- Teacher ID
- Name
- Subject
- Qualification

### Data File

```text
data/teacher.txt
```

### Operations

- ➕ Add Teacher
- 📄 View Teachers
- 🔍 Search Teacher
- ❌ Delete Teacher

---

## 🏫 Classroom

Handles classroom records.

### Stores

- Room Number
- Class Name
- Capacity

### Data File

```text
data/classroom.txt
```

### Operations

- ➕ Add Classroom
- 📄 View Classrooms
- 🔍 Search Classroom
- ❌ Delete Classroom

---

## 📅 Timetable

Stores timetable information.

### Stores

- Day
- Subject
- Teacher Name
- Time

### Data File

```text
data/timetable.txt
```

### Operations

- ➕ Add Timetable
- 📄 View Timetable
- 🔍 Search Timetable
- ❌ Delete Timetable

---

## 📋 View Module

Displays all stored records together.

### View All Records

- Students
- Teachers
- Classrooms
- Timetable

---

# 🔄 Program Flow

```text
                    Main Menu
                        │
    ┌───────────────────┼───────────────────┐
    │                   │                   │
 Student Menu     Teacher Menu      Classroom Menu
    │                   │                   │
 ├── Add           ├── Add            ├── Add
 ├── View          ├── View           ├── View
 ├── Search        ├── Search         ├── Search
 └── Delete        └── Delete         └── Delete

                        │
                  Timetable Menu
                        │
                 ├── Add
                 ├── View
                 ├── Search
                 └── Delete

                        │
                View All Records
                        │
                      Exit
```

The application runs continuously until the user selects **Exit**.

---

# 🔐 Input Validation

The project performs proper validation before saving data.

## ID Validation

- Only integer IDs are accepted.
- IDs must be greater than zero.
- Duplicate IDs are not allowed.
- IDs like `1`, `01`, and `001` are treated as the same value.

---

## Positive Number Validation

Used for:

- Student Age
- Classroom Capacity

Negative numbers and zero are rejected.

---

# 📁 File Handling

The project uses text files to store data.

Features include:

- Automatically creates files if they do not exist.
- Reads records safely.
- Prevents crashes due to malformed data.
- Uses proper read (`r`), write (`w`), and append (`a`) modes.
- Deletes records by rewriting the file.

---

# ⚠️ Exception Handling

The program uses `try` and `except` blocks to handle invalid input and file-related errors gracefully, preventing unexpected crashes.

---

# 🧠 OOP Concepts Used

- Classes & Objects
- Inheritance
- Encapsulation
- Constructors (`__init__`)
- Method Overriding (where applicable)
- Modular Programming

---

# 💾 File Storage Format

## Student

```text
ID,Name,Age,Department
```

Example

```text
101,Ali,20,Computer Science
```

---

## Teacher

```text
ID,Name,Subject,Qualification
```

Example

```text
201,Sara,Mathematics,MS Mathematics
```

---

## Classroom

```text
RoomNo,ClassName,Capacity
```

Example

```text
B-201,BSCS-5A,45
```

---

## Timetable

```text
Day,Subject,Teacher,Time
```

Example

```text
Monday,Python,Mr. Ahmed,09:00 AM
```

---

# ▶️ How to Run

## 1. Install Python

Make sure **Python 3.x** is installed on your system.

---

## 2. Open Terminal

Navigate to the project folder.

```bash
cd SchoolMangement-System
```

---

## 3. Run the Project

```bash
python main.py
```

---

# 📌 Menu Options

### Student Menu

- Add Student
- View Students
- Search Student
- Delete Student

### Teacher Menu

- Add Teacher
- View Teachers
- Search Teacher
- Delete Teacher

### Classroom Menu

- Add Classroom
- View Classrooms
- Search Classroom
- Delete Classroom

### Timetable Menu

- Add Timetable
- View Timetable
- Search Timetable
- Delete Timetable

### View Menu

- View All Records

---

# 🛠 Technologies Used

- Python 3
- Object-Oriented Programming
- File Handling
- Exception Handling
- Text Files
- VS Code / Any Python IDE

---

# 📖 Learning Outcomes

By completing this project, you will understand:

- Creating classes and objects
- Using inheritance effectively
- Reading and writing files
- Exception handling
- Data validation
- Building menu-driven applications
- Organizing projects using multiple Python modules

---

# ⚠️ Notes

- This project uses **text files** instead of a database.
- Timetable currently stores the **teacher name** instead of the teacher ID.
- All records are validated before saving.
- The project is beginner-friendly and suitable for learning Python OOP.

---

# 🚀 Future Improvements

- 🔗 Link Timetable with Teacher ID.
- 🏫 Assign Students to Classrooms.
- ✏️ Add Update/Edit functionality.
- 🔐 Add Login Authentication.
- 🗄️ Replace text files with SQLite/MySQL.
- 🖥️ Develop a GUI using Tkinter or PyQt.
- 📊 Generate reports and statistics.
- 📤 Export records to CSV or Excel.
- 🌐 Convert into a web application using Flask or Django.

---
