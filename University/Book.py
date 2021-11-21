import University.Library as Library


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str,
                 author_surname: str, number_of_pages: int):
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


book1 = Book(Library.library1, "21.08.06", "Anna", "Nowak", 234)
book2 = Book(Library.library2, "01.12.99", "Agnieszka", "Kowalska", 134)
book3 = Book(Library.library1, "11.06.12", "Marek", "Konieczny", 434)
book4 = Book(Library.library2, "06.04.02", "Jacek", "Marchewka", 150)
book5 = Book(Library.library1, "23.10.00", "Agata", "Kwiatkowska", 231)
