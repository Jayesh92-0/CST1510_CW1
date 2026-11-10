import random


# ── Maths operation functions ─────────────────────────────
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None          # signals division by zero
    return a // b            # whole-number answer for first graders


def exponent(a, b):
    return a ** b


def remainder(a, b):
    if b == 0:
        return None          # remainder by zero is also impossible
    return a % b


# ── Menu ──────────────────────────────────────────────────
def show_menu():
    print("\n===== Maths Practice =====")
    print("1. Addition        (+)")
    print("2. Subtraction     (-)")
    print("3. Multiplication  (*)")
    print("4. Division        (/)")
    print("5. Exponent        (**)")
    print("6. Remainder       (%)")
    print("7. Quit")


# ── Ask one question ──────────────────────────────────────
def ask_questions(symbol, operation):
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    correct = operation(number1, number2)

    if correct is None:
        print(f"Error: {number1} {symbol} {number2} can't be done - "
              "you can't divide by zero! Let's try another.")
        return None          # question skipped, not counted

    if symbol == "/":
        print("(Give a whole number - ignore any remainder.)")

    answer_text = input(f"What is {number1} {symbol} {number2}? ").strip()

    if not answer_text.lstrip("-").isdigit():
        print(f"Error: that's not a whole number. The answer was {correct}.")
        return False

    answer = int(answer_text)

    if answer == correct:
        print("Correct! Well done!")
        return True
    else:
        print(f"Not quite. The answer is {correct}.")
        return False


# ── Main program ──────────────────────────────────────────
def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("**", exponent),
        "6": ("%", remainder),
    }
    score = 0
    total = 0

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            break

        if choice not in operations:
            print("Error: please choose a number from 1 to 7.")
            continue

        symbol, operation = operations[choice]
        result = ask_questions(symbol, operation)

        if result is None:   # division by zero - skip scoring
            continue

        total += 1
        if result:
            score += 1
        print(f"Score: {score}/{total} ({round((score / total) * 100, 1)}%)")

    if total > 0:
        print(f"\nFinal Score: {score}/{total} ({round((score / total) * 100, 1)}%)")
    else:
        print("\nNo questions answered.")
    print("Goodbye!")


if __name__ == "__main__":
    main()