#include <stdio.h>

int main() {
    //Decalrando as variaveis para o numero a ser digitado e para a soma 
    int num, sum = 0;

    //Looping infinito para a soma
    do {
        printf("Digite um valor para a soma: ");
        scanf("%d", &num);

        //Caso o valor a ser somado seja menor que zero, o valor não será somado
        if (num < 0) {
            printf("O valor a ser somado deve ser maior que zero!\n\n");
            continue;
        }

        printf("\n");

        //Soma o número digitado a soma total
        sum += num;
    } while (num != 0); //O looping só continuará se o valor digitado for diferente de zero

    printf("A soma total e: %d.", sum);

    return 0;
}