from nltk.tokenize import word_tokenize
from porter import PorterStemmer
from collections import Counter
import sys
import re
import matplotlib.pyplot as plt

# Class: CPSC 475
# Team Member 1: James Stevenson
# Submitted By: James Stevenson
# GU Username: jstevenson4
# File Name: proj2-2.py
# Description: Program tokenizes middlemarch based on input and returns
#   log-log graph of the most frequent tokens
# Write-up: The graphs of each tokenization appear to be Zipfian. This is consistent
#   with what was expected due to the standard language being used and general trend
#   that can come from a large dataset like Middlemarch
# To Execute: python3 proj2-2.py <number for tokenization>


# Pre: fname is a string for the input file
# Post: string of data within file is returned
def get_data(fname):
    fin = open(fname, 'r', encoding='utf8')
    text = fin.read()  #read in text as a string
    fin.close()
    return text


# base condition for tokenizing; only separates spaces into list
# Pre: text is a string
# Post: list of strings is returned separated by spaces
def tokenize_on_spaces(text):
    outfile = open('out1', 'w')
    outfile.write(text)
    outfile.close()
    # splitting on spaces works fine
    word_list = text.split(' ')
    return word_list


# Pre: text is a string
# Post: list of strings is returned, tokenized by nltk
def tokenize_on_word_tokenize(text):
    word_list = []
    outfile = open('out2', 'w')
    for line in text.splitlines():
        line_word_list = word_tokenize(line)
        for word in line_word_list:
            word_list.append(word)
        print(' '.join(line_word_list), end='\n', file=outfile)
    outfile.close()
    return word_list


# Pre: text is a string
# Post: list of strings is returned, tokenized by porter.py
def tokenize_on_porter(text):
    word_list = []
    p = PorterStemmer()
    outfile = open('out3', 'w')
    for line in text.splitlines():
        output = ''
        word = ''
        if line != '':
            for c in line:
                if c.isalpha():
                    word += c.lower()
                else:
                    if word:
                        word_stem = p.stem(word, 0, len(word)-1)
                        output += word_stem
                        word_list.append(word_stem)
                        word = ''
                    output += c.lower()
        print(output, end='\n', file=outfile)
    outfile.close()
    return word_list


# Pre: word_list is a list of strings
# Post: word_list is printed to out4, separated by spaces
def print_custom_tokenize(word_list):
    line_counter = 0
    outfile = open('out4', 'w')
    for word in word_list:
        outfile.write(word + ' ')
        line_counter += 1
        # make a newline after every 14 words
        if line_counter % 15 == 0:
            outfile.write('\n')
    outfile.close()


# Pre: text is a string
# Post: list of strings is returned, tokenized by a custom algorithm
def tokenize_on_custom(text):
    # splitting on any white space, not just spaces
    word_list = text.split()
    # making words lowercase
    word_list = map(str.lower, word_list)
    # removing non alphabetic characters
    word_list = [re.sub('[^a-zA-Z]+', '', word) for word in word_list]

    print_custom_tokenize(word_list)
    return word_list


# Pre: word_lst is a list of strings
# Post: Counter dictionary is returned for word_lst
def count_words(word_lst):
    word_dict = Counter(word_lst)
    return word_dict


# Pre: word_dict is a Counter dictionary of strings
# Post: Sorted word_dict from most frequent to least is returned
def sort_dict(word_dict):
    sorted_list = word_dict.most_common()
    return dict(sorted_list)


# Pre: word_dict is a Counter dictionary of strings
# Post: Strings in word_dict are printed in file, followed by frequency
def output_dict_to_file(outfile_name, word_dict):
    outfile = open(outfile_name, 'w')
    for word in word_dict.keys():
        outfile.write(word + '\t\t' + str(word_dict[word]) + '\n')
    outfile.close()


# Pre: word_lst, word_dict, and tokenizer are all valid inputs
# Post: Returns stats for tokenizer
def stats(word_lst, word_dict, tokenizer):
    print("Tokenizer: " + tokenizer)
    V = len(word_dict.keys())
    N = len(word_lst)
    print("Tokens: " + str(N))
    print("Types: " + str(V))
    print("Ratio of Types to Tokens: ", str(V/N))


# Pre: word_dict is a sorted Counter dictionary of strings
# Post: Log-log plot is returned of words vs frequency
def plot_word_dict(word_dict):
    x = [i for i in range(0, len(word_dict))]
    y = [value for value in word_dict.values()]
    plt.loglog(x, y)
    plt.show()

    
def main():
    # checking arguments
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print('Invalid number of command line arguments')
        sys.exit()

    file_name = sys.argv[1]

    if not sys.argv[2].isdigit():
        print('Tokenizer must be a digit between 1 & 4')
        sys.exit()
    tokenizer = sys.argv[2]

    if int(tokenizer) > 4 or int(tokenizer) < 0:
        print('Invalid value for tokenizer')
        sys.exit()

    try:
        text = get_data(file_name)
    except:
        print('Could not open file')
        sys.exit()

    # outputs result of tokenizing to 'out1'
    if tokenizer == '1':
        word_list = tokenize_on_spaces(text)
    # outputs result of tokenizing to 'out2'
    if tokenizer == '2':
        word_list = tokenize_on_word_tokenize(text)
    # outputs result of tokenizing to 'out3'
    if tokenizer == '3':
        word_list = tokenize_on_porter(text)
    # outputs result of tokenizing to 'out4'
    if tokenizer == '4':
        word_list = tokenize_on_custom(text)

    # count words
    word_dict = sort_dict(count_words(word_list))

    # plot words
    plot_word_dict(word_dict)
    
main()