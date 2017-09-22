# Student Enrollment System
# 6 Classes
# Student, Fees, Grades, Course, Faculty, System
# Has __init__ in all the classes
import random


# Student class
class Student(object):
    _id = 0  # Private variable

    def __init__(self, name, rollno):
        super(Student, self).__init__()  # Using super keyword
        self.name = name
        self.rollno = rollno
        self._generateRandomID()

    def _generateRandomID(self):  # Private function
        Student.id = random.randint(1000, 9999)

    def getStudentDetails(self):
        print("******** Student Details *********")
        print("Student ID: ", self.id)
        print("Student name: ", self.name)
        print("Student Roll Number: ", self.rollno)


class Fees(object):
    def __init__(self, fees):
        self.fees = fees
        self.enrolled = True

    def feePaid(self):
        print("Fees Paid: ", self.fees)
        print("Enrolled: ", self.enrolled)


class Grades(object):
    def __init__(self, grade):
        self.grade = grade

    def getGrades(self):
        print("Grade: ", self.grade)


class Course(object):
    def __init__(self, courseno, coursename):
        self.courseno = courseno
        self.coursename = coursename

    def getCourseDetails(self):
        print("Course Name: ", self.coursename)
        print("Course Number: ", self.courseno)


class Faculty(object):
    def __init__(self, facultyname, facultydept):
        self.facultyname = facultyname
        self.facultydept = facultydept

    def getFacultyDetails(self):
        print("Faculty Name: ", self.facultyname)
        print("Faculty Department: ", self.facultydept)


class System(Student, Grades, Course, Faculty, Fees):
    def __init__(self, name, rollno, grade, courseno, coursename, facultyname, facultydept, fees):
        self.name = name
        self.rollno = rollno
        self.grade = grade
        self.coursename = coursename
        self.courseno = courseno
        self.facultyname = facultyname
        self.facultydept = facultydept
        self.fees = fees
        self.enrolled = True


# Student Class Instantiation
student = Student("Sibi", 5567)
# Fee Class Instantiation
fees = Fees(3000)
# Grade Class Instantiation
grade = Grades("A")
# Course Class Instantiation
course = Course(1234, "ASE")
# Faculty Class Instantiation
faculty = Faculty("Dr.Lee", "Computer Science")
# System Class inherits all the other classes (Multiple Inheritance)
system = System(student.name, student.rollno, grade.grade, course.courseno, course.coursename, faculty.facultyname,
                faculty.facultydept, fees.fees)
# Calling all the display functions
system.getStudentDetails()
system.getCourseDetails()
system.getGrades()
system.getFacultyDetails()
system.feePaid()
print("**********************************")
