###
#-------------------------------------------------------------------------------
# minesweeper.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Aug 06, 2021
#
# Venv setup:       python3 -m venv venv
# Venv activation:  source venv/bin/activate
# Run TicTacToe:    python runner.py
# Conclusion:       deactivate
#
# Submission instructions:
# Create a .gitignore file with the following contents:
# __pycache__/
# venv/
# Move inside the folder that contains your project code and execute:
#
# git init
# git remote add origin https://github.com/me50/altareen.git
# git add -A
# git commit -m "Submit my project 1: minesweeper"
# git push origin main:ai50/projects/2020/x/minesweeper
#
##

import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # TODO(Completed)
        # Any time the number of cells is equal to the count, all of the cells
        # must be mines
        if self.count == len(self.cells):
            return self.cells.copy()
        return None

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # TODO(Completed)
        # Any time we have a sentence whose count is 0, all of the cells must be safe
        if self.count == 0:
            return self.cells.copy()
        return None

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # TODO(Completed)
        if cell in self.cells:
            self.cells.discard(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # TODO(Completed)
        self.cells.discard(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # TODO(Completed)
        # Mark the cell as a move that has been made
        self.moves_made.add(cell)
        
        # Mark the cell as safe, updating any sentences that contain the cell
        if cell not in self.safes:
            self.mark_safe(cell)
        
        # Add a new sentence, based on the value of cell and count
        neighbors = []
        row = cell[0]
        col = cell[1]
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if 0 <= row+y < self.height and 0 <= col+x < self.width and (row+y, col+x) not in self.moves_made:
                    neighbors.append((row+y, col+x))
        current = Sentence(neighbors, count)
        if len(neighbors) > 0 and current not in self.knowledge:
            self.knowledge.append(current)        

        # Mark any additional cells as safe or as mines, based on the KB
        for sentence in self.knowledge:
            cell_mines = sentence.known_mines()
            if cell_mines is not None:
                for cell in cell_mines:
                    if cell not in self.mines:
                        self.mark_mine(cell)
            cell_safes = sentence.known_safes()
            if cell_safes is not None:
                for cell in cell_safes:
                    if cell not in self.safes:
                        self.mark_safe(cell)
        
        # Purge all empty sentences from the KB
        for i in range(len(self.knowledge)-1, -1, -1):
            if len(self.knowledge[i].cells) == 0:
                self.knowledge.pop(i)
        
        # Add any new sentences that can be inferred from the KB
        spawned = []
        for i in range(len(self.knowledge)-1):
            for j in range(i+1, len(self.knowledge)):
                first, second = self.knowledge[i], self.knowledge[j]
                if len(first.cells) != 0 and len(second.cells) != 0 and first.cells != second.cells:
                    if len(first.cells) < len(second.cells) and first.cells.issubset(second.cells):
                        surplus = second.cells.difference(first.cells)
                        amount = second.count - first.count
                        if len(surplus) > 0 and amount > 0: # Note: changed from amount >= 0
                            current = Sentence(surplus, amount)
                            if current not in self.knowledge and current not in spawned:
                                spawned.append(current)
                    elif len(second.cells) < len(first.cells) and second.cells.issubset(first.cells):
                        surplus = first.cells.difference(second.cells)
                        amount = first.count - second.count
                        if len(surplus) > 0 and amount > 0: # Note: changed from amount >= 0
                            current = Sentence(surplus, amount)
                            if current not in self.knowledge and current not in spawned:
                                spawned.append(current)

        if len(spawned) > 0:
            self.knowledge.extend(spawned[:])

        # Mark any additional cells as safe or as mines, based on the KB
        for sentence in self.knowledge:
            cell_mines = sentence.known_mines()
            if cell_mines is not None:
                for cell in cell_mines:
                    if cell not in self.mines:
                        self.mark_mine(cell)
            cell_safes = sentence.known_safes()
            if cell_safes is not None:
                for cell in cell_safes:
                    if cell not in self.safes:
                        self.mark_safe(cell)
        
        # Purge all empty sentences from the KB
        for i in range(len(self.knowledge)-1, -1, -1):
            if len(self.knowledge[i].cells) == 0:
                self.knowledge.pop(i)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # TODO(Completed)
        unselected_safes = self.safes.difference(self.moves_made)
        unselected_safes.difference_update(self.mines)
        print(f"Unselected safes: {unselected_safes}")
        print(f"Known mines: {self.mines}")
        if len(unselected_safes) == 0:
            return None
        move = random.choice(tuple(unselected_safes))
        print(f"Move: {move}")
        print(f"Probability of winning: {round((1-1.0*(8-len(self.mines))/(64-(len(self.moves_made)+len(unselected_safes))))*100, 1)}")
        print("")
        return move

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # TODO(Completed)
        cells = set([(x,y) for x in range(self.width) for y in range(self.height)])
        cells.difference_update(self.moves_made)
        cells.difference_update(self.mines)
        if len(cells) == 0:
            return None
        return random.choice(tuple(cells))
        
