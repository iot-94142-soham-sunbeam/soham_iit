text = input("Enter a string: ")

print("Original string:", text)

# Basic slicing
print("First 5 characters:", text[:5])
print("Characters from index 2 to 6:", text[2:7])

# Slicing with step
print("Every second character:", text[::2])

# Negative indexing
print("Last 5 characters:", text[-5:])

# Reverse the string
print("Reversed string:", text[::-1])
