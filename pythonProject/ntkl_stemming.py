#stemming reduce the words to its original form

import nltk
from nltk.stem import PorterStemmer


stemmer = PorterStemmer()

words = ["eating","ate","eat","adjustable","rafting","ability","meeting"]

for token in words:
    print(words," | ",stemmer.stem(words))