#include <stdio.h>
int reverse (int a) {
    int b, n=0;
    while ( a != 0 ) {
        b = a % 10;
        n = b + n * 10;
        a /= 10; 
    } return n ; }

    int main () {
        int A, B;
        scanf ("%d %d", &A, &B);
        A = reverse (A);
        B = reverse (B);
        int C = A + B;
        printf ("%d\n", reverse (C));
    }