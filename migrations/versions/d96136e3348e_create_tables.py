"""create_tables

Revision ID: d96136e3348e
Revises: 
Create Date: 2023-09-06 23:42:11.925689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd96136e3348e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'authors',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.Column('birthdate', sa.Date(), nullable=True),
        sa.Column('nationality', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'books',
        sa.Column('isbn', sa.String(length=255), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=True),
        sa.Column('publication_year', sa.Integer(), nullable=True),
        sa.Column('genre', sa.String(length=255), nullable=True),
        sa.Column('author_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
        sa.PrimaryKeyConstraint('isbn')
    )

    op.create_table(
        'libraries',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.Column('location', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'book_copies',
        sa.Column('copy_id', sa.Integer(), nullable=False),
        sa.Column('condition', sa.String(length=255), nullable=True),
        sa.Column('isbn', sa.String(length=255), nullable=True),
        sa.Column('library_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['isbn'], ['books.isbn'], ),
        sa.ForeignKeyConstraint(['library_id'], ['libraries.id'], ),
        sa.PrimaryKeyConstraint('copy_id')
    )

def downgrade():
    op.drop_table('book_copies')
    op.drop_table('libraries')
    op.drop_table('books')
    op.drop_table('authors')
