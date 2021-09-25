from build_model import make_components_from_corpus,parse_corpus
from viterbi import viterbi
import numpy as np
import nltk

train_corpus = nltk.corpus.brown.tagged_sents(tagset='universal')[:10000]
tag_seqs,word_seqs,token_tags,token_words = parse_corpus(train_corpus)

pi,A,B = make_components_from_corpus(10000)

test_corpus = nltk.corpus.brown.tagged_sents(tagset='universal')[10150:10153]
test_tag_seqs,test_word_seqs,test_token_tags,test_token_words = parse_corpus(test_corpus)

correct = 0
wrong = 0
for i in range(len(test_corpus)):
    sentence = test_word_seqs[i]
    obs1 = [token_words[word.lower()] if word.lower() in token_words else len(token_words)  for word in sentence]
    states = viterbi(obs1,pi,A,B)
    all_tags = list(token_tags.keys())
    tags = list(map(lambda state_i:all_tags[state_i], states))
    print(sentence)
    print("expected:",test_tag_seqs[i])
    print("got:",states)
    print("translate to", tags)
    right_n = len(np.array(test_tag_seqs[i])[np.array(test_tag_seqs[i])==np.array(tags)])
    correct += right_n
    print(right_n,'/',len(tags),"\n")
    wrong += len(tags)-right_n

print("score:", correct/(correct+wrong))


# wit h open("test_corpus.txt","w") as f:
#     f.write(str(test_corpus))
# # # with open("tag.txt","w") as f:
# #     f.write(str(token_tags))
# with open("words.txt","w") as f:
#     f.write(str(token_words))