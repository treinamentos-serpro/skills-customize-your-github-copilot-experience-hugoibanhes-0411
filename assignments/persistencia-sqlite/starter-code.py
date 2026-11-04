import sqlite3

DATABASE_NAME = "books.db"


def create_table(connection):
    """Create the books table if it does not already exist."""
    raise NotImplementedError("Complete this function in Task 1")


def add_book(connection, title, author):
    """Insert a book into the database."""
    raise NotImplementedError("Complete this function in Task 2")


def list_books(connection):
    """Print every book in the database."""
    raise NotImplementedError("Complete this function in Task 3")


def find_book(connection, book_id):
    """Print the book with this ID, or a message if it does not exist."""
    raise NotImplementedError("Complete this function in Task 3")


def main():
    connection = sqlite3.connect(DATABASE_NAME)
    try:
        create_table(connection)
        add_book(connection, "The Hobbit", "J. R. R. Tolkien")
        add_book(connection, "A Wrinkle in Time", "Madeleine L'Engle")
        list_books(connection)
        find_book(connection, 1)
    finally:
        connection.close()


if __name__ == "__main__":
    main()