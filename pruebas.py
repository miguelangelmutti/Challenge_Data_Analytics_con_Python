import os
import datetime
import pandas as pd

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

    paths = get_last_files_path()
    for path in paths:
        print(path['categoria'])

    
    