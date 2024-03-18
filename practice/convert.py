import csv
import json

csv_file = open("shein_mens_fashion.csv", "r")

csv_reader = csv.reader(csv_file)

field_names = next(csv_reader)

data = []

for row in csv_reader:
    product = data.append(dict(zip(field_names, row)))

print(f" THIS IS THE LEARN OF THE DATA {len(data)}")

for myd in data:
    with open("shein_mens_fashion.json", "a") as json_filse:
        json.dump(myd, json_filse)
        json_filse.write("\n")
