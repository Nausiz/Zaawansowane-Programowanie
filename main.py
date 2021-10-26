#Zadanie 1

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

print("Zadanie 1")
print(first_Student.is_passed())
print(second_Student.is_passed())


#Zadanie 2
class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka w {self.city} na ulicy {self.street}; Kod pocztowy: {self.zip_code}. " \
               f"Otwarta w godzinach: {self.open_hours}. Numer telefonu: {self.phone}"

class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str,
                 city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}," \
               f"Zatrudniony: {self.hire_date}," \
               f"Urodzony: {self.birth_date}," \
               f"Adres: {self.city} {self.street}, {self.zip_code}," \
               f"Numer telefonu: {self.phone}"

class Order:
    def __init__(self, employee: Employee, student: Student, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        bookInfo = ""
        for book in self.books:
            bookInfo += str(book) + " "

        return f"Informacje o zamówieniu: " \
               f"{self.employee};" \
               f"{self.student};" \
               f"{bookInfo}" \
               f"Data zamówienia: {self.order_date}"

class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka z biblioteki: {self.library};" \
               f"Opublikowana: {self.publication_date};" \
               f"Autor: {self.author_name} {self.author_surname};" \
               f"Liczba stron: {str(self.number_of_pages)}"

library1 = Library("Katowice", "Mickiewicza 12", "40-600", "8:00-17:00", "600700444")
library2 = Library("Mysłowice", "Sienkiewicza 7", "43-600", "9:00-18:30", "700600888")

book1 = Book(library1, "21.08.06", "Anna", "Nowak", 234)
book2 = Book(library2, "01.12.99", "Agnieszka", "Kowalska", 134)
book3 = Book(library1, "11.06.12", "Marek", "Konieczny", 434)
book4 = Book(library2, "06.04.02", "Jacek", "Marchewka", 150)
book5 = Book(library1, "23.10.00", "Agata", "Kwiatkowska", 231)

employee1 = Employee("Martyna", "Malinowska", "03.04.20", "12.02.99", "Katowice", "3 Maja 17", "40-700", "555666777")
employee2 = Employee("Łukasz", "Kowalski", "15.07.12", "15.12.99", "Gliwice", "Polna 4", "42-722", "666777888")
employee3 = Employee("Antoni", "Słoikowski", "02.01.18", "12.02.95", "Tychy", "Gierałtowskiego 5", "41-700", "777888999")

student1 = Student("Krystyna", 78)
student2 = Student("Magdalena", 49)
student3 = Student("Dawid", 65)

order1 = Order(employee1, student1, [book1, book2], "25.10.21")
order2 = Order(employee2, student3, [book3, book4, book5], "12.09.21")

print("Zadanie 2")
print(order1)
print(order2)


#Zadanie 3
class Property:
    def __init__(self, area: str, rooms: int, price: int, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area: str, rooms: int, price: int, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Okolica: {self.area}; Pokoje: {self.rooms}; Cena: {self.price}; Adres: {self.address}; Rozmiar działki: {self.plot}"

class Flat(Property):
    def __init__(self, area: str, rooms: int, price: int, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Okolica: {self.area}; Pokoje: {self.rooms}; Cena: {self.price}; Adres: {self.address}; Piętro: {self.floor}"

house = House("Wieś", 7, 340000, "Mała Wieś 123 41-500", 1400)
flat = Flat("Miasto", 4, 210000, "Katowice 3 Maja 2 41-500", 120)

print("Zadanie 3")
print(house)
print(flat)
