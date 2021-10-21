# Zadanie 1
name = "Martyna"
surname = "Jurczak"

def say_hello(name: str,surname: str) -> str:
    return f'Cześć {name} {surname}!'

text = say_hello(name, surname)
print(text)


# Zadanie 2
def multiplication(a: int, b: int) -> int:
    return a*b

print(multiplication(3, 4))


# Zadanie 3
def isEvenNumber(a: int) -> bool:
    return a%2==0

isEven = isEvenNumber(3)

if isEven:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")


# Zadanie 4
def isSumGreater(a: int, b: int, c: int) -> bool:
    return a + b >= c

print(isSumGreater(3, 4, 2))
print(isSumGreater(3, 4, 10))


# Zadanie 5
def isThere(list: list, a: int) -> bool:
    for number in list:
        if number==a:
            return True
    return False

list = [1, 2, 3, 4, 5]
print(isThere(list, 3))
print(isThere(list, 6))


# Zadanie 6
def mergeLists(listA: list, listB: list) -> list:
    list = []
    for number in listA + listB:
        if number not in list:
            list.append(number**3)
    return list

listA = [1, 2, 3, 3, 4]
listB = [3, 4, 5, 6, 7]
print(mergeLists(listA, listB))