#include <stdio.h>

int main() {
    float value1;
    float value2;
    float result; 

    printf("Digite o primeiro valor: \n");
    scanf("%f", &value1);

    printf("Digite o segundo valor: \n");
    scanf("%f", &value2);

    result = (value1 + value2) / 2;

    printf("A média dos valores é: %.2f", result);

    return 0;
}