#include <stdio.h>

int main() {
    int c;
    
    while ((c = getchar()) != EOF) {
        putchar(c);
        putchar(c-'0');
    }
}
