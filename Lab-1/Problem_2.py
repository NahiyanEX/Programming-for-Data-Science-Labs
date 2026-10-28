# Defining a OOP style student class

class Student:
    def __init__(self, name, ID, age, dep, CGPA):
        self.name = name
        self.ID = ID
        self.age = age
        self.dep = dep
        self.CGPA = CGPA

# Creating a list of students

class main:
    
    students = [
        Student("Remi", "S001", 23, "Computer Science", 3.2),
        Student("Mike", "S002", 22, "Mathematics", 3.6)]

     #printing the list of students

    print("List of Students:")
    for student in students:
        print(f"Name: {student.name}, ID: {student.ID}, Age: {student.age}, Department: {student.dep}, CGPA: {student.CGPA}")
