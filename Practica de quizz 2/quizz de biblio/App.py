from Book import Physical
from Book import Virtual
from Booking import Booking
from Person import Student
from Person import Professor
            
class App:
    def __init__(self,data):
        self.data = data
        self.bookings = []
        self.university_people = []
        self.books = []

    #LLAMA A TODOS LOS REGISTROS -----
    def register_data(self):
        self.register_books()
        self.register_university_people()
        self.register_bookings()

    #REGISTRAR LIBROS
    def register_books(self):        
        for book in self.data["books"]:
            id = book["id"]
            title = book["title"]
            author = book["author"]
            status = book["status"]

            if status == "virtual":
                license = book["license"]
                new_book = Virtual(title,author,id,license)
                self.books.append(new_book)
            else:
                location = book["location"]
                new_book = Physical(title,author,id,location)
                self.books.append(new_book)

    #REGISTRAR PERSONAS
    def register_university_people(self):
        for person in self.data["university_people"]:
            id = person["id"]
            first_name = person["first_name"]
            last_name = person["last_name"]
            position = person["position"]

            if position == "student":
                gpa = person["gpa"]
                new_person = Student(first_name,last_name,id,gpa)
                self.university_people.append(new_person)
            else:
                department = person["department"]
                new_person = Professor(first_name,last_name,id,department)
                self.university_people.append(new_person)

    #REGISTRAR RESERVACIONES
    def register_bookings(self):
        for booking in self.data["bookings"]:
            book_id = booking["book_id"]

            #CAMBIAR DISPONIBILIDAD DE LIBROS RESERVADOS
            for book in self.books:
                if book.id == book_id:
                    book.available = False

            people_id = booking["people_id"]
            until = booking["until"]
            new_booking = Booking(book_id, people_id, until)
            self.bookings.append(new_booking)
    # -----------

    #LIBROS DISPONIBLES
    def available_books(self):
        for book in self.books:
            if isinstance(book,Physical):
                if book.available == True:
                   print(book.show())
            else:
                print(book.show())

    #MOSTRAR PERSONAS
    def show_university_people(self):
        estudiantes = []
        profesores = []
        for person in self.university_people:
            if isinstance(person,Student):
                estudiantes.append(person)
            else:
                profesores.append(person)
        print('ESTUDIANTES')
        for e in estudiantes:
            print(e.show())
            print('==================')
        print('PROFESORES')
        for p in profesores:
            print(p.show())
            print('==================')

    #MOSTRAR RESERVACIONES
    def show_bookings(self):
        print(len(self.bookings))
        for b in self.bookings:
            for book in self.books:
                if b.book_id == book.id:
                    print(book.show())


    #REALIZAR RESERVA
    def reserve_book(self):
        dni = input('Ingrese su número de carnet: ')
        while not dni.isnumeric() or len(dni) != 11:
            print('Carnet inválido')
            dni = input('Ingrese su número de carnet: ')
        
        registered =  False
        for person in self.university_people:
            if person.id == dni:
                registered = True
                break

        if not registered:
            print('La persona consultada no está autorizada a reservar un libro')
        else:
            while True:
                self.available_books()
                seleccion = input('Ingrese el ID del libro deseado: ')
                for book in self.books:
                    if book.id == seleccion:
                        if isinstance(book,Physical) and book.available == True or isinstance(book,Virtual):
                            date = input('¿Hasta qué día lo desea? [dd/mm/aaaa]: ')
                            booking = Booking(seleccion, dni, date)
                            self.bookings.append(booking)
                            book.available = False
                            print(f'RESERVA EXITOSA\n{booking.show()}')
                            break
                        else:
                            print('El libro seleccionado no está disponible')
                            break



    def menu(self):
        self.register_data()
        print('-- BIBLIOTECA PEDRO GRASES --\n Bienvenido/a')
        while True:
            print('''
1. Ver libros disponibles
2. Ver personas de la universidad
3. Ver libros reservados
4. Realizar reservación
=========================
5. Salir
''')
            
            seleccion = input("Ingrese el número correspondiente a su selección: ")
            while not seleccion.isnumeric() or int(seleccion) not in range(1,6):
                print('Error')
                seleccion = input("Ingrese el número correspondiente a su selección: ")

            if seleccion == '1':
                print('\nLIBROS DISPONIBLES')
                self.available_books()
            elif seleccion == '2':
                print('\nPERSONAS DE LA UNIVERSIDAD')
                self.show_university_people()
            elif seleccion == '3':
                print('\nLIBROS RESERVADOS')
                self.show_bookings()
            elif seleccion == '4':
                self.reserve_book()
            else:
                print('Gracias por su visita. Vuelva pronto...')
                break

            ans = input('¿Desea continuar? [y/n]: ')
            while ans not in ['y','n']:
                print('Inválido')
                ans = input('¿Desea continuar? [y/n]: ')
            
            if ans == 'n':
                print('Gracias por su visita. Vuelva pronto...')
                break

