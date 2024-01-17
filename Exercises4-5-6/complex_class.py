class ComplexNumbers:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def form(self, real, imaginary):
        if imaginary > 0:
            return str(real) + ' + ' + str(imaginary) + 'i'
        else:
            return str(real) + ' - ' + str(imaginary) + 'i'

    def add(self, comp):
        total_real = self.real + comp.real
        total_imaginary = self.imaginary + comp.imaginary
        print('The sum is: ' + self.form(total_real,total_imaginary))

    def subtract(self, comp):
        total_real = self.real - comp.real
        total_imaginary = self.imaginary - comp.imaginary
        print('The difference is: ' + self.form(total_real,total_imaginary))

    def multiply(self, comp):
        total_real = self.real*comp.real - self.imaginary*comp.imaginary
        total_imaginary = self.real*comp.imaginary + self.imaginary*comp.real
        print('The product is: ' + self.form(total_real,total_imaginary))

    def division(self, comp):
        if (comp.real != 0 and comp.imaginary != 0):
            total_real = (self.real*comp.real + self.imaginary*comp.imaginary)/(comp.real*comp.real + comp.imaginary*comp.imaginary)
            total_imaginary = (self.imaginary*comp.real - self.real*comp.imaginary)/(comp.real*comp.real + comp.imaginary*comp.imaginary)
            print('The division is: ' + self.form(total_real,total_imaginary))
        else:
            print('cannot divide by 0')


if __name__ == '__main__':
    c1 = ComplexNumbers(1.0,2.0)
    c2 = ComplexNumbers(2.0, -3.0)
    c3 = ComplexNumbers(0,0)
    c1.add(c2)
    c1.subtract(c2)
    c1.multiply(c2)
    c1.division(c2)
    c1.division(c3)
