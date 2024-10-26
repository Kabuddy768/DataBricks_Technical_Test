# Write a Python function that checks whether a word or phrase is palindrome or
# not.

def is_palindrome(text):
    checked_text=''.join(char.lower() for char in text if char.isalnum())
    return checked_text==checked_text[::-1]

print(is_palindrome("MADAM"))  # False