import numpy as np

#word1 is potentially wrong, word2 is a word for the dictionary
def make_distance_matrix(word1, word2,del_cost,ins_cost,sub_cost):
    D = np.zeros([len(word1)+1,len(word2)+1],dtype=int)
    #D[0,0] = 0 
    # Initialization: the zeroth column is the distance of word1 to an empty string 
    for i in range(1,len(word1)+1):
        D[i,0] = D[i-1,0]+del_cost #cost of deletion is 1
    # Initialization: the zeroth row is the distance of an empty string to word2
    for j in range(1,len(word2)+1):
        D[0,j] = D[0,j-1]+ins_cost #cost of insertion is 1
    
    for i in range(1,len(word1)+1): 
        for j in range(1,len(word2)+1):# fill rows and columns starting at (1,1)
            D[i,j] = find_min_cost(word1,word2,i,j,D,del_cost,ins_cost,sub_cost)
    return D


def find_min_cost(word1, word2, i,j,D,del_cost,ins_cost,sub_cost):
    deletion = D[i-1,j]+del_cost
    insertion = D[i,j-1]+ins_cost
    substitution = D[i-1,j-1] if word1[i-1]==word2[j-1] else D[i-1,j-1]+sub_cost
    
    return min([deletion,insertion,substitution])

### find minimum distanc between two words

def find_min_distance(word1,word2,del_cost,ins_cost,sub_cost):
    D = make_distance_matrix(word1, word2,del_cost,ins_cost,sub_cost)
    return D[-1,-1] #the lower right element is the minimum edit distance

assert make_distance_matrix("intention","execution",1,1,2)[3,2] == 5
assert find_min_distance("intention","execution",1,1,2)==8
# print(find_min_distance("sensibility","sensitivity",1,1,1))
# print(find_min_distance("sensibility","posibility",1,1,1))