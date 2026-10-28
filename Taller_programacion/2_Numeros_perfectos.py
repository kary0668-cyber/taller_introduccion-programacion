numero = int(input("Ingrese un numero positivo mayor que 2 o un negativo para terminar: "))
while numero >= 0:
    
    suma = 0
    
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma = suma + divisor
            
    if suma == numero:
        print("Es un numero perfecto")
    else:
        print("No es un numero perfecto")
        
    numero = int(input("Ingrese otro numero: "))
    