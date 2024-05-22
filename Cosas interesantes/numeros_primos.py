def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = int(input("Introdusca un numero: "))
if is_prime(num):
    print(num, "es un numero primo.")
elif num==1:
    print(num,"es un numero primo")
else:
    print(num, "no es un numero primo.")