age = int(input("Enter your age: "))
if age == 18:
    print("You are okay to drive.")
elif age < 30:
    print("Please use the driving safety guide.")
elif age > 30:
    print("You are greater than 30.")
else:
    print("You are not ok to drive.")


