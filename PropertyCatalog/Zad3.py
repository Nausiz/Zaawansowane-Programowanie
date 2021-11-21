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
        return f"Okolica: {self.area}; Pokoje: {self.rooms}; Cena: {self.price}; " \
               f"Adres: {self.address}; Rozmiar działki: {self.plot}"


house = House("Wieś", 7, 340000, "Mała Wieś 123 41-500", 1400)


class Flat(Property):
    def __init__(self, area: str, rooms: int, price: int, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Okolica: {self.area}; Pokoje: {self.rooms}; Cena: {self.price};" \
               f" Adres: {self.address}; Piętro: {self.floor}"


flat = Flat("Miasto", 4, 210000, "Katowice 3 Maja 2 41-500", 120)