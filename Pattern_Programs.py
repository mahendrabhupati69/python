#  Right angle Triangle

value = int(input("Please enter the value"))

"""for i in range(1, value+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

for i in range(1, value+1, 1):
    for j in range(1, i+1):
        print(j, end='')
    print() """
#  Print Even Numbers Odd Numbers


for i in range(1, value, 2):
    if i%2 == 0:
        print(f" {i}, is Even Number")
    else:
        print(f" {i}, is Odd Number")
