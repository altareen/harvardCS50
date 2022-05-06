/**
|-------------------------------------------------------------------------------
| caesar.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jul 03, 2020
| Compilation:  make caesar
| Execution:    ./caesar 20
| Check50:      check50 cs50/problems/2020/x/caesar
| Submit50:     submit50 cs50/problems/2020/x/caesar
|
| This program implements the caesar cipher encryption scheme.
|
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    char plaintext[] = "hello";

    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }
    else
    {
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (!isdigit(argv[1][i]))
            {
                printf("Usage: %s key\n", argv[0]);
                return 1;
            }
        }
    }
    
    int key = atoi(argv[1]);
    
    printf("plaintext:  %s\n", plaintext);
    printf("ciphertext: ");
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isupper(plaintext[i]))
        {
            printf("%c", (plaintext[i]-65 + key) % 26 + 65);
        }
        else if (islower(plaintext[i]))
        {
            printf("%c", (plaintext[i]-97 + key) % 26 + 97);
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");

    return 0;
}

