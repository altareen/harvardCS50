/**
|-------------------------------------------------------------------------------
| credit.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jan 27, 2021
| Compilation:  make credit
| Execution:    ./credit
| Check50:      check50 cs50/problems/2021/x/credit
| Submit50:     submit50 cs50/problems/2021/x/credit
|
| This program determines whether a given credit card number is valid.
|
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int first = 0;
    int second = 1;
    int batch = 0;
    char digits[17];
    strcpy(digits, "378282246310005");
    //strcpy(digits, "5555555555554444");
    //strcpy(digits, "4003600000000014");
    //strcpy(digits, "6176292929");
    //strcpy(digits, "369421438430814");
    //strcpy(digits, "4062901840");
    //strcpy(digits, "5673598276138003");
    //printf("%s\n", digits);
    int size = strlen(digits);

    if (size%2 == 1)
    {
        first = 1;
        second = 0;
    }
    
    // Digits which are multiplied by 2, summed into batch
    for (int i = first; i < size; i += 2)
    {
        int num = 2 * (digits[i] - '0');
        if (num > 9)
        {
            batch += num%10;
            num /= 10;
            batch += num;
        }
        else
        {
            batch += num;
        }
    }
    
    // The remaining digits summed into batch
    for (int i = second; i < size; i += 2)
    {
        batch += (digits[i] - '0');
    }

    int verify = batch % 10;
    int uno = digits[0] - '0';

    char deuce[3];
    strncpy(deuce, digits, 2);
    deuce[2] = '\0';
    int duo = atoi(deuce);

    if (verify == 0 && size == 15 && (duo == 34 || duo == 37))
    {
        printf("AMEX\n");
    }
    else if (verify == 0 && size == 16 && duo >= 51 && duo <= 55)
    {
        printf("MASTERCARD\n");
    }
    else if (verify == 0 && (size == 13 || size == 16) && uno == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
    
    return 0;
}
