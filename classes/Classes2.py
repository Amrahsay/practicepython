class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I'm {self.name}")
#__________
yash = Person('Yash Sharma')
yash.talk()
#__________
name1 = input('Name of user ').upper()
message = Person(name1)
message.talk()
#__________
name2 = input('Name of user ')
name2 = f'{name2[0:1].upper()}{name2[1:].lower()}'
message = Person(name2)
message.talk()