def get_data(fname):
    f = open(fname, 'r', encoding='utf8')
    return [line for line in f]


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


# gram_size > 0 and < 5
def make_grams(sent_lst, gram_size):
    n_grams = []
    for line in sent_lst:
        line = line.split()
        for i in range(len(line) - gram_size + 1):
            n_grams.append(line[i: i + gram_size])
    return n_grams
