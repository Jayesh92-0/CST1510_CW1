#task 1 Password strength checker
password = input("Enter your password: ")
if len(password) >= 12:
    print("Strong")
elif len(password) >= 8:
    print("Moderate")
else:
    print("Weak")
