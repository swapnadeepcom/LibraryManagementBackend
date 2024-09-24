
class Authentication:
    def __init__(self, admins, librarians, users):
        self.admins = admins
        self.librarians = librarians
        self.users = users

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

    def login(self, role):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if role == 'admin' and self.admins.get(username) == password:
            print("Logged in as Admin")
        elif role == 'librarian' and self.librarians.get(username) == password:
            print("Logged in as Librarian")
        elif role == 'user' and self.users.get(username) == password:
            print("Logged in as User")
        else:
            print("Invalid credentials")
