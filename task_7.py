class ComplexNumber:
    def __init__(self, number, imag=None):
        if imag is not None:
            self.number = complex(number, imag)
        else:
            self.number = complex(number, 0)

    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number


x = ComplexNumber(1)
y = ComplexNumber(3)

print(x + y)
print(x * y)