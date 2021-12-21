class Developer:
    def __init__(self, imie: str, nazwisko: str, numer_telefonu: str, staz: int):
        self._imie = imie
        self._nazwisko = nazwisko
        self._numer_telefonu = numer_telefonu
        self._staz = staz

    def __str__(self):
        return f"Imię: {self._imie}; Nazwisko: {self._nazwisko};" \
               f" Numer telefonu: {self._numer_telefonu}; Staż pracy (w latach): {self._staz}"

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def numer_telefonu(self) -> str:
        return self._numer_telefonu

    @property
    def staz(self) -> int:
        return self._staz


developer1 = Developer("Arkadiusz", "Nowak", "222333444", 3)
