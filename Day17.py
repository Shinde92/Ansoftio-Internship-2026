# Parent class
class Person:
    
    # Constructor for Person
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Child class
class Student(Person):
    
    # Constructor for Student
    def __init__(self, name, age, course):
        # Call parent constructor
        super().__init__(name, age)
        self.course = course

    # Method to display all details
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Create object of Student class
s1 = Student("Shraddha", 27, "MCA-Engineering")

# Print details
s1.display()
