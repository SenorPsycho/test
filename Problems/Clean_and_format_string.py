# Clean and Format String
#    Given text = "   hello world! welcome to Python.   ", write code to:
#    - Remove leading/trailing spaces
#    - Capitalize each word
#    - Replace the word "Python" with "Programming"

text = '   hello world! welcome to Python.   '
cleaned_text = text.strip()
capitalized_text = cleaned_text.title()
formatted_text = capitalized_text.replace("Python", "Programming")
print(formatted_text) 


