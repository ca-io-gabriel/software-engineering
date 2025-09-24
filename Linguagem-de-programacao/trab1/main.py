"""
    Este programa e um sistema simples para a gestao das notas de um aluno
    Ele permite Cadastrar as notas, calcular a media, determinar a situacao
    e exibir um relatorio final sobre o aluno
"""

# Criado uma lista para guardas as notas
student_grades = []


def register_notes():
    """ Esta funcao permite que o usuario insira as notas do aluno e guarda elas na lista """
    student_grades.append(int(input("Digite a primeira nota do aluno: ")))
    student_grades.append(int(input("Digite a segunda nota do aluno: ")))
    student_grades.append(int(input("Digite a terceira nota do aluno: ")))
    student_grades.append(int(input("Digite a quarta nota do aluno: ")))

    # Nao e permitido notas negativas
    for grade in student_grades:
        if grade < 0:
            print("Digite notas validas.\n")
            student_grades.clear()
            return

    print("Notas inseridas com sucesso!\n")


def calculate_average():
    """ Esta funcao calcula a media das notas e verifica a situacao do aluno """
    # Criando variaveis globais para serem acessadas em outra funcao
    global student_average, situation

    #Verificando se as notas já foram inseridas
    if len(student_grades) == 0:
        print("Nenhuma nota foi digitada.\n")
        return

    # Calculando a media do aluno
    student_average = sum(student_grades) / len(student_grades)

    # Verifica a situacao do aluno
    if student_average >= 7:
        situation = "Aprovado"
    else:
        situation = "Reprovado"

    print(f"A media do aluno é: {student_average:.2f} ({situation})\n")


def final_report():
    """" Esta funcao exibe a situacao final do aluno """
    # Verificando se a notas ja foram inseridas
    if len(student_grades) == 0:
        print("A média ainda nao foi calculada.\n")
        return

    print("\n----- Relatorio final -----")
    print("Notas do aluno:", ", ".join(str(grade) for grade in student_grades))
    print(f"Media do aluno: {student_average:.2f}")
    print(f"Situação: {situation}")
    print("----------------------------\n")


def menu():
    """ Esta funcao exibe um menu interativo para o usuario utilizar as funcoes """
    # Mantem o usuario no menu, ate que ele digite 0
    while True:
        # Opcoes do menu
        print("1 - Inserir notas do aluno")
        print("2 - Calcular media do aluno")
        print("3 - Exibir situacao final do aluno")
        print("0 - Sair\n")

        opt = int(input("Escolha uma opcao: "))

        # Usando um match-case para enviar o usuario para a funcao escolhida
        match opt:
            case 1:
                register_notes()
            case 2:
                calculate_average()
            case 3:
                final_report()
            case 0: # Opcao de saida
                print("Programa finalizado com sucesso.")
                break
            case _:
                print("Digite um número valido.\n")


if __name__ == '__main__':
    menu()
