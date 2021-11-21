class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}; Ocena: {self.marks} %"

    def is_passed(self) -> bool:
        return self.marks > 50


first_Student = Student("Daniel", 60)
second_Student = Student("Karol", 40)

student1 = Student("Krystyna", 78)
student2 = Student("Magdalena", 49)
student3 = Student("Dawid", 65)
