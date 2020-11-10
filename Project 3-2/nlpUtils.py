import numpy as np
from random import random
from collections import Counter
import sys

# Class: CPSC 475
# Team Member 1: James Stevenson
# Submitted By: James Stevenson
# GU Username: jstevenson4
# File Name: nlpUtils.py
# Description: Program gives functionality for tokenizing an input file,
#   generating n-grams from tokenized file, and generating random weighted n-grams
# To Execute: import as a package in a main python script


"""
Returns list of each line in an input file
Pre: fname is a valid string name of an input file
Post: returns list of each line from input file
"""
def get_data(fname):
    f = open(fname, 'r', encoding='utf8')
    return [line for line in f]


"""
Tokenizes a list of lines from an input file
Pre: text_lst is a list with each line as an item
Post: returns tokenized list of sentences
"""
def tokenize(text_lst):
    new_text_lst = []
    for line in text_lst:
        new_line = ''
        for word in line:
            # fill new_word with only ASCII characters
            new_word = ''.join([char if ord(char) < 128 else '' for char in word])
            # append new_word to new_line
            new_line += new_word
        # remove '\n' from new_line (last 2 characters)
        new_line = new_line[:-1]
        # remove whitespace from beginning of new_line
        new_line = new_line.lstrip()
        new_line = '<s> ' + new_line + ' </s>'
        new_text_lst.append(new_line)
    return new_text_lst


"""
Makes a list of n_grams from the sentence list with n being the gram_size
Pre: sent_lst is a list with item a tokenized sentence, and gram_size is greater
    than zero and less than five
Post: returns a list of all n_grams of sent_lst
"""
def make_grams(sent_lst, gram_size):
    n_grams = []
    for line in sent_lst:
        line = line.split()
        for i in range(len(line) - gram_size + 1):
            n_grams.append(line[i: i + gram_size])
    return n_grams


"""
Makes a dictionary of n-grams to their weight based on cumulative sums
Pre: n_gram_counts is a Counter of all n_grams in a corpus
Post: returns a dictionary of n_grams to weighted sums
"""
def compute_weights(n_gram_counts):
    n_gram_sum = sum(n_gram_counts.values())
    n_gram_weight_dict = {}
    cumulative_sum = 0.0
    for n_gram, count in n_gram_counts.items():
        cumulative_sum += count / n_gram_sum
        n_gram_weight_dict[n_gram] = cumulative_sum
    return n_gram_weight_dict


"""
Makes a dictionary of n-grams to their weight based on cumulative sums
    from list of n_grams
Pre: n_gram_list is a list of all n_grams in corpus with repeats
Post: returns a dictionary of n_grams to weighted sums
"""
def set_cumulative_weight_dictionary(n_gram_list):
    n_gram_tuples = [tuple(item) for item in n_gram_list]
    n_gram_counts = Counter(n_gram_tuples)
    return compute_weights(n_gram_counts)


#generate a random number
#traverse the cumulative probabilities looking for the first one greater than
#the random number generated
#in the city example, object is a city, weight is a population
def make_choice(n_gram_weight_dict):
    choice = random()
    for n_gram, weight in n_gram_weight_dict.items():
      if choice < weight:
         return n_gram


"""
Makes the output object for use with printing random unigrams
Pre: n_gram_weight_dict is a dictionary of n_grams to their weighted sums
Post: returns a list of lines where each line is a list of 3 grams
"""
def generate_unigram_random_output(n_gram_weight_dict):
    output = []
    while len(output) < 5:
        line = []
        # generating first gram
        # must start with <s>
        n_gram = make_choice(n_gram_weight_dict)
        while n_gram[0] != '<s>' or n_gram[-1] == '</s>':
            n_gram = make_choice(n_gram_weight_dict)
        for word in n_gram:
                line.append(word)
        
        # generating middle gram
        n_gram = make_choice(n_gram_weight_dict)
        while n_gram[0] == '<s>' or n_gram[-1] == '</s>':
            n_gram = make_choice(n_gram_weight_dict)
        for word in n_gram:
            line.append(word)
        
        # generating last gram
        # must end with </s>
        n_gram = make_choice(n_gram_weight_dict)
        while n_gram[0] == '<s>' or n_gram[-1] != '</s>':
            n_gram = make_choice(n_gram_weight_dict)
        for word in n_gram:
            line.append(word)

        output.append(line)

    return output


"""
Makes the output object for use with printing random n-grams from 2-4
Pre: n_gram_weight_dict is a dictionary of n_grams to their weighted sums
Post: returns a list of lines where each line is a list of 12 grams maximum
"""
def generate_random_output(n_gram_weight_dict):
    # get 'n' of n-grams
    n = len(next(iter(n_gram_weight_dict)))

    # generate unigram output
    if n == 1:
        return generate_unigram_random_output(n_gram_weight_dict)

    output = []
    while len(output) < 5:
        line = []

        # generating first gram
        # must start with <s>
        n_gram = make_choice(n_gram_weight_dict)
        while n_gram[0] != '<s>' or n_gram[-1] == '</s>':
            n_gram = make_choice(n_gram_weight_dict)
        for word in n_gram:
                line.append(word)
        
        # generating middle grams
        # counting <s> and </s> as words
        while len(line) <= 12 - 2*n:
            n_gram = make_choice(n_gram_weight_dict)
            while n_gram[0] == '<s>' or n_gram[-1] == '</s>':
                n_gram = make_choice(n_gram_weight_dict)
            for word in n_gram:
                line.append(word)
        
        # generating last gram
        # must end with </s>
        n_gram = make_choice(n_gram_weight_dict)
        while n_gram[0] == '<s>' or n_gram[-1] != '</s>':
            n_gram = make_choice(n_gram_weight_dict)
        for word in n_gram:
            line.append(word)

        output.append(line)

    return output


"""
Prints output object, limiting each line to 12 grams
Pre: n_gram_weight_dict is a dictionary of n_grams to their weighted sums
Post: prints output as shown in homework example
"""
def display_output(n_gram_weight_dict):
    n = len(next(iter(n_gram_weight_dict)))
    output = generate_random_output(n_gram_weight_dict)
    print('Gram Size =', n)
    word_line_count = 0
    for line in output:
        print(line[0], line[1].capitalize(), end=" ")
        for gram in line[2:]:
            print(gram.lower(), end=" ")
        print()
    print()
    