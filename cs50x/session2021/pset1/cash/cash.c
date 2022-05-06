/**
|-------------------------------------------------------------------------------
| cash.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jan 27, 2021
| Compilation:  make cash
| Execution:    ./cash
| Check50:      check50 cs50/problems/2021/x/cash
| Submit50:     submit50 cs50/problems/2021/x/cash
|
| This program displays the minimum number of coins for a given amount of cash.
|
*/

#include <math.h>
#include <stdio.h>

int main(void)
{
    int coins = 0;
    float dollars = 0.0;
    do
    {
        printf("Change owed: ");
        scanf("%f", &dollars);
    } while (dollars < 0.0);
    
    int cents = round(dollars * 100);
    
    while (cents > 0)
    {
        if (cents/25 > 0)
        {
            cents -= 25;
        }
        else if (cents/10 > 0)
        {
            cents -= 10;
        }
        else if (cents/5 > 0)
        {
            cents -= 5;
        }
        else if (cents/1 > 0)
        {
            cents -= 1;
        }
        coins++;
    }
    
    printf("%d\n", coins);
    return 0;
}
