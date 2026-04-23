import library_services as lib
from helper import header, menu

while True:
    print(menu())
    choice = input("Enter choice: ")

    if choice == "1":
        print(header("ADD BOOK"))
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        print("\n" + lib.add_book(book_id, title, author))

    elif choice == "2":
        print(header("BOOK LIST"))
        print(lib.view_books())

    elif choice == "3":
        print(header("ISSUE BOOK"))
        book_id = input("Book ID: ")
        student = input("Student Name: ")
        duration = int(input("Duration (days): "))
        print("\n" + lib.issue_book(book_id, student, duration))

    elif choice == "4":
        print(header("RETURN BOOK"))
        book_id = input("Book ID: ")
        print("\n" + lib.return_book(book_id))

    elif choice == "5":
        print("\nExiting system...")
        break

    else:
        print("\nInvalid choice.")