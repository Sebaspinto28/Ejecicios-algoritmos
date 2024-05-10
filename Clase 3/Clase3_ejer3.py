n=int(input("Agregar numero:"))
aux=2
isprime=True
if n >= 2:
    isprime = True
    while aux < n:
        if n%aux==0:
            isprime=False
            break
        aux+=1
    if isprime:
        print(f"el numero {n}  es primo")
    else:
        print(f"el numero {n}  no es primo")
else:
    print(f"el numero {n}  es primo")
