
feliz=[]
narcicista=[]
palindromo=[]
omirp=[]

for numero in numeros:
    num=str(numero)

    #feliz
suma_final=numero
while True:
    suma=0
    for digito in suma_final:
        suma+= int(digito)**2 
        suma_final=str(suma)  
    if len(str(suma))==1:
        break

    if suma_final=="1":
        feliz.append(numero)



 #narcicisita
potencia=len(num)
suma=0
for digito in num:
    suma+= int(digito)**potencia
if suma==numero:
    narcicista.append(numero)

    #palindromo

if num==num[::-1]:
    palindromo.append(numero)
    #omirp
divisores=0
for i in range(1,numero):
    if numero%i==0:
        divisores+=1

if divisores==1 and (num !=num[::-1]):
    num2= num[::-1]
    divisores=0
    for i in range(1,num2):
        if num2 % i ==0:
            divisores+=1
if divisores==1:
    omirp.append(numero)


print(f"numeros felices ---->{feliz}\n")
print(f"numeros felices ---->{narcicista}\n")
print(f"numeros felices ---->{palindromo}\n")
print(f"numeros felices ---->{omirp}\n")