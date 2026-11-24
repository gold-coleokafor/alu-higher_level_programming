#!/usr/bin/python3
"""Defines the City class."""
from relationship_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """Represents a row of the cities table."""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
