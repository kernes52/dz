class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def devide(self):
        if self.num2 == 0:
            raise ValueError("Ділення на 0 не можливо")
        return self.num1 / self.num2

calculator = Calculator(30, 2)
print("Додавання:", calculator.add())
print("Віднімання:", calculator.subtract())
print("Множення:", calculator.multiply())
print("Ділення:", calculator.devide())