import requests
import os 
import datetime
import database
import db 
from models import EspacioCultural, Cine
import pandas as pd 

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


def get_last_files_path():
    rootdirs = ['./bibliotecas', './cines', './museos']
    data = []
    files_path = []

    for rootdir in rootdirs:
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                #print(os.path.join(subdir, file))
                fecha = os.path.getmtime(os.path.join(subdir, file))
                dt = datetime.datetime.fromtimestamp(fecha)
                data.append({'categoria':rootdir.replace('./',''), 'archivo':file,'ruta':os.path.join(subdir, file), 'fecha_modif': dt})

    df = pd.DataFrame.from_dict(data)
    series_max_fecha_modif = df.groupby('categoria')['fecha_modif'].max()
    df_max_fecha_modif = pd.DataFrame(series_max_fecha_modif)
    df_max_fecha_modif = df_max_fecha_modif.rename(columns={'fecha_modif':'fecha_modif_max'})

    # Unir los DataFrames por la columna 'categoria'
    df_unido = df.merge(df_max_fecha_modif, on='categoria', how='inner')

    # Filtrar por la fecha máxima
    df_filtrado = df_unido[df_unido['fecha_modif'] == df_unido['fecha_modif_max']]

    # Visualizar el resultado
    for ind in df_filtrado.index:
        files_path.append({'categoria':df_filtrado['categoria'][ind] ,'ruta':df_filtrado['ruta'][ind]})

    return files_path



if __name__ == '__main__':

    """
            categorias = {

                'bibliotecas':'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/11_bibliotecapopular-datos-abiertos.csv',
                'museos': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv',
                'cines': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/f7a8edb8-9208-41b0-8f19-d72811dcea97/download/salas_cine.csv'
            }

            crear_carpetas(categorias)
            
            for categoria, url in categorias.items():
                respuesta = descargar_archivo(url)
                guardar_archivo(respuesta, categoria)
            
            #drop y crear base de datos
            database.Base.metadata.drop_all(database.engine)
            database.Base.metadata.create_all(database.engine)
            

            dict_ruta_archivos = get_last_files_path()

            for ruta_archivo in dict_ruta_archivos:
                if ruta_archivo['categoria'] in ('bibliotecas','museos'):
                    if ruta_archivo['categoria'] == 'museos':
                        dict_cast = {'cod_area': 'object'}
                        columnas_seleccionadas = ["Cod_Loc","IdProvincia","IdDepartamento","categoria","provincia","localidad","nombre","direccion","CP","cod_area","telefono","Mail","Web"]
                        columnas_reemplazo = {"Cod_Loc":'cod_localidad',
                                                        "IdProvincia":'id_provincia',
                                                        "IdDepartamento":'id_departamento',
                                                        "direccion":'domicilio',
                                                        "CP":'cp',
                                                        "Mail":'mail',
                                                        "Web":'web'
                                                        }
                    elif ruta_archivo['categoria'] == 'bibliotecas':
                        dict_cast = {'cod_tel': 'object', 'telefono':'object'}
                        columnas_seleccionadas = ["cod_localidad","id_provincia","id_departamento","categoria","provincia","localidad","nombre","domicilio","cp","cod_tel","telefono","mail","web"]
                        columnas_reemplazo = {"cod_tel":'cod_area'}
                    else:
                        pass
                else:
                    columnas_seleccionadas_cine = ["cod_localidad","id_provincia","id_departamento","categoria","provincia","localidad","nombre","direccion","cp","web","fuente","sector","pantallas","butacas","espacio_incaa"]
                    columnas_seleccionadas = ["cod_localidad","id_provincia","id_departamento","categoria","provincia","localidad","nombre","direccion","cp","web"]
                    columnas_reemplazo = {"direccion":'domicilio'}
                    
                df = pd.read_csv(ruta_archivo['ruta'],dtype=dict_cast)
                df = df[columnas_seleccionadas]
                df = df.rename(columns= columnas_reemplazo)
                if ruta_archivo['categoria'] == 'cines':
                    df['telefono'] = None
                else:
                    df['telefono'] = df['cod_area'] + '-' + df['telefono']
                    df.drop(['cod_area'], axis=1, inplace=True)
                df['creado'] = datetime.datetime.now()
                df.to_sql('espacios_culturales',con=database.engine, if_exists='append', index=False)
                
    """        
    db.create_db()
    sql_stmt = db.read_sql()
    db.create_table(sql_stmt)