class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        return result

    def subtract(self):
        result = self.num1 - self.num2
        return result

    def multiply(self):
        result = self.num1 * self.num2
        return result

    def divide(self):
        try:
            result = self.num1 / self.num2
            return result
        except ZeroDivisionError:
            return "Can`t divide by zero"


def main():
    while True:
        action = input('Enter action(add, subtract, multiply, divide or quit):').lower()
        if action.startswith('q'):
            quit()
        while True:
            number1 = input('Enter first number:')
            number2 = input('Enter second number:')
            try:
                number1, number2 = int(number1), int(number2)
                break
            except ValueError:
                print('Invalid input')
                continue
        calculator = Calculator(number1, number2)
        if action.startswith('a'):
            print(calculator.add())
        elif action.startswith('s'):
            print(calculator.subtract())
        elif action.startswith('m'):
            print(calculator.multiply())
        elif action.startswith('d'):
            print(calculator.divide())
        else:
            print('Invalid action')


if __name__ == '__main__':
    main()
