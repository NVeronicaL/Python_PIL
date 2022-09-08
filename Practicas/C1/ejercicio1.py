# Consigna: Idear la manera de realizar la siguiente salida (a,b y c son variables)
#   a    b      c
#  2.4  -3.21   47.8

try: 
    a = float(input("Ingrese un valor para a: "))
    b = float(input("Ingrese un valor para b: "))
    c = float(input("Ingrese un valor para c: "))

    print("a\t b\t c\t\n")
    print(a+"\t", b+"\t", c+"\t")

except ValueError as e:
    print("\n❌ Error: Deberia ser de tipo float\n")
    print(e)
except TypeError as e:
    print("\n❌ Error: tipos de operandos no admitidos para +: 'float' y 'str't\n")
    print(e)

