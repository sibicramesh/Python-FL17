class Student(object):
    totalStudents = 0

    def __init__(self, name, rollno, grades):
        self.name = name
        self.rollno = rollno
        self.grades = grades
        self.transfer = False
        self._countStudents()

    def _countStudents(self):
        Student.totalStudents += 1

    def totalNoOfStudents(self):
        print("Total number of students: ", self.totalStudents)

    def displayStudentDetails(self):
        print("*******Student Details*******")
        print("Name:", self.name)
        print("RollNo:", self.rollno)
        print("Grades:", self.grades)
        print("Transfer:", self.transfer)
        print("*****************************")


class TransferStudent(Student):
    def __init__(self, name, rollno, grades):
        super(TransferStudent, self).__init__(name, rollno, grades)
        self.name = name
        self.rollno = rollno
        self.grades = grades
        self.transfer = True

# Student 1
std1 = Student("Arun", 4566, 3.5)
std1.displayStudentDetails()
# Student 2 - Transfer Student
std2 = TransferStudent("Sibi", 2354, 4)
std2.displayStudentDetails()
# Total Students
std2.totalNoOfStudents()
