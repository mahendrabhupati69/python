name = "Mahendra"
age = 26
print(name)
print(name[1])
print(name[-2:])  # String  is array of characters we can traverse through index
print("Hello \\n " + name)  # /n Escape sequence to bypass use another /
print("This \'statement\' eplains how to \"print\" ")
# -- It checks for sequence of characters exists in the String or not
print("Ma3" in name)  # In method which returns boolean value

# Formated String is used to make it dynamic
print("My name is %s and my age is %d" % (name, age))
print("-----------")
# to print any para graphs
Para = """hi  
hello 
World"""
print(Para)
print(name.__sizeof__())
print(name.__len__())
print(len(name))

# String Comparison
Str1 = "Hello"
Str2 = "Hello"
print(Str1 is Str2)  # Checks for Identity
print(Str1 == Str2)  # Checks for Value


def print_hi(person):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {person}')  # formatted string accepts string arguments
