# Main entry point of the application

from user_management import UserManagement
from book_management import BookManagement
from dashboard import Dashboard

def main():
    system = UserManagement()
    books = BookManagement()
    dashboard = Dashboard()
    
    while True:
        print("\nLibrary Management System")
        role = input("Select role (admin, librarian, user): ")
        
        if role in ['admin', 'librarian', 'user']:
            system.register(role)
        else:
            print("Invalid role selected.")

if __name__ == "__main__":
    main()
