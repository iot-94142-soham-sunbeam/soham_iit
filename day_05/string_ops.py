
def reverse_string(s):
    """Returns the reversed string"""
    return s[::-1]


def count_vowels(s):
    """Returns the number of vowels in the string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count