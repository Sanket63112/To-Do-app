import csv

with open('locations.csv','r', encoding='utf-8') as file:
    data = list(csv.reader(file))

for row in data:
    print(row)