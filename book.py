def create_book(book_id, title, author):
    return {
        "id": book_id,
        "title": title,
        "author": author,
        "is_issued": False,
        "issued_to": None,
        "issue_date": None,
        "duration": 0
    }