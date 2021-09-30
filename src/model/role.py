from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import true

Base = declarative_base()


class Roles(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=true)
    rolename = Column(String)
    permission_id = Column(Integer)

    def __init__(self, rolename, permission_id) -> None:
        self.rolename
        self.permission_id
