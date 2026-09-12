#Module 1 Practice Exercises

"""
#Exercise 1.1
print("Kofi", 14, "I am growing found of python", sep= "\n")

#Exercise 1.2
a, b = (7, 2)
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a // b = {a ** b}")

#Exercise 1.3
kilometres = int(input("Number of Kilometres: "))
convertion = kilometres / 0.621371
print(f"{convertion:.2f}")

#Exercise 1.4
print(type(10 / 2))
print(type(10 // 2))
print(type(10 == 10))
print(type("10"))

#Exercise 1.5
first_name = input("What is your first name? ")
surname = input("What is your surname? ")

print(first_name, surname, sep="-")

#Exercise 1.6
price = 1234.5678

print(f"{price:.2f}")
print(f"{price:,.2f}")
print(f"{price:,.2f}")

#Exercise 1.7
temperarture = int(input("Temperature in Celcius: "))  #Input is converted into an int 
fahrenheit = temperarture * 9 / 5 + 32  
print(f"That is {fahrenheit} degrees") #F - string used to format printing 


#Exercise 1.9
seconds = int(input("Seconds: "))
hour = seconds // 3600 
minutes = seconds % 3600 // 60
secs = seconds % 60

print(f"{hour}h {minutes:02d}m {secs:02d}s")
"""

#Exercise 1.11
John = "John"
print(f"{John}")

total = 3 + 5
print(total)

name = input("What is your name? ")
print(name)