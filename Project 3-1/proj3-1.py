from nlpUtils import get_data, tokenize, make_grams
from sys import argv

# Class: CPSC 475
# Team Member 1: James Stevenson
# Submitted By: James Stevenson
# GU Username: jstevenson4
# File Name: proj3-1.py
# Description: Program displays number of n-grams from user based on functions
#   in nlpUtils.py
# To Execute: python3 proj3-1.py <size of grams> <number of grams to display>


"""
Generates n-grams and displays given number of generated n-grams
Pre: grams is a list of n-grams, num_grams is not greater
    than number of n-grams in grams
Post: prints n-grams from grams based on num_grams
"""
def display(grams, num_grams):
    for i in range(num_grams):
        print(grams[i])


def main():
    gram_size = int(argv[1])
    num_grams = int(argv[2])

    sentence_list = get_data('pride_and_prejudice.txt')
    tokenized_list = tokenize(sentence_list)
    n_grams = make_grams(tokenized_list, gram_size)
    display(n_grams, num_grams)


main()
