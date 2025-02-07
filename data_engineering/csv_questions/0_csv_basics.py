"""
How do you read a CSV file in Python?
"""

import pandas as pd

df = pd.read_csv("data.csv")

# OR

import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

"""
How do you write a CSV file in Python?
"""

df.to_csv("output.csv", index=False)

# OR

import csv

data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read large csv files in chunk
for chunk in pd.read_csv("large_file.csv", chunksize=10000):
    process(chunk)  # Process each chunk separately
