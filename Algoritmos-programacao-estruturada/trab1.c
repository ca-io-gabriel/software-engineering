#include <stdio.h>
#include <stdbool.h>

int main() {
    // O usuário digita três números e o programa armazena-os
    int num1, num2, num3;

    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);
    printf("Digite o segundo numero: ");
    scanf("%d", &num2);
    printf("Digite o terceiro numero: ");
    scanf("%d", &num3);

    //Calcula e imprime a soma, a subtração, a multiplicação e a divisão do números
    //Imprime uma mensagem diferente caso os divisores sejam iguais a 0 
    int sum, min, times;
    float div;

    sum = num1 + num2 + num3;
    min = num1 - num2 - num3;
    times = num1 * num2 * num3;

    printf("\nA soma dos numeros e: %d", sum);
    printf("\nA subtracao dos numeros e: %d", min);
    printf("\nA multiplicacao dos numeros e: %d", times);

    if (num2 == 0 || num3 == 0) {
        printf("\nNao e possivel fazer divisoes por 0");
    } else {
        div = (float) (num1 / num2) / num3; //Força o resultado a ser um valor do tipo ponto flutuante 
        printf("\nA divisao entre os numeros e: %.2f", div);
    }

    //Verifica e imprime se o primeiro numero é maior que o segundo número
    //Verifica e imprime se o segundo numero é maior que o terceiro número
    bool num1IsGreaterThanNum2, num2IsGreaterThanNum3;

    num1IsGreaterThanNum2 = num1 > num2;
    num2IsGreaterThanNum3 = num2 > num3;

    printf("\n\nO primeiro numero e maior que o segundo (0 -> Nao | 1 -> Sim)? %d", num1IsGreaterThanNum2);
    printf("\nO segundo numero e maior que o terceiro (0 -> Nao | 1 -> Sim)? %d", num2IsGreaterThanNum3);

    //Verifica se o primeiro número é positivo e se o segundo é par
    //Caso as duas condições sejam atendidas imprime uma mensagem
    int restOfDiv;
    bool num1IsPositive, num2IsPair;

    num1IsPositive = num1 > 0;

    restOfDiv = num2 % 2;
    if (restOfDiv == 0) 
        num2IsPair = true;
    else 
        num2IsPair = false;

    if (num1IsPositive && num2IsPair)
        printf("\n\nO primeiro numero e positivo e o segundo e par.");

    return 0;
}