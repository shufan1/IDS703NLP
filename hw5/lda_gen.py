import numpy as np

def lda_gen(vocabulary, beta,alpha,xi):

    v = np.shape(beta)[0]
    topic_porportion = np.random.dirichlet(alpha) # generate topic proportion dist
    print(topic_porportion)
    topic_list = np.random.choice(range(v),xi,p=topic_porportion) #sample frmo topic proportion dist
    print(topic_list)

    #pick word for each topic
    word_bags = []
    for topic_index in topic_list:
        word = np.random.choice(vocabulary,p=beta[topic_index])
        word_bags.append(word)

    return word_bags

vocabulary = [
        "bass", "pike", "deep", "tuba", "horn", "catapult",
    ]
beta = np.array([
        [0.4, 0.4, 0.2, 0.0, 0.0, 0.0],
        [0.0, 0.3, 0.1, 0.0, 0.3, 0.3],
        [0.3, 0.0, 0.2, 0.3, 0.2, 0.0]
    ])
alpha = np.array([0.2, 0.2, 0.2])
xi = np.random.poisson(50)

if  __name__=="__main__":
    lda_text = lda_gen(vocabulary,beta,alpha,xi)
    print(lda_text)


