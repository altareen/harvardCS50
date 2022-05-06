/**
|-------------------------------------------------------------------------------
| helpers.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Nov 17, 2020
| Compilation:  make filter
| Execution:    ./filter -g images/yard.bmp out.bmp
| Check50:      check50 cs50/problems/2020/x/filter/less
| Submit50:     submit50 cs50/problems/2020/x/filter/less
|
| This program applies grayscale, sepia, reflection, or blur filters to images.
|
*/

#include <math.h>
#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            int blue = image[row][col].rgbtBlue;
            int green = image[row][col].rgbtGreen;
            int red = image[row][col].rgbtRed;
            int avg = (int) round((blue + green + red)/3.0);
            image[row][col].rgbtBlue = avg;
            image[row][col].rgbtGreen = avg;
            image[row][col].rgbtRed = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            int blue = image[row][col].rgbtBlue;
            int green = image[row][col].rgbtGreen;
            int red = image[row][col].rgbtRed;
            
            int sepiaRed = round(.393 * red + .769 * green + .189 * blue);
            int sepiaGreen = round(.349 * red + .686 * green + .168 * blue);
            int sepiaBlue = round(.272 * red + .534 * green + .131 * blue);
            
            if (sepiaRed > 255)
                sepiaRed = 255;
            if (sepiaGreen > 255)
                sepiaGreen = 255;
            if (sepiaBlue > 255)
                sepiaBlue = 255;
            
            image[row][col].rgbtRed = sepiaRed;
            image[row][col].rgbtGreen = sepiaGreen;
            image[row][col].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        RGBTRIPLE buffer[width];
        for (int col = 0; col < width; col++)
        {
            buffer[col] = image[row][col];
        }
        
        int mark = width-1;
        for (int col = 0; col < width; col++)
        {
            image[row][col] = buffer[mark];
            mark--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Make a copy of the image
    RGBTRIPLE pic[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            pic[row][col] = image[row][col];
        }
    }
    
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            double items = 9.0;
            int sumRed = pic[row][col].rgbtRed;
            int sumGreen = pic[row][col].rgbtGreen;
            int sumBlue = pic[row][col].rgbtBlue;
            
            if (row != 0 && col != 0)
            {
                sumRed += pic[row-1][col-1].rgbtRed;
                sumGreen += pic[row-1][col-1].rgbtGreen;
                sumBlue += pic[row-1][col-1].rgbtBlue;
            }
            if (row != 0)
            {
                sumRed += pic[row-1][col].rgbtRed;
                sumGreen += pic[row-1][col].rgbtGreen;
                sumBlue += pic[row-1][col].rgbtBlue;
            }
            if (row != 0 && col != width-1)
            {
                sumRed += pic[row-1][col+1].rgbtRed;
                sumGreen += pic[row-1][col+1].rgbtGreen;
                sumBlue += pic[row-1][col+1].rgbtBlue;
            }
            if (col != 0)
            {
                sumRed += pic[row][col-1].rgbtRed;
                sumGreen += pic[row][col-1].rgbtGreen;
                sumBlue += pic[row][col-1].rgbtBlue;
            }
            if (col != width-1)
            {
                sumRed += pic[row][col+1].rgbtRed;
                sumGreen += pic[row][col+1].rgbtGreen;
                sumBlue += pic[row][col+1].rgbtBlue;
            }
            if (row != height-1 && col != 0)
            {
                sumRed += pic[row+1][col-1].rgbtRed;
                sumGreen += pic[row+1][col-1].rgbtGreen;
                sumBlue += pic[row+1][col-1].rgbtBlue;
            }
            if (row != height-1)
            {
                sumRed += pic[row+1][col].rgbtRed;
                sumGreen += pic[row+1][col].rgbtGreen;
                sumBlue += pic[row+1][col].rgbtBlue;
            }
            if (row != height-1 && col != width-1)
            {
                sumRed += pic[row+1][col+1].rgbtRed;
                sumGreen += pic[row+1][col+1].rgbtGreen;
                sumBlue += pic[row+1][col+1].rgbtBlue;
            }
            
            if ((row==0 && col==0) || (row==0 && col==width-1) || (row==height-1 && col==0) || (row==height-1 && col==width-1))
                items = 4.0;
            else if (row==0 || row==height-1 || col==0 || col==width-1)
                items = 6.0;
                
            int avgRed = (int) round(sumRed/items);
            int avgGreen = (int) round(sumGreen/items);
            int avgBlue = (int) round(sumBlue/items);
            
            image[row][col].rgbtRed = avgRed;
            image[row][col].rgbtGreen = avgGreen;
            image[row][col].rgbtBlue = avgBlue;
        }
    }
    return;
}

