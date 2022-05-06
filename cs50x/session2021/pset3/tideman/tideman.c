/**
|-------------------------------------------------------------------------------
| tideman.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Feb 05, 2021
| Compilation:  make tideman
| Execution:    ./tideman Alice Bob Charlie
| Check50:      check50 cs50/problems/2021/x/tideman
| Submit50:     submit50 cs50/problems/2021/x/tideman
|
| This program runs a tideman election.
|
*/

//#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
//string candidates[MAX];
char *candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
//bool vote(int rank, string name, int ranks[]);
bool vote(int rank, char *name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
int compare(const void *av, const void *bv);
void lock_pairs(void);
bool cycle_exists(int victor, int defeat);
void print_winner(void);

//int main(int argc, string argv[])
int main(int argc, char *argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    //int voter_count = get_int("Number of voters: ");
    printf("Number of voters: ");
    int voter_count = 0;
    scanf("%d", &voter_count);

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            //string name = get_string("Rank %i: ", j + 1);
            printf("Rank %i: ", j + 1);
            char *name = malloc(16);
            scanf("%s", name);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
            
            free(name);
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
//bool vote(int rank, string name, int ranks[])
bool vote(int rank, char *name, int ranks[])
{
    // TODO(Completed)
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO(Completed)
    for (int i = 0; i < candidate_count-1; i++)
    {
        for (int j = i+1; j < candidate_count; j++)
        {
            int like = ranks[i];
            int dislike = ranks[j];
            preferences[like][dislike]++;
        }
    }
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO(Completed)
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
        }
    }
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO(Completed)
    qsort(pairs, pair_count, sizeof(pair), compare);
}

// Take pointers to the two elements to compare in qsort above
int compare(const void *av, const void *bv)
{
    // TODO(Completed)
    pair *a = (pair *)av;
    pair *b = (pair *)bv;
    if (preferences[a->winner][a->loser] < preferences[b->winner][b->loser])
        return 1;
    if (preferences[a->winner][a->loser] > preferences[b->winner][b->loser])
        return -1;
    return 0;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO(Completed)
    for (int i = 0; i < pair_count; i++)
    {
        int victor = pairs[i].winner;
        int defeat = pairs[i].loser;
        if (!cycle_exists(victor, defeat))
        {
            locked[victor][defeat] = true;
        }
    }
}

bool cycle_exists(int victor, int defeat)
{
    // TODO(Completed)
    if (victor == defeat)
        return true;    
    else
    {
        for (int i = 0; i < candidate_count; i++)
        {
            if (locked[defeat][i] && cycle_exists(victor, i))
                return true;
        }
    }
    return false;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO(Completed)
    for (int col = 0; col < candidate_count; col++)
    {
        bool flag = false;
        for (int row = 0; row < candidate_count; row++)
        {
            if (locked[row][col])
                flag = true;
        }
        if (!flag)
            printf("%s\n", candidates[col]);
    }
}

