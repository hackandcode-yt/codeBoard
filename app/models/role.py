from sqlalchemy import Column, Integer, String
from fastapi_framework import database


class Roles(database.Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rolename = Column(String)
    permission_id = Column(Integer)

    def __init__(self, rolename, permission_id) -> None:
        self.rolename = rolename
        self.permission_id = permission_id
