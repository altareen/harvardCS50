/**
|-------------------------------------------------------------------------------
| substitution.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jul 03, 2020
| Compilation:  make substitution
| Execution:    ./substitution JTREKYAVOGDXPSNCUIZLFBMWHQ
| Check50:      check50 cs50/problems/2020/x/substitution
| Submit50:     submit50 cs50/problems/2020/x/substitution
|
| This program implements the substitution cipher encryption scheme.
|
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    char large[26] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char small[26] = "abcdefghijklmnopqrstuvwxyz";

    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
    }
    
    for (int i = 0; i < strlen(argv[1])-1; i++)
    {
        for (int j = i+1; j < strlen(argv[1]); j++)
        {
            if (strncmp(&argv[1][i], &argv[1][j], 1) == 0)
            {
                printf("Key must contain 26 characters.\n");
                return 1;
            }
        }
    }

    char plaintext[] = "HeLlO";
    printf("plaintext:  %s\n", plaintext);
    printf("ciphertext: ");

    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isupper(plaintext[i]))
        {
            for (int j = 0; j < strlen(large); j++)
            {
                if (strncmp(&plaintext[i], &large[j], 1) == 0)
                {
                    printf("%c", toupper(argv[1][j]));
                }
            }
        }
        else if (islower(plaintext[i]))
        {
            for (int j = 0; j < strlen(small); j++)
            {
                if (strncmp(&plaintext[i], &small[j], 1) == 0)
                {
                    printf("%c", tolower(argv[1][j]));
                }
            }
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");

    return 0;
}

