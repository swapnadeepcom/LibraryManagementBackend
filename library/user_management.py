# Handles user registration and login

class UserManagement:
    def __init__(self):
        self.admins = {}
        self.librarians = {}
        self.users = {}

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
            print("Logged in as Admin")
            # Call admin dashboard here
        elif role == 'librarian' and self.librarians.get(username) == password:
            print("Logged in as Librarian")
            # Call librarian dashboard here
        elif role == 'user' and self.users.get(username) == password:
            print("Logged in as User")
            # Call user dashboard here
        else:
            print("Invalid credentials")
