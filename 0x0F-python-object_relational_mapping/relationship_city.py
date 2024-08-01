#!/usr/bin/python3

"""
    City module inherits from declarative_base()
    Create city table
"""


from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ City Class """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
