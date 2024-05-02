#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión.
n1=float(input("Agrege la cantidad a inevertir:\n"))
n2=float(input("Agrege el interes anual:\n"))
n3=float(input("Agrege el numero de a;os de la inversion:\n"))
#Capital final = Capital inicial * (1 + (Tasa de interés anual / 100))^Tiempo
Capital_final= n1*((1+(n2/100))**n3)
print(f"El capital final de su inversion de {n1} es de {Capital_final:.3f}")
