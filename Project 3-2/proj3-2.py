from nlpUtils import get_data, tokenize, make_grams, set_cumulative_weight_dictionary, display_output
import sys
# Class: CPSC 475
# Team Member 1: James Stevenson
# Submitted By: James Stevenson
# GU Username: jstevenson4
# File Name: proj3-2.py
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
    # change print() function to print to file 
    sys.stdout = open('Project 3-2 Example Output', 'w')

    for gram_size in range (1,5):
        sentence_list = get_data('pride_and_prejudice.txt')
        tokenized_list = tokenize(sentence_list)
        n_grams = make_grams(tokenized_list, gram_size)
        n_gram_weight_dict = set_cumulative_weight_dictionary(n_grams)
        display_output(n_gram_weight_dict)
        
    sys.stdout.close()
main()
