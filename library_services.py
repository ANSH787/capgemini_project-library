from datetime import datetime
from book import create_book
from helper import calculate_fine

books = {}

def add_book(book_id, title, author):
    if book_id in books:
        return "Book already exists."

    books[book_id] = create_book(book_id, title, author)
    return "Book added successfully."




def issue_book(book_id, student_name, duration):
    if book_id not in books:
        return "Book not found."

    book = books[book_id]

    if book["is_issued"]:
        return "Book already issued."

    book["is_issued"] = True
    book["issued_to"] = student_name
    book["issue_date"] = datetime.now()
    book["duration"] = duration

    return f"Book issued to {student_name} for {duration} days."


def return_book(book_id):
    if book_id not in books:
        return "Book not found."

    book = books[book_id]

    if not book["is_issued"]:
        return "Book was not issued."

    fine = calculate_fine(book["issue_date"], book["duration"])

    student = book["issued_to"]

    # reset
    book["is_issued"] = False
    book["issued_to"] = None
    book["issue_date"] = None
    book["duration"] = 0

    return f"Book returned by {student}. Fine: ₹{fine}"

def view_books():
    if not books:
        return "No books available."

    result = "\n" + "-" * 55 + "\n"
    result += f"{'ID':<8}{'TITLE':<20}{'AUTHOR':<15}{'STATUS':<10}\n"
    result += "-" * 55 + "\n"

    for b in books.values():
        status = "Issued" if b["is_issued"] else "Available"
        result += f"{b['id']:<8}{b['title']:<20}{b['author']:<15}{status:<10}\n"

    result += "-" * 55
    return result