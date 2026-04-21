from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
SQLite database configuration module for SQLAlchemy ORM.
This module sets up a SQLite database connection engine for the FastAPI application.
Attributes:
    SQLALCHEMY_DATABASE_URL (str): SQLite database URL pointing to './todos.db' file
        in the current directory.
    engine (Engine): SQLAlchemy engine instance configured for SQLite with special
        connection settings.
Note:
    The 'check_same_thread' parameter is set to False because SQLite by default
    enforces that database connections are used only in the same thread that created them.
    This check is disabled here to allow SQLAlchemy connection pooling to work properly
    in multi-threaded environments like FastAPI applications, where multiple threads
    may use connections from the pool. Without this setting, SQLite would raise errors
    when different threads try to access the database through pooled connections.
"""

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()