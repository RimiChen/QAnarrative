'''
This example demonstrates how to extract simple Rensa assertions from natural text.
'''
#### nltk 
import nltk
import math
from nltk.corpus import gutenberg
from nltk.tokenize import PunktSentenceTokenizer

#### import rensa
import sys
import os
from pprint import pprint
import json
import codecs
from nltk.corpus import wordnet as wn
from sets import Set

#### improt rensa extractor
memory_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '.', 'src'))
sys.path.insert(0, memory_path)
from Brain import *
from ConceptExtractor_v2 import *


def preprocessing_text_file(input_file):


    train_text = gutenberg.raw(input_file)
    sample_text = gutenberg.raw(input_file)
    #### understand input type and content
    #print(train_text)
    #print("=====================")
    #print(type(train_text))
    #### unicode text 

    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    tokenized = custom_sent_tokenizer.tokenize(sample_text)
    #### show chunked result
    #print("\n\n".join(tokenized))
    #print("=================")
    #print(type(tokenized))
    #### list of sentences (separated by ".")

    return tokenized

def process_content(sentences):
    chunked_list = []
    try:
        for i in sentences:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #### chunked by this grammer rule
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            #### transform to string list
            chunked_list.append(str(chunked))
            
            
            #### print chunked result
            #print(chunked)
            #print("============")
            #print(type(chunked))
            #### <class nltk.tree.Tree>

            #chunked.draw()     

    except Exception as e:
        print(str(e))

    return chunked_list

if __name__ == '__main__':
    print("Test chunking story: AROUND WORLD 80 DAYS")

    #### chunking nouns and noun phrases
    input_file = "AROUND_THE_WORLD_IN_EIGHTY_DAYS_CH_1.txt"
    sentences = preprocessing_text_file(input_file)
    chunked_list = process_content(sentences) 
    #### test chunked result
    #print("\n\n".join(chunked_list))
    #print("=====================")
    #print(chunked_list[0])
    #print("=====================")
    #print(chunked_list[1])
    