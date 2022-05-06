/**
|-------------------------------------------------------------------------------
| runoff.c
|-------------------------------------------------------------------------------
|
| Author:       Alwin Tareen
| Created:      Jul 05, 2020
| Compilation:  make runoff
| Execution:    ./runoff Alice Bob Charlie
| Check50:      check50 cs50/problems/2020/x/runoff
| Submit50:     submit50 cs50/problems/2020/x/runoff
|
| This program simulates a runoff vote election.
|
| Sample election:
| Number of voters: 5
| Rank 1: Alice
| Rank 2: Bob
| Rank 3: Charlie
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
| Rank 2: Alice
| Rank 3: Charlie
|
| Rank 1: Charlie
| Rank 2: Alice
| Rank 3: Bob
|
| Expected output:
| Alice
|
*/

//#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    char* name;
    int votes;
    int eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
int vote(int voter, int rank, char* name);
void tabulate(void);
int print_winner(void);
int find_min(void);
int is_tie(int min);
void eliminate(int min);

int main(int argc, char* argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = 0;
    }

    printf("Number of voters: ");
    scanf("%i", &voter_count);

    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            //string name = get_string("Rank %i: ", j + 1);
            char name[20];
            printf("Rank %i: ", j + 1);
            scanf("%s", name);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (1)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        int won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        int tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
int vote(int voter, int rank, char* name)
{
    // TODO(Completed)
    for (int j = 0; j < candidate_count; j++)
    {
        if (strcmp(name, candidates[j].name) == 0)
        {
            preferences[voter][rank] = j;
            return 1;
        }
    }
    return 0;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // TODO(Completed)
    for (int i = 0; i < voter_count; i++)
    {
        int rank = 0;
        int choice = preferences[i][rank];
        if (!candidates[choice].eliminated)
        {
            candidates[choice].votes++;
        }
        else
        {
            rank++;
            choice = preferences[i][rank];
            if (!candidates[choice].eliminated)
            {
                candidates[choice].votes++;
            }
            else
            {
                rank++;
                choice = preferences[i][rank];
                if (!candidates[choice].eliminated)
                {
                    candidates[choice].votes++;
                }
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
int print_winner(void)
{
    // TODO(Completed)
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > voter_count/2)
        {
            printf("%s\n", candidates[i].name);
            return 1;
        }
    }
    return 0;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO(Completed)
    int lowest = MAX_VOTERS;
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated && candidates[i].votes < lowest)
        {
            lowest = candidates[i].votes;
        }
    }
    return lowest;
}

// Return true if the election is tied between all candidates, false otherwise
int is_tie(int min)
{
    // TODO(Completed)
    int outcome = 1;
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated && candidates[i].votes != min)
        {
            outcome = 0;
        }
        
    }
    return outcome;
}

// Eliminate the candidate (or candidiates) in last place
void eliminate(int min)
{
    // TODO(Completed)
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated && candidates[i].votes == min)
        {
            candidates[i].eliminated = 1;
        }
    }
    return;
}

