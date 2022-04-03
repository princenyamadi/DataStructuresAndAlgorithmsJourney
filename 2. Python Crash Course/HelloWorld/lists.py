names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'

print(names)


numbers = [3, 6, 2, 8, 4, 8, 10]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number

print(largest_number)


numbers.insert(0, 5)

print(50 in numbers)
print(numbers.count(8))


# tuples
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


coordinates = (4, 5, 6)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates
