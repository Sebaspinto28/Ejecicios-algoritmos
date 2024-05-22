'''Se propone que se implemente un algoritmo que, dado un número introducido por el usuario*, 
diga si ese número es par y triangular.

Definiciones:
Número triangular: es aquel que se obtiene al sumar n números naturales consecutivos,
 comenzando desde el 1. (Por ejemplo: 3 (1+2), 6 (1+2+3), 10 (1+2+3+4))

*debe validarse que el input sea un número natural.
'''

numero = int(input("Ingrese un número natural: "))

if numero%2==0:
       print(f"el numero {numero} es par")
else:
        print(f"el numero {numero} no es par ")



if numero < 1:
  print("Error: Debe ingresar un número natural positivo.")
else:
  es_triangular = False
  n = 1
  triangular = 0
  
  while triangular < numero:
    triangular = n * (n + 1) / 2
    n += 1
  es_triangular = triangular 
  if triangular== numero:
    print(f"el numero {numero} es triangular")
  else:
        print(f"el numero {numero} no es triangular")





 

  
