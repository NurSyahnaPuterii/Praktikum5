#include <stdio.h>

void Biodata (int tahun, char nama [20], char asal [20] ) {
    int tahun_sekarang = 2020;
    printf ("Perkenalkan Nama Saya :%s \n", nama);
    printf ("Umur Saya : %d \n", tahun_sekarang-tahun);
    printf ("Saya Adalah Angkatan :%d \n", tahun_sekarang );
    printf ("Asal Saya dari : %s\n", asal);
}

int main () {
    int tahunLahir;
        char A[20], B[15];
        scanf ("%d", &tahunLahir);
        scanf ("%s[^\n]%*c",&A);
        scanf ("%s[^\n]%*c",&B);
    Biodata(tahunLahir, A, B);
    return 0;
}