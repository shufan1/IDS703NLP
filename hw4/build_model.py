import nltk
import random
import re
from nltk import tag
import numpy as np
import timeit

#nltk.download('brown')
#nltk.download('universal_tagset')
n=2
corpus = nltk.corpus.brown.tagged_sents(tagset='universal')

def parse_sentence(sentence):
    tag_seq = list(list(zip(*sentence))[1])
    word_seq = list(list(zip(*sentence))[0])
    return tag_seq,word_seq

# compute initial state distribution
def update_initial_dist(tag_seq,initial_dist,token_tags): #find the first tag in a sentence, update counts at its column
    index_1st_tag = token_tags[tag_seq[0]]
    initial_dist[index_1st_tag]+=1

def compute_init_dist(tag_seqs,token_tags):
    initial_dist = np.zeros(len(token_tags)) # initialize the distribution with an array, ncol = # of possible tags
    list(map(lambda x: update_initial_dist(x,initial_dist,token_tags),tag_seqs)) #update inital distribution based on all tag sequences once
    initial_dist = initial_dist/np.sum(initial_dist) # normalize the inital distribution
    return initial_dist

# make the transistion matrix
def trans_matrix_from_1_tag_seq(tag_seq,transition_prob_matrix):
    for i in range(len(tag_seq)-1):
        tag = tag_seq[i]
        next_tag= tag_seq[i+1]
        transition_prob_matrix[token_tags[tag],token_tags[next_tag]]+=1 #get the indext and update count

def make_transition_matrix(token_tags,tag_seqs):
    n_tag = len(token_tags)
    transition_prob_matrix = np.zeros((n_tag,n_tag))
    list(map(lambda tag_seq: trans_matrix_from_1_tag_seq(tag_seq,transition_prob_matrix),tag_seqs)) #look at each tag seq at once
    return transition_prob_matrix

def count_obs(tagged_seq):
    for word in tagged_seq:
        obs_matrix[(token_tags[word[1]],token_words[word[0]])]+=1

def compute_obs_matrix():
    global obs_matrix
    obs_matrix = np.zeros((len(token_tags),len(token_words))) #initialize the observation matrix
    list(map(count_obs,corpus[:n])) 
    return obs_matrix

# build vocabulary and tags
tag_words = list(zip(*(map(parse_sentence,corpus[:n]))))
tag_seqs = list(tag_words[0])
print(tag_seqs)
words_seqs = list(tag_words[1])

# token tags and words
vocabulary = sorted(set(sum(words_seqs,[])))
all_tags = sorted(set(sum(tag_seqs,[])))
token_words = {word: ind for ind, word in enumerate(vocabulary)}
token_tags = {word: ind for ind, word in enumerate(all_tags)}

start = timeit.default_timer()
init_dist = compute_init_dist(tag_seqs,token_tags)
end = timeit.default_timer()
print("time:",end-start)
print("init_dist:", init_dist)

start = timeit.default_timer()
transition_matrix = make_transition_matrix(token_tags,tag_seqs)
end = timeit.default_timer()
print("time:",end-start)
print("transition matrixs:\n",transition_matrix)
# add smoothing

# # observation matrix
start = timeit.default_timer()
obs_matrix = compute_obs_matrix()
end = timeit.default_timer()
print("time:",end-start)
#print("obs_matrix:\n",obs_matrix)
print(np.shape(obs_matrix))
# give oov the same observation likelihood
obs_matrix = np.append(obs_matrix, np.zeros([len(token_tags),1]), axis=1)
print(np.shape(obs_matrix))
