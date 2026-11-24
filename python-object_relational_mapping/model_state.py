#!/usr/bin/python3
"""Defines the State class and the Base instance."""
from sqlalchemy import Column, Integer, String
try:
    from sqlalchemy.orm import declarative_base
except ImportError:
    from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a row of the states table."""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
