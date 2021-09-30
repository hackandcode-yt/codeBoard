from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import true

Base = declarative_base()


class Permissions(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, autoincrement=true)
    name = Column(String)
    role_id = Column(Integer)

    def __init__(self, name, role_id) -> None:
        self.name = name
        self.role_id = role_id
