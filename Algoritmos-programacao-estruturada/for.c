# include <stdio.h>

int main() {
    int linhas, espacos, asteriscos;

    printf("Digite o número de linhas do triângulo: ");
    scanf("%d", &linhas);

    for (int i = 1; i <= linhas; i++) {

        for (espacos = 1; espacos <= linhas - i; espacos++) {
            printf(" ");
        }

        for (asteriscos = 1; asteriscos <= 2 * i - 1; asteriscos++) {
            printf("*");
        }

        printf("\n");
    }

    return 0;
}