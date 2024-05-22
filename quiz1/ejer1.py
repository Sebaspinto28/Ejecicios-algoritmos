lista_numeros = [-6, 1, 2, 4, 5, 6, 7, 18, 9, 10]
num1=int(input("ingrese un numero entero\n--->"))
num2=int(input("ingrese un numero entero\n--->"))

if num1 not in lista_numeros:
    print("los numeros ingresados no son validos")
elif num2 not in lista_numeros:
    print("los numeros ingresados no son validos")

elif num2<=num1:
    print("los numeros ingresados no son validos")
else:
    lista_numeros.sort()
for i in lista_numeros:
        if i<num1 or i> num2:
            print(i, end=" ")
    