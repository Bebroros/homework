class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def action(rectangle):
    act = input('Enter your action(find perimeter or area):').lower()
    if act.startswith('p'):
        return print(rectangle.perimeter())
    elif act.startswith('a'):
        return print(rectangle.area())
    else:
        print('Invalid input')
        action(rectangle)


def main():
    while True:
        try:
            height = float(input("Enter height: "))
            width = float(input("Enter width: "))
        except ValueError:
            print("Please enter a float")
            main()
        rectangle = Rectangle(width, height)
        action(rectangle)
        if input('Do you want to quit(Y)').lower() == 'y':
            break


if __name__ == '__main__':
    main()
