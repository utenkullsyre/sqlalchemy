from sqlalchemy import Column, String, Integer, Date

from base import Base

class Kommune(Base):
    __tablename__='kommuner'

    ogc_fid = Column(Integer, primary_key=True)
    navn = Column(String)

    def __init__(self, navn):
        self.navn = navn


