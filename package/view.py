from package.student import Student
from package.teacher import Teacher
from package.classroom import Classroom
from package.timetable import Timetable


class View:

    def view_all(self):
        student = Student("", "", "", "")
        teacher = Teacher("", "", "", "")
        classroom = Classroom("", "", "")
        timetable = Timetable("", "", "", "")

        student.view_students()
        teacher.view_teachers()
        classroom.view_classrooms()
        timetable.view_timetable()