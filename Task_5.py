class ComplexDigit:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return self.re + other.re, self.im + other.im

    def __mul__(self, other):
        return (self.im + self.re) * (other.im + other.re)


a = ComplexDigit(2, 4j)

b = ComplexDigit(3, 5j)

print(a + b)
print(a * b)
