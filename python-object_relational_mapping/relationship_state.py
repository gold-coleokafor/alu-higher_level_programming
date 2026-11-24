#!/usr/bin/python3
"""Defines the State class with a relationship to City."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
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
    cities = relationship("City", cascade="all, delete", backref="state")
