# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:admin@localhost/kommuner')
Session = sessionmaker(bind=engine)

Base = declarative_base()

##from sqlalchemy import create_engine
##from json import loads
##
##db_connect = create_engine('postgresql://postgres:admin@localhost/kommuner')
##
##conn = db_connect.connect()
##
##query = conn.execute("SELECT navn from kommuner limit 5")
##
##resultat = [x for x in query.fetchall()]
##


