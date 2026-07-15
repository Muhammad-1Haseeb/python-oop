# Sab se pehly person class or usme 1 constructor jo name age email set kery ga or name hum private rekhy gy 

class Person:
    def __init__(self, name, age, email):
        self.set_name(name)
        self.set_age(age)
        self.set_email(email)

# aik setter bnaye gy jisme name ki validation hogi 
    def set_name(self, new_name):
        if new_name.strip() == "":
            raise ValueError("Empty value is not accepted")
        self.__name = new_name

    def set_age(self, new_age):
        if new_age <= 0:
            raise ValueError("Age must be greater than 0")
        self.__age = new_age

    def set_email(self, new_email):
        if not new_email.endswith("@gmail.com"):
            raise ValueError("Invalid Email")
        self.__email = new_email

        

# or aik display bnaye gy 
    def display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Email: {self.__email}")

class Admin(Person):
    def __init__(self,admin_id, name, age, email):
        super().__init__(name, age, email)
        self.admin_id = admin_id

    def change_student_name(self, student, new_name):
        student.set_name(new_name)

    def change_student_cgpa(self, student, new_cgpa):
        student.set_cgpa(new_cgpa)

    def change_student_email(self, student, new_email):
        student.set_email(new_email)

    
    def display(self):
        super().display()
        print(f"Admin ID: {self.admin_id}")


class Teacher(Person):
    def __init__(self, name, age, email, teacher_id, subject, department, salary, attendance):
        super().__init__(name, age, email)
        self.teacher_id = teacher_id
        self.subject = subject
        self.department = department
        self.set_salary(salary)
        self.attendance = attendance

    def set_salary(self, new_salary):
        if new_salary <= 0:
            raise ValueError("Salary must be greater than or equal to 0")
        self.salary = new_salary



    def display(self):
        super().display()
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Subject: {self.subject}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print(f"Present: {self.attendance['Present']}")
        print(f"Absent: {self.attendance['Absent']}")

# Student constructor: `student_id`, `semester`, `cgpa`, `attendance`.
# Use `self.set_cgpa(cgpa)` to assign CGPA (validation is reused).
class Student(Person):
    def __init__(self, name, age, email, student_id, semester, cgpa, attendance):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.semester = semester
        self.set_cgpa(cgpa)
        self.attendance = attendance
        self.marks = {} # Dictionary to store marks yeh baad me jb teacher marks add kery ga to ye dictionary me store ho gy
    

    def set_cgpa(self, new_cgpa):
        if new_cgpa < 0 or new_cgpa > 4:
            raise ValueError("CGPA must be between 0 and 4")
        self.__cgpa = new_cgpa

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")
        print(f"Semester: {self.semester}")
        print(f"CGPA: {self.__cgpa}")
        print(f"Present: {self.attendance['Present']}")
        print(f"Absent: {self.attendance['Absent']}")
