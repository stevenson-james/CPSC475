from nlpUtils import get_data, tokenize, make_grams
from sys import argv


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
