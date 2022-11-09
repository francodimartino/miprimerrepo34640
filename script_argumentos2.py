import sys
#scripts_argumentos2.py palabra cantidad
argumentos=sys.argv

if len(argumentos)!=3:
    print("Error: Debes ingresar dos argumentos")
    print("Ejemplo: python script_argumentos2.py palabra cantidad")
else:
    palabra=argumentos[1]
    cantidad=int(argumentos[2])

    for i in range(cantidad):
        print(palabra)

