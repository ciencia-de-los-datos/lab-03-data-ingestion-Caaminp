"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

import pandas as pd

def ingest_data():

    with open('clusters_report.txt', 'r') as file:
        data = []
        for line in file:
            columns= line.split()  
            if len(columns) >=1: 
                    try:
                        cluster = int(columns[0]) 
                        cantidad_de_palabras_clave = int(columns[1]) 
                        porcentaje_de_palabras_clave = columns[2] 
                        principales_palabras_clave= ' '.join(columns[4:]) 
                        data.append([cluster, cantidad_de_palabras_clave, porcentaje_de_palabras_clave, principales_palabras_clave])
                    except:
                        if len(data) > 0:
                            principales_palabras_clave= ' '.join(columns)
                            data[len(data)-1][3] += ' ' + principales_palabras_clave 

    df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',','.').astype(float)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('.','')
    df.columns= df.columns.str.replace(' ', '_').str.lower()
    return df
print(ingest_data())       