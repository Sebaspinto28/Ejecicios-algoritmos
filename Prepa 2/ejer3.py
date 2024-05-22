numeros = [
    1634, 225, 490, 9926315, 800, 93084, 313, 216, 864, 757, 243, 301, 833,
    200, 54748, 32, 787, 536, 343, 353, 24678050, 16, 370, 181, 131, 818,
    24678051, 153, 196, 400, 784, 31, 371, 9474, 10301, 729, 648, 973, 256,
    548834, 9800817, 9, 289, 302, 81, 101, 36, 716, 968, 100, 49, 432, 169,
    484, 128, 125, 961, 1000, 608, 219, 739, 529, 797, 931, 27, 108, 379, 727,
    324, 121, 841, 288, 373, 919, 92727, 8208, 64, 632, 625, 4210818, 144,
    1741725, 72, 151, 929, 675, 790, 655, 11, 407, 512, 25, 262, 900, 383, 441,
    392, 576, 7, 361, 972, 88593477, 500, 676, 191, 1597, 7951
]
feliz=[]
narcicista=[]
palindromo=[]
omirp=[]

for numero in numeros:
    num=str(numero)

        #feliz
    suma_final=num
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
        if numero % i==0:
            divisores+=1

    if divisores==1 and (num !=num[::-1]):
        num2= int(num[::-1])
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