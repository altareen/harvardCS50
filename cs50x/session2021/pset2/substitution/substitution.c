/**
|-------------------------------------------------------------------------------
| substitution.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Feb 01, 2021
| Compilation:  make substitution
| Execution:    ./substitution YTNSHKVEFXRBAUQZCLWDMIPGJO
| Check50:      check50 cs50/problems/2021/x/substitution
| Submit50:     submit50 cs50/problems/2021/x/substitution
|
| This program encrypts messages using the substitution cipher.
|
*/

#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char *key;
    key = argv[1];

    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(key) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    
    // Check if all characters in the key are alphabetical
    for (int i = 0, size = strlen(key); i < size; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }
    }
    
    // Check for repeated alphabetical characters
    for (int i = 0, size = strlen(key); i < size-1; i++)
    {
        for (int j = i+1; j < size; j++)
        {
            if (key[i] == key[j])
            {
                printf("Key must not contain repeated characters.\n");
                return 1;
            }
        }
    }

    const int BUFFER = 128;
    char plaintext[BUFFER];
    char ciphertext[BUFFER];
    
    printf("plaintext: ");
    fgets(plaintext, BUFFER, stdin);
    
    for (int i = 0, size = strlen(plaintext); i < size; i++)
    {
        if (isupper(plaintext[i]))
        {
            ciphertext[i] = toupper(key[plaintext[i]-65]);
        }
        else if (islower(plaintext[i]))
        {
            ciphertext[i] = tolower(key[plaintext[i]-97]);
        }
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }

    printf("ciphertext: %s\n", ciphertext);

    return 0;
}

