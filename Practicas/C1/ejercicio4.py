# Crear un dicicionario del ejercicio anterior

dic_palabras = {
    'palabra': ' ',
    'valor': ' '
}

print("Ingrese una palabra: ")
palabra = input()
dic_palabras['palabra'] = palabra
for i in range(len(palabra)):
    dic_palabras['valor'] += '*'

print(dic_palabras)