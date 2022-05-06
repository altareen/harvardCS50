/**
|-------------------------------------------------------------------------------
| hello.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jan 26, 2021
| Compilation:  make hello
| Execution:    ./hello
| Check50:      check50 cs50/problems/2021/x/hello
| Submit50:     submit50 cs50/problems/2021/x/hello
|
| This program displays a simple greeting to the user.
|
*/

#include <stdio.h>

int main(void)
{
    char name[32];
    printf("What is your name?\n");
    scanf("%s", name);
    printf("hello, %s\n", name);
    return 0;
}
