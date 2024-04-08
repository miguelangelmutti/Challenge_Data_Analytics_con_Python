from datetime import datetime
import database

from sqlalchemy import Column, Integer, String, Float, DateTime

"""
Observaciones	
nombre	Archivo Y Museo Histórico Gral. Julio De Vedia
direccion	Libertad 1191
piso	
CP	B6500EVL
cod_area	2317
telefono	425 279
Mail	archivoymuseo@yahoo.com.ar
Web	www.portaldel9.com.ar
Latitud	-35.4417620
Longitud	-60.8875980
TipoLatitudLongitud	Localización precisa
Info_adicional	
jurisdiccion	Municipal
año_inauguracion	1920
actualizacion	2017
"""

class Museo(database.Base):
    __tablename__ = 'museos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(100), nullable=False)
    CP  =   Column(String(100))
    cod_area  =   Column(String(100))
    telefono  =   Column(String(100))
    Mail  =   Column(String(100))
    Web  =   Column(String(100))
    Latitud =   Column(Float)
    Longitud =   Column(Float)
    TipoLatitudLongitud = Column(String(50))
    Info_adicional =   Column(String(100))
    jurisdiccion	= Column(String(50))
    anio_inauguracion = Column(Integer)
    actualizacion	= Column(Integer)
    creado = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f'Museo({self.nombre}, {self.direccion})'

    def __str__(self):
        return self.nombre