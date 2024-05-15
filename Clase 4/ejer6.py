print("HOLA MUNDO")
n=int(input("escriba su numero\n-->"))
for i in range(1,n):

    multi=i*(i+1)
    if multi == n:
        print("Es oblongo")
        break
else:
    print("No")

   



