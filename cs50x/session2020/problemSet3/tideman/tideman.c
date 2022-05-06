/**
|-------------------------------------------------------------------------------
| tideman.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jul 06, 2020
| Compilation:  make tideman
| Execution:    ./tideman Alice Bob Charlie
| Check50:      check50 cs50/problems/2020/x/tideman
| Submit50:     submit50 cs50/problems/2020/x/tideman
|
| This program simulates a tideman vote election.
|
| Sample election:
| Number of voters: 5
| Rank 1: Alice
| Rank 2: Charlie
| Rank 3: Bob
|
| Rank 1: Alice
| Rank 2: Charlie
| Rank 3: Bob
|
| Rank 1: Bob
| Rank 2: Charlie
| Rank 3: Alice
|
| Rank 1: Bob
| Rank 2: Charlie
| Rank 3: Alice
|
| Rank 1: Charlie
| Rank 2: Alice
| Rank 3: Bob
|
| Expected output:
| Charlie
|
*/

//#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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

// Each candidate has a name
typedef struct
{
    char* name;
}
person;

// Array of candidates
person candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, char* name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
int compare(const void *av, const void *bv);
void lock_pairs(void);
bool check_cycle(int champ, int downer);
void print_winner(void);

int main(int argc, char* argv[])
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
        candidates[i].name = argv[i + 1];
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
    int voter_count = 0;
    printf("Number of voters: ");
    scanf("%i", &voter_count);

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            char name[20];
            printf("Rank %i: ", j + 1);
            scanf("%s", name);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
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
bool vote(int rank, char* name, int ranks[])
{
    // TODO(Completed)
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
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
        int individual = ranks[i];
        for (int j = i+1; j < candidate_count; j++)
        {
            int opponent = ranks[j];
            preferences[individual][opponent]++;
        }
    }
    return;
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
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO(Completed)
    qsort(pairs, pair_count, sizeof(pair), compare);
    return;
}

int compare(const void *av, const void *bv)
{
    pair *a = (pair *)av;
    pair *b = (pair *)bv;
    if (preferences[a->winner][a->loser] > preferences[b->winner][b->loser])
        return -1;
    else if (preferences[a->winner][a->loser] < preferences[b->winner][b->loser])
        return 1;
    else
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
        if (!check_cycle(victor, defeat))
        {
            locked[victor][defeat] = true;
        }
    }
}

bool check_cycle(int champ, int downer)
{
    bool result = false;
    if (champ == downer)
    {
        return true;
    }
    else
    {
        for (int i = 0; i < candidate_count; i++)
        {
            if (locked[downer][i] == true)
            {
                result = check_cycle(champ, i);
                if (result == true)
                    return true;
            }
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
            if (locked[row][col] == true)
                flag = true;
        }
        if (!flag)
            printf("%s\n", candidates[col].name);
    }
    return;
}

