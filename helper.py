from datetime import datetime

def calculate_fine(issue_date, duration):
    today = datetime.now()
    days_passed = (today - issue_date).days

    if days_passed <= duration:
        return 0

    late_days = days_passed - duration
    weeks = (late_days // 7) + 1

    fine = 0
    for i in range(1, weeks + 1):
        fine += i * 10   # progressive fine

    return fine

def line():
    return "=" * 40

def header(title):
    return f"\n{line()}\n{title.center(40)}\n{line()}"

def menu():
    return f"""
{line()}
        LIBRARY SYSTEM MENU
{line()}
1. Add Book
2. View Books
3. Issue Book
4. Return Book
5. Exit
{line()}
"""