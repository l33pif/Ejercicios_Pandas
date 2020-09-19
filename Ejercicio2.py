# El fichero cotizacion.csv contiene las cotizaciones de las empresas del QAX con las siguientes columnas: 
# nombre (nombre de la empresa), 
# Final (precio de la acción al cierre de bolsa), 
# Máximo (precio máximo de la acción durante la jornada),
# Mínimo (precio mínimo de la acción durante la jornada), 
# volumen (Volumen al cierre de bolsa), 
# Efectivo (capitalización al cierre en miles de euros). 
# Construir una función que construya un DataFrame a partir del fichero con el formato anterior 
# y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.

import pandas as pd
import numpy as np


def main():

    data = {'Nombre':  ['Empresa Inc', 'Empresa Inc2'],
            'Final': [1000, 900],
            'Max':  [1500, 1000],
            'Min':  [500, 200],
            'Volumen':  [1000, 800],
            'Efectivo':  [10000, 70000],
        }

    df = pd.DataFrame(data, columns = ['Nombre', 'Final', 'Max', 'Min', 'Volumen', 'Efectivo'])

    df_2 = df.copy(deep=True)

    df_2['Media-Max'] = df_2['Max'].mean()
    df_2['Media-Min'] = df_2['Min'].mean()

    df_2.to_csv('df2.csv')


if __name__ == '__main__':
    main()
    