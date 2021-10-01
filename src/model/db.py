from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import role
import permissions
import person

engine = create_engine('sqlite:///test.db')
session = sessionmaker(bind=engine)()

role.Base.metadata.create_all(engine)
permissions.Base.metadata.create_all(engine)
person.Base.metadata.create_all(engine)
