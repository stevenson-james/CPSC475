import sys
import math
from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.corpus import gutenberg
from string import punctuation
from collections import Counter
import pandas as pd

# DO NOT GRADE, PLEASE IGNORE

# Pre: fname is a string for the input file
# Post: string of data within file is returned
def get_data(fname):
    fin = open(fname, 'r', encoding='utf8')
    text = fin.read()  #read in text as a string
    fin.close()
    return text


# Pre: text is a string
# Post: list of strings is returned, tokenized by nltk
def tokenize_on_word_tokenize(text):
    sentence_list = []
    for line in text.splitlines():
        word_list = word_tokenize(line)
        word_list = [word.lower() for word in word_list if word not in punctuation and word != '“' and word != '”']
        if len(word_list) > 0:
            sentence_list.append(word_list)
    return sentence_list


# Pre: sentence_list is a list of sentences which are each a list of words
# Post: list of tokenized sentences is returned
def tokenize_sentence_list(sentence_list):
    new_sentence_list = []
    for sentence in sentence_list:
        word_list = []
        word_list = [word.lower() for word in sentence if word not in punctuation and word != '“' and word != '”']
        if len(word_list) > 0:
            new_sentence_list.append(word_list)
    return new_sentence_list


"""
Makes a list of n_grams from the sentence list with n being the gram_size
Pre: sent_lst is a list with item a tokenized sentence, and gram_size is greater
    than zero and less than five
Post: returns a list of all n_grams of sent_lst
"""
def make_grams(sent_lst, gram_size):
    n_grams = []
    for line in sent_lst:
        for i in range(len(line) - gram_size + 1):
            n_grams.append(tuple(line[i: i + gram_size]))
    return n_grams


def find_tf(n_gram_counter, gram_length):
    tf_dictionary = {}
    for gram, count in n_gram_counter.items():
        tf_dictionary[gram] = count / float(gram_length)
    return tf_dictionary


def find_idf(counter_dict):
    document_len = len(counter_dict)
    
    idf_dictionary = {}
    for file_name, counter in counter_dict.items():
        for word in counter:
            idf_dictionary[word] = 0

    for file_name, counter in counter_dict.items():
        for word in counter:
            if counter[word] > 0:
                idf_dictionary[word] += 1
    
    for word, value in idf_dictionary.items():
        idf_dictionary[word] = math.log(document_len / float(value))
    return idf_dictionary
 

def find_tfidf(tf_dictionary, idf_dictionary):
    tfidf_dict = {}
    for word, val in tf_dictionary.items():
        tfidf_dict[word] = val * idf_dictionary[word]
    return tfidf_dict


def main():
    gram_size = 1

    corpus = ['austen-emma', 'austen-persuasion', 'austen-sense']

    # dictionary from file name to list of n-gram tuples in file
    gram_dict = {}
    counter_dict = {}
    tf_dict_dictionary = {}
    
    for file_name in corpus:
        gram_dict[file_name] = make_grams(tokenize_sentence_list(gutenberg.sents(file_name + '.txt')), gram_size)
        counter_dict[file_name] = Counter(gram_dict[file_name])
        tf_dict_dictionary[file_name] = find_tf(counter_dict[file_name], gram_size)
    idf_dictionary = find_idf(counter_dict)
    
    tfdif_dict_dictionary = {}
    for file_name in corpus:
        tfdif_dict_dictionary[file_name] = find_tfidf(tf_dict_dictionary[file_name], idf_dictionary)

    for file_name in tfdif_dict_dictionary.keys():
        print('\n\n--------', file_name, '--------')
        for word in tfdif_dict_dictionary[file_name].keys():
            print(word, ':', tfdif_dict_dictionary[file_name][word])

main()
