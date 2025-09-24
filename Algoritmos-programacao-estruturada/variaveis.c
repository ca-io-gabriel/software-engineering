#include <stdio.h>

#define taxa 0.1;

int main() {
    int result;
    int taxaimp;
    int desconto;
    
    taxaimp = 1500 * taxa;
    
    desconto = 1500 * desconto;
    
    result = taxaimp - desconto;

    printf("O resultado é %d", result);

    return 0;
}