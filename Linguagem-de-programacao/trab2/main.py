"""
    Este programa e um sistema simples para o gerenciamento de livros
    Ele permite cadastrar novos livros, listar todos os livros disponiveis, buscar
    um livro pelo título, e gerar um gráfico com a quantidade de livros por genero.
"""
#Importando a lib e a classe que serao utilizadas
from matplotlib import pyplot as plt
from book import Book

#Lista para guardar os livros
books = []

def register_book():
    """ Esta funcao permite que o usuario cadastre novos livros e guarda eles na lista"""
    title = input("Digite o titulo do livro: ")
    author = input("Digite o autor do livro: ")
    genre = input("Digite o genero do livro: ")
    quantity = int(input("Digite a quantidade de livros: "))

    #Instanciando um livro com base nas informacoes inseridas
    book = Book(title, author, genre, quantity)
    books.append(book)

    print("Livro cadastrado com sucesso!\n")


def show_books():
    """ Esta funcao imprime todos os livros da lista """
    #Verifica se ha livros na lista
    if len(books) == 0:
        print("Nao ha nehum livro cadastrado.\n")
        return

    print("------------ Livros ------------")

    for book in books:
        print(f"| {book.title}, {book.author} | {book.genre} | {book.quantity} |")

    print("--------------------------------\n")


def find_book_by_title():
    """ Esta funcao busca um livro pelo seu titulo """
    #Verificando se ha livros na lista
    if len(books) == 0:
        print("Nao ha nehum livro cadastrado.\n")
        return

    title = input("Digite o titulo do livro para buscar: ")

    #Iterando sobre a lista para buscar o livro
    for book in books:
        if book.title == title:
            print(f"{book.title}, {book.author} ({book.genre}); quantidade: {book.quantity}.\n")

    print("Livro nao encontrado.")


def show_graph():
    """ Esta funcao exibe o grafico da quantidade de livros por genero"""
    # Verificando se ha livros na lista
    if len(books) == 0:
        print("Nao ha nehum livro cadastrado.\n")
        return

    #Iterando sobre a lista para criar o grafico
    for book in books:
        plt.bar(book.genre, book.quantity, label=book.genre)

    #Configurando o grafico
    plt.xlabel("Genero")
    plt.ylabel('Quantidade de livros')
    plt.title('Quantidade de livros por genero')
    plt.legend()

    plt.show()

def menu():
    """ Esta funcao exibe um menu interativo para o usuario utilizar as funcoes """
    # Mantem o usuario no menu, ate que ele digite 0
    while True:
        # Opcoes do menu
        print("1 - Cadastrar novo livro")
        print("2 - Mostrar todos os livros")
        print("3 - Buscar livro por titulo")
        print("4 - Mostrar grafico da quantidade de livros por genero")
        print("0 - Sair\n")

        opt = int(input("Escolha uma das opcoes acima: "))

        # Usando um match-case para enviar o usuario para a funcao escolhida
        match opt:
            case 1:
                register_book()
            case 2:
                show_books()
            case 3:
                find_book_by_title()
            case 4:
                show_graph()
            case 0: # Opcao de saida
                print("Programa finalizado com sucesso.")
                break
            case _:
                print("Digite um número valido.\n")


if __name__ == '__main__':
    menu()
