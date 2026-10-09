nota = float(input("Ingresa la nota del alumno\n\n "))

if nota < 0:
    print("INCORRECTO\n")
elif nota < 5:
    print("INSUFICIENTE\n")
elif nota < 6:
    print("SUFICIENTE\n")
elif nota < 7:
    print("BIEN\n")
elif nota < 9:
    print("NOTABLE\n")
elif nota <= 10:
    print("SOBRESALIENTE\n")
else:
    print("INCORRECTO\n")

print("ADIÓS\n")
