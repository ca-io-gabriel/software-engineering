#include <stdio.h>

#include <windows.h>

int main() {

    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);


    int j = 0;
    char cpfSemFormatacao[15];
    char cpfFormatado[12];

    printf("Digite o CPF: ");
    scanf("%s", cpfSemFormatacao);

    for (int i = 0; i <= 15; i++) {
        if (!(cpfSemFormatacao[i] == '.' || cpfSemFormatacao[i] == '-')) {
            cpfFormatado[j] = cpfSemFormatacao[i];
            j = j + 1;
        }
    }

    for (int i = 0; i <= 11; i++)
        printf("%c", cpfFormatado[i]);

    return 0;
}