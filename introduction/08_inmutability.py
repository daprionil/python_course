# Inmutabilidad
# Esta hace referencia a que algo no debe/puede ser cambiado
# Todo en python es un objeto, y python no permite reasignar/mutar
# el contenido interno de strings, tuplas, booleanos, enteros, flotantes y frozen-sets

nombre = "David"
# nombre[1] = "e" // Esto no se puede, estamos cambiando un valor interno del objeto 'str'
# La forma aceptable es la reasignación  de la variable

print(nombre)
