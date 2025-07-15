#Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

input_string = input("Enter a string: ")
print("Is palindrome:", is_palindrome(input_string))