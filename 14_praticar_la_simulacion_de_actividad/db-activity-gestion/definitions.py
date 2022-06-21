## ------------------------------------- 
## DEFINICIONES DE LA BASE DE DATOS 
## ------------------------------------- 
 
import os 
import sys 
from sqlalchemy import Column, ForeignKey 
from sqlalchemy import Integer, String, DateTime, Date, Float,  
BigInteger 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship 
from sqlalchemy import create_engine 
import datetime 
 
Base = declarative_base() 
 
BASE_NAME = 'sqlite:///data.dbf' 
 
class BASE_TABLE(): 
   " Clase común al resto " 
   id = Column(Integer, primary_key=True) 
   d_cre = Column(DateTime, default = datetime.datetime.now() ) 
   d_mod = Column(DateTime,  
                  default = datetime.datetime.now(),   
                  onupdate=datetime.datetime.now() 
           ) 
 
class Contador(Base, BASE_TABLE): 
   "Tabla de los contadores" 
   __tablename__ = "CONTADORES" 
   nombre = Column(String(20), nullable=False, unique=True) 
   val = Column(Integer) 
 
   def __repr__(self): 
       return "< contador: {0:} / {1:} >".format( self.nombre,   
                                                   self.val ) 
 
class Cliente(Base, BASE_TABLE): 
   "El archivo cliente" 
   __tablename__ = 'CLIENTES' 
   nombre = Column(String(20), nullable=False, unique=True) 
 
   def __repr__(self): 
       return "< cliente: {0:} >".format(self.nombre) 
 
class Producto(Base, BASE_TABLE): 
   "Los productos" 
   __tablename__ = 'PRODUCTOS' 
   desc = Column(String(30), nullable=False, unique=True) 
   precio = Column(Float(12,2)) 
 
   def __repr__(self): 
       return "< producto: {0:} / {1:} >".format(self.desc,   
                                                 self.precio) 
 
class Proveed(Base, BASE_TABLE): 
   "Los proveedores" 
   __tablename__ = 'PROVDR' 
   nombre = Column(String(20), nullable=False, unique=True) 
   plazo = Column(Integer) 
 
   def __repr__(self): 
       return "< proveed: {0:}/{1:} >".format(self.nombre,   
                                             self.plazo) 
 
class Stock(Base, BASE_TABLE): 
   "El stock por almacén" 
   __tablename__ = 'STOCK' 
   almacen = Column(String(10), nullable=False) 
   producto_id = Column(Integer, ForeignKey('PRODUCTOS.id')) 
   producto = relationship(Producto) 
   qstock = Column(Integer) 
 
   def __repr__(self): 
       return "< Stock: {0:}/{1:}/{2:} >".format(self.almacen,   
                                                  self.producto_id,   
                                                  self.qstock ) 
 
class PedCli(Base, BASE_TABLE): 
   "Los pedidos de clientes" 
   __tablename__ = 'PEDCLI' 
   numped = Column(Integer, unique=True) 
   fecped = Column(DateTime, default = datetime.datetime.now() ) 
   cliente_id = Column(Integer, ForeignKey('CLIENTS.id')) 
   cliente = relationship(Cliente) 
   factura = Column(Integer) 
 
   def __repr__(self): 
       return "< Pedcli:{0:}/{1:}/{2:}/{3:}>".format(self.numped, 
                                                     self.fecped, 
                                                     self.cliente_id, 
                                                     self.factura ) 
 
class LinCli(Base, BASE_TABLE): 
   "Las líneas de pedidos de clientes" 
   __tablename__ = 'LINCLI' 
   numped = Column(Integer) 
   numlin = Column(Integer) 
   producto_id = Column(Integer, ForeignKey('PRODUCTOS.id')) 
   producto = relationship(Producto) 
   cped = Column(Integer) 
   precio = Column(Float(12,2)) 
   centreg = Column(Integer) 
   cfac = Column(Integer)  
 
   def __repr__(self): 
       return "<lincli:{0:}/{1:}/{2:}/{3:} >".format(self.numped, 
                                                     self.numlin,   
                                                     self.producto_id,   
                                                     self.cped ) 
 
class LinProv(Base, BASE_TABLE): 
   "Los pedidos proveedores" 
   __tablename__ = 'LINPROV' 
   numped = Column(Integer, unique=True) 
   numlin = Column(Integer) 
   prov_id = Column(Integer, ForeignKey('PROVDR.id')) 
   prov = relationship(Proveed) 
   producto_id = Column(Integer, ForeignKey('PRODUCTOS.id')) 
   producto = relationship(Producto) 
   cped = Column(Integer) 
   precio = Column(Float(12,2)) 
   fprevi = Column(Date)  
   crec = Column(Integer) 
 
   def __repr__(self): 
       return "<linprov:{0:}/{1:}/{2:}/{3:}/{4:}>".format(self.numped, 
                                                         self.numlin, 
                                                         self.prov_id, 
                                                         self.producto_id, 
                                                         self.cped ) 
 
 
 
 
# Creación de la base de datos 
engine = create_engine(BASE_NAME) 
 
# Creación de las tablas en la base de datos 
Base.metadata.create_all(engine)
