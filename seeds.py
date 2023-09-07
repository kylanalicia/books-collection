from models import Author, Book, Library, BookCopy
from faker import Faker
from db import session

if __name__ == '__main__':

    session.query(Author).delete()
    session.query(Book).delete()
    session.query(Library).delete()
    session.query(BookCopy).delete()


    fake = Faker()

    # Generate Authors
authors = []
for i in range(5):  # Generate 5 fake authors
    author = Author(
        name=fake.name(),
        nationality=fake.country()
    )
    session.add(author)
    session.commit()
    authors.append(author)

# Generate Books
books = []
for i in range(10):  # Generate 10 fake books
    book = Book(
        isbn=fake.isbn13(),
        title=fake.catch_phrase(),
        publication_year=fake.random_int(min=1900, max=2023),
        genre=fake.word(),
        author=authors[i % len(authors)]  # Assign authors in a round-robin fashion
    )
    session.add(book)
    session.commit()
    books.append(book)

# Generate Libraries
libraries = []
for i in range(2):  # Generate 2 fake libraries
    library = Library(
        name=fake.company(),
        location=fake.city()
    )
    session.add(library)
    session.commit()
    libraries.append(library)

# Generate Book Copies
for i in range(15):  # Generate 15 fake book copies
    copy = BookCopy(
        condition=fake.random_element(elements=('Good', 'Fair', 'Excellent')),
        book=books[i % len(books)],  # Assign books in a round-robin fashion
        library=libraries[i % len(libraries)]  # Assign libraries in a round-robin fashion
    )
    session.add(copy)
    session.commit()


