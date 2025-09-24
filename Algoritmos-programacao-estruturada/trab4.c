#include <stdio.h>
#include <stdbool.h>

int calcular_salario_bruto(int rateWork, int numberHoursWorked);
float calcular_desconto(int grossSalary);
float calcular_salario_liquido(int grossSalary, int discount);

int main() {
    int numberHoursWorked;
    float rateWork;

    while (true) {
        printf("Digite o valor da sua hora de trabalho: ");
        scanf("%f", &rateWork);

        if (rateWork <= 0) {
            printf("O valor da hora trabalhada deve ser maior que zero!\n\n");
        } else {
            break;
        }
    }

    while (true) {
        printf("Digite a quantidade de horas trabalhadas: ");
        scanf("%d", &numberHoursWorked);

        if (numberHoursWorked <= 0) {
            printf("O numero de horas trabalhadas deve ser maior que zero!\n\n");
        } else {
            break;
        }
    }

    int grossSalary;
    float discount, liquidSalary;

    grossSalary = calcular_salario_bruto(rateWork, numberHoursWorked);
    discount = calcular_desconto(grossSalary);
    liquidSalary = calcular_salario_liquido(grossSalary, discount);

    printf("\nO seu salario bruto e: R$ %d.00", grossSalary);
    printf("\nO desconto aplicado no seu salario e de: R$ %.2f", discount);
    printf("\nO seu salario liquido e: R$ %.2f", liquidSalary);

    return 0;
}

int calcular_salario_bruto(int rateWork, int numberHoursWorked) {
    return rateWork * numberHoursWorked;
}

float calcular_desconto(int grossSalary) {
    const float discount = 0.09;

    return grossSalary * discount;
}

float calcular_salario_liquido(int grossSalary, int discount) {
    return grossSalary - discount;
}