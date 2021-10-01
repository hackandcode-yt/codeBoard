from sqlalchemy import Column, Integer, String
from fastapi_framework import database


class Persons(database.Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    role_id = Column(Integer)

    def __init__(self, first_name, last_name, role) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.role = role