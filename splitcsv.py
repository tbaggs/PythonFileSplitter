import os
import csv
from collections import defaultdict

FILE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_file_path(filename):
    return os.path.join(FILE_DIR, filename)


file_path = get_file_path("hackdata.csv")

with open(file_path, "r") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    data = defaultdict(lambda:[header])
    _ = data[header[5][:5]]
    
    for row in reader: 
        with open(row[0] + ".txt", 'w+') as f:
            f.write(str(row) + '\n')