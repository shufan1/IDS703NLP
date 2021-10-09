"""Latent Dirichlet Allocation

Patrick Wang, 2021
"""
from typing import List
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
import numpy as np


def lda_gen(vocabulary,alpha,beta,xi):
    v = np.shape(beta)[0]
    topic_porportion = np.random.dirichlet(alpha) # generate topic proportion dist
    topic_list = np.random.choice(range(v),xi,p=topic_porportion) #sample frmo topic proportion dist

    #pick word for each topic
    word_bags = []
    for topic_index in topic_list:
        word = np.random.choice(vocabulary,p=beta[topic_index])
        word_bags.append(word)

    return word_bags


def test():

    """Test the LDA generator."""
    vocabulary = [
        "bass", "pike", "deep", "tuba", "horn", "catapult",
    ]
    beta = np.array([
        [0.4, 0.4, 0.2, 0.0, 0.0, 0.0],
        [0.0, 0.3, 0.1, 0.0, 0.3, 0.3],
        [0.3, 0.0, 0.2, 0.3, 0.2, 0.0]
    ])
    alpha = np.array([0.2, 0.2, 0.2])
    xi = 50
    # np.random.seed(1)

    documents = [
        lda_gen(vocabulary, alpha, beta, xi)
        for _ in range(100)
    ]

    # Create a corpus from a list of texts
    dictionary = Dictionary(documents)
    corpus = [dictionary.doc2bow(text) for text in documents]
    model = LdaModel(
        corpus,
        id2word=dictionary,
        num_topics=3,
    )
    print(model.alpha)
    print(model.show_topics())


if __name__ == "__main__":
    test()