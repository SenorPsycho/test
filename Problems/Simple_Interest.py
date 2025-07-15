def Simple_Interest(principal, rate, time):
    return (principal * rate * time) / 100

print("Enter your princple, rate and time")
principal = float(input("Principal: "))
rate = float(input("Rate: "))
time = float(input("Time: "))
print(
Simple_Interest(principal, rate, time)
)

