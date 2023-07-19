# Create a Python class called "Student" with the following fields and methods:

# Fields:
# name (string)
# age (integer)
# grade (integer)

# Methods:
# promote(): Increases the student's grade by 1.
# get_details(): Prints the student's name, age, and grade in the following format: "Name: [name], Age: [age], Grade: [grade]".

class Student:

    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade
    
    def promote(self):
        self.grade += 1

    def get_details(self):
        print("Name: [%s], Age: [%s], Grade: [%s]" % (self.name, self.age, self.grade))

student = Student("Andrii", 20, 4)
student.get_details()