# Part 1: Class Definition
class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")
        print("-" * 30)


# Part 2: Working with Objects

# Create 3 student objects
student1 = Student("Alice Johnson", "alice@example.com", [85, 90, 88])
student2 = Student("Bob Smith", "bob@example.com", [78, 82, 80])
student3 = Student("Charlie Brown", "charlie@example.com", [92, 95, 93])

# Add 2 new grades to each student
student1.add_grade(91)
student1.add_grade(87)

student2.add_grade(85)
student2.add_grade(88)

student3.add_grade(96)
student3.add_grade(94)

# Display information and average grade for each student
student1.display_info()
student2.display_info()
student3.display_info()


# Part 3: Dictionary & Set Integration

# Create a dictionary to map student names to their email addresses
student_dict = {
    student1.name: student1.email,
    student2.name: student2.email,
    student3.name: student3.email,
}

#Write a function get_student_by_email(email) that retrieves a student object from the dictionary safely using .get(). 

def get_student_by_email(email):
    for student in [student1, student2, student3]:
        if student.email == email:
            return student
        return None
    
# Create a set of all unique grades across all students and print it.

unique_grades = set(student1.grades + student2.grades + student3.grades)
print(f"Unique Grades Across All STudents: {unique_grades}")


# Part 4: Tuple Practice

# Add a method to the Student class called grades_tuple(self) that returns the grades as a tuple.

def grades_tuple(self):
    return tuple(self.grades)

# Demonstrate that tuples are immutable by trying to change a value (catch the exception with try/except and print a message).

try:
    grades = student1.grades_tuple()
    grades[0] = 100
except TypeError as e:
    print("Tuples are immutable, cannot change values.")
    
# Part 5: List Operations

# Remove the last grade from each student’s grades list using .pop().

student1.grades.pop()
student2.grades.pop()
student3.grades.pop()

# Access and print the first and last grade for each student.

for student in [student1, student2, student3]:
    if student.grades:
        print(f"{student.name} - First Grade: {student.grades[0]}, Last Grade: {student.grades[-1]}")
    else:
        print(f"{student.name} has no grades.")
        
# Print the number of grades each student has using len().

for student in [student1, student2, student3]:
    print(f"{student.name} has {len(student.grades)} grades.")
    
    
# Part 6: Bonus (Optional)

# Use regular expressions to validate that each student’s email follows the format: name@domain.com.

import re 
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
for student in [student1, student2, student3]:
    if re.match(email_pattern, student.email):
        print(f"{student.email} is a valid email.")
    else:
        print(f"{student.email} is not a valid email.")
        
# Count how many grades are above 90 across all students.
high_achievers_count = sum(1 for student in [student1, student2, student3] for grade in student.grades if grade > 90)
print(f"Number of grades above 90: {high_achievers_count}")

