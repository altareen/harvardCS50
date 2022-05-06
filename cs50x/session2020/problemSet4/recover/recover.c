/**
|-------------------------------------------------------------------------------
| recover.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Nov 22, 2020
| Compilation:  make recover
| Execution:    ./recover card.raw
| Check50:      check50 cs50/problems/2020/x/recover
| Submit50:     submit50 cs50/problems/2020/x/recover
|
| This program recovers JPEGs from a forensic image.
|
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    
    // Open input file
    FILE *inptr = fopen(argv[1], "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 1;
    }
    
    int count = 0;
    char filename[8];
    FILE *img = NULL;
    BYTE buffer[512];
    while (fread(&buffer, sizeof(BYTE), 512, inptr) == 512)
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

    fclose(img);
    fclose(inptr);
}

