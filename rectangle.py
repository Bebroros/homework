class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def action(rectangle):
    while True:
        act = input('Enter your action(find perimeter or area):').lower()
        if act.startswith('p'):
            return print(rectangle.perimeter())
        elif act.startswith('a'):
            return print(rectangle.area())
        else:
            print('Invalid input')


def main():
    while True:
        while True:
            try:
                height = float(input("Enter height: "))
                width = float(input("Enter width: "))
                break
            except ValueError:
                print("Please enter a float")
        rectangle = Rectangle(width, height)
        action(rectangle)
        if input('Do you want to quit(Y/N)').lower() == 'y':
            break


if __name__ == '__main__':
    main()
