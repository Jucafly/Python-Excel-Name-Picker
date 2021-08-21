#Libreria de OpenPython
import openpyxl
#Leyendo Archivo
book = openpyxl.load_workbook('Libro1.xlsx',data_only=True)
#Seleccionamos la Hoja 
hoja = book.active
celdas = hoja['A2':'C4']

lista_alumnos = []

for fila in celdas:
    alumno = [celda.value for celda in fila]
    lista_alumnos.append(alumno)


print(f'El alumno con nombre {alumno[0]} va en la seccion {alumno[1]} en el salon {alumno[2]}')