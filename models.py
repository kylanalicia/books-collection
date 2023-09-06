#!/usr/bin/env python
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from db import Base, session

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nationality = Column(String)
    
    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}', nationality='{self.nationality}')"


class Book(Base):
    __tablename__ = 'books'

    isbn = Column(String, primary_key=True)
    title = Column(String)
    publication_year = Column(Integer)
    genre = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')
    copies = relationship('BookCopy', back_populates='book')

    def __repr__(self) -> str:
        return super().__repr__()
    
    def __repr__(self):
        return f"Book(isbn='{self.isbn}', title='{self.title}', publication_year={self.publication_year}, genre='{self.genre}', author_id={self.author_id})"

class Library(Base):
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    copies = relationship('BookCopy', back_populates='library')

    def __repr__(self):
        return f"Library(id={self.id}, name='{self.name}', location='{self.location}')"

class BookCopy(Base):
    __tablename__ = 'book_copies'

    copy_id = Column(Integer, primary_key=True)
    condition = Column(String)
    isbn = Column(String, ForeignKey('books.isbn'))
    library_id = Column(Integer, ForeignKey('libraries.id'))

    book = relationship('Book', back_populates='copies')
    library = relationship('Library', back_populates='copies')

    def __repr__(self):
        return f"BookCopy(copy_id={self.copy_id}, condition='{self.condition}', isbn='{self.isbn}', library_id={self.library_id})"
    
    