#include <stdio.h>
#include <stdbool.h>

//Declarando as funções para calular o salário
float calcular_salario_bruto(int rateWork, int numberHoursWorked);
float calcular_desconto(float grossSalary);
float calcular_salario_liquido(int grossSalary, int discount);

int main() {
    //Declarando as variáveis para o número de horas trabalhadas e o valor da hora
    int numberHoursWorked;
    float rateWork;

    //Loopings para garantir que o valor das horas sejam válidas
    while (true) {
        printf("Digite o valor da sua hora de trabalho: ");
        scanf("%f", &rateWork);

        if (rateWork <= 0) {
            printf("O valor da hora trabalhada deve ser maior que zero!\n\n");
        } else {
            break;
        }
    }

    //Loopings para garantir que númeero de horas trabalhadas sejam válidas
    while (true) {
        printf("Digite a quantidade de horas trabalhadas: ");
        scanf("%d", &numberHoursWorked);

        if (numberHoursWorked <= 0) {
            printf("O numero de horas trabalhadas deve ser maior que zero!\n\n");
        } else {
            break;
        }
    }

    //Declarando as variáveis para o salários e o desconto
    float grossSalary, discount, liquidSalary;

    //Armazenando os retornos da variáveis e usando-os como paramêtro
    grossSalary = calcular_salario_bruto(rateWork, numberHoursWorked);
    discount = calcular_desconto(grossSalary);
    liquidSalary = calcular_salario_liquido(grossSalary, discount);

    //Imprimindo os valores na tela
    printf("\nO seu salario bruto e: R$ %d.00", grossSalary);
    printf("\nO desconto aplicado no seu salario e de: R$ %.2f", discount);
    printf("\nO seu salario liquido e: R$ %.2f", liquidSalary);

    return 0;
}

//Declarando o escopo da função para calcular o salário bruto por meio de parâmetros 
float calcular_salario_bruto(int rateWork, int numberHoursWorked) {
    return rateWork * numberHoursWorked;
}

//Declarando o escopo da função para calcular o desconto por meio de parâmetros
float calcular_desconto(float grossSalary) {
    const float discount = 0.09;

    return grossSalary * discount;
}

//Declarando o escopo da função para calcular o salário líquido por meio de parâmetros
float calcular_salario_liquido(int grossSalary, int discount) {
    return grossSalary - discount;
}