# ============================================================
# PERSON CLASS
# ============================================================
# Person parent (base) class hai.
# Is project me Student, Teacher aur Admin sab Person hain.
# Isliye jo common cheezen hain (name, age, email)
# woh sirf ek hi jagah likhenge.
# Isse code repeat nahi hoga.
# ============================================================

class Person:

    # Constructor automatically object banne par call hota hai.
    # Har Person ka name, age aur email hoga.
    def __init__(self, name, age, email):

        # Direct assign nahi kar rahe.
        # Validation reuse karne ke liye setters use kar rahe hain.
        self.set_name(name)
        self.set_age(age)
        self.set_email(email)

    # ========================================================
    # NAME SETTER
    # ========================================================
    # Name ko safely update karega.
    # Har baar validation chalegi.
    # ========================================================

    def set_name(self, new_name):

        # Empty string allow nahi.
        if new_name.strip() == "":
            raise ValueError("Empty value is not accepted")

        # Private variable.
        # Bahar se direct access nahi hoga.
        self.__name = new_name

    # ========================================================
    # AGE SETTER
    # ========================================================

    def set_age(self, new_age):

        # Age 0 ya negative nahi ho sakti.
        if new_age <= 0:
            raise ValueError("Age must be greater than 0")

        # Private variable.
        self.__age = new_age

    # ========================================================
    # EMAIL SETTER
    # ========================================================

    def set_email(self, new_email):

        # Simple validation.
        # Baad me isko better karenge.
        if not new_email.endswith("@gmail.com"):
            raise ValueError("Invalid Email")

        # Private variable.
        self.__email = new_email

    # ========================================================
    # DISPLAY METHOD
    # ========================================================
    # Person ki common information print karega.
    # Student, Teacher aur Admin bhi isi ko reuse karenge.
    # ========================================================

    def display(self):

        print(f"Name : {self.__name}")
        print(f"Age : {self.__age}")
        print(f"Email : {self.__email}")


# ============================================================
# UNIVERSITY CLASS
# ============================================================


class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.teachers = {}
        self.students = {}
        self.courses = {}
        self.admins = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_teacher(self, teacher):
        self.teachers[teacher.teacher_id] = teacher

    def add_course(self, course):
        self.courses[course.course_id] = course

    def add_admin(self, admin):
        self.admins[admin.admin_id] = admin

# ============================================================
# ADMIN CLASS
# ============================================================
# Admin bhi Person hai.
# Isliye Person se inherit karega.
# ============================================================

class Admin(Person):

    # Constructor
    def __init__(self, admin_id, name, age, email):

        # Parent constructor call.
        # Name, Age aur Email Person handle karega.
        super().__init__(name, age, email)

        # Admin ki apni unique property.
        self.admin_id = admin_id

    # ========================================================
    # Admin Student ka name change kar sakta hai.
    # ========================================================

    def change_student_name(self, student, new_name):

        # student ek Student object receive karega.
        # Direct variable change nahi kar rahe.
        # Setter use kar rahe hain.
        student.set_name(new_name)

    # ========================================================
    # Student ka CGPA update.
    # ========================================================

    def change_student_cgpa(self, student, new_cgpa):

        # Validation Student class karegi.
        student.set_cgpa(new_cgpa)

    # ========================================================
    # Student ka Email update.
    # ========================================================

    def change_student_email(self, student, new_email):

        # Validation Student ki parent class (Person) karegi.
        student.set_email(new_email)

    # ========================================================
    # Display
    # ========================================================

    def display(self):

        # Pehle Person wali information print hogi.
        super().display()

        # Phir Admin ki apni information.
        print(f"Admin ID : {self.admin_id}")


# ============================================================
# TEACHER CLASS
# ============================================================
# Teacher bhi Person hai.
# ============================================================

class Teacher(Person):

    # Constructor
    def __init__(self, name, age, email, teacher_id, subject, department, salary,   attendance):
        # Parent constructor call.
        super().__init__(name, age, email)

        # Teacher ki unique information.

        self.teacher_id = teacher_id

        self.subject = subject

        self.department = department

        # Direct assign nahi kar rahe.
        # Validation ke liye setter use karenge.
        self.set_salary(salary)

        # Attendance dictionary.
        self.attendance = attendance

        # Teacher multiple courses padha sakta hai.
        # Isliye dictionary bana rahe hain.
        # Example:
        #
        # {
        #   "CS101": DSA Object,
        #   "CS102": OOP Object
        # }
        self.courses = {}

    # ========================================================
    # Salary Setter
    # ========================================================

    def set_salary(self, new_salary):

        # Salary positive honi chahiye.
        if new_salary <= 0:
            raise ValueError("Salary must be greater than 0")

        self.salary = new_salary

    # ========================================================
    # Add Course
    # ========================================================
    # Jab Course kisi Teacher ko assign karega,
    # tab Teacher bhi us Course ko yaad rakhega.
    # ========================================================

    def add_course(self, course):

        # Dictionary me Course Object store ho raha hai.
        #
        # Key:
        # Course ID
        #
        # Value:
        # Complete Course Object
        self.courses[course.course_id] = course

    def assign_marks(self, student, course, marks):
        # Validation 1
        if course.course_id not in self.courses:
            raise ValueError("Teacher is not assigned to this course")

        # Validation 2
        if course.course_id not in student.courses:
            raise ValueError("Student is not enrolled in this course")

        # Save Marks
        student.marks[course.course_id] = marks
        

    # ========================================================
    # Display
    # ========================================================

    def display(self):

        # Parent information.
        super().display()

        # Teacher ki own information.
        print(f"Teacher ID : {self.teacher_id}")
        print(f"Subject : {self.subject}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")
        print(f"Present : {self.attendance['Present']}")
        print(f"Absent : {self.attendance['Absent']}")

