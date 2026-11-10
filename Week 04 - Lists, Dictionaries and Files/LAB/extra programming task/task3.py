def sum_row(matrix, rowIndex):
    total = 0
    for value in matrix[rowIndex]:
        total += value
    return total

matrix = []
print("enter a 4x4 matrix row by row: ")
for i  in range(4):
    row = input(f"row {i}: ").split()
    matrix.append([float(x) for x in row])

for i in range(len(matrix)):
    print(f"Sum of the elements in row {i} is {sum_row(matrix, i)}")