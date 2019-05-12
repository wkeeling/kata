#include <stdio.h>

int main() {

    int count;
    int c;

    while ((c = getchar()) != EOF) {
        if (c == '\n' || c == '\t' || c == ' ') {
            count++;
        }
    }

    printf("%d whitespace characters found\n", count);
}

