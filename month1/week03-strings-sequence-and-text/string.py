"""
This file contains an example of how to use the methods on a string
"""

name = "  Ada  "        
name.strip()        #returns "Ada" - and throws it away
print(f"[{name}]")  #still "  Ada  "

name = name.strip() # keep the result
print(f"[{name}]")

print(f"[{name.lower()}]")  #prints in lower case

print(f"[{name.upper()}]")  #prints in upper case 

print(f"[{name.replace("Ada", "Kwame")}]")  #replaces characters in the string

name = name.split(",")
print(f"[{name}]")   #sperates characters per the delimeter ","

str = "the quick brown".split()
print(str)

new_str = "-".join(str)
print(new_str)

print(type(name))

name2 = "John"
state = name2.startswith("A")
print(state)

state2 = name2.endswith("n")
print(state2)

print("hello".find('l'))

print("hello".count("l"))

print("123".isdigit())

print("al".isalnum())