#Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r
class Circle():
    def __init__(self,a,b,r):         
        self.a = a         
        self.b = b         
        self.r = r
    def Area(self):
        return 3.14*(self.r)**2
    def Perimeter(self):
        return (2*3.14*self.r)
    #testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not.
    def testBelongs(self,x,y):
        d = ((self.a-x)**2 + (self.b-y)**2)**0.5
        return d <= self.r

    def Display(self):
        print(f"Circle Area:{self.Area()} \nCircle Perimeter: {self.Perimeter()} \nCircle Center: ({self.a},{self.b})")

circle1 = Circle(5,5,5)
circle1.Display()
print(circle1.testBelongs(8,18))
