/**
|-------------------------------------------------------------------------------
| caesar.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jan 31, 2021
| Compilation:  make caesar
| Execution:    ./caesar 20
| Check50:      check50 cs50/problems/2021/x/caesar
| Submit50:     submit50 cs50/problems/2021/x/caesar
|
| This program encrypts messages using the Caesar cipher.
|
*/

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0, size = strlen(argv[1]); i < size; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    
    const int BUFFER = 128;
    char plaintext[BUFFER];
    char ciphertext[BUFFER];
    
    int key = atoi(argv[1]);
    printf("key: %d\n", key);

    printf("plaintext: ");
    fgets(plaintext, BUFFER, stdin);

    for (int i = 0, size = strlen(plaintext); i < size; i++)
    {
        if (isupper(plaintext[i]))
        {
            ciphertext[i] = (plaintext[i] - 65 + key) % 26 + 65;
        }
        else if (islower(plaintext[i]))
        {
            ciphertext[i] = (plaintext[i] - 97 + key) % 26 + 97;
        }
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }

    printf("ciphertext: %s\n", ciphertext);

    return 0;
}
