## --------------------
## SCRIPT DE BASE
## --------------------

## ATENCION es IMPORTE EN ALGUNOS SCRIPTS

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
 
from definitions import Base, BASE_NAME
from definitions import Client, Producto, Fourn, Stock, ComCli, LigCli, LigFou

#import sequence as seq

#import datetime
#import random
#import pdb

## Conexion
def connect():
	engine = create_engine(BASE_NAME, echo=False)
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def get_catalog():
	session = connect()
	s = select([Producto.id])
	prods = session.execute(s)
	p = [ x[0] for x in prods]
	session.close()
	return p


def run():
	get_catalog()
 

if __name__ == '__main__':
	run()
