/**
|-------------------------------------------------------------------------------
| helpers.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Feb 07, 2021
| Compilation:  make filter
| Execution:    ./filter -g images/yard.bmp out.bmp
| Check50:      check50 cs50/problems/2021/x/filter/more
| Submit50:     submit50 cs50/problems/2021/x/filter/more
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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
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

    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Perform the edge technique
    for (int i = 1; i < height+1; i++)
    {
        for (int j = 1; j < width+1; j++)
        {
            int GxRed = 0;
            int GyRed = 0;
            int GxGreen = 0;
            int GyGreen = 0;
            int GxBlue = 0;
            int GyBlue = 0;
            
            GxRed += (clone[i-1][j-1].rgbtRed*Gx[0][0] + clone[i-1][j].rgbtRed*Gx[0][1] + clone[i-1][j+1].rgbtRed*Gx[0][2]);
            GxRed += (clone[i][j-1].rgbtRed*Gx[1][0] + clone[i][j].rgbtRed*Gx[1][1] + clone[i][j+1].rgbtRed*Gx[1][2]);
            GxRed += (clone[i+1][j-1].rgbtRed*Gx[2][0] + clone[i+1][j].rgbtRed*Gx[2][1] + clone[i+1][j+1].rgbtRed*Gx[2][2]);
            
            GyRed += (clone[i-1][j-1].rgbtRed*Gy[0][0] + clone[i-1][j].rgbtRed*Gy[0][1] + clone[i-1][j+1].rgbtRed*Gy[0][2]);
            GyRed += (clone[i][j-1].rgbtRed*Gy[1][0] + clone[i][j].rgbtRed*Gy[1][1] + clone[i][j+1].rgbtRed*Gy[1][2]);
            GyRed += (clone[i+1][j-1].rgbtRed*Gy[2][0] + clone[i+1][j].rgbtRed*Gy[2][1] + clone[i+1][j+1].rgbtRed*Gy[2][2]);

            GxGreen += (clone[i-1][j-1].rgbtGreen*Gx[0][0] + clone[i-1][j].rgbtGreen*Gx[0][1] + clone[i-1][j+1].rgbtGreen*Gx[0][2]);
            GxGreen += (clone[i][j-1].rgbtGreen*Gx[1][0] + clone[i][j].rgbtGreen*Gx[1][1] + clone[i][j+1].rgbtGreen*Gx[1][2]);
            GxGreen += (clone[i+1][j-1].rgbtGreen*Gx[2][0] + clone[i+1][j].rgbtGreen*Gx[2][1] + clone[i+1][j+1].rgbtGreen*Gx[2][2]);
            
            GyGreen += (clone[i-1][j-1].rgbtGreen*Gy[0][0] + clone[i-1][j].rgbtGreen*Gy[0][1] + clone[i-1][j+1].rgbtGreen*Gy[0][2]);
            GyGreen += (clone[i][j-1].rgbtGreen*Gy[1][0] + clone[i][j].rgbtGreen*Gy[1][1] + clone[i][j+1].rgbtGreen*Gy[1][2]);
            GyGreen += (clone[i+1][j-1].rgbtGreen*Gy[2][0] + clone[i+1][j].rgbtGreen*Gy[2][1] + clone[i+1][j+1].rgbtGreen*Gy[2][2]);

            GxBlue += (clone[i-1][j-1].rgbtBlue*Gx[0][0] + clone[i-1][j].rgbtBlue*Gx[0][1] + clone[i-1][j+1].rgbtBlue*Gx[0][2]);
            GxBlue += (clone[i][j-1].rgbtBlue*Gx[1][0] + clone[i][j].rgbtBlue*Gx[1][1] + clone[i][j+1].rgbtBlue*Gx[1][2]);
            GxBlue += (clone[i+1][j-1].rgbtBlue*Gx[2][0] + clone[i+1][j].rgbtBlue*Gx[2][1] + clone[i+1][j+1].rgbtBlue*Gx[2][2]);
            
            GyBlue += (clone[i-1][j-1].rgbtBlue*Gy[0][0] + clone[i-1][j].rgbtBlue*Gy[0][1] + clone[i-1][j+1].rgbtBlue*Gy[0][2]);
            GyBlue += (clone[i][j-1].rgbtBlue*Gy[1][0] + clone[i][j].rgbtBlue*Gy[1][1] + clone[i][j+1].rgbtBlue*Gy[1][2]);
            GyBlue += (clone[i+1][j-1].rgbtBlue*Gy[2][0] + clone[i+1][j].rgbtBlue*Gy[2][1] + clone[i+1][j+1].rgbtBlue*Gy[2][2]);
            
            int resultRed = (int) round(sqrt(pow(GxRed, 2) + pow(GyRed, 2)));
            int resultGreen = (int) round(sqrt(pow(GxGreen, 2) + pow(GyGreen, 2)));
            int resultBlue = (int) round(sqrt(pow(GxBlue, 2) + pow(GyBlue, 2)));
            
            image[i-1][j-1].rgbtRed = (resultRed > 255) ? 255 : (BYTE) resultRed;
            image[i-1][j-1].rgbtGreen = (resultGreen > 255) ? 255 : (BYTE) resultGreen;
            image[i-1][j-1].rgbtBlue = (resultBlue > 255) ? 255 : (BYTE) resultBlue;
        }
    }
}

