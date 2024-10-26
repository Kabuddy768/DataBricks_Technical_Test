# Write a program that accepts a string as input, capitalizes the first letter of each
# word in the string, and then returns the result string.

def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

print(capitalize_words("hi"))
print(capitalize_words("i love programming"))