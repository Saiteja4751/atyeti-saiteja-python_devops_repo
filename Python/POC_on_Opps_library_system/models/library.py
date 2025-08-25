from utils.logger import Logger

class Library:
    def __init__(self):
        self.books = []
        self.borrowed = {}

    def add_book(self, book):
        self.books.append(book)
        Logger.log(f"Book added: {book}")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            Logger.log(f"Book removed: {book}")

    def lend_book(self, book, student):
        if book in self.books and book not in self.borrowed:
            self.borrowed[book] = student.name
            Logger.log(f"{book} lent to {student.name}")
            return True
        Logger.log(f"{book} is not available")
        return False

    def return_book(self, book, student):
        if self.borrowed.get(book) == student.name:
            del self.borrowed[book]
            student.borrowed_books.remove(book)
            Logger.log(f"{book} returned by {student.name}")
