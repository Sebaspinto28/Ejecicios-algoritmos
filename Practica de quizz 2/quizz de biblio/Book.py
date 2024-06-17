class Book:
    def __init__(self,title,author,id):
        self.title=title
        self.author=author
        self.id=id
    
    def show(self):
        return f'''
Titulo : {self.title}
author: {self.author}
id: {self.id}'''



class Physical(Book):
    def __init__(self, title, author, id,location):
        super().__init__(title, author, id)
        self.location=location 
        self.available=True
        

    def show(self):
        return f'''{super().show()}
        licensia: {self.location}'''


class Virtual(Book):
    def __init__(self, title, author, id,license):
        super().__init__(title, author, id)
        self.license=license
    def show(self):
        return f'''{super().show()}
            licensia: {self.license}'''
        