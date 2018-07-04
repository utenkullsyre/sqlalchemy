from sqlalchemy import Column, String, Integer, Date

from base import Base

class Kommune(Base):
    __tablename__='kommuner'

    ogc_fid = Column(Integer, primary_key=True)
    navn = Column(String)
    fylke = Column(String)
    kommunenummer = Column(String)
    kommunenavn = Column(String)
    fylkesnavn = Column(String)



    def __init__(self,ogc_fid, navn, fylke, kommunenummer, kommunenavn, fylkesnavn):
        self.ogc_fid = ogc_fid
        self.navn = navn
        self.fylke = fylke
        self.kommunenummer = kommunenummer
        self.kommunenavn = kommunenavn
        self.fylkesnavn = fylkesnavn


