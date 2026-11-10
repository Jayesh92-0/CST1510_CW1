import pandas as pd
df = pd.read_csv(r"Week 06 - Pandas\LAB\DATA\students.csv")

print("Data types: ")
print(df.dtypes)

print("\nSummary Statistics: ")
print(df.describe())

avg_grade = df['Grade'].mean()
max_attendance = df['Attendance'].max()
youngest_age = df['Age'].min()

print(f"\nAverage grade: {avg_grade:.2f}")
print(f"Maximum attendence: {max_attendance}")
print(f"Youngest student's age: {youngest_age}")