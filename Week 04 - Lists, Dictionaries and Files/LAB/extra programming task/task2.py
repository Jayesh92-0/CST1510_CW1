import random 
throws = []
for i in range(7):
    throws.append(random.randint(1, 6))
print("Origianl: ", throws)

random.shuffle(throws)
print("Shuffled: ", throws)

throws.sort(reverse=True)
print("Descending: ", throws)

print("\n Occurence: ")
for face in range(1,7):
    print(f"{face}: {throws.count(face)}")
