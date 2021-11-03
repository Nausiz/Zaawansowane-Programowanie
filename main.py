# Zadanie 2a
def print_names(list_names):
    for name in list_names:
        print(name)


print_names(["Martyna", "Anna", "Joanna", "Patrycja", "Wiktoria"])


# Zadanie 2b i
def multiply_numbers(list1):
    list2 = []
    for number in list1:
        list2.append(number*2)
    return list2


print(multiply_numbers([1, 2, 3, 4, 5]))


# Zadanie 2b ii
def multiply_numbers2(list_numbers):
    list2 = []
    for number in list_numbers:
        list2.append(number*2)
    return list2


print(multiply_numbers2([1, 2, 3, 4, 5]))


# Zadanie 2c
list2c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list2c:
    if i % 2 == 0:
        print(i)


# Zadanie 2d
list2d = [1, 3, 9, 12, 15, 18, 21, 24, 27, 30]
for i in list2d:
    if i % 2 == 0:
        print(i)
