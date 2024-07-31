#!/usr/bin/python3
"""
    State module inherits from declarative_base()
    Create state table
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """ State Class """
    __tablename__ = 'states'
    id = Column(Integr, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
