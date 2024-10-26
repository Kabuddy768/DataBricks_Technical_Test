# Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)

def is_pangram(string):
    string = string.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    string_set =set(string.replace(" ", ""))

    return alphabet.issubset(string_set)

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello World"))