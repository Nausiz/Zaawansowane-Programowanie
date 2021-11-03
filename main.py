# Zadanie 1
def say_hello(name: str, surname: str) -> str:
    return f'Cześć {name} {surname}!'


text = say_hello("Martyna", "Jurczak")
print(text)


# Zadanie 2
def multiplication(a: int, b: int) -> int:
    return a*b


print(multiplication(3, 4))


# Zadanie 3
def is_even_number(a: int) -> bool:
    return a % 2 == 0


isEven = is_even_number(3)

if isEven:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")


# Zadanie 4
def is_sum_greater(a: int, b: int, c: int) -> bool:
    return a + b >= c


print(is_sum_greater(3, 4, 2))
print(is_sum_greater(3, 4, 10))


# Zadanie 5
def is_there(list_num: list, a: int) -> bool:
    for number in list_num:
        if number == a:
            return True
    return False


list_numbers = [1, 2, 3, 4, 5]
print(is_there(list_numbers, 3))
print(is_there(list_numbers, 6))


# Zadanie 6
def merge_lists(list1: list, list2: list) -> list:
    list_merged = []
    for number in list1 + list2:
        if number not in list_merged:
            list_merged.append(number**3)
    return list_merged


listA = [1, 2, 3, 3, 4]
listB = [3, 4, 5, 6, 7]
print(merge_lists(listA, listB))
