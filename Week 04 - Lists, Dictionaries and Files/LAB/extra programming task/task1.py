numbers = []

value = int(input("Enter an Interger(0 to stop): "))
while value != 0:
    numbers.append(value)
    value = int(input("Enter an Interger(0 to stop): "))

for num in reversed(numbers):
    print(num) 
    