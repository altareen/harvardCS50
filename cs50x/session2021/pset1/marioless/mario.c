/**
|-------------------------------------------------------------------------------
| mario.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jan 26, 2021
| Compilation:  make mario
| Execution:    ./mario
| Check50:      check50 cs50/problems/2021/x/mario/less
| Submit50:     submit50 cs50/problems/2021/x/mario/less
|
| This program creates a right-aligned pyramid of hash marks.
|
*/

#include <stdio.h>

int main(void)
{
    int height = 0;
    do
    {
        printf("Height: ");
        scanf("%d", &height);
    } while (height < 1 || height > 8);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height-i-1; j++)
        {
            printf(" ");
        }
        for (int j = 0; j < i+1; j++)
        {
            printf("#");
        }
        printf("\n");
    }

    return 0;
}
