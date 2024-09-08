# loops Example

# Print 10 numbers using While loop
# Irrespective loop type you can use else part for loop
num = 1
while num <= 10:
    print(f"Current number is : ", num)
    num = num + 1
else:
    print(" End of loop ")

print("*********************************************** ")
# For loop Example

Numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
for i in Numbers:
    print(i)

print("*********************************************** ")
for i in range(len(Numbers)):
    print(Numbers[i])

print("*********************************************** ")

