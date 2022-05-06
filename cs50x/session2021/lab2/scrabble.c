/**
|-------------------------------------------------------------------------------
| scrabble.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jan 28, 2021
| Compilation:  make scrabble
| Execution:    ./scrabble
| Check50:      check50 cs50/labs/2021/x/scrabble
| Submit50:     submit50 cs50/labs/2021/x/scrabble
|
| This program determines which of two Scrabble words is worth more points.
|
*/

#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

//int compute_score(string word);
int compute_score(char word[]);

int main(void)
{
    // Get input words from both players
    //string word1 = get_string("Player 1: ");
    //string word2 = get_string("Player 2: ");
    char word1[20];
    char word2[20];
    printf("Player 1: ");
    scanf("%s", word1);
    printf("Player 2: ");
    scanf("%s", word2);

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);
    
    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    return 0;
}

//int compute_score(string word)
int compute_score(char word[])
{
    // TODO: Compute and return score for string
    int result = 0;
    int size = strlen(word);
    
    for (int i = 0; i < size; i++)
    {
        int position = tolower(word[i]) - 97;
        if (position >= 0 && position <= 25)
        {
            result += POINTS[position];
        }
    }
    
    return result;
}

