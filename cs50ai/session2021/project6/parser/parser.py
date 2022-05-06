###
#-------------------------------------------------------------------------------
# parser.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Sep 08, 2021
#
# Venv setup:       python3 -m venv venv
# Venv activation:  source venv/bin/activate
# Requirements:     pip install -r requirements.txt
# Run:              python parser.py sentences/10.txt
# Conclusion:       deactivate
#
# Submission instructions:
# Create a .gitignore file with the following contents:
# venv/
#
# Move inside the folder that contains your project code and execute:
# git init
# git remote add origin https://github.com/me50/altareen.git
# git add -A
# git commit -m "Submit my project 6: parser"
# git push origin main:ai50/projects/2020/x/parser
#
##

import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP

SP -> S Conj S
AdjP -> Adj | Adj AdjP
AdvP -> Adv | Adv AdvP
ConjP -> Conj S
NP -> N | Det NP | AdjP NP | NP PP | NP ConjP | NP AdvP
PP -> P NP
VP -> V | V NP | V PP | V NP PP | AdvP VP | VP AdvP | VP Conj VP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    result = [x.lower() for x in nltk.word_tokenize(sentence) if x.isalpha()]
    print(result)
    return result


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    result = []
    for item in tree.subtrees(lambda x: x.label() == 'NP' and x.height() == 3):
        result.append(item)
    return result


if __name__ == "__main__":
    main()
