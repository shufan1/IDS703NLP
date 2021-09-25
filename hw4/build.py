import nltk
import numpy as np
import timeit

#nltk.download('brown')
#nltk.download('universal_tagset')

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
    initial_dist = (initial_dist+1)/(np.sum(initial_dist)+len(token_tags)) # normalize the inital distribution
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
    # add Laplace Smoothing
    transition_prob_matrix = (transition_prob_matrix+ 1)/(np.sum(transition_prob_matrix,axis=1, keepdims=True)+len(token_tags)) #add one and normalize
    return transition_prob_matrix

def count_obs(tagged_seq):
    for word in tagged_seq:
        obs_matrix[(token_tags[word[1]],token_words[word[0].lower()])]+=1

def compute_obs_matrix(corpus):
    global obs_matrix
    obs_matrix = np.zeros((len(token_tags),len(token_words))) #initialize the observation matrix
    list(map(count_obs,corpus))
    obs_matrix = np.append(obs_matrix, np.zeros([len(token_tags),1]), axis=1) #add one count for OOV, equally likely
    obs_matrix = (obs_matrix+1)/(np.sum(obs_matrix,axis=1,keepdims=True)+np.shape(obs_matrix)[1]) # normalize
    return obs_matrix

def parse_corpus(corpus):
    tags_words = list(zip(*(map(parse_sentence,corpus))))
    tag_seqs = list(tags_words[0])
    words_seqs = list(tags_words[1])

    # token tags and words
    vocabulary = sum(words_seqs,[])
    vocabulary = map(str.lower,vocabulary)
    vocabulary = sorted(set(vocabulary))
    all_tags = sorted(set(sum(tag_seqs,[])))
    token_words = {word: ind for ind, word in enumerate(vocabulary)}
    token_tags = {word: ind for ind, word in enumerate(all_tags)}

    return tag_seqs,tags_words,token_tags,token_words


def make_components_from_corpus(n):# build vocabulary and tags
    global corpus
    corpus = nltk.corpus.brown.tagged_sents(tagset='universal')[:n]
    global tag_seqs,tags_words,token_tags,token_words 
    tag_seqs,tags_words,token_tags,token_words = parse_corpus(corpus)

    init_dist = compute_init_dist(tag_seqs,token_tags)
    transition_matrix = make_transition_matrix(token_tags,tag_seqs)
    obs_matrix = compute_obs_matrix(corpus)


    return init_dist,transition_matrix,obs_matrix



if __name__ == "__main__":
    a,b,c = make_components_from_corpus(2000)
    with open("corpus.txt","w") as f:
        f.write(str(corpus))
    with open("tag.txt","w") as f:
        f.write(str(token_tags))
    with open("words.txt","w") as f:
        f.write(str(token_words))