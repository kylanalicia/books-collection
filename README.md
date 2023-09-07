# Library Management System CLI

## Overview

The Library Management System CLI is a Python command-line application for managing a library's data. It allows you to perform various tasks related to authors, books, libraries, and book copies, such as adding new entries, listing existing records, and more. This project serves as an example of how to build a CLI application using Python, SQLAlchemy for database management, and Faker for generating test data.

## Features

- Add authors to the database with their names and nationalities.
- Add books to the database with details like ISBN, title, publication year, genre, and associate them with authors.
- Add libraries to the database with names and locations.
- Add book copies to the database with information about their condition and associations with books and libraries.
- List authors, books, libraries, and book copies from the database.

## Requirements

To run this project, you need the following:

- SQLAlchemy (for database management)
- Alembic (for database migrations)
- Faker (for generating test data)

## installation
clone the repository
cd repository
start the project

## Usage
To add an author: python main.py --action add_author
To add a book: python main.py --action add_book
To add a library: python main.py --action add_library
To add a book copy: python main.py --action add_copy
To list authors: python main.py --action list_authors
To list books: python main.py --action list_books
To list libraries: python main.py --action list_libraries
To list book copies in a library: python main.py --action list_copies

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your branch to your fork.
Create a pull request to the main branch of the original repository.

## License
This project is licensed under the MIT License

