import numpy as np
from numpy.core.fromnumeric import argmax
from build_model import make_components_from_corpus

def viterbi(obs,pi,A,B):
    n_state = len(pi)
    viterbi_matrix = np.zeros((n_state,len(obs))) # initialize the viterbi matrix
    backpointers = np.zeros((n_state,len(obs)),dtype=int) #the matrix that holds the previous state that is most likely to get to this state of a given obs at t
    # initial state
    viterbi_matrix[:,0] = np.log(pi*B[:,obs[0]])
    backpointers[:,0] = 0 #point to the start
    # 
    for i in range(1,len(obs)):# for individual word after the first one
        x = np.shape(B)[1] if obs[i]>=np.shape(B)[1] else i
        for j in range(len(pi)):# for each state, which was the most likely previous state
            p = viterbi_matrix[:,i-1] + np.log(A[:,j])+np.log(B[j,obs[i]])
            viterbi_matrix[j,i] = np.max(p)
            backpointers[j,i] = np.argmax(p)

    # backtrack from the end to the beginning
    bestLastPointer = np.argmax(viterbi_matrix[:,-1])
    states = np.zeros(len(obs),dtype=int)
    states[-1] = bestLastPointer
    for i in reversed(range(1,len(obs))): #from the last column to column at index=1.
        bestLastPointer = backpointers[states[i],i]
        states[i-1] = bestLastPointer #ends at states[0]
    return states


# if __name__ =="__main__":
#     pi,A,B = make_components_from_corpus(10000)
#     obs1 = [19161,1907,2110,9578] #they are at home
#     states = viterbi(obs1,pi,A,B)
#     # #PRON ADP PART NOUN
#     print("expected: 8 10? 9? 6")
#     print(states)

#     obs1 = [9288,18836,1176] #he takes action
#     states = viterbi(obs1,pi,A,B)
#     # #PRON ADP PART NOUN
#     print("expected: 8 10 6")
#     print(states)