# coding=utf-8

# 1 - imports
from base import Session, engine, Base
from kommune import Kommune


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

testkommune = Kommune("Drittkommune")

session.add(testkommune)

session.commit()
session.close()