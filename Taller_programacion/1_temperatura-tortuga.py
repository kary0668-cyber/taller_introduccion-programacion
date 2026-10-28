temperatura = float(input("Ingrese la temperatura de la incubadora: "))

if temperatura < 26:
    print("T. baja")
elif temperatura <= 34:
    print("T. normal")
else:
    print("T. alta")