# ============================================================
# STUDENT CLASS
# ============================================================
# Student bhi Person hai.
# Isliye Student Person se inherit karega.
#
# Student ke paas apni extra information hogi:
# - Student ID
# - Semester
# - CGPA
# - Attendance
# - Marks
# - Courses
# ============================================================

class Student(Person):

    # Constructor
    def __init__(self, name, age, email, student_id, semester, cgpa, attendance):

        # Parent constructor call.
        # Name, Age aur Email Person handle karega.
        super().__init__(name, age, email)

        # Student ki unique ID.
        self.student_id = student_id

        # Current semester.
        self.semester = semester

        # Direct assign nahi kar rahe.
        # Validation reuse hogi.
        self.set_cgpa(cgpa)

        # Attendance dictionary.
        self.attendance = attendance

        # ====================================================
        # Marks Dictionary
        # ====================================================
        # Jab Student banta hai tab uske marks nahi hote.
        #
        # Lekin hume future ke liye ek empty container chahiye.
        #
        # Example (future):
        #
        # {
        #     "CS101": 88,
        #     "CS102": 91
        # }
        #
        # Abhi ye sirf empty box hai.
        # ====================================================

        self.marks = {}

        # ====================================================
        # Courses Dictionary
        # ====================================================
        # Student multiple courses enroll karega.
        #
        # Isliye dictionary bana rahe hain.
        #
        # Key:
        # Course ID
        #
        # Value:
        # Complete Course Object
        #
        # Example:
        #
        # {
        #     "CS101": dsa_course_object,
        #     "CS102": oop_course_object
        # }
        # ====================================================

        self.courses = {}

    # ========================================================
    # Add Course
    # ========================================================
    # Jab koi Course Student ko enroll karega,
    # tab Student bhi us Course ko yaad rakhega.
    # ========================================================

    def add_course(self, course):

        # Dictionary me complete Course Object store ho raha hai.
        self.courses[course.course_id] = course

    # ========================================================
    # CGPA Setter
    # ========================================================

    def set_cgpa(self, new_cgpa):

        # CGPA 0 se 4 ke beech honi chahiye.
        if new_cgpa < 0 or new_cgpa > 4:
            raise ValueError("CGPA must be between 0 and 4")

        # Private variable.
        self.__cgpa = new_cgpa

    # ========================================================
    # Display
    # ========================================================

    def display(self):

        # Person information.
        super().display()

        # Student ki own information.
        print(f"Student ID : {self.student_id}")
        print(f"Semester : {self.semester}")
        print(f"CGPA : {self.__cgpa}")
        print(f"Present : {self.attendance['Present']}")
        print(f"Absent : {self.attendance['Absent']}")



# ============================================================
# COURSE CLASS
# ============================================================
# Course independent class hai.
#
# Ye Student ka child nahi.
#
# Ye Teacher ka child nahi.
#
# Ye apni separate entity hai.
#
# Kyun?
#
# Real university me bhi Course alag cheez hota hai.
# Teacher badal sakta hai.
# Students badal sakte hain.
#
# Lekin Course exist karta rehta hai.
# ============================================================

