# Zadanie 2a
name1 = "Martyna"
name2 = "Anna"
name3 = "Joanna"
name4 = "Patrycja"
name5 = "Wiktoria"

def print_names(str_name1, str_name2, str_name3, str_name4, str_name5):
    print(f'{str_name1}, {str_name2}, {str_name3}, {str_name4}, {str_name5}')

print_names(name1, name2, name3, name4, name5)


# Zadanie 2b i
list = [1, 2, 3, 4, 5]
def multiply_numbers(list):
    list2 = []
    for i in range(len(list)):
        list2.append(list[i]*2)
    return list2

print(multiply_numbers(list))


# Zadanie 2b ii
def multiply_numbers2(list):
    list2 = []
    for number in list:
        list2.append(number*2)
    return list2

print(multiply_numbers2(list))


# Zadanie 2c
list2c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(list2c)):
    if list2c[i]%2==0:
        print(list2c[i])

# Zadanie 2d
list2d = [1, 3, 9, 12, 15, 18, 21, 24, 27, 30]
for i in range(len(list2d)):
    if i%2==0:
        print(list2d[i])