class LibraryManagementSystem:
    def __init__(self):
        self.admins = {}
        self.librarians = {}
        self.users = {}
        self.books = {}
        self.issued_books = {}

    def register(self, role):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if role == 'admin':
            self.admins[username] = password
        elif role == 'librarian':
            self.librarians[username] = password
        elif role == 'user':
            self.users[username] = password

        print(f"Registration successful for {role}!")
        self.login(role)

    def login(self, role):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if role == 'admin' and self.admins.get(username) == password:
            self.admin_dashboard()
        elif role == 'librarian' and self.librarians.get(username) == password:
            self.librarian_dashboard()
        elif role == 'user' and self.users.get(username) == password:
            self.user_dashboard()
        else:
            print("Invalid credentials!")

    def admin_dashboard(self):
        while True:
            print("\nAdmin Dashboard:")
            print("1. Add Librarian")
            print("2. Delete Librarian")
            print("3. Add User")
            print("4. Delete User")
            print("5. Search Books")
            print("6. Update Member Information")
            print("7. Search Members")
            print("8. View Members List")
            print("9. Add Books")
            print("10. View Issued and Available Books")
            print("0. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.register('librarian')
            elif choice == '2':
                self.delete_librarian()
            elif choice == '3':
                self.register('user')
            elif choice == '4':
                self.delete_user()
            elif choice == '5':
                self.search_books()
            elif choice == '6':
                self.update_member_information()
            elif choice == '7':
                self.search_members()
            elif choice == '8':
                self.view_members_list()
            elif choice == '9':
                self.add_books()
            elif choice == '10':
                self.view_issued_and_available_books()
            elif choice == '0':
                break
            else:
                print("Invalid choice!")

    def librarian_dashboard(self):
        while True:
            print("\nLibrarian Dashboard:")
            print("1. View Issued and Available Books")
            print("2. View Users List")
            print("3. Generate Reports for Issued and Returned Books")
            print("4. Search Books")
            print("5. Search Users")
            print("0. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_issued_and_available_books()
            elif choice == '2':
                self.view_users_list()
            elif choice == '3':
                self.generate_reports()
            elif choice == '4':
                self.search_books()
            elif choice == '5':
                self.search_users()
            elif choice == '0':
                break
            else:
                print("Invalid choice!")

    def user_dashboard(self):
        while True:
            print("\nUser Dashboard:")
            print("1. Search and Borrow Books")
            print("2. View Borrowed Books")
            print("3. View Issued and Available Books")
            print("0. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.search_and_borrow_books()
            elif choice == '2':
                self.view_borrowed_books()
            elif choice == '3':
                self.view_issued_and_available_books()
            elif choice == '0':
                break
            else:
                print("Invalid choice!")

    def delete_librarian(self):
        username = input("Enter librarian username to delete: ")
        if username in self.librarians:
            del self.librarians[username]
            print("Librarian deleted successfully!")
        else:
            print("Librarian not found!")

    def delete_user(self):
        username = input("Enter user username to delete: ")
        if username in self.users:
            del self.users[username]
            print("User deleted successfully!")
        else:
            print("User not found!")

    def search_books(self):
        book_name = input("Enter book name to search: ")
        if book_name in self.books:
            print(f"Book '{book_name}' is available.")
        else:
            print(f"Book '{book_name}' is not available.")

    def update_member_information(self):
        username = input("Enter member username to update: ")
        role = input("Enter role (admin/librarian/user): ")

        if role == 'admin' and username in self.admins:
            password = input("Enter new password: ")
            self.admins[username] = password
            print("Admin information updated successfully!")
        elif role == 'librarian' and username in self.librarians:
            password = input("Enter new password: ")
            self.librarians[username] = password
            print("Librarian information updated successfully!")
        elif role == 'user' and username in self.users:
            password = input("Enter new password: ")
            self.users[username] = password
            print("User information updated successfully!")
        else:
            print("Member not found!")

    def search_members(self):
        role = input("Enter role (admin/librarian/user): ")
        if role not in ['admin', 'librarian', 'user']:
            print("Invalid role! Going back to admin dashboard.")
            return

        username = input("Enter username to search: ")

        if role == 'admin' and username in self.admins:
            print(f"Admin '{username}' found.")
        elif role == 'librarian' and username in self.librarians:
            print(f"Librarian '{username}' found.")
        elif role == 'user' and username in self.users:
            print(f"User '{username}' found.")
        else:
            print("Member not found!")

    def view_members_list(self):
        print("Admins:")
        for admin in self.admins:
            print(admin)
        print("Librarians:")
        for librarian in self.librarians:
            print(librarian)
        print("Users:")
        for user in self.users:
            print(user)

    def add_books(self):
        book_name = input("Enter book name to add: ")
        self.books[book_name] = "available"
        print(f"Book '{book_name}' added successfully!")

    def view_issued_and_available_books(self):
        print("Books:")
        for book, status in self.books.items():
            print(f"{book}: {status}")

    def view_users_list(self):
        print("Users:")
        for user in self.users:
            print(user)

    def generate_reports(self):
        print("Issued Books Report:")
        for user, books in self.issued_books.items():
            print(f"{user} has issued {books}")

    def search_users(self):
        username = input("Enter username to search: ")
        if username in self.users:
            print(f"User '{username}' found.")
        else:
            print("User not found!")

    def search_and_borrow_books(self):
        book_name = input("Enter book name to search and borrow: ")
        if book_name in self.books and self.books[book_name] == "available":
            self.books[book_name] = "issued"
            username = input("Enter your username: ")
            if username in self.issued_books:
                self.issued_books[username].append(book_name)
            else:
                self.issued_books[username] = [book_name]
            print(f"Book '{book_name}' borrowed successfully!")
        else:
            print(f"Book '{book_name}' is not available or already issued.")

    def view_borrowed_books(self):
        username = input("Enter your username: ")
        if username in self.issued_books:
            print(f"You have borrowed: {self.issued_books[username]}")
        else:
            print("You have not borrowed any books.")


def main():
    system = LibraryManagementSystem()
    while True:
        print("\nLibrary Management System")
        print("1. Admin")
        print("2. Librarian")
        print("3. User")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                print("\nAdmin Menu:")
                print("1. Register")
                print("2. Login")
                print("0. Back")
                action = input("Enter your action: ")
                if action == '1':
                    system.register('admin')
                    break
                elif action == '2':
                    system.login('admin')
                    break
                elif action == '0':
                    break
                else:
                    print("Invalid action!")
        elif choice == '2':
            while True:
                print("\nLibrarian Menu:")
                print("1. Register")
                print("2. Login")
                print("0. Back")
                action = input("Enter your action: ")
                if action == '1':
                    system.register('librarian')
                    break
                elif action == '2':
                    system.login('librarian')
                    break
                elif action == '0':
                    break
                else:
                    print("Invalid action!")
        elif choice == '3':
            while True:
                print("\nUser Menu:")
                print("1. Register")
                print("2. Login")
                print("0. Back")
                action = input("Enter your action: ")
                if action == '1':
                    system.register('user')
                    break
                elif action == '2':
                    system.login('user')
                    break
                elif action == '0':
                    break
                else:
                    print("Invalid action!")
        elif choice == '0':
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()