class Student:
    def __init__(self, name, max_marks):
        self.name = name
        self.marks = {}
        self.max_marks = max_marks

    def __add__(self, subject, mark):
        self.marks[subject] = mark

    def totalMarks(self):
        return sum(self.marks.values())

    def percentage(self):
        total_obtained = self.totalMarks()
        total_possible = len(self.marks) * self.max_marks
        return (total_obtained / total_possible) * 100 if total_possible > 0 else 0


student = Student("Bob", 100)
student.__add__("English", 95)
student.__add__("Physics", 60)
student.__add__("Mathematics", 40)

print("All marks", student.totalMarks())
print("Percent", student.percentage())
