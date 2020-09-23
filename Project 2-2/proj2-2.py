from nltk.tokenize import word_tokenize
from porter import PorterStemmer
from collections import Counter
import string
import sys

def get_data(fname):
    fin = open(fname, 'r', encoding='utf8')
    text = fin.read()  #read in text as a string
    fin.close()
    return text

# base condition for tokenizing; only separates spaces into list
def tokenize_on_spaces(text):
    outfile = open('out1', 'w')
    outfile.write(text)
    outfile.close()
    #splitting on white space works fine
    word_lst = text.split(' ')
    return word_lst


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
                        word_stem = p.stem(word, 0,len(word)-1)
                        output += word_stem
                        word_list.append(word_stem)
                        word = ''
                    output += c.lower()
        print(output, end='\n', file=outfile)
    outfile.close()
    return word_list


def count_words(word_lst):
    word_dict = Counter(word_lst)
    return word_dict


def sort_dict(word_dict):
    sorted_list = word_dict.most_common()
    return dict(sorted_list)


def output_dict_to_file(outfile_name, word_dict):
    outfile = open(outfile_name, 'w')
    for word in word_dict.keys():
        outfile.write(word + '\t\t' + str(word_dict[word]) + '\n')
    outfile.close()


def stats(word_lst, word_dict, tokenizer):
    print("Tokenizer: " + tokenizer)
    V = len(word_dict.keys())
    N = len(word_lst)
    print("Tokens: " + str(N))
    print("Types: " + str(V))
    print ("Ratio of Types to Tokens: ", str(V/N))

    
def main():
    file_name = sys.argv[1]
    tokenizer = sys.argv[2]
    outfile_name = 'out'

    text = get_data(file_name)

    if tokenizer == '1':
        word_list = tokenize_on_spaces(text)
        outfile_name = 'out1'
   
    if tokenizer == '2':
        word_list = tokenize_on_word_tokenize(text)
        outfile_name = 'out2'
    
    if tokenizer == '3':
        word_list = tokenize_on_porter(text)
        outfile_name = 'out3'

    #count words
    word_dict = sort_dict(count_words(word_list))

    stats(word_list, word_dict,tokenizer)

    output_dict_to_file(outfile_name, word_dict)
            
    
main()