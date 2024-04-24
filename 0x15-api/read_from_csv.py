import csv

with open('2.csv', 'r', newline='') as f:
    read = csv.reader(f, delimiter=',')

    for r in read:
        print(r)