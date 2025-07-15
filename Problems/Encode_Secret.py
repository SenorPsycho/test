# Takes a secret word as input (without spaces).
# Then encodes the word using a custom cipher.
# Replace all vowels with *
# Reverse the entire string
# Then shift each letter 2 places ahead in the alphabet(wrap around if needed, eg, y->a, z->b)
# Finally, print the resulting encoded word. 

Initial_word = input("Enter a secret word")
no_space_word = Initial_word.replace(" ", "")

no_vowel_word = no_space_word.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*").replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")

reverse_no_vowel_word = no_vowel_word[::-1]


def shift_char(c):
    if c.islower():
        return chr((ord(c) - ord('a') + 2) % 26 + ord('a'))
    elif c.isupper():
        return chr((ord(c) - ord('A') + 2) % 26 + ord('A'))
    else:
        return c

encoded_word = ''.join(shift_char(c) for c in reverse_no_vowel_word)
print(encoded_word)


