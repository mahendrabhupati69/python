Score = [20, 10, 30, 40, 50]
print(Score)
# [0 : 4] or [-1 : -5] for both positive and negative indexes
print(Score[1])  # get value through Index
print(Score[-1])

Names = ["Raj", "John", "Sam", "Nitin"]
Names_Mix = ["Raj", 23, "John", 42]
print(Names_Mix)

#  Create a Shallow/new copy
print(Score[:])
print(Score + [1, 2, 3])  # List concatenation at run time don't do anything to original
print(Score)

print(Score + Names)  # List concatenation with another List
Score[2] = 69

print(Score)  # List is mutable we can manipulate the data

# Append method -- Add value at very End of the list
Score.append(59)
print(Score)

Score.extend([69, 79])
print(Score)
