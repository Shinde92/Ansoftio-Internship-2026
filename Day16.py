# Create Student class
class Student:
    
    # Constructor to initialize values
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method to display details
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Create object of Student class
s1 = Student("Shraddha", 27, "MCA-Engineering")

# Print student details
s1.display()
