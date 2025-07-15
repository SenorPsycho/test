# 1. WAP to store seven fruits in a list entered by the user.
# 2. WAP to accept marks of 6 students and display them in a sorted manner.
# 3. WAP to sum a list with 4 numbers.

# (1)
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i + 1}: ")
    fruits.append(fruit)
print("Fruits entered:", fruits)

# (2)
marks = []
for i in range(6):
    mark = float(input(f"Enter marks for student {i + 1}: "))
    marks.append(mark)
marks.sort()
print("Sorted marks:", marks)

# (3)
numbers = []
for i in range(4):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)
sum_of_numbers = sum(numbers)
print("Sum of the numbers:", sum_of_numbers)

