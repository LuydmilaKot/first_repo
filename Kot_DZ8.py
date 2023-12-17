# №1
# a = b'r\xc3\xa9sum\xc3\xa9'
# s = a.decode('utf-8')
# print(s)
# c = s.encode('Latin1')
# print(c)
# d = c.decode('Latin1')
# print(d)

# №2
# a, b, c, d = input(), input(), input(), input()
# with open('text.file.txt', 'w') as file:
#     file.write(f'{a}\n{b}')
# with open('text.file.txt', 'a') as file:
#     file.write(f'\n{c}\n{d}')

# №3
# import json
# a = {
#     111111: ['Tim', 20],
#     222222: ['Tom', 21],
#     333333: ['Tad', 15],
#     444444: ['Rob', 16],
#     555555: ['Bob', 17],
#     666666: ['Kim', 18],
#     }
# with open('vocabulary.json', 'w') as file:
#      json.dump(a, file)

# №4
import csv
import json
with open('vocabulary.json', 'r') as json_file:
    data = json.load(json_file)
name_data = ['id', 'name', 'age', 'number_phone']

with open('data_file.csv', "w", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=name_data)

    writer.writeheader()

    for key, values in data.items():
        writer.writerow({'id': key, 'name': values[0], 'age': values[1], 'number_phone': ''})
