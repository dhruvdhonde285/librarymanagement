class BookNode:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.next = None


class Library:
    def __init__(self):
        self.head = None

    def add_book(self, book_id, title):
        new_book = BookNode(book_id, title)
        if not self.head:
            self.head = new_book
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_book
        print(f"Book '{title}' added!")

    def delete_book(self, book_id):
        if not self.head:
            print("No books to delete.")
            return

        if self.head.book_id == book_id:
            print(f"Book '{self.head.title}' deleted!")
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.book_id != book_id:
            current = current.next

        if current.next:
            print(f"Book '{current.next.title}' deleted!")
            current.next = current.next.next
        else:
            print("Book not found.")

    def search_book(self, book_id):
        current = self.head
        while current:
            if current.book_id == book_id:
                print(f"Book Found: [ID: {current.book_id}, Title: '{current.title}']")
                return
            current = current.next
        print("Book not found.")

    def display_books(self):
        if not self.head:
            print("No books in the library.")
            return

        print("Books in the Library:")
        current = self.head
        while current:
            print(f"[ID: {current.book_id}, Title: '{current.title}']")
            current = current.next


if __name__ == "__main__":
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            library.add_book(book_id, title)
        elif choice == "2":
            book_id = input("Enter Book ID to delete: ")
            library.delete_book(book_id)
        elif choice == "3":
            book_id = input("Enter Book ID to search: ")
            library.search_book(book_id)
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice! Please try again.")
