import random
names =['Yash', 'Harsh', 'Garvit', 'Sambhav']
print(names[1:-1])
print(names)
names[0] = 'Amrahsay'
print(names)
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number>max:
        max= number
print(max)
print('_'*15)
#multi dimensional list
matrix1= [
    [9,4,7],
    [2,5,8],
    [3,6,9]
]
matrix = matrix1.copy()
print(matrix)
print(matrix[0])
print(matrix[2][1])
print('_'*15)
for row in matrix:
    for element in row:
        print(element)
matrix.append([20,30,40])
matrix.append(20)
matrix.append([20,40])
print(matrix)
matrix.insert(0,2)
print(matrix)
matrix.remove(2)
print(matrix)
matrix.pop()
print(matrix)
print(matrix.index(20))
print(2 in matrix)
print(matrix.count(5))
matrix[0].sort()
print(matrix)
matrix[2].reverse()
print(matrix)
matrix.clear()
print(matrix)
print(matrix1)
