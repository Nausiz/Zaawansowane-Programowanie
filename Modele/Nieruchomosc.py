class Nieruchomosc:
    def __init__(self, miasto: str, cena: float, rozmiar: float):
        self._miasto = miasto
        self._cena = cena
        self._rozmiar = rozmiar

    @property
    def miasto(self) -> str:
        return self._miasto

    @property
    def cena(self) -> float:
        return self._cena

    @property
    def rozmiar(self) -> float:
        return self._rozmiar


class Dom(Nieruchomosc):
    def __init__(self, miasto: str, cena: float, rozmiar: float, wykonczony: bool):
        super().__init__(miasto, cena, rozmiar)
        self._wykonczony = wykonczony

    def __str__(self):
        return f"Miasto: {self._miasto}; Cena: {self._cena};" \
               f" Rozmiar(m2): {self._rozmiar}; Czy wykończony: {self._wykonczony};"

    @property
    def wykonczony(self) -> bool:
        return self._wykonczony


class Mieszkanie(Nieruchomosc):
    def __init__(self, miasto: str, cena: float, rozmiar: float, pietro: int):
        super().__init__(miasto, cena, rozmiar)
        self._pietro = pietro

    def __str__(self):
        return f"Miasto: {self._miasto}; Cena: {self._cena};" \
               f" Rozmiar(m2): {self._rozmiar}; Piętro: {self._pietro};"

    @property
    def pietro(self) -> int:
        return self._pietro
