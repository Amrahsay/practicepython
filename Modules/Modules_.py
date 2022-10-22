from Modules import Modules1UnitConvertor
from Modules.Module2 import find_max
# well can import the whole module and then use pointer type calling or can directly call the function like this
print(Modules1UnitConvertor.kg_to_lbs(75))
numbers = [10,3,6,2]
print(max(numbers))
numbers = [10,13,6,2]
max_num = find_max(numbers)
print(max_num)