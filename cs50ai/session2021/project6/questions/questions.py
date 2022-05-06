###
#-------------------------------------------------------------------------------
# questions.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Sep 09, 2021
#
# Venv setup:       python3 -m venv venv
# Venv activation:  source venv/bin/activate
# Requirements:     pip install -r requirements.txt
# Run:              python questions.py corpus
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
# git commit -m "Submit my project 6: questions"
# git push origin main:ai50/projects/2020/x/questions
#
##

import math
import nltk
import os
import string
import sys

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    filenames = os.listdir(directory)
    wikis = {name: "" for name in filenames}

    for filename in filenames:
        with open(os.path.join(directory + os.sep + filename)) as fhand:
            for line in fhand:
                wikis[filename] += line
    return wikis


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    words = [x.lower() for x in nltk.word_tokenize(document) if x.isalpha()]
    result = list(filter(lambda x: x not in string.punctuation and x not in nltk.corpus.stopwords.words("english"), words))
    return result
    

def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    total_docs = len(documents)
    result = dict()
    words = set()
    for value in documents.values():
        words.update(set(value))

    for word in words:
        count = 0
        for value in documents.values():
            if word in value:
                count += 1
        result[word] = math.log(1.0*total_docs/count)
    return result


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    ranking = {x: 0 for x in files.keys()}
    for word in query:
        for filename in files:
            score = 0
            if word in files[filename]:
                score += files[filename].count(word) * idfs[word]
            ranking[filename] += score
    result = [k for k, v in sorted(ranking.items(), key=lambda item: item[1], reverse=True)]
    return result[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    ranking = {x: [0, 0] for x in sentences.keys()}
    for word in query:
        for sentence in sentences:
            score = 0
            if word in sentences[sentence]:
                score += idfs[word]
                ranking[sentence][1] += 1.0/len(sentence)
            ranking[sentence][0] += score
    result = [k for k, v in sorted(ranking.items(), key=lambda item: (item[1][0], item[1][1]), reverse=True)]
    return result[:n]


if __name__ == "__main__":
    main()
