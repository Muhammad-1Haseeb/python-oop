# # class Student:
# #     def __init__(self, name, age, rollno, cgpa):
# #         self.name = name
# #         self.age = age
# #         self.rollno = rollno
# #         self.cgpa = cgpa

# #     def change_name(self, new_name):
# #         self.name = new_name
        
# #     def display(self):
# #         print(self.name)
# #         print(self.age)
# #         print(self.rollno)
# #         print(self.cgpa)

# # haseeb = Student("Muhammad Haseeb", 20, 1234, 3.5)
# # haseeb.display()

# # haseeb.change_name("Muhammad Haseeb Khan")
# # haseeb.display()


# class Student:
#     def __init__(self, name, cgpa):
#         self.name = name
#         self.cgpa = None   # default value set kar di
#         self.set_cgpa(cgpa)

#     def set_cgpa(self, cgpa):
#         if 0 <= cgpa <= 4:
#             self.cgpa = cgpa
#         else:
#             print("CGPA 0 aur 4 ke beech hona chahiye")

#     def show(self):
#         print("Name:", self.name, "CGPA:", self.cgpa)


# haseeb = Student("Haseeb", 100)   # galat value
# haseeb.show()

# ali = Student("Ali", 3.2)         # sahi value
# ali.show()

# ali.set_cgpa(4)                   # update
# ali.show()

# ali.set_cgpa(-1)                  # galat update
# ali.show()




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

# class Student(Person):
#     def __init__(self, name, age, email, cgpa):
#         super().__init__(name, age, email)
#         self.cgpa = cgpa

# haseeb = Student("Haseeb", 20, "muhammadhaseeb@gmail.com", 3.6)

# print(haseeb.name, haseeb.age, haseeb.email, haseeb.cgpa)

# class Person:
#     def display(self):
#         print("Person Display")

# class Student(Person):
#     def display(self):
#         print("Student Display")

# haseeb = Student()
# haseeb.display()



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
#     def __init__(self, name, age, email,cgpa):
#         super().__init__(name, age, email)
#         self.cgpa

#     def display(self):
#         super().display()
#         print(f"CGPA: {self.cgpa}")

# haseeb = Student("Muhammad Haseeb", 20, "muhammadhaseeb@gmail.com", 3.6)

# haseeb.display()


# class Dog:
#     def speak(self):
#         print("Woof")


# class Cat:
#     def speak(self):
#         print("Meow")


# class Human:
#     def speak(self):
#         print("Hello")

# def make_sound(obj):
#     obj.speak()

# make_sound(Dog())
# make_sound(Cat())
# make_sound(Human())


# from abc import ABC, abstractmethod

# class Person(ABC):

#     @abstractmethod
#     def login(self):
#         print("Login method must be implemented in the subclass")


# class Student(Person):
#     def login(self):
#         super().login()


# haseeb = Student()
# haseeb.login()

# from abc import ABC, abstractmethod

# class Person(ABC):

#     @abstractmethod
#     def login(self):
#         pass


# class Student(Person):

#     def login(self):
#         print("Student Login")


# haseeb = Student()
# haseeb.login()

# from abc import ABC, abstractmethod

# class Person(ABC):

#     @abstractmethod
#     def login(self):
#         pass


# class Student(Person):

#     def login(self):
#         print("Student Login")


# # person = Person()
# student = Student()



class Student:
    def __init__(self,name ,age ,rollno ,cgpa):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.set_cgpa(cgpa)


    def set_cgpa(self, cgpa):
        if 0 <= cgpa <= 4:
            self.__cgpa = cgpa
        else:
            raise ValueError("Invalid CGPA")
        
    def display(self):
        # print(f"Name: {self.name}")
        # print(f"Age: {self.age}")
        # print(f"Roll No: {self.rollno}")
        # print(f"CGPA: {self.__cgpa}")
        return f"Name: {self.name}, Age: {self.age}, Roll No: {self.rollNo}, CGPA: {self.__cgpa}"

    def change_name(self, new_name):
        self.name = new_name


haseeb = Student("Muhammad Haseeb", 20, "12345", 3.6)
haseeb.display()
haseeb.change_name("Haseeb")
haseeb.display()
