class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def Perimeter(self):
        return 2*(self.length+self.width)
    def area(self):
        return self.length*self.width
    def display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.Perimeter())
        print("The area of rectangle is: ", self.area())

class Parallelepipede(Rectangle):
    def __init__(self,l,w,h):
        Rectangle.__init__(self,l,w)
        self.height = h
    def volume(self):
        return self.height*self.width*self.length

myParallelepipede = Parallelepipede(7 , 5 , 2)
print(myParallelepipede.volume())

myrect = Rectangle (7,5)
myrect.display()

