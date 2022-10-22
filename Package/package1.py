import Modules.Module2
#can use
# from Modules.Modules1UnitConvertor import lbs_to_kg
# import Package
# import classes

lnumber= [1,2,3,4,8,56,544,7897,35,4,31,4,64,13,4654,5343,132,13,135,43,5435,4,354,35]
print(max(lnumber))
lnumber1= [1,2,3,4,8,56,544,789,35,4,31,4,64,13,4654,5343,132,13,135,43,5435,4,354,35]
max = Modules.Module2.find_max(lnumber1)
print(max)