import pandas as pd

df = pd.read_csv(r"Week 06 - Pandas\LAB\DATA\students.csv")

print("First 5 rows: ")
print(df.head())

print("\nLast 3 rows: ")
print(df.tail(3))

print("\nShape(rows, columns): ", df.shape)
rows, cols = df.shape

print(f"Rows: {rows}, Columns: {cols}")

print("\n Column names: ", df.columns.tolist())
