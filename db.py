#!/usr/bin/env python
from sqlalchemy import  MetaData, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define a naming convention for foreign keys
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
# Create a metadata object with the naming convention
metadata = MetaData(naming_convention=convention)

# Create a base class for declarative models with the metadata
Base = declarative_base(metadata=metadata)

# Create an SQLAlchemy engine and session connected to an SQLite database
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()