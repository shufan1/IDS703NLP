import nltk
import random
import re
from nltk.chunk import ne_chunk
import numpy as np
#import timeit

nltk.download('gutenberg')

def make_seq(starting_ind,n,corpus): 
    #get all n words starting at a specific index, helper function for make token_seqs(n)
    seq = " ".join(corpus[starting_ind:starting_ind+n-1])
    return seq

def update_ngram(i,n,seq_before,ngram_table_row,corpus): 
    # check if each n sequence contains the n-1 word in the sentence
    # if yes, update the count for the word followed
    # helper function for build_ngram_for_prefix
    seq =(" ").join(corpus[i:i+n-1])
    if seq == seq_before:
        next_word = corpus[i+n-1]
        next_word =  next_word[0] if (re.match(r'^[.,;!?]\W+$',next_word) != None) else next_word
        #print("here", next_word) if "." in next_word else print("no")
        index = token_words[next_word]
        ngram_table_row[index] += 1

def build_n_gram_for_prefix(n,seq_before,corpus): #make an ngram table for a specific preceeding n-1 sequence 
    ngram_table_row = np.zeros(size)
    list(map(lambda i: update_ngram(i,n,seq_before,ngram_table_row,corpus),range(len(corpus)-n)))# count, update ngram
    ngram_table_row = ngram_table_row / np.sum(ngram_table_row)
    return ngram_table_row

def make_token_seqs(n,corpus): #get all unique the n sequence from the corpus
    sequence = list(map(lambda i: make_seq(i,n,corpus),range(len(corpus)-n+1)))
    sequence = sorted(set(sequence))
    token_seqs = {seq: ind for ind, seq in enumerate(sequence)}
    return token_seqs

def generat_text(prefix,n,deterministic,corpus):
    prefix_copy = prefix.copy() # make a copy of the prefix, so prefix won't be changed
    token_seqs = make_token_seqs(n,corpus) # get all unique n words sequence
    for _ in range(15):
        if prefix_copy[-1] in ':;.?!': #if find punuctation, stop
            return prefix_copy
        else: #find word
            prefix_n_1 =(" ").join(prefix_copy[-n+1:])
            if prefix_n_1 in token_seqs:
                dist = build_n_gram_for_prefix(n,prefix_n_1,corpus) #build n gram for the last n-1 sequence
                next_word = vocabulary[np.argmax(dist)] if deterministic else random.choices(vocabulary,dist)[0]
                prefix_copy.append(next_word)
            else:  # stupid back-off make n-1 gram for this sequence
                n_copy = n-1
                found = False
                while n_copy >=2 and not found: #do stupid back-off until bigram
                    prefix_n_2 =(" ").join(prefix_copy[-n_copy+1:])
                    token_seqs_n_1 = make_token_seqs(n_copy,corpus)
                    if prefix_n_2 in token_seqs_n_1:
                        dist_n_minus_1 = build_n_gram_for_prefix(n_copy-1,prefix_n_2,corpus)
                        next_word = vocabulary[np.argmax(dist_n_minus_1)] if deterministic else random.choices(vocabulary,dist_n_minus_1)
                        prefix_copy.append(next_word)
                        found = True
                    n_copy -= 1
    return prefix_copy

def finish_sentence(sentence, n, corpus, deterministic=False):
    global vocabulary 
    vocabulary = sorted(set(corpus)) #extract all the unique words
    global token_words 
    token_words = {word: ind for ind, word in enumerate(vocabulary)}
    global size
    size = len(vocabulary) #how many columns for n-gram
    sentence_new = generat_text(sentence,n,deterministic,corpus)
    return sentence_new


if __name__=="__main__":
    prefix = ["she","was","not"]
    n = 3
    corpus = [
        w.lower() for w in nltk.corpus.gutenberg.words("austen-sense.txt") 
        ]

    random.seed(12)
    sentence = finish_sentence(prefix,n,corpus,deterministic=True)
#     sentence1 = finish_sentence(prefix,n,corpus,deterministic=False)
#     sentence2 = finish_sentence(prefix,4,corpus,deterministic=True)

#     prefix2 = ["", "went", "to"]
#     sentence3 = finish_sentence(prefix2,3,corpus,deterministic=True)
#     sentence4 = finish_sentence(prefix2,4,corpus,deterministic=True)
#     sentence5 = finish_sentence(prefix2,2,corpus,deterministic=True)
    print(sentence)
#     print(sentence1)
#     print(sentence2)
#     print(sentence3)
#     print(sentence4)
#     print(sentence5)











