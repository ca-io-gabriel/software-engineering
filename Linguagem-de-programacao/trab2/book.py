class Book:
    """ Esta classe sera utilizada para instanciar objetos de um tipo personalizado """
    def __init__(self, title: str, author: str, genre: str, quantity: int):
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
