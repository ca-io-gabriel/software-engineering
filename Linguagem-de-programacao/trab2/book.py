"""
Passo 1: Definir a classe Livro
• Comece definindo a estrutura básica de um livro usando uma classe em Python. Cada livro
terá atributos como título, autor, gênero e quantidade disponível.
"""

class Book:
    """"Ola"""
    def __init__(self, title: str, author: str, genre: str, quantity: int):
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
