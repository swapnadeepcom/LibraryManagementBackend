# Manages book transactions

class TransactionManagement:
    def __init__(self, books, issued_books):
        self.books = books
        self.issued_books = issued_books

    def issue_book(self, book_id, user):
        if book_id in self.books and book_id not in self.issued_books:
            self.issued_books[book_id] = user
            print(f"Book '{self.books[book_id]}' issued to {user}.")
        else:
            print("Book is either not available or already issued.")

    def return_book(self, book_id):
        if book_id in self.issued_books:
            user = self.issued_books.pop(book_id)
            print(f"Book '{self.books[book_id]}' returned by {user}.")
        else:
            print("Book not issued or invalid book ID.")
