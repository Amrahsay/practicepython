for item in 'python':
    print(item)
for item in ['Yash', 'Harsh', 'Garvit', 'Sambhav']:
    print(item)
for item in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(item)
for item in range(8, 100, 2):
    print(item)
prices = [5, 10, 15]
total = 0
for item in prices:
    total += item
print(f"Total cost:{total}")
for x in range(10):
    for y in range(9):
        print(f'({x},{y})')
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    print("X"*x)
print('_'*15)
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
    