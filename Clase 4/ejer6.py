print("HOLA MUNDO")
n=int(input("escriba su numero\n-->"))
for i in range(1,n):

    multi=i*(i+1)
    if multi == n:
        print("Es oblongo")
        break
else:
    print("No")

   
#n = int(input("Escriba su número: "))
#
#for i in range(1, n):
#    multi = i * (i + 1)
#    if n % multi == 0:  # Verificamos si n es divisible por multi
#        print("Es oblongo")
#        break
#else:
#    print("No es oblongo")


