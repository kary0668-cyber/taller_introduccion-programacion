numero = int(input("Ingrese un numero positivo mayor a 0 o un negativo para terminar: "))
while numero > 0:
    texto = str(numero)
    cantidad = len(texto)
    suma = 0
    
    for digito in texto:
        digito = int(digito)
        suma = suma + digito ** cantidad
        
    if suma == numero:
        print("Es un numero narcisista")
    else:
        print("No es un numero narcisista")
        
    numero = int(input("Ingrese otro numero: "))