import requests
import os 
import datetime

"""
Organizar los archivos en rutas siguiendo la siguiente estructura:
“categoría\año-mes\categoria-dia-mes-año.csv”
○ Por ejemplo: “museos\2021-noviembre\museos-03-11-2021”
○ Si el archivo existe debe reemplazarse. La fecha de la nomenclatura
es la fecha de descarga.

"""


def get_fechas_string(tipo):
    
    meses_ingles_espanol = {
    "January": "Enero",
    "February": "Febrero",
    "March": "Marzo",
    "April": "Abril",
    "May": "Mayo",
    "June": "Junio",
    "July": "Julio",
    "August": "Agosto",
    "September": "Septiembre",
    "October": "Octubre",
    "November": "Noviembre",
    "December": "Diciembre"
    }

    x = datetime.datetime.now()
    if tipo == 1:
        periodo_ingles = x.strftime("%B-%Y")
        periodo = periodo_ingles.replace(x.strftime("%B"),meses_ingles_espanol[x.strftime("%B")])
    elif tipo == 2:
        periodo = x.strftime("%d-%m-%Y")
    else: 
        pass 
    return periodo


def crear_carpetas(categorias):
    for categoria in categorias:
        #if not os.path.exists(path):
        periodo = get_fechas_string(1)
        new_path = f"{categoria}/{periodo}"
        if not os.path.exists(new_path):
            os.makedirs(new_path)
    

def descargar_archivo(url):
    respuesta = requests.get(url)
    nombre = url.split('/')[-1::][0].split('.csv')[0]
    respuesta_diccionario = {"nombre" : nombre, "respuesta": respuesta}
    return respuesta_diccionario 

def guardar_archivo(respuesta_diccionario, categoria):
    respuesta = respuesta_diccionario["respuesta"]
    nombre = categoria + "-" + get_fechas_string(2)
    periodo = get_fechas_string(1)
    ruta_al_archivo = f"{categoria}/{periodo}/{nombre}.csv"
    with open(ruta_al_archivo, "wb") as archivo:
        archivo.write(respuesta.content)
    print(f"Descarga completada: {respuesta.status_code}")





















if __name__ == '__main__':
        
        categorias = {

            'bibliotecas':'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/11_bibliotecapopular-datos-abiertos.csv',
            'museos': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv',
            'cines': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/f7a8edb8-9208-41b0-8f19-d72811dcea97/download/salas_cine.csv'
        }

        crear_carpetas(categorias)
        
        for categoria, url in categorias.items():
            respuesta = descargar_archivo(url)
            guardar_archivo(respuesta, categoria)
