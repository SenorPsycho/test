# 1. Take a number from the user and print whether it's even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
    
    
# 2. Write a program to count the number of vowels in a given string.
count = 0
string = input("Enter a string: ")
for char in string.lower():
    if char in 'aeiou':
        count += 1
print(f"Number of vowels in '{string}': {count}")

# 3. Ask the user to input a sentence and print the number of words in it.
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"Number of words in the sentence: {word_count}")


# 4. Take a number from the user and print its multiplication table from 1 to 10 using a function.
def print_multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter a number: "))
print_multiplication_table(number)

# 5. Write a program to accept 5 numbers from the user, store them in a list, and print the maximum and minimum values.
numbers = []
for _ in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
print(f"Maximum value: {max(numbers)}")
print(f"Minimum value: {min(numbers)}")

# 6. Accept a string and check whether it is a palindrome or not (same forward and backward).
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

# 7. Create a loop that keeps asking the user to guess a secret number between 1 to 10 until they guess it correctly. (Use while loop and break)
secret_number = 7
while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess == secret_number:
        print("Congratulations! You've guessed the secret number.")
        break
    else:
        print("Wrong guess. Try again.")

# 8. Accept 5 numbers from the user and store only the even numbers in a new list. Print the final list.
even_numbers = []
for _ in range(5):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

# 9. Write a program that prints the Fibonacci sequence up to n terms. (Ask user for n)
n = int(input("Enter the number of terms for Fibonacci sequence: "))
a, b = 0, 1
fibonacci_sequence = []
for _ in range(n):
    fibonacci_sequence.append(a)
    a, b = b, a + b
print(f"Fibonacci sequence (first {n} terms): {fibonacci_sequence}")

# 10. Accept a list of numbers and remove all duplicate values
def remove_duplicates(lst):
    return list(set(lst))

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
unique_numbers = remove_duplicates(numbers)
print(f"List after removing duplicates: {unique_numbers}")