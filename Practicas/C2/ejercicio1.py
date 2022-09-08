# Consigna: Realizar un menú de un cajero automático, donde el usuario pueda escoger entre alguna de las siguientes opciones.
# Deposito - Extracción, Transferencia, Salir.
# En todos los casos se le pedirá al usuario un monto de dinero y el programa deberá mostrar en todo momento la sección del menú
# en la que se encuentre, pudiendo restornar al menú principal simpre que se quiera y solo se detendrá la ejecución cuando se ingrese la opción de "Salir" en el menú principal.

menu = ['Deposito', 'Extracción', 'Transferencia', 'Salir']
while (menu != []):
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\t\t MENU DE OPCIONES")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")

    for o in menu:
        print("|--->", o)
    op_elegida = input("\nIngresa una opcion: ")
    if op_elegida in menu and op_elegida!= 'Salir': 
        print("\n********************* " + op_elegida.upper() + " *********************")
        monto = input("Ingresa un monto 💲: ")
        if monto.isnumeric():
            print("\n✅ Felicidades la operación de", op_elegida, "se realizo con Exito!😀")
            print("\nDesea realaizar otra operación? SI o NO")
            respuesta = input().upper()
            if respuesta != 'SI':
                break                    
        else: 
            print("\n❌ Error 🙁, porfavor ingrese  un monto vaálido")
    else: 
        if op_elegida == 'Salir':
            break
        print("\n❌ Error 🙁, no coincide con ninguna opcion del MENU DE OPCIONES\n")