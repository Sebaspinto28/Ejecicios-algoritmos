
numero = int(input("Coloque un número: "))
felices = []

num = str(numero)
suma_final = num

while True:
    suma = 0
    for digito in suma_final:
        suma += int(digito) ** 2
    suma_final = str(suma)
    
    if len(suma_final) == 1:
        break

if suma_final == "1":
    print(f"El número {numero} es feliz")
else:
    print(f"El número {numero} no es feliz")