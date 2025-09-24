#include <stdio.h>

int main() {
    //Declarando a varivável para a soma total dos valores de vendas e um array para guardar os valores de venda
    float salesSum = 0;
    float dailySales[5];

    //Declarando dois arrays constantes de ponteiros para guardar strings
    //que serão utilizadas para tornar o código mais dinâmico
    const char *daysOfWeek[] = {"primeiro", "segundo", "terceiro", "quarto", "quinto"};
    const char *daysOfWeekLowerCase[] = {"Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"};

    //Loping para que o usuário digite os valores e eles sejam armazenados no array e somados na variável
    for (int i = 0; i < 5; i++) { 
        printf("Digite o valor do %s dia de vendas: ", daysOfWeek[i]); //A cada repetição, pega uma string do array constante
        scanf("%f", &dailySales[i]);

        salesSum += dailySales[i]; //Acumula a soma total
    }

    printf("\n");

    //Imprime os valores do array 
    for (int i = 0; i < 5; i++) 
        //A cada repetição, pega uma string do array constante e a posição atual (valor de i)
        printf("%s dia de vendas (posicao %d): R$ %.2f\n", daysOfWeekLowerCase[i], i, dailySales[i]);
    
    printf("\n");

    //Imprime a soma total
    printf("A soma total das vendas e: R$ %.2f", salesSum);

    return 0;
}