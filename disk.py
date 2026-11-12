total_space= float(input("Cuanto espacio tiene el disco: "))
disk_space= float(input("Cuanto espacio ocupado: "))

def disk_space(total, disk):
    result = ""
    if total > disk_space:
       result = "GUARDAR"
    elif total == disk_space:
       result = "NO HAY SITIO"
    else:
       result = "ERROR"
    return result
print(disk_space(total_space, disk_space))
