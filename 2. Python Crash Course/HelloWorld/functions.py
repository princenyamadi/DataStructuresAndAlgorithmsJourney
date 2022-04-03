def greet_user(first_name, last_name):
    """Display a simple greeting."""
    print(f"Hi {first_name} {last_name}!")
    print('Welcome aboard')


print("Start")
# positional arguments
greet_user("John", "Smith")
greet_user("Jane", "Doe")

# keyword arguments
greet_user(last_name="Smith", first_name="John")

print("Finish")


def square(number):
    return number * number


print(square(3))
