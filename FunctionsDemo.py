#  No Parameter Function
"""
def test():
    print("Hello Worlds")


#  Parameter Function

def Hello(name):
    print(f"Hello {name}")


#  Default Parameter Function


def Country(name="India"):
    print(f"Hello {name}")


Country()

#  Pass list to a function
li = ["Rof", "sam", "tom"]


def cityNames(list):
    for i in list:
        print(i)


cityNames(li)


# Factorial of a given Number

def fact(num):
    if num >1:
        num = num * fact(num - 1)
    return num


print(fact(5))



#  Function with multiple arguments ---* args

def greet(*args) :
    for name in args:
        print(f" Hello! {name}")

greet("mahendra", "Sam")


from typing import Any


#  Function with multiple arguments --- * args :Any

def greet(*args: Any):
    for name in args:
        print(f" Hello! {name}")

greet("mahendra", "Sam", 1, 1123.23)
"""

#  Function with multiple arguments --- **kwargs


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")






















