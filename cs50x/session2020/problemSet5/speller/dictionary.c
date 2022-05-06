/**
|-------------------------------------------------------------------------------
| dictionary.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Nov 23, 2020
| Compilation:  make speller
| Execution:    ./speller dictionaries/small texts/cat.txt
|               ./speller texts/wordsworth.txt
|               ./speller texts/lalaland.txt
| Check50:      check50 cs50/problems/2020/x/speller
| Submit50:     submit50 cs50/problems/2020/x/speller
|
| This program implements a dictionary's functionality.
|
*/

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
// TODO Uncomment this line when submitting
//const unsigned int N = 17576;
// TODO Comment this line when submitting
#define N 17576

// Hash table
node *table[N];

// Number of words loaded into the dictionary
int count;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO(Completed)
    int location = hash(word);
    if (table[location] == NULL)
        return false;
    
    node *cursor = NULL;
    cursor = table[location];

    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
            return true;
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
// The djb2 algorithm: http://www.cse.yorku.ca/~oz/hash.html
unsigned int hash(const char *word)
{
    // TODO(Completed)
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

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // TODO(Completed)
    // Open dictionary file
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", dictionary);
        return false;
    }
    
    // Read strings from file one at a time
    char entry[LENGTH + 1];
    int location = 0;
    count = 0;
    while (fscanf(dict, "%s", entry) != EOF)
    {
        // Create a new node for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fprintf(stderr, "malloc ran out of memory.\n");
            return false;
        }
        
        strcpy(n->word, entry);
        
        // Hash each word to obtain a hash value
        location = hash(entry);
        
        // Insert node into hash table at that location
        if (table[location] == NULL)
        {
            table[location] = n;
            n->next = NULL;
        }
        else
        {
            n->next = table[location];
            table[location] = n;
        }
        count++;
    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO(Completed)
    if (count > 0)
    {
        return count;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO(Completed)
    node *cursor = NULL;
    node *temp = NULL;
    
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            cursor = table[i];
            temp = cursor;

            while (cursor != NULL)
            {
                cursor = cursor->next;
                free(temp);
                temp = cursor;
            }
            free(temp);
        }
    }
    return true;
}

