# Christian Garcia Jimenez Nc = 0068 
# fecha = miercoles/28/octubre/10/2026
print("Christian Garcia Jimenez Nc = 0068")

import numpy as np
import pandas as pd

## datos 
## Datos de matriz 4 x 3
datos_alumno = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]

# poner nombre a las columnas 3
# y almacenar la tabla en la variable df = DATAFRAME
print("--- datos de los estudiantes de una matriz 4 x 3 ----")
df = pd.DataFrame(datos_alumno, columns = ["ci", "marcas", "paquetes"])
print(df)

# datos a partir de un diccionario
print("--- datos de los estudiantes de un diccionario ----")
alumno_diccionario = {
 "nombre" : ["Christian", "Scarlet", "Karol", "Sammy", "Ambar", "Pedro", "Alejandra"],
 "califa" : [80, 100, 30, 100, 16, 90, 80],
 "edad"   : [16, 15, 16, 16, 16, 16, 15]
}
estudiantes = pd.DataFrame(alumno_diccionario) 
print(estudiantes)
print("Christian Garcia Jimenez Nc = 0068")