/**
|-------------------------------------------------------------------------------
| helpers.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Nov 18, 2020
| Compilation:  make filter
| Execution:    ./filter -g images/yard.bmp out.bmp
| Check50:      check50 cs50/problems/2020/x/filter/more
| Submit50:     submit50 cs50/problems/2020/x/filter/more
|
| This program applies grayscale, reflection, blur, or edge filters to images.
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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
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
        for (int col = 0; col < height; col++)
        {
            int GxRed = 0;
            int GxGreen = 0;
            int GxBlue = 0;
            
            int GyRed = 0;
            int GyGreen = 0;
            int GyBlue = 0;
            
            if (row != 0 && col != 0)
            {
                GxRed += -1 * pic[row-1][col-1].rgbtRed;
                GxGreen += -1 * pic[row-1][col-1].rgbtGreen;
                GxBlue += -1 * pic[row-1][col-1].rgbtBlue;
                
                GyRed += -1 * pic[row-1][col-1].rgbtRed;
                GyGreen += -1 * pic[row-1][col-1].rgbtGreen;
                GyBlue += -1 * pic[row-1][col-1].rgbtBlue;
            }
            if (row != 0)
            {
                GyRed += -2 * pic[row-1][col].rgbtRed;
                GyGreen += -2 * pic[row-1][col].rgbtGreen;
                GyBlue += -2 * pic[row-1][col].rgbtBlue;
            }
            if (row != 0 && col != width-1)
            {
                GxRed += 1 * pic[row-1][col+1].rgbtRed;
                GxGreen += 1 * pic[row-1][col+1].rgbtGreen;
                GxBlue += 1 * pic[row-1][col+1].rgbtBlue;
                
                GyRed += -1 * pic[row-1][col+1].rgbtRed;
                GyGreen += -1 * pic[row-1][col+1].rgbtGreen;
                GyBlue += -1 * pic[row-1][col+1].rgbtBlue;
            }
            if (col != 0)
            {
                GxRed += -2 * pic[row][col-1].rgbtRed;
                GxGreen += -2 * pic[row][col-1].rgbtGreen;
                GxBlue += -2 * pic[row][col-1].rgbtBlue;
            }
            if (col != width-1)
            {
                GxRed += 2 * pic[row][col+1].rgbtRed;
                GxGreen += 2 * pic[row][col+1].rgbtGreen;
                GxBlue += 2 * pic[row][col+1].rgbtBlue;
            }
            if (row != height-1 && col != 0)
            {
                GxRed += -1 * pic[row+1][col-1].rgbtRed;
                GxGreen += -1 * pic[row+1][col-1].rgbtGreen;
                GxBlue += -1 * pic[row+1][col-1].rgbtBlue;
                
                GyRed += 1 * pic[row+1][col-1].rgbtRed;
                GyGreen += 1 * pic[row+1][col-1].rgbtGreen;
                GyBlue += 1 * pic[row+1][col-1].rgbtBlue;
            }
            if (row != height-1)
            {
                GyRed += 2 * pic[row+1][col].rgbtRed;
                GyGreen += 2 * pic[row+1][col].rgbtGreen;
                GyBlue += 2 * pic[row+1][col].rgbtBlue;
            }
            if (row != height-1 && col != width-1)
            {
                GxRed += 1 * pic[row+1][col+1].rgbtRed;
                GxGreen += 1 * pic[row+1][col+1].rgbtGreen;
                GxBlue += 1 * pic[row+1][col+1].rgbtBlue;
                
                GyRed += 1 * pic[row+1][col+1].rgbtRed;
                GyGreen += 1 * pic[row+1][col+1].rgbtGreen;
                GyBlue += 1 * pic[row+1][col+1].rgbtBlue;
            }
            
            double ChannelRed = sqrt(pow(GxRed, 2) + pow(GyRed, 2));
            double ChannelGreen = sqrt(pow(GxGreen, 2) + pow(GyGreen, 2));
            double ChannelBlue = sqrt(pow(GxBlue, 2) + pow(GyBlue, 2));
            
            int SobelRed = (int) round(ChannelRed);
            int SobelGreen = (int) round(ChannelGreen);
            int SobelBlue = (int) round(ChannelBlue);
            
            if (SobelRed > 255)
                SobelRed = 255;
            if (SobelGreen > 255)
                SobelGreen = 255;
            if (SobelBlue > 255)
                SobelBlue = 255;
            
            image[row][col].rgbtRed = SobelRed;
            image[row][col].rgbtGreen = SobelGreen;
            image[row][col].rgbtBlue = SobelBlue;
        }
    }
    return;
}

