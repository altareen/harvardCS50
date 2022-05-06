/**
|-------------------------------------------------------------------------------
| dictionary.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Feb 11, 2021
| Compilation:  make speller
| Execution:    ./speller texts/wordsworth.txt
| Check50:      check50 cs50/problems/2021/x/speller
| Submit50:     submit50 cs50/problems/2021/x/speller
|
| This program implements a dictionary's functionality.
|
*/

// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

int word_count = 0;

// Number of buckets in hash table
//const unsigned int N = 1;
#define N 17576

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int location = hash(word);
    node *head = table[location];
    node *cursor = head;
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }
    
    return false;
}

// Hashes word to a number
// The djb2 algorithm: http://www.cse.yorku.ca/~oz/hash.html
unsigned int hash(const char *word)
{
    // TODO
    unsigned int bucket = 5381;
    int current = 0;
    int i = 0;
    
    while (word[i] != 0)
    {
        current = tolower(word[i]);
        bucket = ((bucket << 5) + bucket) + current;
        i++;
    }
    
    return bucket % 17576;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    char word[LENGTH + 1];
    
    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Error: file %s cannot be opened.\n", dictionary);
        return false;
    }
    
    // Read strings from file
    while (fscanf(file, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Insufficient memory to create a node.\n");
            return false;
        }
        strcpy(n->word, word);
        int location = hash(word);
        word_count++;
        
        // Insert node n into the linked list
        n->next = table[location];
        table[location] = n;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    //return false;
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        node *tmp = table[i];
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }

    return true;
}

