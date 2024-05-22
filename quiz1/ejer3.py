#Se ha solicitado un programa que facilite la gestión de calificaciones de los
#alumnos de una sección de Algoritmos y Programación 🖥 al final de trimestre.
#Se otorgarán 2 listas, alumnos que almacena los nombres de todos los
#estudiantes, y notas_alumnos que almacena las notas del “Quiz 1”, “Parcial 1”, “Quiz
#2”, “Parcial 2”, y “Evaluación Continua” respectivamente. Su tarea es mostrar al
#usuario las calificaciones de manera amigable, permitiéndole ingresar el nombre de
#un estudiante para visualizar su información.
#Bono (1.5pts): Deberá guardar la información de ambas listas en una
#estructura de datos que facilite su almacenamiento (diccionario)
#Ejemplo:
#calificaciones = {
#“Sofia Garcia”: {“Quiz 1”: 15, “Parcial 1”: “No presentó”, “Quiz 2”: 12,
#“Parcial 2”: 19, “Evaluacion Continua”: 14},
#.
#.
#}

alumnos = ["Sofia Garcia", "Mateo Martinez", "Valentina Lopez", "Alejandro Rodriguez", "Lucia Perez", "Santiago Gonzalez", "Emma Hernandez", "Nicolas Diaz", "Julio Moreno", "Daniel Fernandez"]
dic={}
notas_alumnos = [
[15, "No presentó", 12, 19, 14],
[10, 17, 8, 16, 20],
[13, 11, 19, 7, 16],
[18, 9, 14, 12, 17],
[16, 20, 15, "No presentó", 13],
[9, 14, 18, 7, 10],
[12, 16, 19, 8, 11],
[17, 13, 10, 15, 18],
[11, 20, 14, 16, 9],
[19, 8, 15, "No presentó", 17]]






for nino in range(len(alumnos)):
    dic[alumnos[nino]]={
        "Quizz 1":notas_alumnos[nino][0],
        "Parcial 1":notas_alumnos[nino][1],
        "Quizz 2":notas_alumnos[nino][2],
        "Parcial 2":notas_alumnos[nino][3],
        "Evaluacion continua":notas_alumnos[nino][4]
    }

#del “Quiz 1”, “Parcial 1”, “Quiz
#2”, “Parcial 2”, y “Evaluación Continua”
busca=str(input("Que alumno quieres buscar\n-->")).title()
for x in dic:     
        if busca==x:
            print(f"estudiante: {busca}\nQuizz 1:{dic[busca]["Quizz 1"]}\nParcial 1: {dic[busca]["Parcial 1"]}\nQuizz 2:{dic[busca]["Quizz 2"]}\nParcial 2:{dic[busca]["Parcial 2"]}\nEvaluacion continua: {dic[busca]["Evaluacion continua"]} ")





