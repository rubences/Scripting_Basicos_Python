## ------------ 
## DEFINICIONES 
## ------------ 
 
import os 
import sys 
from sqlalchemy import Column 
from sqlalchemy import Integer, String, DateTime, Date, Numeric 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine 
import datetime 
 
## Definiciones de la base de datos 
Base = declarative_base() 
 
SQLITE_FILE_NAME = "data.dbf" 
BASE_NAME = 'sqlite:///'+SQLITE_FILE_NAME 
 
## Declaraciones de las clases 
class BASE_TABLE(): 
   " Clas común al resto" 
   id = Column(Integer, primary_key=True) 
   d_cre = Column(DateTime, 
                  default = datetime.datetime.now() 
                  ) 
   d_mod = Column(DateTime, 
                  default = datetime.datetime.now(), 
                  onupdate=datetime.datetime.now() 
                   ) 
   status = Column(String(5), default = "OK", nullable = False ) 
 
class Contact(Base, BASE_TABLE): 
   "El archivo Contactocs" 
   __tablename__ = 'CONTACTOS' 
   nombre         = Column(String(20), nullable=False) 
   fecnac      = Column(Date) 
   sexo       = Column(String(1)) 
   tel         = Column(String(30)) 
   profesion  = Column(String(40)) 
 
## Creaión de un motor 
## Para cla creión del esquema 
engine = create_engine(BASE_NAME) 
 
## Si no se ha hecho durante la creación del esquema 
Base.metadata.create_all(engine)
