# class Student:

#     def __init__(self, name, cgpa):
#         self.name = name
#         self.set_cgpa(cgpa)

#     def get_cgpa(self):
#         return self.__cgpa
        

#     def set_cgpa(self, cgpa):
#         if 0 <= cgpa <= 4:
#             self.__cgpa = cgpa
#         else:
#             print("Invalid")
        

#     def display(self):
#         print(f"Name: {self.name}, CGPA: {self.get_cgpa()}")



# class Person:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Email: {self.email}")

# class Student(Person):
#     def __init__(self, name, age, email, cgpa):
#         super().__init__(name, age, email)
#         self.cgpa

#     def display(self):
#         super().display()
#         print(f"CGPA: {self.cgpa}")

# class Teacher(Person):
#     def __init__(self, name, age, email, subject, salary):
#         super().__init__(name, age, email)
#         self.subject = subject
#         self.salary = salary

#     def display(self):
#         super().display()
#         print(f"Subject: {self.subject}")
#         print(f"Salary: {self.salary}") 

# haseeb = Teacher("Muhammad Haseeb", 20, "muhammadhaseeb@gmail.com", "Python", 500000)

# haseeb.display() 


# class Person:
#     def display(self):
#         print("Person")

# class Student(Person):
#     pass

# haseeb = Student()
# haseeb.display()


# class Person:
#     def display(self):
#         print("Person")

# class Student(Person):
#     def display(self):
#         print("Student")

# class Topper(Student):
#     pass

# haseeb = Topper()
# haseeb.display()

# class Person:
#     def display(self):
#         print("Person")


# class Student(Person):
#     def display(self):
#         print("Student")


# class Topper(Student):
#     def display(self):
#         super().display()
#         print("Topper")


# haseeb = Topper()
# haseeb.display()


# class Person:
#     def display(self):
#         print("Person")

# class Student(Person):
#     def display(self):
#         print("Student")

# class Teacher(Person):
#     def display(self):
#         print("Teacher")

# def show(person):
#     person.display()

# show(Student())
# show(Teacher())

# class Person:
#     def display(self):
#         print("Person")


# def show(person):
#     person.display()


# show(Person())
# show("Hello")

# class Dog:
#     def display(self):
#         print("Woof!")

# class Student:
#     def display(self):
#         print("Student")

# def show(obj):
#     obj.display()

# show(Dog())
# show(Student())





# class Student:
#     def __init__(self, name, cgpa):
#         self.name = name
#         self.cgpa = cgpa

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"CGPA: {self.cgpa}")

# ali = Student("Ali", 3.6)
# ahmed = Student("Ahmed", 3.4)

# students = {
#     101: ali,
#     102: ahmed
# }

# print("University Records")
# students[101].display()
# students[102].display()


# student = students[102]
# student.cgpa = 3.99

# print("After Updating")

# print("student variable:")
# student.display()

# print("ahmed variable:")
# ahmed.display() 


class Pokemon:
    def __init__(self, pokemon_id, name):
        self.pokemon_id = pokemon_id
        self.name = name

    def display(self):
        print(f"Pokemon ID: {self.pokemon_id}")
        print(f"Pokemon Name: {self.name}")

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = {}


pikachu = Pokemon(1, "Pikachu")

ash = Trainer("Ash")