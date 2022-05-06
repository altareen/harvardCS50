###
#-------------------------------------------------------------------------------
# pagerank.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Aug 10, 2021
#
# Run PageRank: python3 pagerank.py corpus0
#
# Submission instructions:
# Move inside the folder that contains your project code and execute:
#
# git init
# git remote add origin https://github.com/me50/altareen.git
# git add -A
# git commit -m "Submit my project 2: pagerank"
# git push origin main:ai50/projects/2020/x/pagerank
#
##

import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probabilities = {x: (1-damping_factor)/len(corpus) for x in corpus.keys()}
    outlinks = corpus[page]
    for link in outlinks:
        probabilities[link] += damping_factor/len(outlinks)
    return probabilities
    

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_ranks = {x: 0 for x in corpus.keys()}
    sample = random.choice(list(corpus.keys()))
    page_ranks[sample] += 1
    for trial in range(n):
        odds = transition_model(corpus, sample, damping_factor)
        sample = random.choices(list(odds.keys()), weights=odds.values(), k=1)[0]
        page_ranks[sample] += 1
    for key in page_ranks:
        page_ranks[key] /= n
    return page_ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_ranks = {x: 1.0/len(corpus) for x in corpus.keys()}
    convergence = {x: False for x in corpus.keys()}
    
    while True:
        for page in page_ranks:
            incoming = 0
            for key, value in corpus.items():
                if page in value:
                    incoming += 1.0*page_ranks[key]/len(value)
                elif len(value) == 0:
                    incoming += 1.0*page_ranks[key]/len(page_ranks)
            previous_pr = page_ranks[page]
            current_pr = 1.0*(1-damping_factor)/len(corpus) + damping_factor*incoming
            page_ranks[page] = current_pr
            delta = abs(previous_pr - current_pr)
            if delta < 0.001:
                convergence[page] = True
            if all(convergence.values()):
                return page_ranks
    return page_ranks


if __name__ == "__main__":
    main()
