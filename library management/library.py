from tkinter import *

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x400")

        # Create widgets
        self.book_id_label = Label(self.root, text="Book ID")
        self.book_id_label.grid(row=0, column=0)
        self.book_id_entry = Entry(self.root)
        self.book_id_entry.grid(row=0, column=1)

        self.book_title_label = Label(self.root, text="Book Title")
        self.book_title_label.grid(row=1, column=0)
        self.book_title_entry = Entry(self.root)
        self.book_title_entry.grid(row=1, column=1)

        self.add_button = Button(self.root, text="Add Book", command=self.add_book, bg="green")
        self.add_button.grid(row=2, column=0)
        self.delete_button = Button(self.root, text="Delete Book", command=self.delete_book, bg="red")
        self.delete_button.grid(row=2, column=1)
        self.search_button = Button(self.root, text="Search Book", command=self.search_book, bg="blue")
        self.search_button.grid(row=3, column=0)
        self.display_button = Button(self.root, text="Display Books", command=self.display_books, bg="yellow")
        self.display_button.grid(row=3, column=1)
        self.exit_button = Button(self.root, text="Exit", command=self.root.quit, bg="gray")
        self.exit_button.grid(row=4, columnspan=2)

        self.message_label = Label(self.root, text="")
        self.message_label.grid(row=5, columnspan=2)

        # Initialize book data (replace with your data source)
        self.books = []

    def add_book(self):
        book_id = self.book_id_entry.get()
        book_title = self.book_title_entry.get()
        if book_id and book_title:
            self.books.append({"id": book_id, "title": book_title})
            self.message_label.config(text="Book added successfully!")
            self.clear_fields()
        else:
            self.message_label.config(text="Please provide both Book ID and Title.")

    def delete_book(self):
        book_id = self.book_id_entry.get()
        for i, book in enumerate(self.books):
            if book["id"] == book_id:
                del self.books[i]
                self.message_label.config(text="Book deleted successfully!")
                self.clear_fields()
                return
        self.message_label.config(text="Book not found.")

    def search_book(self):
        book_id = self.book_id_entry.get()
        for book in self.books:
            if book["id"] == book_id:
                self.message_label.config(text=f"Book Title: {book['title']}")
                return
        self.message_label.config(text="Book not found.")

    def display_books(self):
        if not self.books:
            self.message_label.config(text="No books found.")
        else:
            book_list = "\n".join([f"Book ID: {book['id']}, Title: {book['title']}" for book in self.books])
            self.message_label.config(text=book_list)

    def clear_fields(self):
        self.book_id_entry.delete(0, END)
        self.book_title_entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
