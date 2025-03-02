import random

##can't decide if i need a master list class, dictionary or something else. going to stop here

def main():
    runMainMenu()

#variables that don't change
easy = -5
hard = 5

questionList = []
currentList = questionList

masterList = {"first list": questionList}

#Meg's menu system
def runMainMenu():
    while True:
        options = {
            1: ("Add Cards To Current List", "add card"),
            2: ("Do A Set Of Questions", "play"),
            3: ("View Question List", "view list"),
            4: ("Change Current List", "change list"),
            5: ("Delete Current List", "delete list"),
            6: ("Quit", "quit")
        }
        nextAction = displayMenuPrompt(options)

        if nextAction == "add card":
            #works!
            addLotsOfQuestions()

        elif nextAction == "play":
            #does nothing
            runSetOfQuestions()

        elif nextAction == "view list":
            #works!
            viewList(questionList)

        elif nextAction == "change list":
            #does nothing
            changeList()

        elif nextAction == "delete list":
            #does nothing
            deleteList()
            
        elif nextAction == "quit":
            #works!
            print ("Goodbye!")
            exit(0)


class Card:
    def __init__(self, question, answer):
        self.level = "regular"
        self.challenge = 0
        self.answer = answer
        self.question = question
        self.history = []
        
    #adds or subtracts from the challenge level, lower is easier, higher is harder
    def correct(self):
        choice = None
        while choice != "y" or choice != "n":
            choice = input("Did you get it right? y/n  ")
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

    #prints out questions for viewList function
    def printQuestion(self):
        print (self.question)





#runs from the main menu to add lots of flash cards
def addLotsOfQuestions():
    choice = None
    while choice != "n":
        choice = input("Add a question? y/n  ")
        if choice != "n":
            addQuestion()

#adds flash card
def addQuestion():
    question = input("What's the question?  ")
    answer = input("And the answer is?  ")
    questionList.append(Card(question, answer))
    
#
def runSetOfQuestions():
    pass

#prints the current list of questions
def viewList(x):
    for question in x:
        Card.printQuestion(question)


#
def changeList():
    for key in masterList:
        print (key)
    choice = None
    while choice == None:
        choiceOfList = input("which list would you like?: ")
        if choiceOfList = key in masterList:
            currentList
    

#
def deleteList():
    pass


questionList.append(Card("how are you?1", "fine, thanks", currentListName))
questionList.append(Card("how are you?2", "fine, thanks", currentListName))
questionList.append(Card("how are you?3", "fine, thanks", currentListName))



##FUTURE FEATURES

###delete unwanted cards

###save and load stuff

###ask questions from list, 5 random, X random

###make lists based on self.level

###make different sets of question lists (dictionary of lists)

###delete old lists

##scores and saving scores per set of questions

###type in answer mode



##DONE FEATURES

##view questions



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