class Course:

    # Constructor
    def __init__(self, course_id, course_name, credit_hours):

        # Unique Course ID.
        self.course_id = course_id

        # Course Name.
        self.course_name = course_name

        # Credit Hours.
        self.credit_hours = credit_hours

        # ====================================================
        # Teacher
        # ====================================================
        # Shuru me Course ke paas teacher nahi hai.
        #
        # Example:
        #
        # Teacher = None
        #
        # Baad me:
        #
        # Teacher = Sir Wani Object
        # ====================================================

        self.teacher = None

        # ====================================================
        # Students Dictionary
        # ====================================================
        #
        # Is Course me jitne students enrolled honge,
        # sab yahan store honge.
        #
        # Example:
        #
        # {
        #     101: haseeb_object,
        #     102: ahmed_object
        # }
        # ====================================================

        self.students = {}


    # ========================================================
    # Assign Teacher
    # ========================================================
    # Ye method Teacher aur Course dono ko connect karta hai.
    # ========================================================

    def assign_teacher(self, teacher):

        # Step 1
        # Course ko teacher mil gaya.
        self.teacher = teacher

        # Step 2
        # Teacher ko bhi pata chal gaya
        # ke woh ye course padha raha hai.
        teacher.add_course(self)

    # ========================================================
    # Enroll Student
    # ========================================================
    # Ye method Student aur Course dono ko connect karta hai.
    # ========================================================

    def enroll_student(self, student):

        # Step 1
        # Course ko Student mil gaya.
        self.students[student.student_id] = student

        # Step 2
        # Student ko bhi pata chal gaya
        # ke usne ye Course enroll kiya hai.
        student.add_course(self)

    # ========================================================
    # Display
    # ========================================================

    def display(self):

        print(f"Course ID : {self.course_id}")
        print(f"Course Name : {self.course_name}")
        print(f"Credit Hours : {self.credit_hours}")

# ============================================================
# ATTENDANCE DICTIONARIES
# ============================================================
# Ye dummy data hai.
# Real project me ye database se ayega.
# ============================================================

student_attendance = {
    "Present": 25,
    "Absent": 2
}

teacher_attendance = {
    "Present": 40,
    "Absent": 1
}


# ============================================================
# CREATE ADMIN OBJECT
# ============================================================

admin = Admin(
    admin_id=1,
    name="Ali",
    age=35,
    email="ali@gmail.com"
)


# ============================================================
# CREATE TEACHER OBJECTS
# ============================================================

sir_wani = Teacher(
    name="Sir Wani",
    age=40,
    email="wani@gmail.com",
    teacher_id="T101",
    subject="Data Structures",
    department="Computer Science",
    salary=150000,
    attendance=teacher_attendance
)

sir_ahmed = Teacher(
    name="Sir Ahmed",
    age=38,
    email="ahmed@gmail.com",
    teacher_id="T102",
    subject="Object Oriented Programming",
    department="Computer Science",
    salary=145000,
    attendance=teacher_attendance
)


# ============================================================
# CREATE STUDENT OBJECTS
# ============================================================

haseeb = Student(
    name="Muhammad Haseeb",
    age=21,
    email="haseeb@gmail.com",
    student_id=101,
    semester=3,
    cgpa=3.58,
    attendance=student_attendance
)

ahmed = Student(
    name="Ahmed",
    age=22,
    email="ahmed123@gmail.com",
    student_id=102,
    semester=3,
    cgpa=3.21,
    attendance=student_attendance
)

usman = Student(
    name="Usman",
    age=21,
    email="usman@gmail.com",
    student_id=103,
    semester=5,
    cgpa=3.82,
    attendance=student_attendance
)


# ============================================================
# CREATE COURSE OBJECTS
# ============================================================

dsa = Course(
    course_id="CS201",
    course_name="Data Structures",
    credit_hours=4
)

oop = Course(
    course_id="CS202",
    course_name="Object Oriented Programming",
    credit_hours=3
)


# ============================================================
# ASSIGN TEACHERS
# ============================================================
# Is point par:
#
# Course ko Teacher mil raha hai.
#
# Aur Teacher ko bhi Course yaad ho raha hai.
# ============================================================

dsa.assign_teacher(sir_wani)

oop.assign_teacher(sir_ahmed)


# ============================================================
# ENROLL STUDENTS
# ============================================================
# Is point par:
#
# Course ko Student mil raha hai.
#
# Student ko bhi Course yaad ho raha hai.
# ============================================================

dsa.enroll_student(haseeb)

dsa.enroll_student(ahmed)

oop.enroll_student(haseeb)

oop.enroll_student(usman)


# ============================================================
# ADMIN ACTIONS
# ============================================================
# Admin validation ke through Student update kar raha hai.
# ============================================================

admin.change_student_name(haseeb, "Captain Haseeb")

admin.change_student_email(
    ahmed,
    "ahmed_new@gmail.com"
)

admin.change_student_cgpa(
    usman,
    3.95
)


# ============================================================
# DISPLAY
# ============================================================

print("\n========== ADMIN ==========\n")
admin.display()


print("\n========== TEACHER ==========\n")
sir_wani.display()


print("\n========== STUDENT ==========\n")
haseeb.display()


print("\n========== COURSE ==========\n")
dsa.display()


# ============================================================
# CHECK RELATIONSHIPS
# ============================================================

print("\n========== DSA STUDENTS ==========\n")

for student in dsa.students.values():
    student.display()
    print()


print("\n========== HASEEB COURSES ==========\n")

for course in haseeb.courses.values():
    course.display()
    print()


print("\n========== SIR WANI COURSES ==========\n")

for course in sir_wani.courses.values():
    course.display()
    print()