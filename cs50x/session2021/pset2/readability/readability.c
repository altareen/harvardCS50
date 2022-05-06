/**
|-------------------------------------------------------------------------------
| readability.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jan 31, 2021
| Compilation:  make readability
| Execution:    ./readability
| Check50:      check50 cs50/problems/2021/x/readability
| Submit50:     submit50 cs50/problems/2021/x/readability
|
| This program determines the approximate grade level needed to comprehend some
| text.
|
*/

#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int letters = 0;
    int words = 0;
    int sentences = 0;
    const int BUFFER = 1024;
    char text[BUFFER];
    
    printf("Text: ");
    fgets(text, BUFFER, stdin);
    
    for (int i = 0, size = strlen(text); i < size; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
        
        if (text[i] == ' ')
        {
            words++;
        }
        
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
        
    }
    words++;
    
    double L = letters * (100.0 / words);
    double S = sentences * (100.0 / words);
    
    double index = 0.0588 * L - 0.296 * S - 15.8;
    int result = (int) round(index);
    
    if (result < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (result >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", result);
    }
    
    //printf("%d letters(s)\n", letters);
    //printf("%d word(s)\n", words);
    //printf("%d sentence(s)\n", sentences);
    
    return 0;
}

