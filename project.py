class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability=True):
        self._book_id = book_id  
        self._title = title  
        self._author = author 
        self._availability = availability  
        Library.entry_book(self)

    # Method to borrow the book
    def borrow_book(self):
        if self._availability:
            self._availability = False
            print(f"You have successfully borrowed the book: {self._title}.")
        else:
            print("The book is already borrowed.")

    # Method to return the book
    def return_book(self):
        if not self._availability:
            self._availability = True
            print(f"You have successfully returned the book: {self._title}.")
        else:
            print("The book was not borrowed.")

    def view_book_info(self):
        availability_status = "Available" if self._availability else "Not Available"
        print(f"Book ID: {self._book_id} Title: {self._title} Author: {self._author} Availability: {availability_status}")

    def get_book_id(self):
        return self._book_id

    def __str__(self):
        return f"Book ID: {self._book_id}, Title: {self._title}, Author: {self._author}, Availability: {self._availability}"

# Menu System
def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if Library.book_list:
                print("\nAll Books in Library:")
                for book in Library.book_list:
                    book.view_book_info()
            else:
                print("No books available in the library.")
        
        elif choice == "2":
            try:
                book_id = int(input("Enter the book ID to borrow: "))
                book_to_borrow = next((book for book in Library.book_list if book.get_book_id() == book_id), None)
                
                if book_to_borrow:
                    book_to_borrow.borrow_book()
                else:
                    print("Invalid Book ID.")
            except ValueError:
                print("Please enter a valid number for the Book ID.")
        
        elif choice == "3":
            try:
                book_id = int(input("Enter the book ID to return: "))
                book_to_return = next((book for book in Library.book_list if book.get_book_id() == book_id), None)
                
                if book_to_return:
                    book_to_return.return_book()
                else:
                    print("Invalid Book ID.")
            except ValueError:
                print("Please enter a valid number for the Book ID.")
        
        elif choice == "4":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice, please try again.")

book1 = Book(1, "Python", "Razan")
book2 = Book(2, "Java", "Nam jani na")
book3 = Book(3, "Deep Learning", "DL")
book4 = Book(4, "Machine Learning", "ML")
book5 = Book(5, "C++", "Shumit")
book6 = Book(6, "Chemistry", "Haradon Nag")

menu()
