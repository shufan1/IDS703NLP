import re

import nltk.corpus
import numpy as np

text = nltk.corpus.gutenberg.raw("austen-sense.txt")

corrupted = ""

p_edit = 0.04

for char in text:
    if re.fullmatch("[a-zA-Z]", char) is not None and np.random.rand() < p_edit:
        edit = np.random.randint(3)
        if edit == 0:
            # insert
            if 97 <= ord(char) < 123:
                corrupted += chr(97 + np.random.randint(26))
            elif 65 <= ord(char) < 91:
                corrupted += chr(65 + np.random.randint(26))
            corrupted += char
        elif edit == 1:
            # delete
            pass
        else:
            # substitute
            if 97 <= ord(char) < 123:
                corrupted += chr(97 + np.random.randint(26))
            elif 65 <= ord(char) < 91:
                corrupted += chr(65 + np.random.randint(26))
    else:
        corrupted += char

with open("austen-sense-corrupted.txt", "w") as stream:
    stream.write(corrupted)
