i = 1

while i <= 5:
    print("*"*i)
    i += 1

print("done")


for item in 'Python':
    print(item)


for item in range(5, 10, 2):
    print(item)


prices = [10, 20, 30, 40, 50]

total = 0
for item in prices:
    total = total + item
    print(total)

print(f"Total: {total}")
