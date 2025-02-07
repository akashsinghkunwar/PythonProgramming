import pandas as pd

# 1. skip data
df = pd.read_csv("corrupt_data.csv", on_bad_lines="skip")
print(df)

##########################################

# 2. handle in logs
bad_rows = []


def bad_line_handler(line):
    bad_rows.append(line)
    return None


df = pd.read_csv("corrupt_data.csv", on_bad_lines=bad_line_handler)


print("Corrupt Rows:", bad_rows)

##########################################
# 3. CSV try except block

import csv

with open("corrupt_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            # Process row
            print(row)
        except Exception as e:
            print(f"Skipping corrupt row: {row}, Error: {e}")

##########################################
