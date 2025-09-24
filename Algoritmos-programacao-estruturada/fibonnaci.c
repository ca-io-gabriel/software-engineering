#include <stdio.h>

int main()
{
    int phi = 1, lastNumber = 1, quantity = 1;

    printf("Digite a quantidade de termos da sequencia: \n");
    scanf("%d", &quantity);

    for (int i = 1; i <= quantity; i++) {
        lastNumber = phi;

        phi += lastNumber;
        printf(" %d ", i);
    }
    
    return 0;
}