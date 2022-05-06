/**
|-------------------------------------------------------------------------------
| mario.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jun 30, 2020
| Compilation:  make mario
| Execution:    ./mario
| Check50:      check50 cs50/problems/2020/x/mario/more
| Submit50:     submit50 cs50/problems/2020/x/mario/more
|
| This program creates a pyramid of hash marks.
|
*/

#include <stdio.h>

int main(void)
{
    int num;

    do
    {
        printf("Height: ");
        scanf("%d", &num);
    } while (num < 1 || num > 8);

    printf("Stored: %d\n", num);

    for (int i = 1; i <= num; i++)
    {
        for (int j = num-i; j >= 1; j--)
        {
            printf(" ");
        }

        for (int k = 1; k <= i; k++)
        {
            printf("#");
        }

        printf("  ");

        for (int m = 1; m <= i; m++)
        {
            printf("#");
        }

        printf("\n");
    }
}

