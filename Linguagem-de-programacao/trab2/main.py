"""
Passo 1: Definir a classe Livro
• Comece definindo a estrutura básica de um livro usando uma classe em Python. Cada livro
terá atributos como título, autor, gênero e quantidade disponível.

Passo 2: Criar a lista de livros
• Inicialize uma lista vazia para armazenar os livros que serão cadastrados.

Passo 3: Implementar funções para gerenciar os livros
• Função para cadastrar um novo livro
• Função para listar todos os livros
• Função para buscar um livro pelo título

Passo 4: Utilizar a biblioteca Matplotlib para gerar um gráfico
• Instalação da Matplotlib
• Gerar o gráfico de quantidade de livros por gênero
"""
from matplotlib import pyplot as plt
from book import Book

books = []

def register_book():
    """"Ola"""
    title = input("Digite o titulo do livro: ")
    author = input("Digite o autor do livro: ")
    genre = input("Digite o genero do livro: ")
    quantity = int(input("Digite a quantidade de livros: "))

    book = Book(title, author, genre, quantity)
    books.append(book)

    print("Livro cadastrado com sucesso!\n")


def show_books():
    """"Ola"""
    if len(books) == 0:
        print("Nao ha nehum livro cadastrado.\n")
        return

    print("------------ Livros ------------")

    for book in books:
        print(f"| {book.title}, {book.author} | {book.genre} | {book.quantity} |")

    print("--------------------------------\n")


def find_book_by_title():
    """"Ola"""
    if len(books) == 0:
        print("Nao ha nehum livro cadastrado.\n")
        return

    title = input("Digite o titulo do livro para buscar: ")

    for book in books:
        if book.title == title:
            print(f"{book.title}, {book.author} ({book.genre}) quatidade: {book.quantity}.\n")

    print("Livro nao encontrado.")


def show_graph():
    """"Ola"""
    for book in books:
        plt.bar(book.genre, book.quantity, label=book.genre)

    plt.xlabel("Genero")
    plt.ylabel('Quantidade de livros')
    plt.title('Quantidade de livros por genero')
    plt.legend()

    plt.show()

def menu():
    """Ola"""
    while True:
        print("1 - Cadastrar novo livro")
        print("2 - Mostrar todos os livros")
        print("3 - Buscar livro por titulo")
        print("4 - Mostrar grafico da quantidade de livros por genero")
        print("0 - Sair\n")

        opt = int(input("Escolha uma das opcoes acima: "))

        match opt:
            case 1:
                register_book()
            case 2:
                show_books()
            case 3:
                find_book_by_title()
            case 4:
                show_graph()
            case 0:
                print("Programa finalizado com sucesso.")
                break
            case _:
                print("Digite um número valido.\n")


if __name__ == '__main__':
    menu()
