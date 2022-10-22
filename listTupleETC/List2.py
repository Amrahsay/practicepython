numbers = [2,2,2,4,5,6,3,4,6,1,7,8,5,9,2,1,5,7,3,4,6,1,2,3,6,9,8,5,4,7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
uniques.sort()
print(uniques)