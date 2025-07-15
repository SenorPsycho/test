# Remove Duplicate Characters
#    Write a function that removes all duplicate characters from a string but keeps the first occurrence.

def remove_duplicate_characters(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

input_string = "programming"
output_string = remove_duplicate_characters(input_string)
print("Input string:", input_string)
print("Output string:", output_string)