import random

def main():
    runMainMenu()

easy = -5
hard = 5

#holds the flash cards, key is a number and class Card is the card
questionList = []  


def runMainMenu():
    while True:
        options = {
            1: ("Add Cards To Current List", "add card"),
            2: ("Do A Set Of Questions", "play"),
            3: ("Change Current List", "change list"),
            4: ("Quit", "quit")
        }
        nextAction = displayMenuPrompt(options)

        if nextAction == "add card":
            #does it work?
            addLotsOfQuestions()

        elif nextAction == "play":
            #does nothing
            runSetOfQuestions()

        elif nextAction == "change list":
            #does nothing
            changeList()
            
        elif nextAction == "quit":
            #works!
            print ("Goodbye!")
            exit(0)



class Card:
    def __init__(self, answer, question):
        self.level = "regular"
        self.challenge = 0
        self.answer = answer
        self.question = question
        self.history = []
        
    #adds or subtracts from the challenge level
    def correct(self):
        choice = None
        while choice != "y" or choice != "n":
            choice = input("Did you get it right? y/n")
        if choice == "y":
            self.challenge -= 1
            levelCheck(self)
            self.history.append("y")
        elif choice == "n":
            self.challenge += 1
            levelCheck(self)
            self.history.append("n")

    #checks to see what the level should be
    def levelCheck(self):
        if self.challege <= easy:
            self.level = "easy"
        elif self.challenge >= hard:
            self.level = "hard"
        else:
            self.level = "regular"

#adds flash card
def addQuestion():
    question = input("What's the question?")
    answer = input("And the answer is?")
    questionList.append(Card(answer, question))

def addLotsOfQuestions():
    choice = None
    while choice != "n":
        choice = input("Add a question? y/n")
        if choice != "n":
            addQuestion()

#
def runSetOfQuestions():
    pass


#
def changeList():
    pass
    

##FUTURE FEATURES

###save and load stuff

###ask questions from list, 5 random, X random

###make lists based on self.level

##view all questions

###delete unwanted cards

###make different sets of question lists (dictionary of lists)

###delete old lists

##scores and saving scores per set of questions

###type in answer mode

#Meg's code... makes the numbered menus work
def displayMenuPrompt(options):
    while True:
        for num, item in options.items():
            print (str(num) + " - " + item[0])

        choice = input(">")

        if not choice.isdigit():
            print ("Please pick a number from 1 to %d. \n" % len(options))
            continue

        choice = int(choice)
        if choice > 0 and choice <= len(options):
            (optionDisplayText, optionInternalText) = options[choice]
            print ("You picked option %d - %s\n" % (choice, optionDisplayText))
            return optionInternalText
        else:
            print("Please pick a number from 1 to %d. \n" % len(options))



main()
