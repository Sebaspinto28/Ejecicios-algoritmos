class Booking:
    def __init__(self,book_id,people_id,until):
        self.book_id=book_id
        self.people_id=people_id
        self.until=until
    
    def show(self):
        return f'''
book id : {self.book_id}
people id: {self.people_id}
until: {self.until}'''
    