from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Author, Book, Library, BookCopy
import argparse

# Replace 'sqlite:///database.db' with your actual database connection string
db_engine = create_engine('sqlite:///database.db')

# Create a session
Session = sessionmaker(bind=db_engine)
session = Session()


# Define your methods here

def add_author(name, nationality):
    author = Author(name=name, nationality=nationality,)
    session.add(author)
    session.commit()

def add_book(isbn, title, publication_year, genre, author_id):
    book = Book(isbn=isbn, title=title, publication_year=publication_year, genre=genre, author_id=author_id)
    session.add(book)
    session.commit()

def add_library(name, location):
    library = Library(name=name, location=location)
    session.add(library)
    session.commit()

def add_book_copy(condition, isbn, library_id):
    copy = BookCopy(condition=condition, isbn=isbn, library_id=library_id)
    session.add(copy)
    session.commit()

def list_authors():
    authors = session.query(Author).all()
    for author in authors:
        print(f"{author.id}: {author.name}, {author.nationality}")

def list_books():
    books = session.query(Book).all()
    for book in books:
        author = session.query(Author).filter_by(id=book.author_id).first()
        print(f"{book.isbn}: {book.title} ({book.publication_year}), Author: {author.name}")

def list_libraries():
    libraries = session.query(Library).all()
    for library in libraries:
        print(f"{library.id}: {library.name}, Location: {library.location}")

def list_library_copies(library_id):
    copies = session.query(BookCopy).filter_by(library_id=library_id).all()
    for copy in copies:
        book = session.query(Book).filter_by(isbn=copy.isbn).first()
        print(f"Copy ID: {copy.copy_id}, Book: {book.title}, Condition: {copy.condition}")

def main():
    parser = argparse.ArgumentParser(description="Library Management System CLI")
    parser.add_argument("--action", choices=["add_author", "add_book", "add_library", "add_copy", "list_authors", "list_books", "list_libraries", "list_copies"], required=True, help="Action to perform")

    args = parser.parse_args()

    if args.action == "add_author":
        name = input("Enter author's name: ")
        nationality = input("Enter author's nationality: ")
        add_author(name, nationality)

    elif args.action == "add_book":
        isbn = input("Enter book's ISBN: ")
        title = input("Enter book's title: ")
        publication_year = int(input("Enter publication year: "))
        genre = input("Enter book's genre: ")
        author_id = int(input("Enter author's ID: "))
        add_book(isbn, title, publication_year, genre, author_id)

    elif args.action == "add_library":
        name = input("Enter library name: ")
        location = input("Enter library location: ")
        add_library(name, location)

    elif args.action == "add_copy":
        condition = input("Enter copy condition (Good/Fair/Excellent): ")
        isbn = input("Enter book's ISBN: ")
        library_id = int(input("Enter library ID: "))
        add_book_copy(condition, isbn, library_id)

    elif args.action == "list_authors":
        list_authors()

    elif args.action == "list_books":
        list_books()

    elif args.action == "list_libraries":
        list_libraries()

    elif args.action == "list_copies":
        library_id = int(input("Enter library ID: "))
        list_library_copies(library_id)

if __name__ == "__main__":
    main()
