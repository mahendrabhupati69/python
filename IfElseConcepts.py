"""x = int(input("Please enter the value of \'X\'\n"))  # Takes value from user at run time like Sacnner class in Java
print(x)
"""
# WAP to find highest of 3 numbers with if else

a = 584
b = 645
c = 942

if a > b:
    if a>c:
        print("\'A\'is the highest number")
    else:
        print(" \'C\' is the highest number")
else:
    if b>c:
        print(" \'B\' is the highest number")
    else:
        print(" \'C\' is the highest number")

print("****************************************")

x = 13
y = 14
z = 12
if (x < y) and (x < z):
    print(" \'x\' is the smallest number")
elif (y < z):
    print(" \'y\' is the smallest number")
else:
    print(" \'z\' is the smallest number")
