#assignment 1
class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def display_student(self):
        print(f"Student: {self.name}, Roll No: {self.roll_number}, Grade: {self.grade}")

    def is_passed(self):
        return "Passed!" if self.grade >= 50 else "Failed."

# Creating an instance
student1 = Student("Alice", 101, 75)
student2 = Student("Elizabeth", 700, 100)
student1.display_student()
student2.display_student()
print(student1.is_passed())  # Output: Passed!
print(student2.is_passed())