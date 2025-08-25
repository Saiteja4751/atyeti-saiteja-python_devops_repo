from models.person import Student, Admin
from models.book import Book
from models.library import Library

# Create library instance
library = Library()

# Create users
admin = Admin("Mr. Raju")
student = Student("Teja")

# Create books
book1 = Book("Clean Code", "Robert C. Martin", "12345")
book2 = Book("Python Crash Course", "Eric Matthes", "67890")

# Admin adds books
admin.add_book(book1, library)
admin.add_book(book2, library)

# Student borrows book
student.borrow_book(book1, library)

# Student returns book
library.return_book(book1, student)

# Admin removes a book
# admin.remove_book(book2, library)
