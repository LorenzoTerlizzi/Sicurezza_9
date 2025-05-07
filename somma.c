#include <stdio.h>

int somma (int a, int b)
{
    int c = a + b;
    return c;
}

int main() {
    int primo_numero;
    int secondo_numero;
    
    printf (" inserisci il primo nuemro: \n");
    scanf ("%d", &primo_numero);
    
    printf (" inserisci il secondo numero: \n");
    scanf ("%d", &secondo_numero);
    
    printf ("la somma è %d\n", somma (primo_numero, secondo_numero));
    return 0;
}