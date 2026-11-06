Espacio_total= float(input("Cuanto espacio tiene el disco: "))
Espacio_ocupado= float(input("Cuanto espacio ocupado: "))
if Espacio_total > Espacio_ocupado:
    print("GUARDAR")
elif Espacio_total == Espacio_ocupado:
    print("NO HAY SITIO")
else:
    print("ERROR")