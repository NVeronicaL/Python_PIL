menu = ['Deposito', 'Extracción', 'Transferencia', 'Salir']
while (menu != []):
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t\t MENU DE OPCIONES")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    for o in menu:
        print("|--->", o)
    op_elegida = input("\nIngresa una opcion: ")
    if op_elegida in menu: 
        if (op_elegida!= 'Salir'):
            print("\n********************* " + op_elegida.upper() + " *********************")
            monto = input("Ingresa un monto: ")
            if monto.isnumeric():
                print("Felicidades la operación de", op_elegida, "se realizo con Exito!😀")
                print("\nDesea realaizar otra operación? SI o NO")
                respuesta = input().upper()
                if respuesta != 'SI':
                    break                    
            else: 
                print("Error 🙁, porfavor ingrese  un número")
        elif op_elegida == 'Salir':
            break
    else: 
        print("Error 🙁, no coincide con ninguna opcion del MENU DE OPCIONES\n")