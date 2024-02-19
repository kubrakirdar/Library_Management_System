import os

class Library:
    def __init__(self):
        self.file_name = 'books.txt'
        self.file = open(self.file_name, 'a+')

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.readlines()
        for line in lines:
            book_info = line.strip().split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Pages: {book_info[3]}")

    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        book_release_year = input("Enter book release year: ")
        book_pages = input("Enter book pages: ")
        book_info = f"{book_title},{book_author},{book_release_year},{book_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        book_title = input("Enter book title to remove: ")
        lines = self.file.readlines()
        books = []
        for line in lines:
            book_info = line.strip().split(',')
            books.append(book_info)
        book_index = -1
        for i in range(len(books)):
            if books[i][0] == book_title:
                book_index = i
                break
        if book_index != -1:
            del books[book_index]
            self.file.seek(0)
            self.file.truncate()
            for book in books:
                book_info = f"{book[0]},{book[1]},{book[2]},{book[3]}\n"
                self.file.write(book_info)
            print("Book removed successfully.")
        else:
            print("Book not found.")

lib = Library()
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    menu_item = int(input("Enter menu item: "))
    if menu_item == 1:
        lib.list_books()
    elif menu_item == 2:
        lib.add_book()
    elif menu_item == 3:
        lib.remove_book()
    elif menu_item == 4:
        break
    else:
        print("Invalid menu item.")
    input("Press Enter to continue...")