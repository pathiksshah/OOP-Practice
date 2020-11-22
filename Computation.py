class Computation():
    def Factorial(self,i):
        n=1
        for m in range (1, i+1):
            n = n * m
        return n
    def Sum(self,i):
        n=0
        for m in range (1, i+1):
            n = n + m
        return n
c = Computation()
print(c.Factorial(5))
print(c.Sum(5))