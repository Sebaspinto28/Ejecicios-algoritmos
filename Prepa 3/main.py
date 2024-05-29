#POO (programacion orientada a objetos)

from Alumno import Alumno
alumnos=[]
while True:
    nombre=input("ingrse el nombre del alumno ")
    edad=int(input("ingrse la edad del alumno "))
    alumno = Alumno(nombre,edad) #objeto
    alumnos.append(alumno)

    seguir=input("desea seguir (si/no)")
    if seguir=="si":
        continue
    else:
        break
for alumno in alumnos:
    print(alumno.toString())