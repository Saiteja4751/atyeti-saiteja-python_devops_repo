from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_role(self):
        pass


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = []

    def display_role(self):
        return "Student"

    def borrow_book(self, book, library):
        if library.lend_book(book, self):
            self.borrowed_books.append(book)


class Admin(Person):
    def __init__(self, name):
        super().__init__(name)

    def display_role(self):
        return "Admin"

    def add_book(self, book, library):
        library.add_book(book)

    def remove_book(self, book, library):
        library.remove_book(book)
