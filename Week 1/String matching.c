#include <stdio.h>
#include <string.h>

int main() {

    char text[100], pattern[50];
    int n, m, i, j, found = 0;

    printf("Enter length of text string: ");
    scanf("%d", &n);

    printf("Enter text string: ");
    scanf("%s", text);

    printf("Enter length of pattern string: ");
    scanf("%d", &m);

    printf("Enter pattern string: ");
    scanf("%s", pattern);

    for(i = 0; i <= n - m; i++) {

        j = 0;

        while(j < m && text[i + j] == pattern[j]) {
            j++;
        }

        if(j == m) {
            printf("Pattern found at position %d\n", i + 1);
            found = 1;
        }
    }

    if(!found) {
        printf("Pattern not found");
    }

    return 0;
}
