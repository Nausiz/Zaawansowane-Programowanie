import csv


def read_file(file_name: str) -> list:
    with open(file_name, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        list_file = []
        for row in csv_reader:
            list_file.append(row)
        list_file.remove(list_file[0])
    return list_file
