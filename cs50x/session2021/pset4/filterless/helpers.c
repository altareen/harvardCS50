/**
|-------------------------------------------------------------------------------
| helpers.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Feb 06, 2021
| Compilation:  make filter
| Execution:    ./filter -g images/yard.bmp out.bmp
| Check50:      check50 cs50/problems/2021/x/filter/less
| Submit50:     submit50 cs50/problems/2021/x/filter/less
|
| This program applies graphical filters to bitmap images.
|
*/

#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double average = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue)/3.0;
            BYTE result = (int) round(average);
            image[i][j].rgbtRed = result;
            image[i][j].rgbtGreen = result;
            image[i][j].rgbtBlue = result;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE originalRed = image[i][j].rgbtRed;
            BYTE originalGreen = image[i][j].rgbtGreen;
            BYTE originalBlue = image[i][j].rgbtBlue;
        
            double sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue;
            double sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue;
            double sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue;
            
            int resultRed = (int) round(sepiaRed);
            int resultGreen = (int) round(sepiaGreen);
            int resultBlue = (int) round(sepiaBlue);
            
            image[i][j].rgbtRed = (resultRed > 255) ? 255 : (BYTE) resultRed;
            image[i][j].rgbtGreen = (resultGreen > 255) ? 255 : (BYTE) resultGreen;
            image[i][j].rgbtBlue = (resultBlue > 255) ? 255 : (BYTE) resultBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width/2; j++)
        {
            BYTE tempRed = image[i][j].rgbtRed;
            BYTE tempGreen = image[i][j].rgbtGreen;
            BYTE tempBlue = image[i][j].rgbtBlue;
            
            image[i][j].rgbtRed = image[i][width-1-j].rgbtRed;
            image[i][j].rgbtGreen = image[i][width-1-j].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width-1-j].rgbtBlue;
            
            image[i][width-1-j].rgbtRed = tempRed;
            image[i][width-1-j].rgbtGreen = tempGreen;
            image[i][width-1-j].rgbtBlue = tempBlue;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Generate a new clone image with greater height and width
    RGBTRIPLE clone[height+2][width+2];
    
    // Fill the clone image with zeros
    for (int i = 0; i < height+2; i++)
    {
        for (int j = 0; j < width+2; j++)
        {
            clone[i][j].rgbtRed = 0;
            clone[i][j].rgbtGreen = 0;
            clone[i][j].rgbtBlue = 0;
        }
    }

    // Copy the original image into the clone image
    for (int i = 1; i < height+1; i++)
    {
        for (int j = 1; j < width+1; j++)
        {
            clone[i][j] = image[i-1][j-1];
        }
    }

    // Perform the blur technique
    for (int i = 1; i < height+1; i++)
    {
        for (int j = 1; j < width+1; j++)
        {
            double factor = 9.0;        
            double averageRed = 0.0;
            double averageGreen = 0.0;
            double averageBlue = 0.0;
            
            averageRed += (clone[i-1][j-1].rgbtRed + clone[i-1][j].rgbtRed + clone[i-1][j+1].rgbtRed);
            averageRed += (clone[i][j-1].rgbtRed + clone[i][j].rgbtRed + clone[i][j+1].rgbtRed);
            averageRed += (clone[i+1][j-1].rgbtRed + clone[i+1][j].rgbtRed + clone[i+1][j+1].rgbtRed);
            
            averageGreen += (clone[i-1][j-1].rgbtGreen + clone[i-1][j].rgbtGreen + clone[i-1][j+1].rgbtGreen);
            averageGreen += (clone[i][j-1].rgbtGreen + clone[i][j].rgbtGreen + clone[i][j+1].rgbtGreen);
            averageGreen += (clone[i+1][j-1].rgbtGreen + clone[i+1][j].rgbtGreen + clone[i+1][j+1].rgbtGreen);
            
            averageBlue += (clone[i-1][j-1].rgbtBlue + clone[i-1][j].rgbtBlue + clone[i-1][j+1].rgbtBlue);
            averageBlue += (clone[i][j-1].rgbtBlue + clone[i][j].rgbtBlue + clone[i][j+1].rgbtBlue);
            averageBlue += (clone[i+1][j-1].rgbtBlue + clone[i+1][j].rgbtBlue + clone[i+1][j+1].rgbtBlue);
            
            // Adjust the factor depending on the cell position
            if ((i==1 && j==1) || (i==1 && j==width) || (i==height && j==1) || (i==height && j==width))
            {
                factor = 4.0;
            }
            else if ((i > 1 && i < height && j==1) || (i > 1 && i < height && j==width) || (j > 1 && j < width && i==1) || (j > 1 && j < width && i==height))
            {
                factor = 6.0;
            }
            
            BYTE resultRed = (int) round(averageRed/factor);
            BYTE resultGreen = (int) round(averageGreen/factor);
            BYTE resultBlue = (int) round(averageBlue/factor);
            
            image[i-1][j-1].rgbtRed = resultRed;
            image[i-1][j-1].rgbtGreen = resultGreen;
            image[i-1][j-1].rgbtBlue = resultBlue;
        }
    }
}

