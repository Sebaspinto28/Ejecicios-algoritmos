def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Introdusca un numero: "))
if is_prime(num):
    print(num, "es un numero primo.")
else:
    print(num, "no es un numero primo.")