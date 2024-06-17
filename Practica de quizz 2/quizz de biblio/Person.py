class Person:
    def __init__(self,firts_name,last_name,id):
        self.firts_name=firts_name
        self.last_name=last_name
        self.id=id

    def show(self):
        return f'''
nombre : {self.firts_name}
apellido: {self.last_name}
id: {self.id}'''
    
class Student(Person):
    def __init__(self, firts_name, last_name, id,gpa):
        super().__init__(firts_name, last_name, id)
        self.gpa=gpa
    def show(self):
        return f'''{super().show()}
gpa: {self.gpa}'''
    
class Professor(Person):
    def __init__(self, firts_name, last_name, id,departament):
        super().__init__(firts_name, last_name, id)
        self.departament=departament
    def show(self):
        return f'''{super().show()}
gpa: {self.departament}'''

