from sys import prefix
from mtg import finish_sentence
import nltk
import re
import random

corpus = [
    w.lower() for w in nltk.corpus.gutenberg.words("austen-sense.txt") 
    if re.search(r"[^\d]*",w)]
 
n3 = 3
prefix1 = ["she", "was", "not"]

try:
    assert finish_sentence(prefix1,n3,corpus,deterministic=True) == ['she', 'was', 'not', 'in', 'the', 'world', '.']
    #print("Pass, the sentence is:\n", " ".join(finish_sentence(prefix1,n3,corpus,deterministic=True)))
except:
    print("Assertion error.")
# random.seed(123)
# assert finish_sentence(prefix1,n3,corpus,deterministic=False) == ['she', 'was', 'not', 'accompanied', 'by', 'violent', 'agitation', ',', '"', 'misery', 'such', 'as', 'every', 'feeling', 'must', 'end', 'with', 'her']