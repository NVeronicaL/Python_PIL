# Consigna: Idear un programa que solicite al usuario dos números enteros y el programa deberá retornar aquellos 
# números pares que se encuentren dentro del rango formado entre los números ingresados.
# Nota: Z= números enteros(negativos, positivos o naturales, cero).

print("+++++++++++++++++++++\tIngrese 2 números: +++++++++++++++++++++\n")
while True:
    try:
        n1 = int(input("Primer número: "))
        n2 = int(input("Segundo número: "))

        if n1 > n2:
            print("\n❌ El primer numero debe ser menor que el segundo\n")
            print("Ingresar nuevamente los números?: SI o NO\n")
            respuesta = input().upper()
            
            if respuesta == 'NO':
                break
            if respuesta != 'SI':
                print("\n❌ Solo admite como respuesta SI o NO\n")
                break
        else: 
            for i in range(n1,n2 +1 ):
                if i % 2 == 0:
                    print(i)
            break        
    except ValueError as e:
        print("\n❌ Error : Debe ingresar un numero entero\n")
