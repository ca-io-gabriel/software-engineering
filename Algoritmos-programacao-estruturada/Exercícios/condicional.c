#include <stdio.h>

int main()
{
    double totalSalary;
    double liquidSalary;

    float inss;
    float ir;

    printf("Digite o seu salario: \n");
    scanf("%lf", &totalSalary);

    if (totalSalary <= 1320)
        inss = 0.075;
    else if (totalSalary <=1320 && totalSalary >= 2571.29) 
        inss = 0.09;
    else if (totalSalary <=2571.30 && totalSalary >= 3856.94) 
        inss = 0.12;
    else
        inss = 0.14;

    if (totalSalary <= 1903.98)
        ir = 0;
    else if (totalSalary <=1903.99 && totalSalary >= 2826.65) 
        ir = 0.075;
    else if (totalSalary <=2826.66 && totalSalary >= 3751.05) 
        ir = 0.15;
    else if (totalSalary <=3751.06 && totalSalary >= 4664.68) 
        inss = 0.225;
    else
        ir = 0.275;

    liquidSalary = (totalSalary - (totalSalary * inss) - (totalSalary * ir));

    printf("O seu salario liquido e: %f", liquidSalary);

    return 0;
}