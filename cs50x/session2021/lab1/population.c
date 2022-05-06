/**
|-------------------------------------------------------------------------------
| population.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jan 05, 2021
| Compilation:  make population
| Execution:    ./population
| Check50:      check50 cs50/labs/2021/x/population
| Submit50:     submit50 cs50/labs/2021/x/population
|
| This program determines how long it takes for a population to reach a
| particular size.
|
*/

#include <stdio.h>

int main(void)
{
    int start = 0;
    int end = 0;
    int years = 0;
    int n = 0;

    // TODO: Prompt for start size
    do
    {
        printf("Start size: ");
        scanf("%i", &start);
    } while (start < 9);
    
    // TODO: Prompt for end size
    do
    {
        printf("End size: ");
        scanf("%i", &end);
    } while (end < start);

    // TODO: Calculate number of years until we reach threshold
    n = start;
    while (n < end)
    {
        n = n + (n / 3) - (n / 4);
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
    
    return 0;
}

