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

class Book(Base):
    __tablename__ = 'books'

    isbn = Column(String, primary_key=True)
    title = Column(String)
    publication_year = Column(Integer)
    genre = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')
    copies = relationship('BookCopy', back_populates='book')

class Library(Base):
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    copies = relationship('BookCopy', back_populates='library')

class BookCopy(Base):
    __tablename__ = 'book_copies'

    copy_id = Column(Integer, primary_key=True)
    condition = Column(String)
    isbn = Column(String, ForeignKey('books.isbn'))
    library_id = Column(Integer, ForeignKey('libraries.id'))

    book = relationship('Book', back_populates='copies')
    library = relationship('Library', back_populates='copies')


