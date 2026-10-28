def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    elif anio % 4 == 0 and anio % 100 != 0:
        return True
    else:
        return False
    
anio1 = int(input("Ingrese el primer año: "))
anio2 = int(input("Ingrese el segundo año: "))

resultado1 = es_bisiesto(anio1)
resultado2 = es_bisiesto(anio2)

print("Bisiesto:", resultado1, resultado2)

if resultado1 == resultado2:
    print("Misma condicion: verdadero")
else:
    print("Misma condicion: falso")