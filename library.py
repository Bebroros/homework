class Book:
    def __init__(self, title, author, isbn, year_published):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published

    def get_info_parent(self):
        return {'Title': self.title, 'Author': self.author, 'ISBN': self.isbn,
                'Year of publishing': self.year_published}


class FictionBook(Book):
    def __init__(self, title, author, isbn, year_published, genre):
        super().__init__(title, author, isbn, year_published)
        self.genre = genre

    def get_info(self):
        book_info = super().get_info_parent()
        book_info['Genre'] = self.genre
        return book_info


class NonFictionBook(Book):
    def __init__(self, title, author, isbn, year_published, topic):
        super().__init__(title, author, isbn, year_published)
        self.topic = topic

    def get_info(self):
        book_info = super().get_info_parent()
        book_info['Topic'] = self.topic
        return book_info


class ReferenceBook(Book):
    def __init__(self, title, author, isbn, year_published, description):
        super().__init__(title, author, isbn, year_published)
        self.description = description

    def get_info(self):
        book_info = super().get_info_parent()
        book_info['Description'] = self.description
        return book_info


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_books(self):
        return self.books

    def get_books_by_category(self, category):
        book_by_category = []
        for book in self.books:
            if isinstance(book, category):
                book_by_category.append(book)
        return book_by_category

    def get_books_by_author(self, author):
        book_by_author = []
        for book in self.books:
            if book.author == author:
                book_by_author.append(book)
        return book_by_author

    def get_books_by_year(self, year):
        book_by_year = []
        for book in self.books:
            if book.title == year:
                book_by_year.append(book)
        return book_by_year


def getting_info(book):
    print(f"Here is all info for {book.title}:")
    info = book.get_info()
    for key in info:
        print(f'{key}: {info[key]}')


def main():
    Bebra = NonFictionBook('bebra', 'me', '123', '2019', 'biology')
    Dune = FictionBook('Dune', 'Frank Herbert', '1234', '1965', 'fantasy')
    library = Library()
    library.add_book(Bebra)
    library.add_book(Dune)
    getting_info(Bebra)
    for book in library.get_books_by_category(FictionBook):
        getting_info(book)
    for book in library.get_books_by_author('me'):
        print(book.title)
    for book in library.get_books_by_year('Dune'):
        print(book.isbn)


if __name__ == '__main__':
    main()
