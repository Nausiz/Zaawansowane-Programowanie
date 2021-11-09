class Firma:
    def __init__(self, nazwa: str, ilosc_pracownikow: int, region: str, branza: str):
        self._nazwa = nazwa
        self._ilosc_pracownikow = ilosc_pracownikow
        self._region = region
        self._branza = branza

    def __str__(self):
        return f"Nazwa firmy: {self._nazwa}; Ilość pracowników: {self._ilosc_pracownikow};" \
               f" Region: {self._region}; Branża: {self._branza}"

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def ilosc_pracownikow(self) -> int:
        return self._ilosc_pracownikow

    @property
    def region(self) -> str:
        return self._region

    @property
    def branza(self) -> str:
        return self._branza


class FirmaTransportowa(Firma):
    def __init__(self, nazwa: str, ilosc_pracownikow: int, region: str, branza: str, ile_przewozow_rocznie: int):
        super().__init__(nazwa, ilosc_pracownikow, region, branza)
        self._ile_przewozow_rocznie = ile_przewozow_rocznie

    def __str__(self):
        return f"Dane firmy: {Firma}; Ilość rocznych przewozów: {self._ile_przewozow_rocznie}"

    @property
    def ile_przewozow_rocznie(self) -> int:
        return self._ile_przewozow_rocznie


class FirmaSpozyczwa(Firma):
    def __init__(self, nazwa: str, ilosc_pracownikow: int, region: str, branza: str, produkt: str):
        super().__init__(nazwa, ilosc_pracownikow, region, branza)
        self._produkt = produkt

    def __str__(self):
        return f"Dane firmy: {Firma}; Produkt: {self._produkt}"

    @property
    def produkt(self) -> str:
        return self._produkt


class Pojazd:
    def __init__(self, marka: str, przebieg: int, pojemnosc: int, rocznik: int, stan: str):
        self._marka = marka
        self._przebieg = przebieg
        self._pojemnosc = pojemnosc
        self._rocznik = rocznik
        self._stan = stan

    def __str__(self):
        return f"Marka: {self._marka}; Przebieg: {self._przebieg};" \
               f" Pojemnosc: {self._pojemnosc}; Rocznik: {self._rocznik}; Stan: {self._stan}"

    @property
    def marka(self) -> str:
        return self._marka

    @property
    def przebieg(self) -> int:
        return self._przebieg

    @property
    def pojemnosc(self) -> int:
        return self._pojemnosc

    @property
    def rocznik(self) -> int:
        return self._rocznik

    @property
    def stan(self) -> str:
        return self._stan


class Odcinek:
    def __init__(self, od: str, do: str, dlugosc: float, czy_odcinki_platne: bool, czas: int):
        self._od = od
        self._do = do
        self._dlugosc = dlugosc
        self._czy_odcinki_platne = czy_odcinki_platne
        self._czas = czas

    def __str__(self):
        return f"Od: {self._od}; Do: {self._do};" \
               f" Długość: {self._dlugosc}; Czy są odcinki płatne: {self._czy_odcinki_platne}; Czas (dni): {self._czas}"

    @property
    def od(self) -> str:
        return self._od

    @property
    def do(self) -> str:
        return self._do

    @property
    def dlugosc(self) -> float:
        return self._dlugosc

    @property
    def czy_odcinki_platne(self) -> bool:
        return self._czy_odcinki_platne

    @property
    def czas(self) -> int:
        return self._czas


class Kurs:
    def __init__(self, pojazd: Pojazd, kierowca: str, odcinki: list,
                 od_firma: FirmaTransportowa, do_firma: FirmaSpozyczwa):
        self._pojazd = pojazd
        self._kierowca = kierowca
        self._odcinki = odcinki
        self._od_firma = od_firma
        self._do_firma = do_firma

    def __str__(self):
        return f"Dane pojazdu: {self._pojazd}; Kierowca: {self._kierowca};" \
               f" Odcinki: {self._odcinki}; Od: {self._od_firma}; Do: {self._do_firma}"

    def suma(self) -> int:
        a = 0
        for odcinek in self._odcinki:
            a += odcinek.dlugosc
        return round(a, 2)

    def marka_pojazdu(self) -> str:
        return self._pojazd.marka

    @property
    def pojazd(self) -> Pojazd:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, value: Pojazd) -> None:
        self._pojazd = value

    @property
    def kierowca(self) -> str:
        return self._kierowca

    @kierowca.setter
    def kierowca(self, value: str) -> None:
        self._kierowca = value

    @property
    def odcinki(self) -> list:
        return self._odcinki

    @odcinki.setter
    def odcinki(self, value: list) -> None:
        self._odcinki = value

    @property
    def od_firma(self) -> FirmaTransportowa:
        return self._od_firma

    @od_firma.setter
    def od_firma(self, value: FirmaTransportowa) -> None:
        self._od_firma = value

    @property
    def do_firma(self) -> FirmaSpozyczwa:
        return self._do_firma

    @do_firma.setter
    def do_firma(self, value: FirmaSpozyczwa) -> None:
        self._do_firma = value


pojazd1 = Pojazd("Opel", 130000, 2000, 2005, "Bardzo dobry")
odcinek1 = Odcinek("Katowice", "Mysłowice", 14.5, False, 0)
odcinek2 = Odcinek("Mysłowice", "Kraków", 80.3111, True, 0)
odcinek3 = Odcinek("Kraków", "Warka", 372.12, False, 0)
odcinki1 = [odcinek1, odcinek2, odcinek3]
firma1 = FirmaTransportowa("Transpolex", 30, "śląsk", "transport", 1200)
firma2 = FirmaSpozyczwa("Cukierki u Małgosi", 16, "wielkopolskie", "spożywcza", "ciastka")

kurs1 = Kurs(pojazd1, "Artur Kowalski", odcinki1, firma1, firma2)

print(kurs1)

print(kurs1.suma())
print(kurs1.marka_pojazdu())
