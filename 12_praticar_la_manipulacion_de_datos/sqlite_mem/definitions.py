## ------------------------------------- 
## DECLARACIONES DE LA BASE DE DATOS 
## ------------------------------------- 
 
import os 
import sys 
from sqlalchemy import Column 
from sqlalchemy import Integer, String, DateTime 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
import datetime 
 
## Definiciones de la base de datos 
Base = declarative_base() 
 
#SQLITE_FILE_NAME = "data.dbf" # para debug 
SQLITE_FILE_NAME = ":memory:" 
BASE_NAME = 'sqlite:///'+SQLITE_FILE_NAME 
 
## Declaraciones de las clases 
class BASE_TABLE(): 
   " Clase común a todos el resto" 
   id = Column(Integer, primary_key=True) 
   d_cre = Column(DateTime, default = datetime.datetime.now() ) 
 
class Producto(Base, BASE_TABLE): 
   "Los productos" 
   __tablename__ = 'PRODUCTOS' 
   codigo           = Column(String(20), nullable=False) 
   nombre            = Column(String(50), nullable=False) 
   cantidad            = Column(String(20), default='') 
   marca         = Column(String(20), default='') 
   codigo_nutri     = Column(String(5), default='') 
   nombre_generico  = Column(String(50), default='') 
 
def init_db(): 
   ## Creación de un motor 
   ## Para la creación del esquema 
   engine = create_engine(BASE_NAME, echo=False) 
     
   ## Si no hace falta la creación del esquema 
   Base.metadata.create_all(engine) 
   return engine 
 
## Conexión 
def connect(): 
   engine = init_db() 
   Base.metadata.bind = engine 
   DBSession = sessionmaker(bind=engine) 
   session = DBSession() 
   return session
