from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import true

Base = declarative_base()


class Persons(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True, autoincrement=true)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String)

    def __init__(self, first_name, last_name, role) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
