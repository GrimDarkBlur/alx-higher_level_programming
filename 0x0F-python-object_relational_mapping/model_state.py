#!/usr/bin/env python3
"""
Holds the definnation for the state model
for the ORM of the AIR BNB project
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Ant object representation of the
    the State table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
