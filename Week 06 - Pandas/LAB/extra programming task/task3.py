import pandas as pd

df = pd.read_csv(r"Week 06 - Pandas\LAB\DATA\students.csv")
grades_df = df[["Name","Course", "Grade"]]

print("First 8 rows of grades_df: ")
print(grades_df.head(8))

print("\nRows 5 to 9 (iloc): ")
print(df.iloc[5:10])

print("\nName and City at index 3(loc): ")
print(df.loc[3,['Name', 'City']])