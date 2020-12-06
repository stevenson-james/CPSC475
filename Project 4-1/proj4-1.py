import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from textwrap import TextWrapper

# Class: CPSC 475
# Team Member 1: James Stevenson
# Submitted By: James Stevenson
# GU Username: jstevenson4
# File Name: proj4-1.py
# Description: Program creates files filled with positive and negative reviews
#   based on what is needed for a naive Bayes classifier
# To Execute: python3 proj4-1.py

"""
Tokenizes a list to remove non-alphanumeric words
Pre: lst is a list of strings
Post: returns tokenized list
"""
def tokenizeLst(lst):
    stop_words = set(stopwords.words('english')) #common small words
    stringLst = ' '.join(lst)  #make into string to tokenize
    tok = word_tokenize(stringLst) #tokenize returns a list
    return [w for w in tok if w not in stop_words and w.isalnum()] #stop words removed


"""
Prints a string to a file limited to a width of 80 characters
Pre: string is a string and file_name is a name of the file to output to
Post: file of name file_name is created with the string printed in it
"""
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