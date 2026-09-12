"""
#For loop
for letter in "Cat":
    print(letter, end="")
print()


#Range function
for i in range(1, 16):
    print(i)

print(list(range(0, 10, 2)))

#Accumulating sum
total = 0   #Initialize accumulator
for n in [4, 8, 15, 16]:
    total = total + n   #Update accumulator
print(total)    #Use the accumulator after the loop

scores = [45, 91, 72, 88, 30]
passes = 0
for s in scores:
    if s >= 50:
        passes += 1
print(f"{passes} passed")

labels = []
for i in range(1, 6):
    labels.append(f"item-{i}")
print(labels)

#Enumerate function
names = ["ada", "grace", "linus"]
for i, name in enumerate(names):
    print(i, name)

for rank, name in enumerate(names, start=1):
    print(f"{rank}. {name.title()}")

#While loop
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")

#Sentinel value
total = 0
while True:
    entry = input("Amount (or 'done'): ")
    if entry == "done":
        break
    total += float(entry)
print(f"Total: {total:.2f}")

for n in range(1, 10):
    if n == 5:
        break
    print(n, end=" ")

for n in range (1, 10):
    if n % 2 == 0:
        continue
    print(n, end=" ")

def find_first_negative(numbers):
    for n in numbers:
        if n < 0:
            return n
    return None

result =find_first_negative(range(-2, 10))
print(result)  # Output: -2

while True:
    raw = input("Enter your age: ")
    if raw.isdigit():
        age = int(raw)
        break
    print("Please type a whole number for your age.")
print(f"You are {age} years old.")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please type a whole number for your age.")
"""
def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError(f"score must be 0 -100, got {score}")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(letter_grade(120))  # Output: B