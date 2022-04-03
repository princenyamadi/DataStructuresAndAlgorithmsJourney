def find_max(numbers):
    """Find the maximum number in a list."""
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number
    return current_max
