try:
    age = int(input('Age: '))
    if age <= 0:
        age = 0
    else:
        print(age)
    _0Error=1/age
except ZeroDivisionError:
    print('Age cannot be equal/less then zero!')
except ValueError:
    print(('Invalid value'))
