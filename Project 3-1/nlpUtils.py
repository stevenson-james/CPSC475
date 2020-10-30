# Class: CPSC 475
# Team Member 1: James Stevenson
# Submitted By: James Stevenson
# GU Username: jstevenson4
# File Name: proj3-1.py
# Description: Program gives functionality for tokenizing an input file and 
#   generating n-grams from tokenized file
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
