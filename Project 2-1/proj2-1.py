import sys
import re

# Class: CPSC 475
# Team Member 1: James Stevenson
# Submitted By: James Stevenson
# GU Username: jstevenson4
# File Name: proj2-1.py
# Program runs a basic chatbot answering questions on Italy
#   in order to practice regex
# To Execute: python3 proj2-1.py

# Pre: instr is a string
# Post: if instr includes 'italy' in it, then start asking for questions
#   otherwise ask for the user to ask about italy
def country_choice(instr):
    instr = instr.lower()
    if re.search(r'italy', instr):
        return 'Perfecto! What questions do you have about Italy?', True
    return 'Hmmmm I don\'t know about that country...maybe ask about the best country in the world?', False


# Pre: instr is a string
# Post: answers questions using regex based on the string passed in
def italy_questions(instr):
    instr = instr.lower()
    # basic hello response
    if re.search(r'^hello|hi$', instr):
        return 'Ciao! (Hi there!)'
    # response to where to go in Italy
    if re.search(r'\W(see)|\W(places)|^(where should i|what cities|where to go)\W', instr):
        return 'It is impossible to say where to go in Italy, since the entire country is \'bello\'!'
    # response to what to eat in Italy
    if re.search(r'^(what)(\W|\w)+(food|eat|dinner|lunch|breakfast|meal)', instr):
        return 'You shoud always get spaghetti and meatballs!'
    # response to when to go to Italy 
    if re.search(r'^(when|what)(\W|\w)+(to go|should i go|best time|worst time|best season|worst season)', instr):
        return 'The best time to be in Italy is all the time!'
    # response to what to drink in Italy
    if re.search(r'^(what)(\W|\w)+(drink|beverage|alcohol|soda)', instr):
        return 'When in Rome(Italy) you must always get \'il vino rosso\'!'
    # response to what currency is used in Italy
    if re.search(r'^(what)(\W|\w)+(money|currency|pay|payment)\W', instr):
        return 'Italia uses the Euro of course!'
    # default response when question is understood
    return 'Scusa, non capisco. Try with a different question!'

# Pre:
# Post: Communicates with user on questions about Italy
def main():
    print ("Welcome! What country would you like to look at? (type \"ciao\" to quit.)\n")
    # used for making sure user answers Italy to the first question
    is_italy = False
    while True:
        # Read user's input
        instr = input("Italy enthusiast: ")
        instr = instr.lower()

        # quit if 'ciao' is written
        if re.search(r'\bciao\b', instr):
            print ("Arrivederci!\n")
            return 0

        if not is_italy:
            stmt, is_italy = country_choice(instr)
        else:
            stmt = italy_questions(instr)
        print('\n' + stmt)
        print()


if __name__ == "__main__":
    sys.exit(main())
