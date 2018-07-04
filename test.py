# coding=utf-8

from base import Session, engine, Base
from kommune import Kommune

session = Session()

kommune = session.query(Kommune).first()




