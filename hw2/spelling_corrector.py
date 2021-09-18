import re
import numpy as np
import sys

# make distance matrix of two words
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

# find minimum cost between, deleting, inserting or substuiting
def find_min_cost(word1, word2, i,j,D,del_cost,ins_cost,sub_cost):
    deletion = D[i-1,j]+del_cost
    insertion = D[i,j-1]+ins_cost
    substitution = D[i-1,j-1] if word1[i-1]==word2[j-1] else D[i-1,j-1]+sub_cost
    
    return min([deletion,insertion,substitution])

### find minimum distanc between two words

def find_min_distance(word1,word2,del_cost,ins_cost,sub_cost):
    D = make_distance_matrix(word1, word2,del_cost,ins_cost,sub_cost)
    return D[-1,-1] #the lower right element is the minimum edit distance
    
### read in the dictionary file and make a list in python
def make_dictionary():
    with open ('google-10000-english.txt') as f:
        words = f.readlines() #each line is one word
        dict = [word[:-1] for word in words] #take line break
    return dict

### go through the dictionary and check if a word is in the dictionary, if not correct it
def correct_word(word,d):
    word_copy = word
    punc= re.findall(r'\W+', word)#take out all non-alphanumeric character
    cap = re.findall(r"[A-Z]+",word[0])# check if first letter is uppercase
    word = re.sub("\W+","",word) #take out all special characters before comparing it to the dictionary
    num = re.match(r"\d+",word)#extract numbers
    if num != None: ## check if this word is a digit, 
        correct = word_copy
    else: 
        if word.lower() in d:#turn to lowercase before checking
            correct = word_copy#return the original format
        else: 
            distances = list(map(lambda w: find_min_distance(word.lower(),w,1,1,1),d))
            min_distance= min(distances)
            correct = d[distances.index(min_distance)]
    
            #check if need to add punctuation before or after the word
            if punc != []:
                if re.match(r"\W",word_copy[0])!= None:
                    correct = punc[0]+correct
                elif re.match(r"\W",word_copy[-1]) != None: 
                    correct = correct+punc[0]
                else:
                    pass
            if cap != []:
                correct = correct[0].upper()+correct[1:]
    return correct

## correct a line 
def clean_line(line,d):
    words = line.split()
    corrected_line = list(map(lambda w: correct_word(w,d),words))
    corrected_line.append("\n")
    s = ' '.join(corrected_line)
    return s

# read in a txt file, a correct given lines specified by start_line and end_line    
def correct_doc(file, line_start, line_end):
    d = make_dictionary()
    with open(file) as f:
        lines = f.readlines()
        clean_text = list(map(lambda line: clean_line(line,d),lines[line_start:line_end]))
        corrected_text = ''.join(clean_text)
        with open('clean.txt', 'w') as f: #write the corrected file to clean.txt
            f.write(corrected_text)
        return corrected_text


## read input from Command Line
file = str(sys.argv[1])
start_line = int(sys.argv[2])
end_line = int(sys.argv[3])

new_text = correct_doc(file,start_line,end_line)
