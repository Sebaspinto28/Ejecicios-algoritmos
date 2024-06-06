class Comercial_anuncio:
    def __init__(self,name,dni,section,title,body):
        self.name=name
        self.dni=dni
        self.section=section 
        self.title=title
        self.body=body

class Classified_anuncio:
    def __init__(self,price,date,day,kind):
        self.price=price
        self.date=date
        self.day=day
        self.kind=kind


class Classified_vehiculo_anuncio(Classified_anuncio):
    def __init__(self,price,date,day,model,brand,year,color,km):
        super().__init__(self,price,date,day,"vehiculo")
        self.price=price
        self.date=date
        self.day=day
        self.model=model
        self.brend=brand
        self.year=year
        self.color=color
        self.km=km
        
class Classified_vivienda_anuncio(Classified_anuncio):
    def __init__(self,price,date,day,model,cuartos,banos,puestos,politica):
        super().__init__(self,price,date,day,"vivienda")
        self.price=price
        self.date=date
        self.day=day
        self.model=model
        self.cuartos=cuartos
        self.banos=banos
        self.puestos=puestos
        self.politica=politica