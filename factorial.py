class Factorial:
    def __init__(self):
        self.cache = {}

    def factorial(self, n):
        if n in self.cache:
            return self.cache[n]
        else:
            if n == 0:
                return 1
            else:
                self.cache[n] = n * self.factorial(n - 1)
                return self.cache[n]


def main():
    factorial_calculator = Factorial()
    while True:
        n = input('Enter a number([q] to quit):')
        if n == 'q':
            quit()
        else:
            try:
                n = int(n)
                if n <= 0:
                    print("Invalid input")
                    raise ValueError
                else:
                    print(factorial_calculator.factorial(n))
            except ValueError:
                print("Invalid input")


if __name__ == '__main__':
    main()
