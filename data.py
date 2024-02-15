import csv
import random

with open("DC.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(346):
        writer.writerow([round(random.uniform(745, 759), 2), round(random.uniform(489, 505), 2),round(random.uniform(215, 240), 2),round(random.uniform(375, 380), 2)])