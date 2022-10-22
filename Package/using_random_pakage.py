import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second

#__________
dice = Dice()
print(dice.roll())
#__________
for i in range(5):
    print(random.random())
    print(random.randint(10,50))
    print(random.randrange(0,100,5))
#__________
day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
day_of_meeting = random.choice(day)
print(day_of_meeting)
