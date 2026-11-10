#task 2 Multiplication Quiz
import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)

answer = int(input(f"What is {num1} * {num2}: "))
if answer == num1 * num2:
    print("Correct answer")
else:
    print("wrong")
    print(f"{num1} * {num2} = {num1 * num2}")
    