from estudiante import Estudiante
from materias import Materias
from materias import Pregrado 
from materias import Postgrado 
def regis_estudientes(estudiantes):
    levels={
        "1":"Pregrado",
        "2":"Postgrado"
    }
    name=input("Coloque el nombre")
    dni=input("Coloque el dni")
    level_opt=input("Coloque el nivel - 1 - Pregrado - 2 - Postgrado")
    estudiantes.append(
        Estudiante(name,dni,levels.get(level_opt,levels["1"]))
    )
def regis_materias(materias):
    option=input("Coloque el nivel - 1 - Pregrado - 2 - Postgrado")
    name=input("coloque el nombre")
    credits=input("coloque los creditos")
    
    if option =="1":
        materias.append(Pregrado(name,credits,input("ingrese el departamento")))
    elif option =="2":
        materias.append(Postgrado(name,credits,input("ingrese el diploma")))


def regis_incrip(inscripciones,estudiantes,materias):
    dni=input("mete la cedula")
    estudiante_selec=None
    materia_estudiante_lista=[]
    for estudiante in estudiantes:
        if estudiante.dni==estudiante:
            estudiante_selec=estudiante
            break
    if estudiante_selec:
        for i,materia in enumerate(materias):
            print(i,materia.name,materia.name,materia.credits,sep=" - ")
        while True:
            materia_i=int(input("Please enter the number of subject you want or -1 if you want to exit:"))
            if materia_i!=1:
                materia_estudiante_lista.append(materias[materia_i])
            else:
                break
    
            
def main():
    estudiantes=[]
    materias=[]
    incripciones=[]
