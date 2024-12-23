class Library:
    def __init__(self, available_books):
        self.available_books = available_books
        self.borrowed_books = {}
        self.user = {}

    def display_available_books(self):
        print("Available books:")
        for book in self.available_books:
            print(book)

    def lend_book(self, book, user):
        if book in self.available_books:
            self.available_books.remove(book)
            self.borrowed_books[book] = user
            self.user[user].append(book)
            print(f"{book} has been borrowed by {user}.")
        else:
            print("Sorry, the book is not available.")

    def return_book_internal(self, book, user):
        if book in self.borrowed_books and self.borrowed_books[book] == user:
            self.available_books.append(book)
            del self.borrowed_books[book]
            self.user[user].remove(book)
            print(f"{user}, you have returned {book}. Thank you!")
        else:
            print(f"{user}, you have not borrowed this book.")

    def add_book(self, book):
        self.available_books.append(book)
        print(f"{book} has been added to the library.")

    def search_book(self, query):
        results = [book for book in self.available_books if query.lower() in book.lower()]
        if results:
            print("Search results:")
            for book in results:
                print(book)
        else:
            print("No books found.")

    def register_user(self, username):
        if username not in self.user:
            self.user[username] = []
            print(f"User {username} has been registered.")
        else:
            print("User already exists.")

    def borrow_book(self, username, book):
        if username in self.user:
            if book in self.user[username]:
                print("You have already borrowed this book.")
            else:
                self.lend_book(book, username)
        else:
            print("User not registered.")

    def return_book(self, username, book):
        if username in self.user:
            self.return_book_internal(book, username)
        else:
            print("User not registered.")


# Main Program
library = Library(['Think and Grow Rich', 'Who Will Cry When You Die', 'For One More Day'])

while True:
    print("\nLibrary Menu:")
    print("Enter 1 to display the available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to search for a book")
    print("Enter 5 to register a user")
    print("Enter 6 to add books")
    print("Enter 7 to exit")
    try:
        user_choice = int(input("Your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if user_choice == 1:
        library.display_available_books()
    elif user_choice == 2:
        username = input("Enter your name: ")
        requested_book = input("Enter the name of the book you'd like to borrow: ")
        library.borrow_book(username, requested_book)
    elif user_choice == 3:
        username = input("Enter your name: ")
        returned_book = input("Enter the name of the book you'd like to return: ")
        library.return_book(username, returned_book)
    elif user_choice == 4:
        query = input("Enter the book name or author name to search: ")
        library.search_book(query)
    elif user_choice == 5:
        username = input("Enter your name: ")
        library.register_user(username)
    elif user_choice == 6:
        book_name = input("Enter the name of the book you want to add: ")
        library.add_book(book_name)
    elif user_choice == 7:
        break
    else:
        print("Invalid choice! Please choose a valid option.")
