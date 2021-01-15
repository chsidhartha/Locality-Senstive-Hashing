from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
import string
import re
import random
import numpy as np
import time

# createShingles:
# input : doc - the link to the dataset
#         k - the shingle size usually between 5 - 9
# returns : a dictionary with key as the DNA string and
#           the set of shingles as the paired value
'''
n
O(n^2)
10^9->10^18
locality sensitive hashing
k-shingling->k=3
chaitanya
  is si id dh hu
1  1  1  0 0  0
2  1  0  1  0  1
3
4
5 
normal hashing
siddhu->h(siddhu)->100
h(sidhu)->2
h(siddu)->300
lsh
h(sidhu)->95
h(siddu)->102
'''

def createShingles(doc, k):
    dataset = open(doc, encoding='utf-8')
    lines = [line.rstrip('\n') for line in dataset]
    dataset.close()

    hashmap = {}
    cnt = 0
    for line in lines:
        dna = line.split(" ")[0]
        n = len(dna)
        i = int(k)
        shingles = set()
        while i < n:
            shingles.add(dna[(i - int(k)):i])
            i += 1
        hashmap[cnt] = shingles
        cnt += 1
    return hashmap
# siddhartha Raman->ex:4shingle->sidd,iddh,ddha,dhar
'''
Query-> shingle size,jaccard sim,band size,query(DNA)
matrix(shingles*documents)
   ab bc cd ef si dd  
1   1  0 1  0
2   0  1 1  1
3
q   1  0  1 0
jaccard similarity->no.of 1 in document/no.of in 
lsh
min-hashing->
100
{1:[],2:[]}
'''



