class Common:
    def breath(self):
        print('Yes, They breath')

    def walk(self):
        print('Yes, They walk')

    def eat(self):
        print('Yes, They eat')

    def drink(self):
        print('Yes, They drink')


class Cat(Common):
    def yawn(self):
        print('Cats like to yawn')


class Dog(Common):
    def bark(self):
        print('Dogs like to bark all the time')


class Human(Common):
    pass
#__________
dog1 = Dog()
dog1.bark()
dog1.walk()
dog1.eat()
dog1.drink()
dog1.breath()
#__________
cat1 = Cat()
cat1.yawn()
cat1.walk()
cat1.eat()
cat1.drink()
cat1.breath()
