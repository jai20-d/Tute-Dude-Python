# 11. Read CSV file as dictionary
import csv
f = open("data.csv","r")
reader = csv.DictReader(f)
for row in reader:
    print(row)
f.close()
print("Name: Jai Tomar Roll No.: 2025UEA6527")
