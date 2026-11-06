Edad_usuario = int(input("Ingresa la edad del usuario: "))
Estudiante = input("¿Es estudiante?: ")
Día = input("¿Qué día es?: ")
Precio_base = 8
if Edad_usuario < 12:
    Precio_menores = Precio_base/2
    print("Pagan la mitad", Precio_menores)
elif Día == "miércoles":
    print("Precio: 4")
elif Estudiante == "si":
    Precio_estudiante = Precio_base*0.3
    print("Descuento", Precio_base - Precio_estudiante)
elif Edad_usuario > 65:
    print("Precio reducido: 5")





