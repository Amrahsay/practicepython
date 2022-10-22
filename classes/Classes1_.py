class Point:
    def __init__(self, x, y): #constructor
        self.x = x
        self.y = y
    def move(self):
        print('move')
    def draw(self):
        print('draw')
#__________
point1 = Point(10, 20)
point1.move()
point1.draw()
#__________
point2 = Point(1, 2)
point2.move()
point2.draw()
#__________
#point3 = Point()
# Well assigning variable like will only cause trouble, so better not do that here
#__________
print(point1.x)
print(point1.y)
print(point2.x)
print(point2.y)
