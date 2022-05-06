###
#-------------------------------------------------------------------------------
# puzzle.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Aug 04, 2021
#
# Submission instructions:
# Create a .gitignore file with the folliwng contents:
# __pycache__/
# venv/
# Move inside the folder that contains your project code and execute:
#
# git init
# git remote add origin https://github.com/me50/altareen.git
# git add -A
# git commit -m "Submit my project 1: knights"
# git push origin main:ai50/projects/2020/x/knights
#
##

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO(Completed)
    # Use exclusive-or: A is either a Knight or a Knave, but not both
    Or(And(Not(AKnight), AKnave), And(AKnight, Not(AKnave))),
    
    # If A is a Knight, then the sentence must be true
    Implication(AKnight, And(AKnight, AKnave)),
    
    # If A is a Knave, then the sentence must be false
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO(Completed)
    # Use exclusive-or: A is either a Knight or a Knave, but not both
    Or(And(Not(AKnight), AKnave), And(AKnight, Not(AKnave))),
    
    # Use exclusive-or: B is either a Knight or a Knave, but not both
    Or(And(Not(BKnight), BKnave), And(BKnight, Not(BKnave))),
    
    # If A is a Knight, then the sentence must be true
    Implication(AKnight, And(AKnave, BKnave)),
    
    # If A is a Knave, then the sentence must be false
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO(Completed)
    # Use exclusive-or: A is either a Knight or a Knave, but not both
    Or(And(Not(AKnight), AKnave), And(AKnight, Not(AKnave))),
    
    # Use exclusive-or: B is either a Knight or a Knave, but not both
    Or(And(Not(BKnight), BKnave), And(BKnight, Not(BKnave))),
    
    # If A is a Knight, then the first sentence must be true
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    
    # If A is a Knave, then the first sentence must be false
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    
    # If B is a Knight, then the second sentence must be true
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    
    # If B is a Knave, then the second sentence must be false
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO(Completed)
    # Use exclusive-or: A is either a Knight or a Knave, but not both
    Or(And(Not(AKnight), AKnave), And(AKnight, Not(AKnave))),
    
    # Use exclusive-or: B is either a Knight or a Knave, but not both
    Or(And(Not(BKnight), BKnave), And(BKnight, Not(BKnave))),
    
    # Use exclusive-or: C is either a Knight or a Knave, but not both
    Or(And(Not(CKnight), CKnave), And(CKnight, Not(CKnave))),
    
    # For the first sentence, use exclusive-or: A says that they are either
    # a Knight or a Knave, but not both.
    
    # If A is a Knight, they are truthful
    Implication(AKnight, Or(And(Not(AKnight), AKnave), And(AKnight, Not(AKnave)))),

    # If A is a Knave, they are telling a falsehood
    Implication(AKnave, Not(Or(And(Not(AKnight), AKnave), And(AKnight, Not(AKnave))))),

    # For the second sentence, if B is a Knight, then he knows that A would lie
    Implication(BKnight, Implication(AKnave, Not(AKnave))),
    
    # For the second sentence, if B is a Knave, then he would lie
    Implication(BKnight, Not(Implication(AKnave, AKnave))),
    
    # If B is a Knight, then the third sentence must be true
    Implication(BKnight, CKnave),
    
    # If B is a Knave, then the third sentence must be false
    Implication(BKnave, Not(CKnave)),
    
    # If C is a Knight, then the fourth sentence must be true
    Implication(CKnight, AKnight),
    
    # If C is a Knave, then the fourth sentence must be false
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
