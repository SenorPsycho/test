# String Operators
#    Given s1 = "Py" and s2 = "thon", what are the results of:
#    - s1 + s2
#    - s1 * 3
#    - "y" in s1

s1 = "Py"
s2 = "thon"

result_concat = s1 + s2

result_repeat = s1 * 3

result_in = "y" in s1


print("s1 + s2:", result_concat)  
print("s1 * 3:", result_repeat)    
print('"y" in s1:', result_in)    


#Output:# s1 + s2: Python
# s1 * 3: PyPyPy
# "y" in s1: True