#task 6 Number Pattern
rows = int(input("No of rows: "))

for row in range(1, rows+1):
    for num in range(1, row+1):
        print(num, end=" ")
    print()
    