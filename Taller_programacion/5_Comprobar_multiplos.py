def es_multiplo(numero, divisor):
    if divisor == 0:
        return  False
    else:
        return numero % divisor == 0
    
numero = int(input("Ingrese el primer numero: "))
divisor = int(input("Ingrese el segundo numero: "))

resultado1 = es_multiplo(numero, divisor)
resultado2 = es_multiplo(divisor, numero)

print(numero, "multiplo de", divisor, ":", resultado1)
print(divisor, "multiplo de", numero, ":", resultado2)