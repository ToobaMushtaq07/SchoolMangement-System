from .student import Student
from .teacher import Teacher
from .classroom import Classroom
from .timetable import Timetable

class View:
    def view_all(self):

        student = Student("", "", "", "")
        student.view_students()

        teacher = Teacher("", "", "", "")
        teacher.view_teachers()

        classroom = Classroom("", "", "")
        classroom.view_classrooms()

        timetable = Timetable("", "", "", "")
        timetable.view_timetable()