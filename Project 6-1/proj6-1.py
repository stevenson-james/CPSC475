from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.corpus import gutenberg
import sys


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
    word_list = []
    tokenizer = RegexpTokenizer(r'\w+')
    outfile = open('cleaned_corpus', 'w')
    for line in text.splitlines():
        line_word_list = word_tokenize(line)
        line_word_list = [word.lower() for word in line_word_list if word.isalnum()]
        for word in line_word_list:
            word_list.append(word)
        print(' '.join(line_word_list), end='\n', file=outfile)
    outfile.close()
    return word_list


def main():
    file_name = 'pride_and_prejudice'

    try:
        text = get_data(file_name)
    except:
        print('Could not open file')
        sys.exit()

    word_list = tokenize_on_word_tokenize(text)


main()
