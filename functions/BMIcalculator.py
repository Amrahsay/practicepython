weight = float(input("Weight: "))
wunit = input("(L)bs or (K)g ")
height = float(input("Height: "))
lunit = input("(C)m or (F)t ")
if wunit.upper() == "L":
    convertedW = weight*0.45
    wunit= 'Kg'
elif wunit.upper() == "K":
    convertedW = weight
    wunit = 'Kg'
else:
    print("Please only type w/l for the type of unit used")
if lunit.upper() == "F":
    convertedL = ((height//1)*30.48+(height%1)*25.4)
    lunit= 'cm'
elif lunit.upper() == "C":
    convertedL = height
    lunit = 'cm'
else:
    print("Please only type w/l for the type of unit used")
BMI = convertedW/((convertedL/100)**2)
print(f"Your BMI is {round(BMI,2)} with {round(convertedW,2)}{wunit} weight and {round(convertedL,2)}{lunit} height")
if BMI <= 18.4:
    print("You are underweight, please have a healthy diet")
elif BMI >= 40:
    print("You are obese, and you need dieting")
else:
    if BMI < 25:
        print("You are normal, keep it up")
    else:
        print("You are overweight, be careful of what you eat")
