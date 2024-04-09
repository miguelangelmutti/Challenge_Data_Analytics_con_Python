from datetime import datetime
import database

from sqlalchemy import Column, Integer, String, Float, DateTime

class EspacioCultural(database.Base):
    __tablename__ = 'espacios_culturales'

    id = Column(Integer, primary_key=True)
    cod_localidad = Column(Integer)
    id_provincia = Column(Integer)
    id_departamento = Column(Integer)
    categoria = Column(String(200), nullable=False)
    provincia = Column(String(200))
    localidad = Column(String(200))
    nombre = Column(String(200), nullable=False)
    domicilio = Column(String(200))
    cp  =   Column(String(200))
    #cod_area  =   Column(String(200))
    #telefono  =   Column(String(200))
    telefono  =   Column(String(200))
    mail  =   Column(String(200))
    web  =   Column(String(200))
    creado = Column(DateTime(), default=datetime.now())
    

    def __repr__(self):
        return f'({self.categoria}, {self.nombre}, {self.domicilio})'

    def __str__(self):
        return self.nombre


class Cine(database.Base):
    __tablename__ = 'info_cines'
    id = Column(Integer, primary_key=True)
    id_provincia = Column(Integer)
    provincia = Column(String(200))
    cant_pantallas = Column(Integer)
    cant_butacas = Column(Integer)
    cant_espacios_incaa = Column(Integer)
    creado = Column(DateTime(), default=datetime.now())
    

    def __repr__(self):
        return f'({self.provincia}, {self.cant_pantallas}, {self.cant_butacas}, {self.cant_espacios_incaa})'

    def __str__(self):
        return f'({self.provincia}, {self.cant_pantallas}, {self.cant_butacas}, {self.cant_espacios_incaa})'
    
