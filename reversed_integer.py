# Write a program that takes an integer as input and returns an integer with
# reversed digit ordering.

def reverse_integer(num):
    sign= -1 if num < 0 else 1
    reversed_num = int(str(abs(num))[::-1])
    return sign *reversed_num


user_input = input("Enter an integer: ")

try:
    num = int(user_input)
    print(f"Reversed integer: {reverse_integer(num)}")
except ValueError:
    print("Please enter a valid integer.")