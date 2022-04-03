# print("Prince Nyamadi")
# print('o----')
# print(' ||||')
# print("*" * 10)


# price = 10
# price = 20
# rating = 4.9
# name = "Prince Nyamadi"
# is_published = False
# print(price)

# name = "John Smith"
# age = 20
# is_new = True

# name = input("what is your name?")
# print('Hi '+name)
# color = input("what is your favorite color?")
# print('your favorite color is '+color)


# birth_year = input("what is your birth year?")
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(age)


# weight_lbs = input("what is your weight in lbs?")
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# course = "Python for Beginners"
# course = """
#     Hi John,
#     Here is our first email to you.

#     Thank you,
#     The support team
# """
# print(course)
# print(course[9])
# print(course[:9])


# name = "Jennifer"
# print(name[1:-1])

# course = "Python for Beginners"
# print(len(course))
# course.upper()
# print(course.find("y"))

# print(course.replace('P', 'J'))

# len() find length of string
# upper() convert string to uppercase
# lower() convert string to lowercase
# replace() replace a string with another string
# find() find a string in a string
# strip() remove whitespace from the beginning and end of a string
# split() split a string into a list of substrings
# join() join a list of strings into a single string
# title() convert the first character of each word to uppercase
# isupper() check if all characters in a string are uppercase
# islower() check if all characters in a string are lowercase
# isalpha() check if all characters in a string are alphabetic
# isdigit() check if all characters in a string are digits
# isalnum() check if all characters in a string are alphanumeric
# isspace() check if all characters in a string are whitespace
# startswith() check if a string starts with another string
# endswith() check if a string ends with another string
# isdecimal() check if all characters in a string are decimal digits
# isidentifier() check if a string is a valid identifier
# isprintable() check if all characters in a string are printable
# join() join a list of strings into a single string
# ljust() left-justify a string
# rjust() right-justify a string
# center() center a string
# zfill() pad a string with zeros
# lstrip() remove whitespace from the left side of a string
# rstrip() remove whitespace from the right side of a string

# import math

# print(10 % 3)
# x = 10+3 * 2
# # order of precedence
# # () parenthesis
# # exponentiation 2**3
# # multiplicatio or # division
# # addition or# subtraction
# *PEMDAS
# x = (2+3) * 10 - 3
# print(x)

# x = 2.9
# print(round(x))
# print("abs:", abs(-2.9))
# print(pow(2, 3))
# print(max(2, 3))
# print(min(2, 3))
# print(round(2.9))
# print(round(2.4))
# print("ceil: ", math.ceil(2.9))
# python3 math module


# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")

# print("Enjoy your day")


price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")
