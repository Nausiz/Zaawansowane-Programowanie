from Modele import Developer
from Modele import Nieruchomosc


class Zamowienie:
    def __init__(self, developer: Developer, nieruchomosci: list, numer: int, nabywca: str):
        self._developer = developer
        self._nieruchomosci = nieruchomosci
        self._numer = numer
        self._nabywca = nabywca

    def __str__(self):
        tekst = f"Developer: {self._developer}; Nieruchomosc:"
        for nieruchomosc in self._nieruchomosci:
            tekst += f"{nieruchomosc};"
        return tekst + f" Numer zamówienia: {self._numer}; Nabywca: {self._nabywca}"

    @property
    def developer(self) -> Developer:
        return self._developer

    @developer.setter
    def developer(self, value: developer) -> None:
        self._developer = value

    @property
    def nieruchomosci(self) -> list:
        return self._nieruchomosci

    @nieruchomosci.setter
    def nieruchomosci(self, value: nieruchomosci) -> None:
        self._nieruchomosci = value

    @property
    def numer(self) -> int:
        return self._numer

    @numer.setter
    def numer(self, value: numer) -> None:
        self._numer = value

    @property
    def nabywca(self) -> str:
        return self._nabywca

    @nabywca.setter
    def nabywca(self, value: nabywca) -> None:
        self._nabywca = value

    def wartosc_zamowienia(self) -> float:
        wartosc = 0
        for nieruchomosc in self._nieruchomosci:
            wartosc += nieruchomosc.cena
        return round(wartosc, 2)

    def suma_metrow(self) -> float:
        suma_metrow = 0
        for nieruchomosc in self._nieruchomosci:
            suma_metrow += nieruchomosc.rozmiar
        return suma_metrow


developer1 = Developer.developer1
nieruchomosc1 = Nieruchomosc.Mieszkanie("Katowice", 230000.333, 150, 2)
nieruchomosc2 = Nieruchomosc.Dom("Mysłowice", 542400.333, 200.345, True)
zamowienie1 = Zamowienie(developer1, [nieruchomosc1, nieruchomosc2], 45, "Agata Kowalska")
