class Point:
    def move(self):
        print('move')
    def draw(self):
        print('draw')
#__________
point1= Point()
point1.move()
point1.draw()
point1.x= 20
point1.y= 30
#__________
point2= Point()
point2.x=2
point2.y=3
point2.move()
point2.draw()
#__________
print(point1.x)
print(point1.y)
print(point2.x)
print(point2.y)
