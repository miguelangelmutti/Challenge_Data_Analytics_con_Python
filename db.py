import psycopg2
import os

# Define la información de la conexión
host = "localhost"
port = 5432
#database = "challenge_data_analytics_con_python"
user = "postgres"
password = "postgres"





def create_db():
    # Connect just to PostgreSQL with the user loaded from the .ini file
    conn = psycopg2.connect(
            host=host,
            port=port,
            #database=database,
            user=user,
            password=password,
        )
    cur = conn.cursor()

    # "CREATE DATABASE" requires automatic commits
    conn.autocommit = True
    sql_query = f"CREATE DATABASE Challenge_Data_Analytics_con_Python;"

    try:
        cur.execute(sql_query)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        print(f"Query: {cur.query}")
        cur.close()
    else:
        # Revert autocommit settings
        conn.autocommit = False
        cur.close()

def ejecutar_sql(sql_query) :
    conn = psycopg2.connect(
        host=host,
        port=port,
        database='challenge_data_analytics_con_python',
        user=user,
        password=password,
    )
    cur = conn.cursor()    
    try:
        # Execute the table creation query
        cur.execute(sql_query)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        print(f"Query: {cur.query}")
        conn.rollback()
        cur.close()
    else:
        # To take effect, changes need be committed to the database
        conn.commit()
        cur.close()




def read_sql(archivo_sql):
        try:
            with open(archivo_sql, "r") as f:
                sql = f.read()
                return sql
        except Exception as e:
            print(f"Error al leer el archivo SQL: {e}")
            exit()

""" 
def ejecutar_sql():

    try:
        #auto_commit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
        connection = psycopg2.connect(
            host=host,
            port=port,
            #database=database,
            user=user,
            password=password,
        )
        
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        exit()

    try:
        with open("archivo.sql", "r") as f:
            sql = f.read()
    except Exception as e:
        print(f"Error al leer el archivo SQL: {e}")
        exit()

    try:
        connection.autocommit = True      
        cursor = connection.cursor()
        #with connection, connection.cursor() as cursor:
        cursor.execute("create database Challenge_Data_Analytics_con_Python_2;")
        cursor.execute(sql)
        #connection.commit()
    except Exception as e:
        print(f"Error al ejecutar el archivo SQL: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
"""

if __name__ == '__main__':
    pass