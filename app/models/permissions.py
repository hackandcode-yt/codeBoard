from fastapi_framework import database
from sqlalchemy import Column, Integer, String


class Permissions(database.Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def __init__(self, name) -> None:
        self.name = name
