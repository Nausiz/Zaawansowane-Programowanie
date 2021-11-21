import University.Student as Student
import University.Employee as Employee
import University.Book as Book


class Order:
    def __init__(self, employee: Employee, student: Student, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        bookinf = ""
        for book in self.books:
            bookinf += str(book) + " "

        return f"Informacje o zamówieniu: " \
               f"{self.employee};" \
               f"{self.student};" \
               f"{bookinf}" \
               f"Data zamówienia: {self.order_date}"


order1 = Order(Employee.employee1, Student.student1, [Book.book1, Book.book2], "25.10.21")
order2 = Order(Employee.employee2, Student.student3, [Book.book3, Book.book4, Book.book5], "12.09.21")
