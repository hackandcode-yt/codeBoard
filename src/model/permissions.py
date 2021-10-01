from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import true

Base = declarative_base()


class Permissions(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, autoincrement=true)
    name = Column(String)

    def __init__(self, name, role_id) -> None:
        self.name = name
