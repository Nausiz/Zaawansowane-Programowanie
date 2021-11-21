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


employee1 = Employee("Martyna", "Malinowska", "03.04.20", "12.02.99",
                     "Katowice", "3 Maja 17", "40-700", "555666777")
employee2 = Employee("Łukasz", "Kowalski", "15.07.12", "15.12.99",
                     "Gliwice", "Polna 4", "42-722", "666777888")
employee3 = Employee("Antoni", "Słoikowski", "02.01.18", "12.02.95",
                     "Tychy", "Gierałtowskiego 5", "41-700", "777888999")
