import sys

# Class: CPSC 475
# Team Member 1: James Stevenson
# Submitted By: James Stevenson
# GU Username: jstevenson4
# File Name: proj1-1.py
# Program finds the number of a given substring from within a given file
# To Execute: python proj1-1.py


# Pre: 
# Post: Input file is opened and returned if inputted name is valid,
#     otherwise input is requested indefinitely
def my_open():
    while True:
        fin = input('Enter an input file name\n')
        try:
            fin = open(fin, 'r')
            break
        except:
            print("file does not exist  Try again.")
    return fin


# Pre: string is string to be searched on, subStr is string being searched for
#     and posStr_in is where the searching begins on 'string'
# Post: True if subStr is in string starting at posStr_in, false otherwise
def isSub(string, subStr, posStr_in):
    posSub = 0;
    posStr = posStr_in
    while posSub < len(subStr):
        if string[posStr] == subStr[posSub]:
            posSub = posSub + 1
            posStr = posStr + 1
        else:
            return False
    return True


# Pre: string is a valid string to be searched on, subStr is a substring to be
#     searched for
# Post: Number of instances of subStr found in string is returned
def find_number_of_subs(string, subStr):
    posStr = 0
    lastSub = len(string) - len(subStr)
    number_of_subs = 0

    while posStr <= lastSub:
        if isSub(string, subStr, posStr):
            number_of_subs += 1
            posStr += len(subStr)
        else:
            posStr += 1
    return number_of_subs


# Pre:
# Post: User-defined file is opened then number of instances of user-defined substring is given
#     within the text file
def main():
    file_as_string = my_open().read()
    print(find_number_of_subs(file_as_string, input("Enter a substring\n")))


if __name__ == '__main__':
    main()