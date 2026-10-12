total_amount = 0

size = input("What size:Larger(L, $25). Medium(M, $20), Small(S, $15) ")
pepperoni = input("Would you like Pepperoni? +$2 for small or +$3 for Medium/Large; Y/N?: ")
cheese = input("Would like you like cheese, +$1; Y/N?: ")
if size == "L" or size == "l":
    total_amount += 25
elif size == "M" or size == "m":
    total_amount += 20
elif  size == "s" or size == "S":
    total_amount += 15
else:
    print("Invalid size, Defaulted to Small ")
    total_amount += 15
if pepperoni == "Y" or pepperoni == "y":
    if size == "L" or size == "l" or size == "M" or size == "m":
        total_amount += 3
    else:
        total_amount += 2

if cheese == "Y" or cheese == "y":
    total_amount += 1

print (f"Your Final Bill is :{total_amount}")
