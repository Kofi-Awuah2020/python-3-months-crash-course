"""
This file contains the practice exercises for month 2.
"""
89
#Exercise 2.1
def is_even(n):
    """Returns True if n is even, False otherwise."""
    return n % 2 == 0
print(is_even(5))

#Exercise 2.2
print(5 > 3 and 2 > 4)  #False
print(5 > 3 or 2 > 4)   #True
print(not 5 > 3)    #False
print(bool(""), bool("0"), bool([]), bool([0])) #False, True, False, True

#Exercise 2.3
def sign(n):
    """Return the sign of n."""
    n = int(n)
    if n == 0:
        return "zero"
    elif n > 0:
        return "positive"
    else:
        return "negative"

print(sign(-2))

#Exercise 2.4
def bmi_category(bmi):
    """Return the standard category for a BMI value."""
    bmi = float(bmi)
    if bmi >= 30 :
        return "obese"
    elif 25 <= bmi < 30:
        return "overweight"
    elif 18.5 <= bmi < 25:
        return "normal"
    else:
        return "underweight"

print(bmi_category(18.5))

#Exercise 2.5
def can_vote(age, is_citizen, is_registered):
    """Return True if the person can vote, False otherwise."""
    if age < 18:
        return False

    if not is_registered:
        return False

    if not is_citizen:
        return False
    
    return True

print(can_vote(19, True, False))

#Exercise 2.6
for n in range(1, 20):
    if n % 3 == 0:
        print(n, end=" ")
print()

#Exercise 2.7
sum = 0 #Initaliase 
for n in range(1, 101):
    sum += n

print(sum)

total = 0
for i in (range(2, 101, 2)):
    total += i

print(total)

#Exercise 2.8
def count_vowels(text):
    """Function counts vowels in a text, and returns the count"""
    count = 0

    for char in text:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    return count

print(count_vowels("Ama is a good girl"))

#Exercis 2.9
count = 0
while count < 11:
    count += 1
    print(count, end=" ")

print("\nLiftoff")

#Exercise 2.10
"""
import random

def guessing_game():
    hidden_number = random.randint(1, 100)
    guesses = 0

    while True:
        user_guess = int(input("Guess the number: "))
        guesses += 1
        if hidden_number == user_guess:
            print("correct")
            break

        if user_guess < hidden_number:
            print("higher")
        else:
            print("lower")

    return guesses

print(guessing_game())
"""
#Exercise 2.11
def first_word_longer_than(words, n):
    """Return the first word in words longer than n characters, else None."""
    for word in words:
        if len(word) > n:
            return word

    return None

print(first_word_longer_than(["cat", "horse", "elephant"], 3))

#Exercise 2.12
def validate_percentage(value):
    if value < 0 or value > 100:
        raise ValueError
    else:
        return value

print(validate_percentage(100))

#Exercise 2.13
for i in range(1,10):
    if i % 2 == 0:
        continue    #Starts the loop over again
        print(i)    #Nothing gets printed

#Exercise 2.14
def fizzbuzz_print(n):
    for i in range(1, n + 1):
        print("fizzbuzz")

fizzbuzz_print(2)