x = [158, 400, 789, 9926315, 1634, 54748, 200, 4843, 481846, 48472, 999, 93084, 24678050,
370, 818, 975, 89, 78914, 5161, 1231, 1515, 3574, 15731, 4748743, 848, 1513, 4545, 657, 490, 987, 50,
47825, 456, 456, 783, 1741725, 88593477, 48, 111, 121, 203, 777, 401, 412, 214, 369887, 456,
6664561, 12, 464, 402, 403, 407, 834, 200, 300, 400, 500, 664, 648, 698, 987, 7, 998, 2467, 149,
377, 9474, 548834, 153, 7, 9, 92727, 8208, 4210818, 407, 487
]
codigo=[]

counts = {
"felices": 0,
"narcisistas": 0,
"Otros": 0 # Para cuando no sea ninguno de los anteriores
}

for numero in x:
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
        codigo.append("\n")
        counts["felices"] += 1
        



    #narcicisita
    potencia=len(num)
    suma=0
    for digito in num:
        suma+= int(digito)**potencia
    if suma==numero:
        codigo.append("X")
        counts["narcisistas"] += 1
    else:
        codigo.append(" ")
        counts["Otros"] += 1
print(codigo)
print(counts)
       
   
