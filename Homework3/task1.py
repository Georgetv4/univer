import csv

# open csv-file and read it
with open('hw3_problem1_mod.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)

    city_dict = {}

    for row in reader:
        if not all(field.isalpha() for field in row[:-1]) or not row:
            print("Incorrect input")
            break

        # извлекаем данные из строки
        first_name, last_name, phone, city = row

        # добавляем данные в словарь
        if city not in city_dict:
            city_dict[city] = {}
        if last_name not in city_dict[city]:
            city_dict[city][last_name] = 0
        city_dict[city][last_name] += 1

    # выводим результаты
    for city, city_data in city_dict.items():
        print(city, ':')
        for last_name, count in city_data.items():
            print('  ', last_name, ':', count)
