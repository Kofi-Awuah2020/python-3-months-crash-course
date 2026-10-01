"""
The file contains examples of how to loop through text
"""

#Looping by character
text = "Hello!"
letters = 0
for ch in text:
    if ch.isalpha():
        letters += 1

print(letters)

#Looping through text
text = "The quick brown fox"
for word in text.split():
    print(word.upper())

#Building a new list with append
words = "the quick brown fox".split()
long_words = []
for w in words:
    if len(w) > 3:
        long_words.append(w)

print(long_words)

#List comprehensions
words = "the Quick Brown Fox in India".split()
long_words = [w for w in words if len(w) > 3]
upper_words = [w.upper() for w in words if len(w) > 3]
lengths = [len(w) for w in words]

print(long_words)

square_root = [num**2 for num in range(1, 11)]
print(square_root)

vowel= [char for char in "Hello World" if char in ["a", "e", "i", "o", "u"]]
print(vowel)

capital_words = [len(char) for char in words if char.startswith(char.upper())]
print(capital_words)