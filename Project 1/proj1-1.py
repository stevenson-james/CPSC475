import sys


def my_open():
    while True:
        fin = input('Enter an input file name\n')
        try:
            fin = open(fin, 'r')
            break
        except:
            print("file does not exist  Try again.")
    return fin


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


def main():
    file_as_string = my_open().read()
    print(find_number_of_subs(file_as_string, input("Enter a substring\n")))


if __name__ == '__main__':
    main()