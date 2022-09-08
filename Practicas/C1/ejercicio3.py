# Escriba un programa  que lea  1 palabra (ingresadas por el usuario), Calcule la longitud de cada una de ellas 
# y las despliegue junto  con su longitud indicada con asteristicos. Ejemplo:
# Árbol ***** 
# Celular *******
# Uno ***

print("Ingrese una palabra: ")
palabra = input()
nro_asteriscos = ' '
for i in range(len(palabra)):
    nro_asteriscos += '*'

print(nro_asteriscos)