import random

class Employee:
    def __init__(self,name,dni,section):
        self.name=name
        self.dni=dni
        self.section=section 

class Boss(Employee):
    def __init__(self, name, dni, section,writters):
        super().__init__(name, dni, section)
        self.writters=writters
    def supervise(self):
        print(f"Supervaising: ")
        for writer in self.writters:
            print(writer.name)
    def choice_public(self,article_list):
        print("El articulo publicado es ")
        article=random.choice(article_list)


class Writer(Employee):
    def __init__(self, name, dni, section):
        super().__init__(name, dni, section)      
    
    def write(self):
        print("writing...")
