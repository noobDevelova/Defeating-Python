# DATA TYPES IN PYTHON

# String
print("#" * 30)
print("1. String")
name = "Randi"

# With Built In Function
name_length = len(name)
print("String Value: " + name)

# This will cause an error
# print("String Length: " + name_length)

# Must be converted to string because the return value of len() is integer
convert_int = str(name_length)
print("String Length: " + convert_int)

# Select some char in name variabel
selected_char = name[2] 
print("Selected char: " + selected_char)

# Detecting the type of the variable
type_var = str(type(name))
print("Type variable: " + type_var)
print("\n")
# Integer
print("2. Integer")
val1 = 20
val2 = 30
summary = val1 + val2

# Using operator
print("Val 1: " + str(val1))
print("Val 2: " + str(val2))
print("Val 1 + Val 2 = " + str(summary))
type_var = str(type(summary))
print("Type variable: " + type_var)
print("\n")

print("#" * 30)

