#Write a function to count the number of vowels in a given string.

def vowel_counting(Given_String):
    vowels = "aeiouAEIOU"
    count = 0
    for char in Given_String:
        if char in vowels:
            count += 1
    return count

Given_String = input("Enter a string: ")

print("Number of vowels in the string:", vowel_counting(Given_String))