temprature = input("What is the temprature arround you? ")
tempr = int(temprature)
if tempr >= 40:
    is_hot = True
    is_cold = False
elif tempr <= 20:
    is_hot = False
    is_cold = True
else:
    is_hot = False
    is_cold = False
if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's better if you wear a sweater")
else:
    print("What a pleasant weather we have here")

print("Remember to enjoy your day")
print('_'*20)
income = input("What is the persons annual income? ")
inc = int(income)
credit = input("Are they creditable?(Y/N) ")
if inc>10000:
    has_high_income = True
else:
    has_high_income = False
if credit == 'N':
    has_good_credit = False
else:
    has_good_credit = True
if has_good_credit and has_high_income:
    print("The client is eligible for the loan")
elif has_good_credit and not has_high_income:
    print("Please consult the client about the interest rates and the penalty charges before proceeding any further")
elif has_high_income and not has_good_credit:
    print("Please ask them to understand that it will be difficult to proceed with the current requested amount of loan with their given profile")
else:
    print("They aren't eligible for the loan")
if has_good_credit or has_high_income:
    print("Tell them to vist us again if they change their minds")
else:
    print('''Reply with "Sir we cannot proceed with the loan, we hope that you aren't offended with our reply"''')
