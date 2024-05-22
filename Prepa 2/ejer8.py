num = 85
binario = ""



# Convertir el número a binario
while num > 0:
    binario = str(num % 2) + binario
    num=num // 2

 
if num > 0:
      binario = binario[2:]
  

print(f"el numeroes Binario: {binario}")