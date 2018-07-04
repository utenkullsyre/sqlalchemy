# coding=utf-8

from base import Session, engine, Base
from kommune import Kommune
from json import loads

session = Session()

kommune = session.query(Kommune).all()
##test = session.query(Kommune).filter(Kommune.navn == 'Testkommune').\
##    delete(synchronize_session=False)
##session.commit()
test =  [[x.ogc_fid ,loads(x.navn), loads(x.fylke)] for x in kommune]

##print test
##
##for x in test:
##    try:
##        print x[0]['navn']
##    except:
##        print x

##liste = [(x[0], x[1][0]['navn'], x[2][0]['navn']) for x in test]
##
##for x in liste:
##    item = session.query(Kommune).filter(Kommune.ogc_fid == x[0]).one()
##    item.fylkesnavn = x[2]
##    item.kommunenavn = x[1]
##    session.add(item)

##item = session.query(Kommune).filter(Kommune.ogc_fid == 54).one()


##session.commit()

