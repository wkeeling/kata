#include <stdio.h>

#define MAX_LINE 10
#define MAX_TOTAL 1000

/* This program prints input lines longer than 80 characters */

int readline(char buf[], int max);

void main() {

    char buf[MAX_TOTAL];
    int len;

    while ((len = readline(buf, MAX_TOTAL)) > 0) {
        if (len > MAX_LINE) {
            printf("Greater than 10 (is %d)", len);
        } 
    }
}

int readline(char buf[], int max) {

    int c;
    int i = 0;

    while ((c = getchar()) != EOF && i < max && c != '\n') {
        if (i < max) {
            buf[i] = c;
        }
        i++;
    }

    return i;
}

