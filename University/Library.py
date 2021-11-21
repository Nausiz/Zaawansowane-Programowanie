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


library1 = Library("Katowice", "Mickiewicza 12", "40-600", "8:00-17:00", "600700444")
library2 = Library("Mysłowice", "Sienkiewicza 7", "43-600", "9:00-18:30", "700600888")
