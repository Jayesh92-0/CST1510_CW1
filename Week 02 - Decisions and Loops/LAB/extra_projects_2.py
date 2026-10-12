import random
random_number = random.randint(0,100)
guess_count = 0
while True:
    guess_count += 1
    number = int(input("Guess your number: "))
    if number > random_number:
        print("Too High")
    elif number < random_number:
        print("Too low")
    else:
        print("Congratulations, You have guess correct")
        break
print(f"Total Guesses: {guess_count}")
