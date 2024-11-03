class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def adding_marks(self, discipline, marks):
        self.marks[discipline] = marks

    def total_marks(self):
        return sum(self.marks.values())

    def obtained_percent(self):
        return self.total_marks() / (len(self.marks) * 100)


def main():
    johns_marks = {'Math': 68, 'English': 76, 'Science': 90}
    John = Student("John", johns_marks)
    John.adding_marks('History', 80)
    print(f'{John.name} obtained {John.total_marks()} total marks and it is '
          f'{John.obtained_percent()} of maximal marks')


if __name__ == '__main__':
    main()
