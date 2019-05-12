#include <stdio.h>

#define IN 0
#define OUT 1

int main() {
    int c, i, w;
    int state;
    int ccount[3];

    for (i = 0; i < 3; i++) {
        ccount[i] = 0;
    }

    w = -1;
    state = OUT;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            if (state == IN) {
                state = OUT;
            }
        } else if (state == OUT) {
            state = IN;
            w++;
        } 

        if (state == IN && w < 3) {
            ccount[w]++;
        }
    }
    
    for (i = 0; i < 3; i++) {
        for (c = 0; c < ccount[i]; c++) {
            printf("=");
        }
        printf("\n");
    }
}
