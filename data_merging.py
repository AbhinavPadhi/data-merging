import csv

data_set1 = []
data_set2 = []

with open("bright_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data_set1.append(i)

with open("dwarf_stars_processed.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data_set2.append(i)

header1 = data_set1[0]
star_data1 = data_set1[1:]

header2 = data_set2[0]
star_data2 = data_set2[1:]

headers = header1 + header2

star_data = []

for i,data in enumerate(star_data1):
    star_data.append(star_data1[i]+star_data2[i])

with open("merged_star_data.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)