/**
|-------------------------------------------------------------------------------
| readability.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jul 02, 2020
| Compilation:  make readability
| Execution:    ./readability
| Check50:      check50 cs50/problems/2020/x/readability
| Submit50:     submit50 cs50/problems/2020/x/readability
|
| This program determines the approximate grade level of a piece of text.
|
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    char passage[] = "When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.";    
    int letters = 0;
    int words = 0;
    int sentences = 0;
    int buffer = 0;
    float index = 0;
    int L = 0;
    int S = 0;
    int level = 0;
    char* mark;

    printf("Text: %s\n", passage);

    // determine the quantity of letters, words, and sentences
    buffer = strlen(passage);
    for (int i = 0; i < buffer; i++)
    {
        if (isalpha(passage[i]))
        {
            letters++;
        }
        if (isspace(passage[i]))
        {
            words++;
        }
        mark = &passage[i];
        if (strncmp(mark, ".", 1) == 0 || strncmp(mark, "?", 1) == 0 || strncmp(mark, "!", 1) == 0)
        {
            sentences++;
        }
    }
    words++;
    printf("%d letters(s)\n", letters);
    printf("%d words(s)\n", words);
    printf("%d sentences(s)\n", sentences);
    
    L = 1.0 * letters/words * 100;
    S = 1.0 * sentences/words * 100;

    index = 0.0588 * L - 0.296 * S - 15.8;
    level = round(index);

    if (level < 1)
        printf("Before Grade 1");
    else if (level >= 16)
        printf("Grade 16+");
    else
        printf("Grade %d\n", level);

    return 0;
}

