import csv

with open('output.csv', mode='r') as data:
    reader = csv.reader(data)
    for row in reader: 
        print(row)