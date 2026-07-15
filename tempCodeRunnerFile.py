class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def display(self):
        print(f"Name: {self.name}")
        print(f"CGPA: {self.cgpa}")


# 3 Student objects banaye
ali = Student("Ali", 3.2)
ahmed = Student("Ahmed", 3.5)
haseeb = Student("Haseeb", 3.8)

# University ke records (Dictionary)
students = {
    101: ali,
    102: ahmed,
    103: haseeb
}

print("=== University Records ===")
students[101].display()
students[102].display()
students[103].display()

print("------------")

# Dictionary se Ahmed ka object nikala
student = students[102]

# CGPA change ki
student.cgpa = 4.0

print("After Updating")

print("student variable:")
student.display()

print("ahmed variable:")
ahmed.display()