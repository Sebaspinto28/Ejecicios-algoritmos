from App import App

data = {
'bookings': [
{'book_id': '2', 'people_id': '24894000234', 'until': '10/5/2024'},
{'book_id': '10', 'people_id': '20211110010', 'until': '24/3/2024'},
{'book_id': '5', 'people_id': '20211110002', 'until': '18/2/2024'},
{'book_id': '1', 'people_id': '24894000241', 'until': '14/3/2024'},
{'book_id': '1', 'people_id': '20211110001', 'until': '23/7/2024'},
],
'university_people': [
{'id': '20211110001', 'first_name': 'Laura', 'last_name': 'Gómez', 'position':
'student', 'gpa': 3.8},
{'id': '24894000232', 'first_name': 'Carlos', 'last_name': 'Martínez',
'position': 'professor', 'department': 'Computer Science'},
{'id': '20211110002', 'first_name': 'Ana', 'last_name': 'Rodríguez',
'position': 'student', 'gpa': 3.5},
{'id': '24894000233', 'first_name': 'Elena', 'last_name': 'López', 'position':
'professor', 'department': 'Physics'},
{'id': '20211110003', 'first_name': 'Juan', 'last_name': 'Hernández',
'position': 'student', 'gpa': 4.0},

{'id': '24894000234', 'first_name': 'Miguel', 'last_name': 'Sánchez',
'position': 'professor', 'department': 'Biology'},
{'id': '20211110004', 'first_name': 'Sofía', 'last_name': 'Fernández',
'position': 'student', 'gpa': 3.2},
{'id': '24894000235', 'first_name': 'María', 'last_name': 'Pérez', 'position':
'professor', 'department': 'Chemistry'},
{'id': '20211110005', 'first_name': 'David', 'last_name': 'Gutiérrez',
'position': 'student', 'gpa': 3.9},
{'id': '24894000236', 'first_name': 'Isabel', 'last_name': 'García',
'position': 'professor', 'department': 'Mathematics'},
{'id': '20211110006', 'first_name': 'Javier', 'last_name': 'Torres', 'position':
'student', 'gpa': 3.7},
{'id': '24894000237', 'first_name': 'Alejandro', 'last_name': 'Díaz',
'position': 'professor', 'department': 'History'},
{'id': '20211110007', 'first_name': 'Paula', 'last_name': 'Martín', 'position':
'student', 'gpa': 3.4},
{'id': '24894000238', 'first_name': 'Eva', 'last_name': 'Núñez', 'position':
'professor', 'department': 'Psychology'},
{'id': '20211110008', 'first_name': 'Roberto', 'last_name': 'Ortega',
'position': 'student', 'gpa': 3.6},
{'id': '24894000239', 'first_name': 'Lucía', 'last_name': 'Ruiz', 'position':
'professor', 'department': 'Economics'},
{'id': '20211110009', 'first_name': 'Adrián', 'last_name': 'López', 'position':
'student', 'gpa': 3.8},
{'id': '24894000240', 'first_name': 'Carmen', 'last_name': 'Herrera',
'position': 'professor', 'department': 'Sociology'},
{'id': '20211110010', 'first_name': 'Marina', 'last_name': 'Gómez', 'position':
'student', 'gpa': 3.9},
{'id': '24894000241', 'first_name': 'Luis', 'last_name': 'Vega', 'position':
'professor', 'department': 'Political Science'},
],
'books': [
{'id': '0', 'title': 'El despertar', 'author': 'Elena A. Martínez', 'status':
'physical', 'location': 'Piso 2, estante 4'},
{'id': '1', 'title': 'Sombras en la ciudad', 'author': 'Carlos M. Ruiz', 'status':
'virtual', 'license': '01/01/2040'},
{'id': '2', 'title': 'Mundos perdidos', 'author': 'Sophia L. Rivera', 'status':
'virtual', 'license': '27/08/2035'},
{'id': '3', 'title': 'El enigma del tiempo', 'author': 'Alejandro V. Santos',
'status': 'physical', 'location': 'Piso 1, estante 1'},
{'id': '4', 'title': 'Sendero de estrellas', 'author': 'Isabel G. López', 'status':
'virtual', 'license': '14/12/2028'},
{'id': '5', 'title': 'Reinos olvidados', 'author': 'Javier R. Navarro', 'status':
'physical', 'location': 'Piso 2, estante 2'},

{'id': '6', 'title': 'La esencia perdida', 'author': 'Ana M. García', 'status':
'physical', 'location': 'Piso 2, estante 2'},
{'id': '7', 'title': 'Aventuras en la nebulosa', 'author': 'Luis F. Sánchez',
'status': 'virtual', 'license': '03/03/2033'},
{'id': '8', 'title': 'Secretos del abismo', 'author': 'María J. Pérez', 'status':
'physical', 'location': 'Piso 1, estante 3'},
{'id': '9', 'title': 'El susurro del viento', 'author': 'Roberto E. Rodríguez',
'status': 'virtual', 'license': '12/12/2027'},
{'id': '10', 'title': 'Luz en la oscuridad', 'author': 'Laura P. Martín', 'status':
'physical', 'location': 'Piso 3, estante 4'},
{'id': '11', 'title': 'La última frontera', 'author': 'Diego A. Gómez', 'status':
'physical', 'location': 'Piso 1, estante 2'},
{'id': '12', 'title': 'Caminos entrelazados', 'author': 'Silvia C. Díaz', 'status':
'physical', 'location': 'Piso 1, estante 4'},
{'id': '13', 'title': 'El misterio de la Luna', 'author': 'Andrés L. Torres',
'status': 'virtual', 'license': '18/07/2045'},
{'id': '14', 'title': 'Travesía intergaláctica', 'author': 'Lucía M. Fernández',
'status': 'physical', 'location': 'Piso 2, estante 1'}
],
}
def main():
    app=App(data)
    app.menu()

main()
