import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from textwrap import TextWrapper

def tokenizeLst(lst):
    stop_words = set(stopwords.words('english')) #common small words
    stringLst = ' '.join(lst)  #make into string to tokenize
    tok = word_tokenize(stringLst) #tokenize returns a list
    return [w for w in tok if w not in stop_words and w.isalnum()] #stop words removed


def printStringToFile(string, file_name):
    f = open(file_name, 'w')
    wrapper = TextWrapper(width=80)
    split_text = '\n'.join(wrapper.wrap(string))
    f.write(split_text)
    f.close()


def main():
    reviews = movie_reviews.words() #all words from all reviews

    posLst = movie_reviews.fileids('pos') #all positive reviews
    negLst = movie_reviews.fileids('neg') #all negative reviews

    posDataLen = int(0.9 * len(posLst)) #length of 90% of positive reviews
    negDataLen = int(0.9 * len(negLst)) #length of 90% of negative reviews

    posWordLst = [] #words from positive reviews used for classifier
    for i in range(posDataLen):
        posWordLst.extend(movie_reviews.words(posLst[i]))

    posTstFileLst = [] #words from positive reviews used for testing classifier
    for i in range(posDataLen, len(posLst)):
        posTstFileLst.append(posLst[i])

    negWordLst = [] #words from negative reviews used for classifier
    for i in range(negDataLen):
        negWordLst.extend(movie_reviews.words(negLst[i]))

    negTstFileLst = [] #words from negative reviews used for classifier
    for i in range(negDataLen, len(negLst)):
        negTstFileLst.append(negLst[i])

    posWordLst = tokenizeLst(posWordLst)
    negWordLst = tokenizeLst(negWordLst)

    printStringToFile(' '.join(posWordLst), 'pos.txt')
    printStringToFile(' '.join(posTstFileLst), 'posTst.txt')
    printStringToFile(' '.join(negWordLst), 'neg.txt')
    printStringToFile(' '.join(negTstFileLst), 'negTst.txt')

main()