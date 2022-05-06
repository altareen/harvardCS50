/**
|-------------------------------------------------------------------------------
| credit.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jun 30, 2020
| Compilation:  make credit
| Execution:    ./credit
| Check50:      check50 cs50/problems/2020/x/credit
| Submit50:     submit50 cs50/problems/2020/x/credit
|
| This program checks if a credit card number is valid.
|
| Sample credit card number: 4003600000000014
| Expected output: VISA
|
*/

#include <stdio.h>

int main(void)
{
    long num = 0;
    long cardnum = 0;
    int single = 0;
    int total = 0;
    int partial = 0;
    int buffer = 0;
    int doubles = 0;
    int singles = 1;
    int check = 0;
    
    printf("Number: ");
    scanf("%ld", &num);
    
    cardnum = num;

    while (num)
    {
        buffer++;
        num = num/10;
    }    

    int digits[buffer];

    num = cardnum;
    for (int i = buffer-1; i >= 0; i--)
    {
        single = num%10;        
        digits[i] = single;
        num = num/10;
    } 

    if (buffer%2 == 1)
    {
        doubles = 1;
        singles = 0;
    }

    for (int i = doubles; i < buffer; i += 2)
    {
        partial = digits[i] * 2;
        if (partial > 9)
        {
            total += partial%10;
            partial = partial/10;
            total += partial%10;
        }
        else
        {
            total += partial;
        }
    }

    for (int i = singles; i < buffer; i += 2)
    {
        total += digits[i];
    }

    check = total%10;

    if (check == 0 && (buffer == 13 || buffer == 16) && digits[0] == 4)
    {
        printf("VISA\n");
    }
    else if (check == 0 && buffer == 15 && digits[0] == 3 && (digits[1] == 4 || digits[1] == 7))
    {
        printf("AMEX\n");
    }
    else if (check == 0 && buffer == 16 && digits[0] == 5 && (digits[1]==1 || digits[1]==2 || digits[1]==3 || digits[1]==4 || digits[1]==5))
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}

