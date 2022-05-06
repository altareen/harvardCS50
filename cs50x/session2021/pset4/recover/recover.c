/**
|-------------------------------------------------------------------------------
| recover.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Feb 08, 2021
| Compilation:  make recover
| Execution:    ./recover card.raw
| Check50:      check50 cs50/problems/2021/x/recover
| Submit50:     submit50 cs50/problems/2021/x/recover
|
| This program recovers JPEG pictures from a forensic card image.
|
*/

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check for invalid usage
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    
    // Open the memory card
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Error: file %s cannot be opened.\n", argv[1]);
        return 1;
    }
    
    BYTE buffer[512];
    int count = 0;
    char filename[8];
    FILE *img = NULL;
    
    while(fread(&buffer, sizeof(BYTE), 512, file) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (count == 0)
            {
                sprintf(filename, "%03i.jpg", count);
                img = fopen(filename, "w");
                fwrite(&buffer, sizeof(BYTE), 512, img);
                count++;
            }
            else
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", count);
                img = fopen(filename, "w");
                fwrite(&buffer, sizeof(BYTE), 512, img);
                count++;
            }
        }
        else if (count > 0)
        {
            fwrite(&buffer, sizeof(BYTE), 512, img);
        }
    }
    
    fclose(file);
    fclose(img);
    return 0;
}

